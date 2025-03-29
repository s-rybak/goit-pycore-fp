# Personal Assistant Application

A command-line personal assistant for managing contacts and notes.

## Project Overview

This Python-based Personal Assistant helps you organize your contacts and notes through an intuitive command-line interface. Developed as a team project with 5 contributors, the application follows clean architecture principles with a focus on maintainability and expandability.

## Features

### Contact Management

- Add contacts with name, phone, email, address, and birthday information
- Find contacts using various search criteria (name, phone, email, address, birthday)
- Edit existing contact information
- Delete contacts
- Display all contacts in a clean tabular format
- Birthday notification for upcoming birthdays

### Note Management

- Add text notes with tags
- Search notes by content and tags
- Edit and delete notes
- Organize notes with tags

### User Interface

- Interactive command-line interface with autocompletion
- Color-coded output for better readability
- Intuitive command structure
- Help command for quick reference

## Architecture

The application follows a clean architecture approach with several key components:

- **Commands**: Each feature is implemented as a separate command
- **Entities**: Core business objects (Contact, Note)
- **Repositories**: Manages data persistence
- **Storage**: Handles the physical storage of data
- **Input/Output**: Manages user interaction

## Installation and Setup

### Prerequisites

- Python 3.10+
- Required packages listed in requirements.txt

### Installation Steps

1. Clone the repository:

```
git clone https://github.com/s-rybak/goit-pycore-fp.git
cd goit-pycore-fp
```

2. Install the required dependencies:

```
pip3 install -r requirements.txt
```

3. Run the application:

```
python main.py
```

## Usage Guide

Once the application is running, you can use the following commands:

- `help` - Display all available commands or get help for a specific command
- `add_contact` - Add a new contact
- `find` - Find contacts by name, phone, email, address or birthday
- `edit` - Edit an existing contact
- `delete` - Delete a contact
- `test_all_contacts` - Display all contacts
- `greet` - Simple greeting command
- `birthday_in_days` - Display contacts with birthdays in the N days 
- `exit` / `quit` / `bye` - Exit the application


### Example Commands

```
# Add a new contact
add_contact

# Find a contact by name
find name Guido van Rossum 

# Edit a contact
edit

# Delete a contact
delete

# Display all commands and their descriptions
help

# Display all contacts
test_all_contacts

# Display contacts with birthdays in the N days
birthday_in_days
```

## Project Team

This project was developed as a team effort by:

- [Serhii Rybak ] - Team Lead
- [Olha Osypenko ] - Scrum manager
- [Iurii Shcherbyna ] - Full stack developer
- [Olena Trzewik ] - Full stack developer
- [Nataliya Pustelnyk ] - Full stack developer

## Acknowledgments

This project was developed as part of the Python Programming: Foundations and Best Practices 2.0 course at GoIT Neoversity.
