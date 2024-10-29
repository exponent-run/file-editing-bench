# Delete Function Task

In the file `analytics.ts`, delete the `calculateSessionDuration` function and its corresponding import `formatDistance` from 'date-fns' that is no longer used after the function is removed.

Note that since `calculateSessionDuration` is the only function using the `formatDistance` import, this import statement can be safely removed.