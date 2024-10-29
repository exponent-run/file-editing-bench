# Combine Authentication Functions

Move the `createSessionToken` function from `sessionManager.ts` into `userAuthentication.ts`. The function should be placed after the existing functions in `userAuthentication.ts` and should maintain its exact implementation and documentation. The `sessionManager.ts` file should be deleted after the move.

## Requirements:
1. Move the `createSessionToken` function from `sessionManager.ts` to `userAuthentication.ts`
2. Place it after the existing functions in `userAuthentication.ts`
3. Keep the function's implementation and documentation exactly the same
4. Delete the `sessionManager.ts` file
5. Make no other changes to any code or documentation

## Success Criteria:
- The `createSessionToken` function is now in `userAuthentication.ts`
- The function's implementation and documentation are unchanged
- The `sessionManager.ts` file no longer exists
- No other code changes have been made