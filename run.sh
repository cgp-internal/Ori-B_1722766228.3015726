#!/bin/bash

# Install Flask and required dependencies
python -m pip install -r requirements.txt

# Initialize a new Flask project
python -m flask init

# Install additional dependencies
pip install flask

# Run the Flask server
python app.py