import psycopg2

# Establish connection parameters
conn_params = {
    "host": "localhost",
    "database": "students",
    "user": "postgres",
    "password": "postgres"
}

# Global variable for database connection
conn = None

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**conn_params)
    print("Connected to the database!")

    # Function to get all students
    def getAllStudents():
        """Fetches and prints all students from the database."""
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()

    # Function to add a new student
    # Function to add a new student
    def addStudent(first_name, last_name, email, enrollment_date):
        """Adds a new student to the database."""
        try:
            cursor = conn.cursor()
            query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (first_name, last_name, email, enrollment_date))
            conn.commit()
            print("Student added successfully!")
        except psycopg2.Error as e:
            conn.rollback()  # Rollback the transaction to prevent further errors
            print("Error adding student:", e)
        finally:
            cursor.close()

    def updateStudentEmail(student_id, new_email):
        """Updates the email of a student."""
        try:
            cursor = conn.cursor()
            query = "UPDATE students SET email = %s WHERE student_id = %s"
            cursor.execute(query, (new_email, student_id))
            conn.commit()
            print("Student email updated successfully!")
        except psycopg2.Error as e:
            print("Could not find specified student:", e)
        finally:
            cursor.close()

    def deleteStudent(student_id):
        """Deletes a student from the database."""
        try:
            cursor = conn.cursor()
            query = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            conn.commit()
            print("Student deleted successfully!")
        except psycopg2.Error as e:
            print("Could not find specified student:", e)
        finally:
            cursor.close()

    while True:
        print("Please enter a command:")
        print("1. getAllStudents()")
        print("2. addStudent(first_name, last_name, email, enrollment_date)")
        print("3. updateStudentEmail(student_id, new_email)")
        print("4. deleteStudent(student_id)")
        print("5. Quit")
        user_input = input("Please enter a command: ")
        if user_input == '1':
            getAllStudents()
        elif user_input == '2':
            print("Input your values:")
            first_name = input("The first Name: ")
            last_name = input("The Last Name: ")
            email = input("The Email: ")
            enrollment_date = input("The Enrollment date: ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif user_input == '3':
            print("Input your values:")
            student_id = input("ID of the student you want to update: ")
            new_email = input("The new email: ")
            updateStudentEmail(student_id, new_email)
        elif user_input == '4':
            print("Input your values:")
            student_id = input("ID of the student you want to delete: ")
            deleteStudent(student_id)
        elif user_input == '5':
            print("Goodbye")
            break
        else:
            print("Please enter a command between 1 - 5.")

except psycopg2.Error as e:
    print("Error while connecting to PostgreSQL:", e)

finally:
    # Close connection
    if conn:
        conn.close()
