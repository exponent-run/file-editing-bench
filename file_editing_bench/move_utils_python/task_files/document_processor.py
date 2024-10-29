import os
import json
import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path
import hashlib
import base64
from .utils import (
    generate_document_id,
    calculate_checksum,
    format_timestamp,
    sanitize_filename,
    parse_metadata,
    validate_document_type
)

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