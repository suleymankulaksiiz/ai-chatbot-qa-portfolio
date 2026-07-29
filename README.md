# AI Chatbot QA Portfolio

## Project Overview

This project is a QA Engineering portfolio project built around an AI Chatbot application.

The goal of this project is to demonstrate real-world software testing practices including:

* Manual Testing
* Test Case Design
* Bug Reporting
* API Testing
* UI Automation Testing
* Test Reporting

---

# Application

The application is a simple chatbot web application built with Node.js and Express.

## Features

* User login validation
* Chat interface
* Chat API endpoint
* Input validation
* Health check endpoint

---

# Tech Stack

## Application

* Node.js
* Express.js
* HTML
* CSS
* JavaScript

## Testing

* Playwright
* Postman
* Newman

## Documentation

* Markdown
* HTML Test Reports

---

# QA Coverage

## Manual Testing

Location:

```
manual-tests/
```

Covered scenarios:

* Login test cases
* Chat functionality test cases
* Negative test scenarios

---

## Bug Reports

Location:

```
bug-reports/
```

Documented issues:

* Empty password validation issue
* Long chat message issue
* XSS vulnerability scenario

---

## UI Automation Testing

Location:

```
automation/
```

Framework:

* Playwright

Automated scenarios:

* Valid login
* Empty password validation
* Empty email validation

Run tests:

```bash
cd automation
npx playwright test
```

---

# API Testing

Location:

```
api-tests/
```

Tools:

* Postman
* Newman

Tested endpoints:

## Health Check

```
GET /api/health
```

Validation:

* Status code 200
* API availability

## Chat API

```
POST /api/chat
```

Validation:

* Successful message response
* Empty message validation
* Missing message validation

---

# API Automation Results

Newman Test Report:

```
Requests: 4
Assertions: 6
Failures: 0
Average Response Time: 6ms
```

HTML report:

```
api-tests/reports/api-test-report.html
```

---

# Project Structure

```
ai-chatbot-qa-portfolio

├── app
│   └── Chatbot Application
│
├── automation
│   └── Playwright Tests
│
├── api-tests
│   ├── Postman Collection
│   ├── API Test Cases
│   └── Newman Reports
│
├── manual-tests
│   └── Manual Test Cases
│
├── bug-reports
│   └── Bug Documentation
│
└── docs
    └── Test Plan
```

---

# Future Improvements

Planned improvements:

* AI response testing
* LLM output validation
* Performance testing
* Database testing
* CI/CD pipeline integration
* Docker environment

---


```
```
