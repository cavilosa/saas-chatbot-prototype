# 🤖 SaaS AI Chatbot Prototype

## 📖 Table of Contents

- [Executive Summary](#-executive-summary)
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Getting Started](#-getting-started)
- [Configuration](#️-configuration)
- [Usage](#️-usage)
- [Security Considerations](#️-security-considerations)
- [Project Roadmap & Archival Status](#️-project-roadmap--archival-status)
- [Let's Connect](#-lets-connect)

> [!IMPORTANT]
> **Project Archival Notice (May 2026)**
> This repository is now archived and serves as a static portfolio piece. It successfully fulfilled its goal of exploring secure SaaS authentication (OAuth 2.0) and foundational API security. I am cur[...]

## 🎯 Executive Summary

**A secure, multi-tenant SaaS application prototype built with Flask and Python, demonstrating secure authentication with OAuth 2.0 (Auth0) and defensive measures like API rate limiting.**

## 🌟 Project Overview

The goal of this project was to build a functional prototype of a Software-as-a-Service (SaaS) chatbot with a primary focus on implementing security best practices from the ground up. The applicat[...]

## ✨ Features

- 🔐 **Secure User Authentication**: User registration and login handled via Auth0 using the OAuth 2.0 protocol.
- 👤 **Role-Based Access Control (RBAC)**: Differentiated permissions for standard users and administrators.
- 💬 **Interactive Chat Interface**: A clean and simple front-end for users to interact with the chatbot.
- 🛡️ **Secure Session Management**: Implementation of secure, server-side session handling.
- 🚦 **Rate Limiting**: Defensive measures implemented to protect API endpoints from abuse.

## 💻 Technology Stack

- **Backend**: Python 3.10+, Flask
- **Authentication**: Auth0 (OAuth 2.0, OpenID Connect)
- **Database**: Flask-SQLAlchemy (with SQLite for development)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Docker, Fly.io (via GitHub Actions)

## 🚀 Getting Started

Follow these instructions to get a local copy of the project up and running for development and testing purposes.

### Prerequisites

- Python 3.10 or later
- pip and venv
- An active Auth0 account

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cavilosa/saas-chatbot-prototype.git
   cd saas-chatbot-prototype
   ```

2. **Create and activate a virtual environment:**

   *For Linux/macOS:*
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   *For Windows:*
   ```bash
   py -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

The application requires several environment variables for configuration, particularly for connecting to Auth0.

1. Create a `.env` file in the root of the project directory.
2. Add the following variables to your `.env` file, replacing the placeholder values with your actual credentials from the Auth0 dashboard:

```env
# DATABASE setup
DATABASE_URL='sqlite:///app.db'
DATABASE_PASSWORD=''

# Flask Configuration
SECRET_KEY='a_very_strong_and_random_secret_key_here'
FLASK_ENV='development'

# Auth0 Configuration
AUTH0_CLIENT_ID='YOUR_AUTH0_CLIENT_ID'
AUTH0_CLIENT_SECRET='YOUR_AUTH0_CLIENT_SECRET'
AUTH0_DOMAIN='your-tenant.us.auth0.com'
```

## ▶️ Usage

Once the installation and configuration are complete, you can run the application locally.

1. **Run the Flask development server:**
   ```bash
   flask run
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`. You should see the application's home page with an option to log in.

## 🛡️ Security Considerations

As a security-focused project, the following areas were given special attention during development:

* **Authentication & Authorization**: Secure implementation of OAuth 2.0 to prevent token leakage or misuse. All sensitive endpoints are protected.
* **Session Management**: Protection against session fixation and hijacking.
* **Input Validation**: Sanitization of all user inputs to prevent injection attacks (e.g., XSS).
* **Secure Logging**: Logging security-relevant events without exposing sensitive information.

## 🗺️ Project Roadmap & Archival Status

* [x] **Phase 1: Setup & Foundations** - Basic Flask application factory, Dockerization, and automated deployment pipelines via GitHub Actions.
* [x] **Phase 2: Secure Identity** - Auth0 integration, OAuth 2.0 implementation, and secure session management.
* [ ] **Phase 3: AI Integration (Archived)** - Connect the backend to a language model to provide functional chat capabilities.
* [ ] **Phase 4: Advanced Hardening (Archived)** - Implementation of advanced rate limiting and comprehensive security auditing.

*Note: Phases 3 and 4 have been archived as my focus has shifted to enterprise cloud infrastructure and security governance.*

---

## 📫 Let's Connect

I am always open to discussing secure IT infrastructure, M365 automation, or cloud architecture.

* **LinkedIn:** [Maryna Korzhyk](https://www.linkedin.com/in/maryna-korzhyk-9339521b8/)
* **Professional Brand:** Follow **NorthShield Cyber** for my latest security mapping and architecture whitepapers.
