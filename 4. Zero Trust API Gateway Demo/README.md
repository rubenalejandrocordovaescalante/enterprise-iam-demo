# Zero Trust API Gateway

This project demonstrates a simplified Zero Trust API security architecture using Python Flask.

The platform simulates how enterprise infrastructure validates every request before granting access to protected resources.

## Features

- API key validation
- Device trust verification
- Request auditing
- Continuous verification concepts
- Secure access enforcement

## Technologies

- Python
- Flask
- REST APIs

## Zero Trust Principles Demonstrated

- Never trust by default
- Verify every request
- Validate identity continuously
- Enforce device trust
- Audit all access attempts

## Example Request

```bash
curl -H "X-API-KEY: admin-key" \
http://127.0.0.1:5000/secure-data
```

## Security Concepts Demonstrated

- Zero Trust Security
- Access Verification
- Identity Validation
- Device Trust Policies
- Secure API Gateways
- Continuous Authentication

## Enterprise Relevance

Zero Trust models are widely used in:
- Cloud Infrastructure
- Enterprise VPN Alternatives
- Secure Remote Access
- Corporate APIs
- Internal Microservices

## Run

```bash
pip install -r requirements.txt

python app.py
```

## Zero Trust API Security Demo

### Admin Access Granted

```bash
curl -H "X-API-KEY: admin-key" http://127.0.0.1:5000/secure-data
```

![Admin Access](screenshots/01_admin.png)

### Employee Access Granted

```bash
curl -H "X-API-KEY: employee-key" http://127.0.0.1:5000/secure-data
```

![Employee Access](screenshots/02_employee.png)

### Missing API Key

```bash
curl http://127.0.0.1:5000/secure-data
```

![Missing Key](screenshots/03_missing.png)

### Invalid API Key

```bash
curl -H "X-API-KEY: wrong" http://127.0.0.1:5000/secure-data
```

![Invalid Key](screenshots/04_invalid.png)

## Educational Purpose

This project demonstrates modern enterprise security principles commonly used in cybersecurity and cloud-native environments.
