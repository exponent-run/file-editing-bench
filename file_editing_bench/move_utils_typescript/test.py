import os
import ast
import re
from typing import List, Set

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()

def get_function_names(content: str) -> Set[str]:
    """Extract function names from TypeScript content using regex"""
    # Match both regular functions and arrow functions
    pattern = r'(?:function\s+(\w+)|(?:export\s+)?const\s+(\w+)\s*=\s*(?:function|\([^)]*\)\s*=>))'
    matches = re.finditer(pattern, content)
    names = set()
    for match in matches:
        # Add whichever group matched (regular function or arrow function)
        names.add(match.group(1) if match.group(1) else match.group(2))
    return names

def get_imports(content: str) -> Set[str]:
    """Extract imported symbols from TypeScript content using regex"""
    # Match both named imports and default imports
    pattern = r'import\s*{([^}]+)}|\bimport\s+(\w+)\s+from'
    matches = re.finditer(pattern, content)
    imports = set()
    for match in matches:
        if match.group(1):  # Named imports
            imports.update(name.strip() for name in match.group(1).split(','))
        elif match.group(2):  # Default import
            imports.add(match.group(2))
    return imports

def test_function_locations():
    """Test that functions are in their correct locations after the move"""
    utils_content = read_file('file_editing_bench/move_utils_typescript/task_files/utils.ts')
    transaction_content = read_file('file_editing_bench/move_utils_typescript/task_files/transactionProcessor.ts')
    
    # Get function names from both files
    utils_functions = get_function_names(utils_content)
    transaction_functions = get_function_names(transaction_content)
    
    # Check that validateAmount is the only function in utils.ts
    assert 'validateAmount' in utils_functions, "validateAmount should be in utils.ts"
    assert len(utils_functions) == 1, "utils.ts should only contain validateAmount"
    
    # Check that all other utility functions are in transactionProcessor.ts
    expected_functions = {'validateDate', 'formatCurrency', 'sanitizeInput', 
                         'generateTransactionId', 'parseCSVRow'}
    for func in expected_functions:
        assert func in transaction_functions, f"{func} should be in transactionProcessor.ts"

def test_imports():
    """Test that imports are correctly updated"""
    utils_content = read_file('file_editing_bench/move_utils_typescript/task_files/utils.ts')
    transaction_content = read_file('file_editing_bench/move_utils_typescript/task_files/transactionProcessor.ts')
    
    # Check utils.ts imports
    utils_imports = get_imports(utils_content)
    required_utils_imports = {'BigNumber', 'Either', 'left', 'right', 'isEmpty'}
    for imp in required_utils_imports:
        assert imp in utils_imports, f"{imp} should be imported in utils.ts"
    
    # Check transactionProcessor.ts imports
    transaction_imports = get_imports(transaction_content)
    assert 'validateAmount' in transaction_imports, "validateAmount should be imported in transactionProcessor.ts"
    
    # Check that moved function dependencies are imported
    required_transaction_imports = {'format', 'BigNumber', 'Either', 'left', 'right', 
                                  'pipe', 'z', 'readFileSync', 'isEmpty'}
    for imp in required_transaction_imports:
        assert imp in transaction_imports, f"{imp} should be imported in transactionProcessor.ts"

if __name__ == "__main__":
    test_function_locations()
    test_imports()
    print("All tests passed!")