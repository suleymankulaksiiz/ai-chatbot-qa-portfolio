# Bug Report - Chat Message Length

## Bug ID
BUG-002

## Title
Chat allows extremely long messages without validation.

## Severity
Medium

## Priority
Medium

## Environment
- Windows 10
- Chrome Latest
- Localhost:3000

## Preconditions
User is logged into chatbot application.

## Steps to Reproduce

1. Open chatbot page
2. Enter a very long message (5000+ characters)
3. Click Send button

## Actual Result

The application accepts the message without any limitation.

## Expected Result

The application should:
- Limit message length
- Display validation message

## Status

Open