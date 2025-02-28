# Simple Flask Books API

A simple REST API built with Flask that demonstrates basic CRUD operations for managing books.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Project Structure
```
flask-books-api/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Installation

1. Clone this repository or download the files
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. The API will be available at `http://localhost:5000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information and available endpoints |
| GET | `/books` | Get all books |
| GET | `/books/<id>` | Get a specific book |
| POST | `/books` | Create a new book |
| PUT | `/books/<id>` | Update a book |
| DELETE | `/books/<id>` | Delete a book |

## Example Usage

### Get all books
```bash
curl http://localhost:5000/books
```

### Get a specific book
```bash
curl http://localhost:5000/books/1
```

### Create a new book
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"title":"New Book","author":"John Doe"}' \
  http://localhost:5000/books
```

### Update a book
```bash
curl -X PUT -H "Content-Type: application/json" \
  -d '{"title":"Updated Title"}' \
  http://localhost:5000/books/1
```

### Delete a book
```bash
curl -X DELETE http://localhost:5000/books/1
```

## Response Examples

### Success Responses

#### Get all books
```json
[
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell"
    }
]
```

#### Create/Update book
```json
{
    "id": 3,
    "title": "New Book",
    "author": "John Doe"
}
```

#### Delete book
```json
{
    "message": "Book deleted successfully"
}
```

### Error Responses

#### Book not found
```json
{
    "error": "Book not found"
}
```

#### Invalid input
```json
{
    "error": "Title and author are required"
}
```

## Notes

- This is a simple demonstration API using an in-memory list to store data
- In a production environment, you should:
  - Use a proper database
  - Add authentication
  - Add input validation
  - Add proper error handling
  - Configure CORS
  - Use environment variables for configuration
  - Add logging
  - Add tests
  - Add API documentation (e.g., Swagger/OpenAPI)

## License

This project is open source and available under the [MIT License](LICENSE).