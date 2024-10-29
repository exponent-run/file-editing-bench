# Delete Permission Check Function

In the `userService.ts` file, there is a permission check function called `validateUserPermissions` that is used inside the `updateUserProfile` method. Your task is to:

1. Delete the entire `validateUserPermissions` helper function
2. Remove the permission check from the `updateUserProfile` method (specifically, remove the if-statement that uses `validateUserPermissions`)

The permission check is no longer needed as the service will handle permissions at a different layer.

Note: Make sure to maintain proper formatting and not introduce any additional changes to the code.