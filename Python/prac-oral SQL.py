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