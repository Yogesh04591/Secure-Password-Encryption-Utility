import pymysql
from password_utinels import get_decrypted_password

connection = pymysql.connect(
    host='localhost',
    user='root',
    # this function hides the password from the develoers if they run the progeam means it can access the database without the password
    password=get_decrypted_password(),
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)
try:
  with connection.cursor() as cursor:
    create_query ="""
    CREATE TABLE IF NOT EXISTS employees(id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100), department VARCHAR(100)
    );
    """
    cursor.execute(create_query)
    # if more values are available in a list use %s method to print it in the databases
    insert_query = "INSERT INTO employees(name,department) VALUES(%s,%s) "
    values=[("John","IT"),("Alice","HR"),("Sam","Sales")]
    # we have to use execute many because there are three values we neeed to insert into the data base
    cursor.executemany(insert_query,values)
    
    # this was used to commit the process
    connection.commit()
    
    # this select line is used to handle the database selection 
    select_query= "SELECT * from employees"
    cursor.execute(select_query)
    result = cursor.fetchall()
    
    # we cannot able to print it directly that's why we use the iteration to print it
    for row in result:
        print(row)
    
    # this will print the save the data as a file
    with open("output_sql.txt","w") as file:
      for file1 in result:
        file.write(f"{file1} \n")
        
    print(get_decrypted_password())
finally:
    connection.close()