#Question 11 (API)

"""What is an API?

API stands for Application Programming Interface.

It’s a set of rules that allows one software application to interact with
another.or Application Programming Interface, is a set of rules and protocols that
allows different software applications to communicate and interact
with each other. It acts as an intermediary, defining how one program can request
services or data from another, and how that data or service will be delivered in return.

Example: Twitter API, OpenWeatherMap API, or Google Maps API.

2. Making a GET request using Python

Python has a library called requests that makes it easy to interact with APIs.

GET request: Used to retrieve data from an API.

Example:
import requests

# URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url)  # Make a GET request
    response.raise_for_status()   # Raise error if request failed
    data = response.json()        # Convert response to JSON
    print("API Response:", data)
except requests.exceptions.RequestException as e:
    print("Error:", e)


Explanation:

requests.get(url) → Sends a GET request to the API endpoint.

response.raise_for_status() → Checks if the request was successful (status code 200).

response.json() → Parses the JSON response into a Python dictionary.

try-except → Catches network errors, timeouts, or invalid URLs.

Part 2: How to connect to a SQLite database using Python

SQLite is a lightweight, file-based database built into Python.

Steps to connect and use SQLite in Python:

Import sqlite3 module

import sqlite3


Connect to a database

conn = sqlite3.connect("my_database.db")


Creates a file my_database.db if it doesn’t exist.

conn is the connection object used to interact with the database.

Create a cursor object

cursor = conn.cursor()


The cursor is used to execute SQL commands like CREATE, INSERT, SELECT, etc.

Execute SQL commands

# Create a table
cursor.execute("""
"""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER"""
""")

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)


Commit changes

conn.commit()  


Saves any changes made (like inserting or updating data).

Close the connection

conn.close()  


Frees resources and ensures the database file is properly saved."""