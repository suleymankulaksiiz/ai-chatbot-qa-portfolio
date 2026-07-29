![Playwright Tests](https://github.com/suleymankulaksiiz/ai-chatbot-qa-portfolio/actions/workflows/playwright.yml/badge.svg)
![Node.js](https://img.shields.io/badge/Node.js-20-green)
![Playwright](https://img.shields.io/badge/UI%20Testing-Playwright-blue)
![API Testing](https://img.shields.io/badge/API-Postman-orange)

# AI Chatbot QA Portfolio

## Project Overview

This project is a QA Engineering portfolio project built around an AI Chatbot web application.

The purpose of this project is to demonstrate real-world software testing practices including:

- Manual Testing
- Test Case Design
- Bug Reporting
- API Testing
- UI Automation Testing
- Test Reporting
- CI/CD Integration

---

# Application

The application is a chatbot web application built with Node.js and Express.

The project simulates a real software product where QA engineers validate functionality, API behavior, user flows, and automation scenarios.

## Features

- User login validation
- Chat interface
- Chat API endpoint
- Input validation
- Health check endpoint

---

# Tech Stack

## Application

- Node.js
- Express.js
- HTML
- CSS
- JavaScript

## Testing

- Playwright
- Postman
- Newman

## CI/CD

- GitHub Actions

## Documentation

- Markdown
- HTML Test Reports

---

# QA Coverage

## Manual Testing

Location:

```
manual-tests/
```

Covered scenarios:

- Login test cases
- Chat functionality test cases
- Negative test scenarios
- Input validation scenarios

---

# Bug Reports

Location:

```
bug-reports/
```

Documented issues:

- Empty password validation issue
- Long chat message issue
- XSS vulnerability scenario

Each bug report includes:

- Bug description
- Steps to reproduce
- Expected result
- Actual result
- Severity information

---

# UI Automation Testing

Location:

```
automation/
```

Framework:

- Playwright

Automated scenarios:

- Valid login
- Empty password validation
- Empty email validation

Run tests locally:

```bash
cd automation
npm install
npx playwright test
```

Test coverage includes:

- Positive login flow
- Negative validation scenarios
- UI element verification

---

# API Testing

Location:

```
api-tests/
```

Tools:

- Postman
- Newman

## Tested Endpoints

### Health Check API

```
GET /api/health
```

Validations:

- Status code 200
- API availability
- Response body validation


### Chat API

```
POST /api/chat
```

Validations:

- Successful message response
- Empty message validation
- Missing message validation

---

# API Automation Results

Newman execution results:

```
Requests: 4
Assertions: 6
Failures: 0
Average Response Time: 6ms
```

Generated HTML report:

```
api-tests/reports/api-test-report.html
```

---

# CI/CD Pipeline

GitHub Actions automatically runs Playwright tests whenever code is pushed to the main branch.

Pipeline flow:

```
Developer Push
        |
        ↓
GitHub Repository
        |
        ↓
GitHub Actions
        |
        ↓
Install Dependencies
        |
        ↓
Start Express Application
        |
        ↓
Run Playwright Tests
        |
        ↓
Test Result
```

Workflow file:

```
.github/workflows/playwright.yml
```

Current CI features:

✅ Automated Playwright execution  
✅ Automatic application startup  
✅ Browser installation in CI environment  
✅ Test result reporting  

---

# Project Structure

```
ai-chatbot-qa-portfolio

├── app
│   └── Chatbot Application
│
├── automation
│   ├── Playwright Configuration
│   └── UI Automation Tests
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
├── docs
│   └── Test Plan
│
└── .github
    └── workflows
        └── playwright.yml
```

---

# Future Improvements

Planned improvements:

- AI response quality testing
- LLM output validation
- Hallucination detection tests
- Prompt testing scenarios
- Performance testing
- Database testing
- Docker environment

---

# Author

Süleyman Kulaksız