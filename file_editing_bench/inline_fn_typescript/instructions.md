# Inline Function Task

In the file `processUserData.ts`, there is a helper function `validateEmailFormat` that is only used once within the `processUserRegistration` function.

Your task is to:
1. Remove the `validateEmailFormat` function
2. Replace the call to `validateEmailFormat` in `processUserRegistration` with the actual implementation of the email validation logic
3. Keep all the functionality exactly the same

The email validation logic should be inlined exactly where the function was called, maintaining the same behavior but removing the separate function definition.