# Inline Function Task

In the file `processUserData.ts`, inline the `validateEmailFormat` helper function directly into the `processUserRegistration` function where it's being called. After inlining, delete the original `validateEmailFormat` function.

The email validation logic should be inserted directly where the `validateEmailFormat()` function is called in the if statement, and the original helper function should be removed entirely.

This task requires:
1. Moving the email validation logic into the `processUserRegistration` function
2. Removing the original `validateEmailFormat` function declaration
3. Maintaining the exact same functionality and validation logic
4. Keeping all type annotations and interfaces unchanged
5. Maintaining the same amount of whitespace between functions and declarations
