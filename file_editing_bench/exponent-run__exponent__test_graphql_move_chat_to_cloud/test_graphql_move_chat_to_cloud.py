import uuid
from collections.abc import Callable

from exponent.core.remote_execution.types import ChatMode
from exponent_server.models import Chat, DevboxLookup, GithubConfig
from fastapi import status
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def test_create_cloud_chat_mutation(
    client: AsyncClient,
    session: AsyncSession,
    default_chat: Chat,
    default_user_headers: dict[str, str],
    add_devbox_create_response: Callable[[DevboxLookup], None],
) -> None:
    # Add GitHub config for the user
    github_config = GithubConfig(user_id=default_chat.user_id, github_pat="test_token")
    session.add(github_config)
    await session.commit()

    mutation = f"""
        mutation {{
            moveChatToCloud(chatUuid: "{default_chat.chat_uuid}") {{
                __typename
                ... on Chat {{
                    chatUuid
                    name
                }}
                ... on UnauthenticatedError {{
                    message
                }}
                ... on ChatNotFoundError {{
                    message
                }}
                ... on CloudSessionError {{
                    message
                }}
            }}
        }}
    """

    add_devbox_create_response(
        DevboxLookup(
            devbox_id="devbox-id",
            chat_id=default_chat.id,
        )
    )

    response = await client.post(
        "/graphql",
        json={"query": mutation},
        headers=default_user_headers,
    )

    assert response
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]
    assert response.json()["data"]["moveChatToCloud"]["__typename"] == "Chat"
    assert (
        response.json()["data"]["moveChatToCloud"]["chatUuid"] == default_chat.chat_uuid
    )

    devbox = await session.scalar(
        select(DevboxLookup).where(DevboxLookup.chat_id == default_chat.id)
    )
    assert devbox
    assert devbox.chat_id == default_chat.id
    assert devbox.devbox_id == "devbox-id"

    chat = await session.get(Chat, default_chat.id)
    assert chat
    assert chat.mode == ChatMode.CLOUD

    # With existing devbox

    response = await client.post(
        "/graphql",
        json={"query": mutation},
        headers=default_user_headers,
    )

    assert response
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]
    assert response.json()["data"]["moveChatToCloud"]["__typename"] == "Chat"
    assert response.json()["data"]["moveChatToCloud"]["chatUuid"]


async def test_create_cloud_chat_mutation_invalid_chat(
    client: AsyncClient,
    session: AsyncSession,
    default_chat: Chat,
    default_user_headers: dict[str, str],
) -> None:
    # Add GitHub config for the user
    github_config = GithubConfig(user_id=default_chat.user_id, github_pat="test_token")
    session.add(github_config)
    await session.commit()

    mutation = f"""
        mutation {{
            moveChatToCloud(chatUuid: "{uuid.uuid4()}") {{
                __typename
                ... on Chat {{
                    chatUuid
                    name
                }}
                ... on UnauthenticatedError {{
                    message
                }}
                ... on ChatNotFoundError {{
                    message
                }}
                ... on CloudSessionError {{
                    message
                }}
            }}
        }}
    """

    response = await client.post(
        "/graphql",
        json={"query": mutation},
        headers=default_user_headers,
    )

    assert response
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]
    assert (
        response.json()["data"]["moveChatToCloud"]["__typename"] == "ChatNotFoundError"
    )
    assert response.json()["data"]["moveChatToCloud"]["message"] == "Invalid Chat ID"

    devbox = await session.scalar(
        select(DevboxLookup).where(DevboxLookup.chat_id == default_chat.id)
    )
    assert devbox is None


async def test_create_cloud_chat_mutation_github_config_not_found(
    client: AsyncClient,
    session: AsyncSession,
    default_chat: Chat,
    default_user_headers: dict[str, str],
) -> None:
    mutation = f"""
        mutation {{
            moveChatToCloud(chatUuid: "{default_chat.chat_uuid}") {{
                __typename
                ... on Chat {{
                    chatUuid
                    name
                }}
                ... on UnauthenticatedError {{
                    message
                }}
                ... on ChatNotFoundError {{
                    message
                }}
                ... on CloudSessionError {{
                    chatUuid
                    message
                }}
            }}
        }}
    """

    response = await client.post(
        "/graphql",
        json={"query": mutation},
        headers=default_user_headers,
    )

    assert response
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]
    assert (
        response.json()["data"]["moveChatToCloud"]["__typename"] == "CloudSessionError"
    )
    assert (
        response.json()["data"]["moveChatToCloud"]["chatUuid"] == default_chat.chat_uuid
    )
    assert (
        response.json()["data"]["moveChatToCloud"]["message"]
        == "Github config not found"
    )

    devbox = await session.scalar(
        select(DevboxLookup).where(DevboxLookup.chat_id == default_chat.id)
    )
    assert devbox is None


async def test_create_cloud_chat_mutation_cloud_session_error(
    client: AsyncClient,
    session: AsyncSession,
    default_chat: Chat,
    default_user_headers: dict[str, str],
    add_devbox_create_failure: Callable[[], None],
) -> None:
    # Add GitHub config for the user
    github_config = GithubConfig(user_id=default_chat.user_id, github_pat="test_token")
    session.add(github_config)
    await session.commit()

    mutation = f"""
        mutation {{
            moveChatToCloud(chatUuid: "{default_chat.chat_uuid}") {{
                __typename
                ... on Chat {{
                    chatUuid
                    name
                }}
                ... on UnauthenticatedError {{
                    message
                }}
                ... on ChatNotFoundError {{
                    message
                }}
                ... on CloudSessionError {{
                    chatUuid
                    message
                }}
            }}
        }}
    """

    add_devbox_create_failure()

    response = await client.post(
        "/graphql",
        json={"query": mutation},
        headers=default_user_headers,
    )

    assert response
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]
    assert (
        response.json()["data"]["moveChatToCloud"]["__typename"] == "CloudSessionError"
    )
    assert (
        response.json()["data"]["moveChatToCloud"]["chatUuid"] == default_chat.chat_uuid
    )
    assert (
        response.json()["data"]["moveChatToCloud"]["message"]
        == "Failed to create cloud session"
    )

    devbox = await session.scalar(
        select(DevboxLookup).where(DevboxLookup.chat_id == default_chat.id)
    )
    assert devbox is None
