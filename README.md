Notes Application README
==========================

Welcome to the Notes Application! This README provides basic documentation and a guide on how to run the application.

About the Application
---------------------

The Notes Application is a RESTful API built with Flask that allows users to perform CRUD operations on notes data. The application uses a CSV file to store data and provides a user-friendly interface to interact with the data.

How to Run the Application
---------------------------

### Prerequisites

* Make sure you have Flask and csv-parser installed. You can install them by running `pip install Flask csv-parser` in your terminal.

### Running the Application

1. Clone the repository and navigate to the project directory.
2. Run the `run.sh` script by typing `./run.sh` in your terminal.
3. Open a web browser and navigate to `http://localhost:5000` to access the application.

### Alternative Method

1. Install Flask by running `pip install Flask` in your terminal.
2. Install csv-parser by running `pip install csv-parser` in your terminal.
3. Run the application by typing `python app.py` in your terminal.
4. Open a web browser and navigate to `http://localhost:5000` to access the application.

API Endpoints
-------------

The application provides the following API endpoints:

* **GET /notes**: Retrieves all notes.
* **POST /notes**: Creates a new note.
* **GET /notes/:id**: Retrieves a note by ID.
* **PUT /notes/:id**: Updates a note.
* **DELETE /notes/:id**: Deletes a note.

Note: The API endpoints are subject to change. For the latest information, please refer to the routes.py file.

Contributing
-------------

Contributions are welcome! If you'd like to contribute to the Notes Application, please fork the repository, make changes, and submit a pull request.

License
-------

The Notes Application is licensed under the MIT License. See the LICENSE file for details.