import os
import pytest
import tempfile
import datetime
from pathlib import Path
from task_files.document_processor import (
    DocumentProcessor,
    calculate_checksum,
    format_timestamp,
    sanitize_filename,
    parse_metadata,
    validate_document_type
)
from task_files.utils import generate_document_id

def test_functions_moved_correctly():
    """Test that functions exist in the correct modules"""
    # These should be in document_processor.py
    assert hasattr(calculate_checksum, '__call__')
    assert hasattr(format_timestamp, '__call__')
    assert hasattr(sanitize_filename, '__call__')
    assert hasattr(parse_metadata, '__call__')
    assert hasattr(validate_document_type, '__call__')
    
    # This should be in utils.py
    assert hasattr(generate_document_id, '__call__')

def test_function_behavior_unchanged():
    """Test that all functions maintain their original behavior"""
    # Test generate_document_id
    doc_id = generate_document_id()
    assert isinstance(doc_id, str)
    assert len(doc_id) == 36  # UUID4 length
    
    # Test format_timestamp
    dt = datetime.datetime(2023, 1, 1, 12, 0, 0)
    assert format_timestamp(dt) == "2023-01-01T12:00:00.000000Z"
    
    # Test sanitize_filename
    assert sanitize_filename('test file?.txt') == 'test_file.txt'
    assert sanitize_filename('test/file.txt') == 'testfile.txt'
    
    # Test validate_document_type
    assert validate_document_type('pdf', ['pdf', 'docx']) is True
    assert validate_document_type('jpg', ['pdf', 'docx']) is False
    
    # Test parse_metadata
    valid_metadata = {'title': 'Test', 'author': 'John'}
    assert parse_metadata(valid_metadata) == valid_metadata
    with pytest.raises(ValueError):
        parse_metadata({'title': 'Test'})  # Missing author

def test_document_processor_integration():
    """Test that DocumentProcessor works correctly with the moved functions"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test document
        doc_path = Path(temp_dir) / 'test.txt'
        with open(doc_path, 'w') as f:
            f.write('test content')
        
        # Create processor instance
        processor = DocumentProcessor(temp_dir)
        
        # Process document
        metadata = {'title': 'Test Doc', 'author': 'Test Author'}
        result = processor.process_document(str(doc_path), metadata)
        
        # Verify result
        assert 'id' in result
        assert result['original_filename'] == 'test.txt'
        assert result['clean_filename'] == 'test.txt'
        assert 'checksum' in result
        assert 'processed_at' in result
        assert result['metadata'] == metadata
        assert result['file_type'] == 'txt'

def test_imports():
    """Test that imports are correctly organized"""
    import inspect
    import task_files.utils as utils_module
    import task_files.document_processor as processor_module
    
    # Check utils.py only has generate_document_id
    utils_functions = [name for name, _ in inspect.getmembers(utils_module, inspect.isfunction)]
    assert utils_functions == ['generate_document_id']
    
    # Check document_processor.py has all other functions
    processor_functions = [name for name, _ in inspect.getmembers(processor_module, inspect.isfunction)]
    assert set(processor_functions) == {
        'calculate_checksum',
        'format_timestamp',
        'sanitize_filename',
        'parse_metadata',
        'validate_document_type'
    }

if __name__ == "__main__":
    pytest.main([__file__])