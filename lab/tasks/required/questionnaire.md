# Questionnaire — API Exploration

## Items endpoints

### GET /items

1. HTTP method: GET
2. Path: /items
3. Status code: 200
4. Status code (unauthorized): 401
5. Response type: array

### GET /items/{item_id}

1. HTTP method: GET
2. Path: /items/{item_id}
3. Status code: 200/404
4. Response type: object

### POST /items

1. HTTP method: POST
2. Path: /items
3. Status code: 201
4. Status code (invalid data): 422
5. Request body: type, parent_id, title, description

### PUT /items/{item_id}

1. HTTP method: PUT
2. Path: /items/{item_id}
3. Status code: 200/400
4. Request body: title, description

## Authentication

1. Header name: Authorization
2. Header format: Bearer <token>
3. Default token value: my-secret-api-key
4. Status code without token: 401
5. Status code with invalid token: 401
6. Status code with valid token: 200
7. API key file: .env.docker.secret
