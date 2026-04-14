# CRISP — CRUD Resource Interface & Service Platform

A lightweight REST API built with **FastAPI** and **SQLite** for performing basic CRUD operations on user records. CRISP provides a simple, fast, and extensible foundation for managing resources through a clean HTTP interface.

## Features

- Create user records via a REST endpoint
- SQLite database for lightweight, file-based storage
- Pydantic data validation
- Auto-generated interactive API docs (Swagger UI)

## Project Structure

```
CRISP/
├── main.py                        # FastAPI application and route definitions
├── Database/
│   └── DatabaseOperations.py      # SQLite connection management
├── DataModel/
│   └── UserModel.py               # Pydantic model for user data
├── requirements..txt              # Python dependencies
└── LICENSE
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/CRISP.git
   cd CRISP
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r "requirements..txt"
   ```

## Usage

**Start the server**

```bash
python main.py
```

The API will be available at `http://localhost:8000`.

### Endpoints

| Method | Path      | Description          |
|--------|-----------|----------------------|
| GET    | `/`       | Health-check message |
| POST   | `/create` | Create a new user    |

### Example — Create a user

```bash
curl -X POST http://localhost:8000/create \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "last_name": "Doe", "address": "123 Main St"}'
```

Interactive API documentation is available at `http://localhost:8000/docs`.

## License

This project is licensed under the [MIT License](LICENSE).
