# Task: Reorder Methods in DataAnalytics Class

Reorder the methods in the `DataAnalytics.ts` file to follow this logical grouping and sequence:

1. Constructor and core data access methods should be first:
   - constructor
   - getData
   - addDataPoint

2. Private utility/validation methods should be next:
   - validateData
   - processData

3. Calculation methods should be grouped together:
   - calculateMean
   - calculateMedian
   - calculateStandardDeviation

4. Result retrieval method should be last:
   - getProcessedResults

Do not modify any method implementations - only change their order within the class. Maintain the exact same code within each method, including whitespace and comments.