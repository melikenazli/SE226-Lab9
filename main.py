import mysql.connector

def create_database():
    database = mysql.connector.connect(host="localhost", user="root", passwd="abcde")
    cursorObject = database.cursor()
    cursorObject.execute("CREATE DATABASE MoviesDatabase")
    connection = mysql.connector.connect(host="localhost", user="root", database="MoviesDatabase", passwd="abcde")
    if connection.is_connected():
        print("You are connected to MySQL server.")

def create_relation():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", database="MoviesDatabase", passwd="abcde")
        mysql_create_table_query = """CREATE TABLE MarvelMovies(ID int(11) NOT NULL,
                                    MOVIE varchar(250) NOT NULL, 
                                    DATE varchar(250) NOT NULL,
                                    MCU_Phase varchar(250) NOT NULL,
                                    PRIMARY KEY (ID))"""
        cursor = connection.cursor()
        result = cursor.execute(mysql_create_table_query)
        print("Marvel Table created successfully!")
    except mysql.connector.Error as error:
        print("Failed! {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL Server is closed!")


def insert_variables_into_relation():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", database="MoviesDatabase", passwd="abcde")
        cursor = connection.cursor()
        f = open("C:\\Users\\melik\\Desktop\\Marvel.txt")
        lines = f.readlines()
        for line in lines:
            mysql_insert_query = """INSERT INTO MarvelMovies(ID, MOVIE, DATE, MCU_Phase) 
                                        VALUES(%s, %s, %s, %s)"""
            words = line.split()
            record = (words[0], words[1], words[2], words[3])
            cursor.execute(mysql_insert_query, record)
            connection.commit()
            print("Record inserted successfully!")
    except mysql.connector.Error as error:
        print("Failed! {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            f.close()
            print("MySQL Server is closed!")

def display_relation():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", database="MoviesDatabase", passwd="abcde")
        sql_select_query = "SELECT * FROM MarvelMovies"
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Marvel Movies Relation:")
        for row in records:
            print("ID =", row[0])
            print("MOVIE =", row[1])
            print("DATE =", row[2])
            print("MCU PHASE =", row[3], "\n")
    except mysql.connector.Error as error:
        print("Failed! {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL Server is closed!")

def remove_incredible_hulk():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", database="MoviesDatabase", passwd="abcde")
        sql_delete_query = """DELETE FROM MarvelMovies WHERE MOVIE = 'TheIncredibleHulk'"""
        cursor = connection.cursor()
        cursor.execute(sql_delete_query)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed! {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL Server is closed!")

def display_phase2_movies():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", database="MoviesDatabase", passwd="abcde")
        sql_select_query = "SELECT * FROM MarvelMovies WHERE MCU_Phase = 'Phase2'"
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Phase 2 Marvel Movies:")
        for row in records:
            print("ID =", row[0])
            print("MOVIE =", row[1])
            print("DATE =", row[2])
            print("MCU PHASE =", row[3], "\n")

    except mysql.connector.Error as error:
        print("Failed! {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL Server is closed!")

def fix_tuple():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", database="MoviesDatabase", passwd="abcde")
        sql_update_query = """UPDATE MarvelMovies SET DATE = 'November3,2017' WHERE MOVIE = 'Thor:Ragnarok'"""
        cursor = connection.cursor()
        cursor.execute(sql_update_query)
        connection.commit()
    except mysql.connector.Error as error:
        print("Failed! {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL Server is closed!")


create_database()
create_relation()
insert_variables_into_relation()
display_relation()
remove_incredible_hulk()
display_phase2_movies()
fix_tuple()
display_relation()

