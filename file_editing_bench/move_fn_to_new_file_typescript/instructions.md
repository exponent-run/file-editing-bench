# Move Time Series Processing Function to Utility File

## Task Description

Move the `preprocessTimeSeriesData` function from `DataVisualization.ts` to a new utility file called `timeSeriesUtils.ts`. The function should:

1. Be moved to the new file and exported as a named export
2. Be updated to accept the same parameters and return the same type
3. Have all necessary types imported from the types.ts file
4. Be imported and used correctly in the original DataVisualization.ts file

The function should maintain exactly the same functionality but be moved to a more appropriate location for better code organization.

## Success Criteria

- A new file `timeSeriesUtils.ts` is created with the moved function
- The original `DataVisualization.ts` file imports and uses the moved function
- All type imports are correctly maintained
- The function's implementation remains unchanged
- The code compiles without any TypeScript errors