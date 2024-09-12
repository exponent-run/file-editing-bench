I just created a new GraphQL mutation called `create_cloud_chat`. Before we only had `move_chat_to_cloud`, but I extracted the logic to share across the two mutations and created the new mutation.

```
import strawberry
from exponent.core.remote_execution.types import ChatMode
from exponent_server.api import api_messages
from exponent_server.api.context import (
    AuthenticatedContext,
)
from exponent_server.api.graphql.schema import (
    GraphChat,
    GraphChatNotFoundError,
    GraphCloudSessionError,
    GraphUnauthenticatedError,
)
from exponent_server.api.utils import (
    chat_to_graph_chat,
)
from exponent_server.core.config import get_cloud_base_api_url
from exponent_server.core.db import ChatStorage, DevboxLookupStorage
from exponent_server.core.services.runloop.utils import get_runloop_client
from exponent_server.models import Chat, DevboxLookup, User
from typing import Union
async def setup_cloud_chat(
    info: strawberry.Info[AuthenticatedContext],
    chat: Chat,
) -> Union[GraphChat, GraphCloudSessionError]:
    user = info.context.current_user
    assert isinstance(user, User)

    devbox = await DevboxLookupStorage.get_devbox_with_chat_id(
        info.context.session, chat.id
    )
    if devbox is not None:
        return chat_to_graph_chat(chat)

    entrypoint = (
        "export PATH=$PATH:~/.local/bin && "
        "cd /home/user && "
        "source venv/bin/activate && "
        "mkdir -p exponent && "
        "cd exponent && "
        f"exponent login --key {user.api_key} && "
        f"exponent run --chat-id={chat.chat_uuid}"
    )

    if api_url := get_cloud_base_api_url():
        entrypoint = f"export BASE_API_URL={api_url} && " + entrypoint

    try:
        devbox_view = await get_runloop_client().devboxes.create(
            name=f"chat-{chat.chat_uuid}",
            blueprint_id="bpt_2xOaKkwE0srSyaWtseJy0",
            entrypoint=entrypoint,
        )
    except Exception:  # noqa: BLE001
        return GraphCloudSessionError(
            chat_uuid=chat.chat_uuid, message=api_messages.CLOUD_SESSION_CREATION_FAILED
        )

    devbox = DevboxLookup(
        chat_id=chat.id,
        devbox_id=devbox_view.id,
    )

    # Update the chat mode to CLOUD
    chat.mode = ChatMode.CLOUD

    info.context.session.add(chat)
    info.context.session.add(devbox)

    await info.context.session.commit()
    await info.context.session.refresh(chat)
    chat.devbox = devbox

    return chat_to_graph_chat(chat)


@strawberry.type
class CloudChatMutation:
    @strawberry.mutation
    async def create_cloud_chat(
        self,
        info: strawberry.Info[AuthenticatedContext],
    ) -> Union[GraphChat, GraphUnauthenticatedError, GraphCloudSessionError]:
        user = info.context.current_user
        if not isinstance(user, User):
            return GraphUnauthenticatedError(
                message=api_messages.JWT_ERROR_USER_REMOVED
            )

        chat = await ChatStorage.create_chat(
            session=info.context.session, user_id=user.id
        )

        return await setup_cloud_chat(info, chat)

    @strawberry.mutation
    async def move_chat_to_cloud(
        self,
        chat_uuid: str,
        info: strawberry.Info[AuthenticatedContext],
    ) -> Union[GraphChat, GraphUnauthenticatedError, GraphChatNotFoundError, GraphCloudSessionError]:
        user = info.context.current_user
        if not isinstance(user, User):
            return GraphUnauthenticatedError(
                message=api_messages.JWT_ERROR_USER_REMOVED
            )

        chat = await ChatStorage.get_chat_with_uuid(info.context.session, chat_uuid)
        if chat is None or chat.user_id != user.id:
            return GraphChatNotFoundError(
                chat_uuid=chat_uuid, message=api_messages.INVALID_CHAT_ID
            )

        return await setup_cloud_chat(info, chat)
```

Can you edit the file `test_graphql_move_chat_to_cloud.py` so that:

- There is one new test for the new mutation called `test_create_cloud_chat_mutation` at the top of the file.
- Renames the existing instances of `create_cloud_chat` to `move_cloud_chat` as apporpriate to accurately match the mutation name being tested.
