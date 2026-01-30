 # DemoQA Login & Register - QA Bug Report
 
 Date: 2026-01-30  
 Target: https://demoqa.com/login and https://demoqa.com/register  
 Environment: Linux 6.1.147, curl (API-backed validation)
 
 ## Scope
 The UI pages are a SPA served from `/login` and `/register`. In this
 environment I validated the backend endpoints used by the UI (Account
 APIs) to cover login and registration behavior.
 
 ### Endpoints tested
 - POST https://demoqa.com/Account/v1/User (register)
 - POST https://demoqa.com/Account/v1/GenerateToken (auth token)
 - POST https://demoqa.com/Account/v1/Login (login)
 
 ### Test data
 - Valid password: `Aa1!aaaa` (meets policy)
 - Invalid password: `abc`
 - New user: `qa_demo_<timestamp>`
 
 ## Summary
 Registration succeeds with a valid password and fails with a weak
 password with a clear error message. However, several security and API
 contract issues were found in the login/token flow.
 
 ---
 
 ## Bugs
 
 ### 1) Plaintext password exposed in login response and JWT payload
 **Severity:** Critical (Security)  
 **Endpoint:** POST `/Account/v1/Login`
 
 **Steps to reproduce**
 1. Register a user:
    ```bash
    curl -X POST https://demoqa.com/Account/v1/User \
      -H "Content-Type: application/json" \
      -d '{"userName":"qa_demo_1769756223","password":"Aa1!aaaa"}'
    ```
 2. Login with the same credentials:
    ```bash
    curl -X POST https://demoqa.com/Account/v1/Login \
      -H "Content-Type: application/json" \
      -d '{"userName":"qa_demo_1769756223","password":"Aa1!aaaa"}'
    ```
 
 **Actual result**
 - Response body includes the plaintext password:
   ```json
   {
     "userId":"...",
     "username":"qa_demo_1769756223",
     "password":"Aa1!aaaa",
     "token":"<jwt>",
     ...
   }
   ```
 - The JWT payload also contains the plaintext password when decoded.
 
 **Expected result**
 - Password should never be returned in any response body.
 - JWT payload should not include sensitive credentials.
 
 **Impact**
 - Credentials are exposed to any client, network capture, logs, and
   third-party tooling. This is a critical security leak.
 
 ---
 
 ### 2) Login returns HTTP 200 with empty body on invalid credentials
 **Severity:** Medium  
 **Endpoint:** POST `/Account/v1/Login`
 
 **Steps to reproduce**
 ```bash
 curl -i -X POST https://demoqa.com/Account/v1/Login \
   -H "Content-Type: application/json" \
   -d '{"userName":"qa_demo_1769756223","password":"BadPass1!"}'
 ```
 
 **Actual result**
 - HTTP status: `200 OK`
 - Empty response body
 
 **Expected result**
 - HTTP status should indicate auth failure (401/403)
 - Response should include a clear error message
 
 **Impact**
 - Clients cannot reliably detect failed authentication and may treat
   the request as success based on HTTP 200.
 
 ---
 
 ### 3) GenerateToken returns HTTP 200 on failed authentication
 **Severity:** Medium  
 **Endpoint:** POST `/Account/v1/GenerateToken`
 
 **Steps to reproduce**
 ```bash
 curl -i -X POST https://demoqa.com/Account/v1/GenerateToken \
   -H "Content-Type: application/json" \
   -d '{"userName":"qa_demo_1769756223","password":"BadPass1!"}'
 ```
 
 **Actual result**
 - HTTP status: `200 OK`
 - Body: `{"token":null,"expires":null,"status":"Failed","result":"User authorization failed."}`
 
 **Expected result**
 - HTTP status should be 401/403 for invalid credentials
 - Error response should be consistent with login failure handling
 
 **Impact**
 - Error handling is inconsistent and can confuse client-side logic,
   leading to false positives in auth flows.
 
 ---
 
 ## Notes
 - UI verification (manual interaction) was not executed here because the
   environment does not provide a browser; the Account API results are
   expected to reflect the login/register behavior used by the UI.
 - Registration password validation behaves correctly (400 + clear
   message) when the password does not meet the policy.
