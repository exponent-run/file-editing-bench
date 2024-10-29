# Delete Legacy Admin Check Function

## Task

In the file `authService.ts`, remove the legacy special admin check functionality. This includes:

1. Delete the `isSpecialAdminUser` method
2. Remove the call to `isSpecialAdminUser` in the `validateUserAccess` method, including the if statement and its block
3. Remove the `adminEmails` private field as it's no longer needed

The task represents a common real-world scenario where legacy code needs to be removed as part of a migration to a new authentication system.

## Notes
- Keep all other functionality intact
- Maintain proper TypeScript syntax
- Preserve all other methods and their implementations
- Keep all imports and exports as they are