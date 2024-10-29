import uuid
from typing import Dict, Any

def generate_document_id() -> str:
    """Generate a unique document ID using UUID4."""
    return str(uuid.uuid4())