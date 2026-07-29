# API Test Cases - AI Chatbot API

## TC_API_001 - Health Check API

Endpoint:
GET /api/health

Steps:
1. Send GET request to /api/health
2. Verify response status code
3. Verify response body

Expected Result:
- Status code should be 200 OK
- Response should contain status "ok"


---

## TC_API_002 - Send Valid Chat Message

Endpoint:
POST /api/chat

Request Body:

{
  "message": "Hello AI"
}

Steps:
1. Send POST request with valid message
2. Verify response

Expected Result:
- Status code should be 200 OK
- Response should contain generated reply


---

## TC_API_003 - Send Empty Message

Endpoint:
POST /api/chat

Request Body:

{
  "message": ""
}

Steps:
1. Send request with empty message
2. Verify validation response

Expected Result:
- Status code should be 400 Bad Request
- Error message should be:
"Message is required"


---

## TC_API_004 - Missing Message Field

Endpoint:
POST /api/chat

Request Body:

{
}

Steps:
1. Send request without message field
2. Verify API validation

Expected Result:
- Status code should be 400 Bad Request
- Error response should be returned


---

## TC_API_005 - Long Message Test

Endpoint:
POST /api/chat

Test Data:
1000+ character message

Steps:
1. Send very long message
2. Observe API behavior

Expected Result:
- API should not crash
- Response should be returned successfully