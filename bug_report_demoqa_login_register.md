## DemoQA Login & Register - Bug Report

**Date:** 2026-01-30  
**Tester:** Senior QA (automated + exploratory)  
**Scope:** https://demoqa.com/login, https://demoqa.com/register  

### Test Environment
- OS: Linux 6.1.147
- Browser: Google Chrome 143.0.7499.146 (headless)
- Automation: Selenium (Python)

### Test Summary
Focused on core login and registration form behavior, validation, and error handling.

**High-level results**
- Login with invalid credentials shows the expected error message.
- Registration flow is blocked by reCAPTCHA (expected).
- Multiple validation gaps and UI inconsistencies found (details below).

---

## Defects

### BUG-001 — Login form allows empty submit with no feedback
**Severity:** Medium  
**Priority:** P2  
**Area:** Login (/login)

**Steps to Reproduce**
1. Open https://demoqa.com/login
2. Leave *User Name* and *Password* blank
3. Click **Login**

**Expected Result**
User sees validation errors indicating required fields.

**Actual Result**
No validation message is shown; UI gives no feedback.

**Impact**
User confusion and poor UX; no guidance on required inputs.

---

### BUG-002 — Register form allows empty submit with no feedback
**Severity:** Medium  
**Priority:** P2  
**Area:** Register (/register)

**Steps to Reproduce**
1. Open https://demoqa.com/register (or click **New User** from login)
2. Leave all fields blank
3. Click **Register**

**Expected Result**
Field-level validation errors should display for required inputs.

**Actual Result**
No validation messages appear; UI provides no feedback.

**Impact**
User confusion; unclear why registration did not proceed.

---

### BUG-003 — Duplicate error message for missing reCAPTCHA
**Severity:** Low  
**Priority:** P3  
**Area:** Register (/register)

**Steps to Reproduce**
1. Open https://demoqa.com/register
2. Fill fields with valid data (e.g., First Name, Last Name, User Name, Password)
3. Leave reCAPTCHA unchecked
4. Click **Register**

**Expected Result**
Single error message prompting reCAPTCHA verification.

**Actual Result**
Same error text appears twice on the page (duplicate message).

**Impact**
Minor UI inconsistency; can reduce clarity and polish.

---

## Notes
- Registration cannot be completed without reCAPTCHA; testing focused on client-side validation and error handling.
- No functional errors observed for invalid-login handling (error displays correctly).
