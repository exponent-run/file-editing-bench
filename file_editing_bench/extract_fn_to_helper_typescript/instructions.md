# Extract Platform Metrics Calculation Helper

## Task Description

In the file `analytics.ts`, there is a method `processUserEngagement` in the `AnalyticsProcessor` class that processes user analytics events. Your task is to extract the event processing loop into a helper function with these exact specifications:

1. Create a new helper function called `calculatePlatformMetrics` within the `AnalyticsProcessor` class
2. The function should:
   - Take parameter: `events: UserEvent[]`
   - Return type: `[{ [key: string]: number }, number, Set<string>]` (platform counts, total session time, and unique users set)
   - Extract the following logic from the main function:
     - Platform counting
     - Session time calculation
     - Unique active users tracking

3. The main `processUserEngagement` method should call this helper function and use its return values

## Function Signature

The helper function should have exactly this signature:
```typescript
private calculatePlatformMetrics(events: UserEvent[]): [{ [key: string]: number }, number, Set<string>]
```

## Expected Behavior

- The helper function should maintain exactly the same logic as the original code
- The main function should use destructuring to receive the helper function's return values
- The final results of `processUserEngagement` should remain exactly the same

The goal is to improve code organization by extracting the event processing logic into a reusable helper function while maintaining the exact same functionality.