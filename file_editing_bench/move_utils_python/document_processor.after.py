import os
import re
import json
import datetime
import hashlib
from typing import Dict, List, Optional, Any
from pathlib import Path
from .utils import generate_document_id

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

class DocumentProcessor:
    def __init__(self, storage_path: str):
        self.storage_path = Path(storage_path)
        self.supported_types = ['pdf', 'docx', 'txt', 'md']

    def process_document(self, file_path: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Document not found: {file_path}")

        # Generate unique ID for document
        doc_id = generate_document_id()
        
        # Validate document type
        file_ext = Path(file_path).suffix.lower()[1:]
        if not validate_document_type(file_ext, self.supported_types):
            raise ValueError(f"Unsupported document type: {file_ext}")

        # Calculate document checksum
        checksum = calculate_checksum(file_path)
        
        # Parse and validate metadata
        processed_metadata = parse_metadata(metadata)
        
        # Create sanitized filename
        clean_filename = sanitize_filename(Path(file_path).name)
        
        # Format current timestamp
        timestamp = format_timestamp(datetime.datetime.now())
        
        # Prepare document info
        doc_info = {
            "id": doc_id,
            "original_filename": Path(file_path).name,
            "clean_filename": clean_filename,
            "checksum": checksum,
            "processed_at": timestamp,
            "metadata": processed_metadata,
            "file_type": file_ext
        }
        
        # Save document to storage
        target_path = self.storage_path / clean_filename
        with open(file_path, 'rb') as src, open(target_path, 'wb') as dst:
            dst.write(src.read())
            
        return doc_info

    def bulk_process(self, file_paths: List[str], metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        results = []
        for file_path in file_paths:
            try:
                result = self.process_document(file_path, metadata)
                results.append(result)
            except Exception as e:
                results.append({
                    "error": str(e),
                    "file": file_path
                })
        return results