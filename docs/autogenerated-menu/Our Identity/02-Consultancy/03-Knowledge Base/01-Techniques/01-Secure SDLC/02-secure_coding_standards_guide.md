# Secure Coding Standards Guide
### Writing Secure, Resilient, and Maintainable Software
## Introduction
Security is not something that can be added to a system after the fact. It must be designed and implemented from the start. Every line of code written has the potential to introduce vulnerabilities—whether that’s exposing sensitive data, allowing unauthorized access, or making systems easier to attack.

This guide outlines secure coding principles, not as a rigid set of rules, but as a mindset for engineering secure solutions. By following these practices, teams can prevent common vulnerabilities, ensure compliance, and build trust in the software they create.

## 1. Secure Input Handling and Validation
### Understanding the Risk
One of the most common ways attackers compromise systems is by sending malicious input—whether that’s attempting SQL injection, cross-site scripting (XSS), or command injection. Poorly validated input can allow attackers to manipulate system behaviour, extract sensitive data, or even execute arbitrary code.

### What Good Looks Like
Every system must validate, sanitize, and encode incoming data. This applies to form inputs, API requests, file uploads, command-line arguments, and database queries. It’s essential to reject unexpected or malformed input rather than trying to "fix" it, which can introduce further vulnerabilities.

### Putting It Into Practice
A strong validation strategy should use:

* Whitelisting (only allowing explicitly permitted input) rather than blacklisting (which attackers can often bypass).
* Parameterised queries to prevent SQL injection.
* Escaping output to prevent injection attacks like XSS.

For example, instead of dynamically constructing an SQL query using user input:

```python
query = f"SELECT * FROM users WHERE username = '{user_input}'"  # ❌ BAD: vulnerable to SQL injection
```

Use a **parameterised query** to ensure input is treated as data, not executable code:

```python
cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))  # ✅ SAFE: prevents SQL injection 
```

Similarly, any user-generated content displayed in a web page should be **escaped to prevent XSS:**

```python
import html
safe_output = html.escape(user_input)  # ✅ SAFE: encodes special characters```
```

## 2. Secure Authentication and Authorization
Understanding the Risk
A system is only as secure as its access controls. Weak authentication mechanisms can lead to account takeovers, while poor authorization checks can allow users to escalate their privileges or access data they shouldn’t.

### What Good Looks Like
Secure systems enforce:
* Strong authentication (e.g., Multi-Factor Authentication (MFA), secure password storage).
* Role-based or attribute-based access control (RBAC/ABAC) to limit access based on a user’s role.
* Short-lived session tokens to minimize risk if they are leaked.

### Putting It Into Practice
Passwords should never be stored in plaintext. Instead, they should be hashed and salted using a strong algorithm like bcrypt, Argon2, or PBKDF2:

```python
import bcrypt

hashed_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())  # ✅ SAFE: properly hashed
```
When working with APIs, JWTs (JSON Web Tokens) should be used cautiously:

```python
import jwt
from datetime import datetime, timedelta

payload = {"user": "admin", "exp": datetime.utcnow() + timedelta(hours=1)}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")  # ✅ SAFE: Expiry time prevents token misuse
```
Ensure that authentication and authorization checks are enforced on the server-side and not just in the frontend—as frontend protections can be bypassed.

## 3. Secure Error Handling and Logging
### Understanding the Risk
Errors are unavoidable, but how they are handled can be the difference between a secure system and a vulnerable one. Poor error handling can leak sensitive data, while improper logging may fail to detect and investigate attacks.

### What Good Looks Like
* Do not expose internal system details (such as stack traces) in error messages shown to users.
* Log security events in a structured way, but ensure sensitive data (passwords, API keys, JWTs) are never logged.
* Implement log monitoring and alerting to detect suspicious behaviour.

### Putting It Into Practice
When handling exceptions, avoid exposing internal details:

```javascript
try:
    user = get_user_by_id(user_id)
except Exception as e:
    logging.error(f"Database query failed: {e}")  # ✅ SAFE: Logs internally but not exposed
    return "Something went wrong. Please try again later."  # ✅ SAFE: Generic error message
Ensure logs are structured and easily searchable by using JSON-based logs rather than plaintext strings:
```

```json
{"event": "login_failure", "user": "john_doe", "reason": "invalid_password"}
```

## 4. Secure API Design and Communication
### Understanding the Risk
APIs are a common attack surface. Insecure API endpoints can expose sensitive data, allow unauthorized access, or be used for denial-of-service (DoS) attacks.

### What Good Looks Like
* All API traffic should be encrypted using TLS (HTTPS-only, TLS 1.3 preferred).
* API endpoints should be authenticated and rate-limited to prevent abuse.
* Secure headers should be set to prevent clickjacking and content sniffing attacks.

### Putting It Into Practice
Set security headers to harden API responses:

```javascript
response.headers["X-Frame-Options"] = "DENY"  # Prevents UI embedding attacks
response.headers["X-Content-Type-Options"] = "nosniff"  # Prevents MIME-type attacks
```

Rate-limit API requests to mitigate brute-force attacks:

```python
from flask_limiter import Limiter

limiter = Limiter(key_func=lambda: request.remote_addr)
@app.route("/api/data")
@limiter.limit("10 per minute")
def get_data():
    return "Secure API Response"
```

## 5. Secure File Handling and Storage
### Understanding the Risk
Unrestricted file uploads can allow attackers to upload and execute malicious files, while insecure storage can lead to data breaches.

### What Good Looks Like
* Restrict file types and sizes to prevent dangerous uploads.
* Use strong encryption for sensitive stored data.

### Putting It Into Practice
To ensure only safe file uploads, enforce whitelisted extensions:

```python
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
```

For sensitive data, encrypt it at rest:

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

encrypted_data = cipher.encrypt(b"Sensitive Data")  # ✅ SAFE: Encrypted before storage
```

## Bringing It All Together
Secure coding is not about ticking a box. It’s about embedding security into everyday engineering practices. By validating input, enforcing strong authentication, handling errors safely, securing APIs, and protecting sensitive data, we can build software that is not just functional, but also secure and resilient.

Security is a continuous process, and everyone on the team has a role to play. 