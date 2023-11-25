# Purffect Games API

Welcome to the Purffect Games API, the backbone of the Purffect Games ecosystem. This Django-based API, enriched with Django Rest Framework and Faker for test data generation, empowers both the Purffect Games Owner and Client applications.

## Entity-Relationship Model

<!-- ![Entity-Relationship Model](./images/er_model.png) -->

## API Endpoints

### Clients

- **GET /api/clients/**
  - Retrieve the list of all clients.
- **GET /api/clients/{id}/**
  - Retrieve details of a specific client.
- **POST /api/clients/**
  - Create a new client.
- **PUT /api/clients/{id}/**
  - Update details of a specific client.
- **DELETE /api/clients/{id}/**
  - Delete a specific client.

### Games

- **GET /api/games/**
  - Retrieve the list of all games.
- **GET /api/games/{id}/**
  - Retrieve details of a specific game.
- **POST /api/games/**
  - Create a new game.
- **PUT /api/games/{id}/**
  - Update details of a specific game.
- **DELETE /api/games/{id}/**
  - Delete a specific game.

### Rentals

- **GET /api/rentals/**
  - Retrieve the list of all rentals.
- **GET /api/rentals/{id}/**
  - Retrieve details of a specific rental.
- **POST /api/rentals/**
  - Create a new rental.
- **PUT /api/rentals/{id}/**
  - Update details of a specific rental.
- **DELETE /api/rentals/{id}/**
  - Delete a specific rental.

### Client Rentals

- **GET /api/client_rentals/{client_id}/**
  - Retrieve all rentals associated with a specific client.

### Create Rental

- **POST /api/create_rental/**
  - Create a new rental with client and game details.

### Most Rented Game by Age

- **POST /api/most_rented_game_by_age/**
  - Retrieve the most rented game within a specified age range.

## Test Data Generation

- **GET /api/fill_test_data/**
  - Generate and fill the database with test data using Faker.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sjanna/purffectgames_api.git
   ```

2. **Install Dependencies:**
   ```bash
   cd purffectgames_api
   pip install -r requirements.txt
   ```
3. **Run Migrations:**
   ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Fill the Database with Test Data:**
   ```bash
   python manage.py runscript populate_database
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the API:**
   Open your browser and navigate to [http://localhost:8000/api/](http://localhost:8000/api/).

## Additional Information

For any inquiries or support, please contact me[sjannadiaz@gmail.com](mailto:sjannadiaz@gmail.com). We're here to ensure a purrfect API experience for you and your applications!