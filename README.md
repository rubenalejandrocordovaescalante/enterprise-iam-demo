# Enterprise IAM Security Demo (OIDC + SCIM + RBAC + Zero Trust)

This repository is a practical demonstration of **Enterprise Identity and Access Management (IAM)** concepts implemented using Python and Flask.

It simulates real-world security systems used in cloud platforms such as authentication, authorization, role-based access control, and API security.

---

## Project Structure

```
1. OIDC Enterprise Login Demo/          → Google OIDC Authentication Demo
2. SCIM Provisioning API Demo/          → SCIM-style User Provisioning API
3. RBAC Authorization Platform/                → Role-Based Access Control (RBAC)
4. Zero Trust API Gateway Demo/      → API Key + Device Trust Security Model
```

---

## 1. OIDC Login (Authentication)

- Google OAuth / OpenID Connect login
- User session management
- Identity-based authentication flow

Demonstrates how users log in using external identity providers.

---

## 2. SCIM User Provisioning

- Create users via REST API
- List users
- Soft delete (deactivate users)

Simulates enterprise user lifecycle management.

---

## 3. RBAC (Role-Based Access Control)

- Roles: admin, employee, security analyst
- Permission-based access checks
- Access decision engine

Demonstrates authorization based on roles.

---

## 4. Zero Trust API Security

- API key authentication
- Device trust validation
- Audit logging
- Secure endpoint protection

Simulates Zero Trust security principles used in modern systems.

---

## Purpose of This Project

This project was built to demonstrate:

- Authentication (OIDC)
- Authorization (RBAC)
- Identity lifecycle (SCIM)
- API security (Zero Trust)

It reflects real enterprise IAM architecture used in cloud environments.

---

## Tech Stack

- Python
- Flask
- Authlib (OIDC integration)
- REST APIs
- JSON-based data handling

---

## Screenshots

Each module contains its own screenshots folder showing:

- API requests
- JSON responses
- Security decisions (allow/deny)

---

## Note

This is a **learning / portfolio project** and not intended for production use.

---

## Author

Ruben Alejandro Cordova Escalante
