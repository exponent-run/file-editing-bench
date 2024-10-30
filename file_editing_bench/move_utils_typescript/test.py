import os
import ast
import re

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def test_function_locations():
    """Test that functions are in their correct locations after the move"""
    # Read both files
    utils_content = read_file('task_files/utils.ts')
    inventory_content = read_file('task_files/inventory.ts')
    
    # Functions that should be moved to inventory.ts
    functions_to_move = [
        'calculateDiscount',
        'formatCurrency',
        'generateItemDescription',
        'sortByRarity',
        'calculateTotalValue'
    ]
    
    # Function that should stay in utils.ts
    function_to_keep = 'validateItemName'
    
    # Check utils.ts
    for func in functions_to_move:
        assert func not in utils_content, f"Function {func} should not be in utils.ts"
    assert function_to_keep in utils_content, f"Function {function_to_keep} should remain in utils.ts"
    
    # Check inventory.ts
    for func in functions_to_move:
        assert func in inventory_content, f"Function {func} should be in inventory.ts"

def test_imports():
    """Test that imports are correctly updated"""
    inventory_content = read_file('task_files/inventory.ts')
    utils_content = read_file('task_files/utils.ts')
    
    # Check utils.ts imports
    assert 'import { DateTime }' not in utils_content, "DateTime import should be removed from utils.ts"
    assert 'import { ItemRarity, InventoryItem }' not in utils_content, "ItemRarity import should be removed from utils.ts"
    assert 'import { z }' in utils_content, "zod import should remain in utils.ts"
    
    # Check inventory.ts imports
    assert 'import { validateItemName }' in inventory_content, "validateItemName should be imported in inventory.ts"
    assert 'from \'./utils\'' in inventory_content, "utils import path should be correct"
    assert 'import { DateTime }' in inventory_content, "DateTime import should be in inventory.ts"

def test_schema_location():
    """Test that the itemNameSchema is in utils.ts"""
    utils_content = read_file('task_files/utils.ts')
    inventory_content = read_file('task_files/inventory.ts')
    
    assert 'itemNameSchema' in utils_content, "itemNameSchema should be in utils.ts"
    assert 'itemNameSchema' not in inventory_content, "itemNameSchema should not be in inventory.ts"

if __name__ == "__main__":
    test_function_locations()
    test_imports()
    test_schema_location()
    print("All tests passed!")