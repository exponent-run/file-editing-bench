# Move Utility Functions Task

## Task Description

You have two TypeScript files:
1. `transactionProcessor.ts` - Contains the main business logic for processing financial transactions
2. `utils.ts` - Contains utility functions used by the transaction processor

Your task is to move all utility functions except `validateAmount` from `utils.ts` into `transactionProcessor.ts`. The `validateAmount` function should remain in `utils.ts`.

## Specific Requirements

1. Move these functions from `utils.ts` to `transactionProcessor.ts`:
   - `validateDate`
   - `formatCurrency`
   - `sanitizeInput`
   - `generateTransactionId`
   - `parseCSVRow`

2. Leave this function in `utils.ts`:
   - `validateAmount`

3. Update all imports in both files accordingly:
   - Remove unused imports from `utils.ts`
   - Move required imports to `transactionProcessor.ts` if they're needed for the moved functions
   - Update the import statement in `transactionProcessor.ts` to only import `validateAmount` from `utils.ts`

4. Maintain the exact same functionality - only the location of the functions should change.

## Success Criteria

1. `utils.ts` should only contain the `validateAmount` function and its required imports
2. `transactionProcessor.ts` should contain all other utility functions
3. All imports should be properly maintained and updated
4. All tests should pass, indicating that the functionality remains unchanged