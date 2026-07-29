# Login Test Cases

## TC_LOGIN_001 - Valid Login

**Precondition**
- User is on login page

**Steps**
1. Enter valid email
2. Enter valid password
3. Click Login button

**Test Data**
Email: test@test.com
Password: 123456

**Expected Result**
- User should navigate to chat page

**Status**
PASS


---

## TC_LOGIN_002 - Empty Email Validation

**Steps**
1. Leave email empty
2. Enter password
3. Click Login

**Expected Result**
- Error message should be displayed:
"Email and password are required"

**Status**
PASS


---

## TC_LOGIN_003 - Empty Password Validation

**Steps**
1. Enter email
2. Leave password empty
3. Click Login

**Expected Result**
- Error message should be displayed

**Status**
PASS