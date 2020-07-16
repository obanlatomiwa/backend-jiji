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
This app is currently hosted at https://jiji-clone.herokuapp.com/

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/jiji_clone` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


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


## Running the server

From within the `./jiji_clone` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python manage.py runserver
```