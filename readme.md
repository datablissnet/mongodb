# MongoDB Python Examples

This repository contains a collection of Python scripts demonstrating how to interact with MongoDB using the PyMongo library. Each script focuses on different aspects of working with MongoDB, including connecting to the server, creating databases and collections, inserting documents, querying data, and performing updates.

## Prerequisites

Before running these scripts, make sure you have the following prerequisites:

- MongoDB installed on your local machine
- Python 3.x installed
- PyMongo library installed (you can install it using pip: `pip install pymongo`)

## Repository Structure

The repository includes the following Python files:

- **mongo_connect.py**: Illustrates how to establish a connection to a MongoDB server and lists the available databases.

- **mongo_glossary.py**: Demonstrates basic CRUD operations (Create, Read, Update, Delete) in MongoDB. It creates a 'training' database and inserts documents into the 'mongodb_glossary' collection.

- **mongo_query.py**: Shows how to perform queries on a MongoDB collection. It inserts a sample document into the 'python' collection and retrieves and prints the documents in the collection.

- **students.py**: Provides examples of working with a 'students' collection in the 'campusManagementDB' database. It demonstrates document insertion, querying, updating, and deletion.

## Usage

To run these scripts:

1. Make sure you have MongoDB running on your local machine.

2. Install the PyMongo library by running `pip install pymongo` in your terminal.

3. Clone this repository or download the individual script files.

4. Open a terminal or command prompt, navigate to the directory containing the script you want to run, and execute the script using the Python interpreter. For example:

   ```shell
   python3 mongo_connect.py
