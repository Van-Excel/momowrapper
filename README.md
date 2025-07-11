# momowrapper
📘 MoMo Wallet API Wrapper

A production-ready microservice for handling wallet management and mobile money (MoMo) transactions, built with FastAPI, PostgreSQL, Docker, and Alembic. Designed for scalability, reliability, and ease of integration.

🚀 Features

🔐 User Authentication with JWT

💻 Wallet Management with UUID identifiers

💰 MoMo Deposit Flow (pending setup)

📦 PostgreSQL + Async SQLAlchemy

📄 Auto-generated API docs with Swagger & ReDoc

📊 Adminer for database inspection

🐳 Dockerized for local development

🔄 Alembic for migrations

✅ Structured for testing and CI/CD

💠 Tech Stack

FastAPI

PostgreSQL

SQLAlchemy (async)

Alembic (migrations)

Docker & Docker Compose

JWT (via python-jose)

Passlib (password hashing)

📂 Project Structure

app/
├── api/            # API routers
├── core/           # Security, config
├── crud/           # DB logic
├── db/             # DB session & base
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas
├── main.py         # Entry point
alembic/            # DB migrations
.env                # Environment variables
docker-compose.yml  # Dev container setup

⚙️ Getting Started

1️⃣ Clone the repo

git clone https://github.com/yourusername/momo-wrapper.git
cd momo-wrapper

2️⃣ Create .env

Create an .env file with your own secure values:

DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>:<port>/<database>
SECRET_KEY=your_very_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

3️⃣ Run with Docker

docker-compose up --build

FastAPI: http://localhost:8000

Docs: http://localhost:8000/docs

Adminer: http://localhost:8080 (default credentials set in Docker Compose)

🥪 Running Migrations

docker-compose exec web alembic revision --autogenerate -m "init"
docker-compose exec web alembic upgrade head

🛡 Key Endpoints

Method

Path

Description

POST

/api/v1/register

Register new user

POST

/api/v1/login

Login and get token

GET

/api/v1/me

Get current wallet info

POST

/api/v1/deposit

(Soon) Initiate deposit

🛡 Security

JWT-based auth (Authorization: Bearer <token>)

Passwords securely hashed with bcrypt/passlib

Environment variables for sensitive data

🧰 Roadmap

This roadmap covers all critical features needed to build a reliable MoMo transaction service, from user management to financial flows and production readiness.

✅ Done

User model and UUID-based identification

User registration and login

Secure password hashing and JWT auth

Wallet creation and retrieval logic

Alembic for migrations

Dockerized PostgreSQL, FastAPI, Adminer

Basic error handling and validation

.env config loading and DB injection

🔜 In Progress / Next
Deposit Request Logic Implementation


📝 License

MIT License. Built with ❤️ by [Vanexcel].

