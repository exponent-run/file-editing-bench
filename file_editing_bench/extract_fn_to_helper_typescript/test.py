import os
import sys
import json
from typing import List, Dict, Any

def read_ts_file(filepath: str) -> str:
    with open(filepath, 'r') as f:
        return f.read()

def check_function_exists(content: str, function_name: str) -> bool:
    return f"function {function_name}" in content

def check_function_called(content: str, function_name: str) -> bool:
    return f"= {function_name}(" in content

def test_extraction():
    # Read the file content
    task_file = os.path.join(os.path.dirname(__file__), 'task_files', 'analytics.ts')
    file_content = read_ts_file(task_file)
    
    # Test 1: The helper function should exist
    assert check_function_exists(file_content, "findMostFrequentEvent"), \
        "Helper function 'findMostFrequentEvent' was not created"
    
    # Test 2: The helper function should be called in processUserAnalytics
    assert check_function_called(file_content, "findMostFrequentEvent"), \
        "Helper function 'findMostFrequentEvent' is not called in processUserAnalytics"
    
    # Test 3: The helper function should have the correct signature
    assert "function findMostFrequentEvent(eventCounts: Record<string, number>): string" in file_content, \
        "Helper function has incorrect signature"
    
    # Test 4: The original function should not contain the extracted logic
    assert "let maxCount = 0;" not in file_content or \
           "Object.entries(eventCounts).forEach(([eventType, count])" not in file_content, \
        "Original logic was not removed from processUserAnalytics"

if __name__ == "__main__":
    test_extraction()