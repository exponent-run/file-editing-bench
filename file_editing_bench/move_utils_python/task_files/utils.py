import os
import re
import uuid
import json
import hashlib
import datetime
from typing import Dict, List, Any
from pathlib import Path

def generate_document_id() -> str:
    """Generate a unique document ID using UUID4."""
    return str(uuid.uuid4())

def calculate_checksum(file_path: str) -> str:
    """Calculate SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def format_timestamp(dt: datetime.datetime) -> str:
    """Format a datetime object to ISO 8601 format."""
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

def sanitize_filename(filename: str) -> str:
    """Remove invalid characters from filename."""
    # Remove invalid characters
    clean_name = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Replace spaces with underscores
    clean_name = clean_name.replace(' ', '_')
    # Ensure name isn't too long
    name_parts = clean_name.rsplit('.', 1)
    if len(name_parts) > 1:
        name, ext = name_parts
        return f"{name[:200]}.{ext}"
    return clean_name[:200]

def parse_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and clean document metadata."""
    required_fields = ['title', 'author']
    for field in required_fields:
        if field not in metadata:
            raise ValueError(f"Required metadata field missing: {field}")
    
    # Convert all string values to stripped strings
    cleaned = {}
    for key, value in metadata.items():
        if isinstance(value, str):
            cleaned[key] = value.strip()
        else:
            cleaned[key] = value
    return cleaned

def validate_document_type(file_ext: str, supported_types: List[str]) -> bool:
    """Check if the document type is supported."""
    return file_ext.lower() in supported_types