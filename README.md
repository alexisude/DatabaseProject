# Database Project README

This project interacts with a PostgreSQL database containing student information. You can perform CRUD operations such as retrieving all students, creating a new student, updating a student's email, and deleting a student.

# Steps to Run the Project:
1. **Install Required Dependencies:**
   - Make sure you have Python installed on your system.
   - Install the psycopg2 package using pip:
     ```
     pip install psycopg2
     ```
2. **Set Up the Database:**
   - Ensure you have PostgreSQL installed on your system.
   - Create a database named "students" and set up the necessary tables. You can use the provided students.sql file for this purpose if you like. Use the Query tool and upload the students.sql file or copy paste into the file and run

3. **Compile and Run the Application:**
   - Save the provided Python script (dbInteraction.py) in your preferred directory.
   - Open a terminal or command prompt and navigate to the directory containing dbInteraction.py.
   - Run the script using Python python dbInteraction.py

4. **Interact with the Application:**
   - Once the application runs, you will be prompted to enter commands.
   - Available commands are:
     - 1: Retrieve all students from the database.
     - 2: Add a new student to the database.
     - 3: Update a student's email.
     - 4: Delete a student from the database.
     - 5: Quit the application.
   - Follow the prompts to execute the desired commands.

5. **Exiting the Application:**
   - To exit the application, enter '5' when prompted for a command.
   - Or, press Ctrl + C in the terminal to terminate the script.

## Important Note:
Before running the application, Ensure that your PostgreSQL server is running and accessible with the connection parameters provided in dbInteraction.py.
- Review and modify the connection parameters in dbInteraction.py if necessary to match your PostgreSQL configuration.
