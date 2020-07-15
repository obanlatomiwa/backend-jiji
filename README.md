# Jiji_Clone

Jiji_Clone is a django and vue.js app designed to connect sellers and buyers.

## Database structure

SQLITE

## Role Based Access Control

##### Buyers are allowed to:
- view all products
- submit a request for a product


##### Sellers that is logged in is allowed to:
- view all products
- add new product
- edit product
- delete product
- get request from buyers

## API Reference

### Base URL
This app is currently hosted at https://wayne-notebook.herokuapp.com/ 

## About the Stack

### Backend

The `./jiji_clone` directory contains a completed Django server.

[View the README.md within ./backend for more details.](./jiji_clone/README.md)

### Frontend

The `./frontend` directory contains a complete Vue.js frontend to consume the data from the Django server.

[View the README.md within ./frontend for more details.](./frontend/README.md)


### Error Handling
Errors are returned as JSON objects with "success" set to False, "error" set to the error's number and a "message" describing the error

The API may return these error types when requests fail:
- 400: Bad Request
- 403: Forbidden
- 404: Resource Not Found
- 422: Request can not be processed
- 500: Internal Server Error

### Endpoints
##### GET  '/api/products'
    This endpoint fetches all the notes in the database and displays them as json.


##### POST '/api/products'
    This endpoint will create a new category in the database based on the json that is in the body of the request.

##### PATCH  '/products/<int:note_id>'
    This endpoint will modify the note that corresponds to the note ID that is passed into the url based on the json that is passed into the body of the request.


##### DELETE  '/api/products/int:<note_id>'
    This endpoint will delete the note that corresponds to the note ID that is passed into the url.


### Basic Requirements

In order to successfully set up the app, you need to have Python3, pip and SQLITE already installed on your local machine


### Running the server

To run the server, execute these three lines from within the `/jiji_clone` directory:
```bash
python manage.py runserver
```