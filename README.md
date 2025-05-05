# URL Shortener Service

A simple URL shortener service built with FastAPI, Redis, and Pydantic. This service allows users to shorten URLs and redirect to the original URLs using the shortened keys.

## Features

- Shorten URLs with a randomly generated key.
- Redirect to the original URL using the shortened key.
- Uses Redis for storing and retrieving URL mappings.
- Built with FastAPI for high performance and easy API development.

## Requirements

- Python 3.10 or higher
- Redis server (version 5.0 or higher)
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder> 
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
   ```

3. Install the required packages:
   ```bash
    pip install -r requirements.txt
   ```
   
4. Start the Redis server: Ensure Redis is running on the specified host and port:
   ```bash
    docker run -d -p 6379:6379 redis
   ```

5. Run the FastAPI application:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

Access the API documentation: Open your browser and navigate to:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure
- app/: Contains the main application code.
  - redis_client.py: Redis client for interacting with the Redis database.
  - serializers.py: Pydantic models for request and response validation.
  - views.py: API endpoints for shortening and redirecting URLs.
- env: Environment variables for configuration.
- requirements.txt: Python dependencies.

## Example

#### Shorten a URL

Request:
```shell
POST /shorten
{
  "url": "https://example.com"
}
```
Response:
```json
{
  "short_url": "http://localhost:8000/abc123"
}
```


## License
This project is licensed under the MIT License.