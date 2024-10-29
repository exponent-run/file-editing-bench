# Function Reordering Task

Reorder the functions in `dataProcessing.ts` to group them logically according to their purpose. The functions should be arranged in the following order:

1. First, keep the `DataPoint` interface at the top
2. Then, group the basic statistical functions together in this order:
   - `findMinValue`
   - `findMaxValue`
   - `calculateAverage`
3. Next, group the data transformation functions together in this order:
   - `normalizeData`
   - `standardizeData`
4. Then, group the data organization functions together in this order:
   - `sortByTimestamp`
   - `filterByTimeRange`
   - `groupByLabel`

Do not modify any of the function implementations - only their order in the file should change.