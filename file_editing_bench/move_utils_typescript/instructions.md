# Move Utility Functions Task

Your task is to reorganize the code by moving most utility functions from `utils.ts` into the main `inventory.ts` file, while keeping exactly one utility function in `utils.ts`.

## Requirements:

1. Move these utility functions from `utils.ts` to `inventory.ts`:
   - `calculateDiscount`
   - `formatCurrency`
   - `generateItemDescription`
   - `sortByRarity`
   - `calculateTotalValue`

2. Keep only this function in `utils.ts`:
   - `validateItemName` (along with its associated `itemNameSchema`)

3. Update all necessary imports in both files:
   - Remove unused imports from `utils.ts`
   - Add any required imports to `inventory.ts`
   - Update the import statement in `inventory.ts` to only import `validateItemName`

4. Maintain the exact same functionality - only the location of the functions should change.

## Success Criteria:
- `utils.ts` should contain only the `validateItemName` function and its schema
- `inventory.ts` should contain all other utility functions
- All imports should be correctly updated
- All tests should pass
- The functionality should remain identical