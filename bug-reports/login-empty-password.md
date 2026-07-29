# Bug Report - Login Validation

## Bug ID
BUG-001

## Title
Login allows navigation when only whitespace is entered.

## Severity
Medium

## Priority
High

## Environment
- Windows 10
- Chrome Latest
- Localhost:3000

## Preconditions
Application is running.

## Steps to Reproduce

1. Open Login page
2. Enter spaces in Email field
3. Enter spaces in Password field
4. Click Login

## Actual Result

User is redirected to Chat page.

## Expected Result

Validation should reject whitespace-only input and display an error message.

## Status

Open