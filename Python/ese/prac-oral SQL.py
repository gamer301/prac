import mysql.connector
# Database connection parameters
db_config = {
"host": "your_host_name",
"user": "your_username",
"password": "your_password",
"database": "COLLEGE",
}

try:
# Connect to the MySQL database
 connection = mysql.connector.connect(**db_config)
 cursor = connection.cursor()
# User input for RollNumber, Name, and Class
 roll_number = input("Enter RollNumber: ")
 name = input("Enter Name: ")
 class_name = input("Enter Class: ")
 sql_insert = "INSERT INTO STUDENT (RollNumber, Name, Class) VALUES(%s, %s, %s)" # values('" + name +"', '"+ roll +"', '" + className +"')
 values = (roll_number, name, class_name)
# Execute the INSERT statement # https://www.w3schools.com/sql/sql_insert.asp #https://www.w3schools.com/mysql/mysql_sql.asp
 cursor.execute(sql_insert, values)
 connection.commit()
 print("Record inserted successfully!")

except mysql.connector.Error as error:
 print("Error: {}".format(error))

finally:
# Close the cursor and database connection
   if connection.is_connected():
     cursor.close()
     connection.close()

# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
insert_stmt = (
  "INSERT INTO employees (emp_no, first_name, last_name, hire_date) "
  "VALUES (%s, %s, %s, %s)"
)
data = (2, 'Jane', 'Doe', datetime.date(2012, 3, 23))
cursor.execute(insert_stmt, data)

select_stmt = "SELECT * FROM employees WHERE emp_no = %(emp_no)s"
cursor.execute(select_stmt, { 'emp_no': 2 })     

*** CREATE DATABASE testDB; 
CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);


CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype CHECK (Age>=18 AND City='Sandnes'),
    column3 datatype DEFAULT 'Sandnes',
    ....
);

NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Prevents actions that would destroy links between tables
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
CREATE INDEX - Used to create and retrieve data from the database very quickly



Insert: Using INSERT INTO table_name (column1, column2, ...) VALUES (%s, %s, ...).
Delete: Using DELETE FROM table_name WHERE condition.
Update: Using UPDATE table_name SET column1 = value1 WHERE condition.