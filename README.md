# AirBnB_Clone Project

## Part 1 - Command Interpreter

### Project Overview:
The AirBnB_Clone project involves creating a command-line interpreter to manage various aspects of an Airbnb-like application. 
This initial part of the project focuses on setting up the foundation and key components necessary for future development.
### Key Objectives:

1. **BaseModel Class:** Implement a parent class called `BaseModel` responsible for handling the initialization, serialization, and deserialization of instances.
2. **Serialization Flow:** Establish a simple flow for serialization and deserialization, allowing data to move seamlessly between instances, dictionaries, JSON strings, and files.
3. **AirBnB Classes:** Create all the classes needed for the AirBnB application, including `User`, `State`, `City`, `Place`, and others. 
						These classes should inherit from the `BaseModel` class to inherit its functionality.
4. **Abstracted Storage Engine:** Develop the first abstracted storage engine for the project, known as File storage. 
								This engine will handle the storage and retrieval of data within the application.
5. **Unit Tests:** Create comprehensive unit tests to validate the functionality and correctness of all classes and the storage engine.
### How to Use:

To use the AirBnB_Clone project, follow these steps:
1. Start the console by running the command `./console` in your terminal.
2. Type `help` to display a list of available commands and their descriptions. 
	This will provide guidance on how to interact with and utilize the command interpreter for managing the application.
This project sets the stage for building a fully functional Airbnb-like application, with the initial focus on implementing the core components and testing their functionality.
### Examples:
```
(hbnb)create BaseModel
8e699221-f846-40cd-94bf-86a3e340973e
(hbnb)show BaseModel 8e699221-f846-40cd-94bf-86a3e340973e
[BaseModel] (8e699221-f846-40cd-94bf-86a3e340973e) {'id': '8e699221-f846-40cd-94bf-86a3e340973e', 'created_at': 
datetime.datetime(2024, 1, 14, 17, 47, 6, 431490), 'updated_at': datetime.datetime(2024, 1, 14, 17, 47, 6, 431586)}

### Authors:
* Charles Agwanda <charlesowino180@gmail.com>
* Clinton Orenge <orengecmo@gmail.com>