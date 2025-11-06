# Chronologue API

FastAPI backend for the Chronologue time tracking application.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Testing

Run tests with pytest:
```bash
pytest
```

## API Documentation

When running, visit `http://localhost:8000/docs` for interactive API documentation.