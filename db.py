
import sqlite3

connection = sqlite3.connect("crud.db")
cursor = connection.cursor()

def create_table():
    create_table_query = """
            CREATE TABLE IF NOT EXISTS cli(
            ID INTEGER PRIMARY KEY,
            NAME TEXT NOT NULL,
            AGE INTEGER,
            EMAIL TEXT UNIQUE
            )
    """

    cursor.execute(create_table_query)
    connection.commit()
    
    try:
        cursor.execute(create_table_query)
        print("Table created successfully")
    except Exception as e:
        print("Table failed to create")
        print(e)


# inserting value in database query
def insert_user_db(user):
    try:
        cursor.execute("INSERT INTO cli(NAME,AGE,EMAIL) VALUES(?,?,?)", user)
        connection.commit()
    except Exception as e:
        print("Failed to insert value")
        print(e)



#reading the value

def reading_query():

    select_query="""
        SELECT * FROM cli;
    """
    try:
        cursor.execute(select_query)
        all_user= cursor.fetchall()

        for user in all_user:
            print(f"{user[0]} | {user[1]} | {user[2]} | {user[3]}")
    except Exception as e:
        print("Error creating table:")
        print(e)

# update the user

def update_user_db(update_value):
    try:
        cursor.execute(
        "UPDATE cli SET NAME=?, AGE=?, EMAIL=? WHERE ID=?",
        update_value
        )
        connection.commit()
        return cursor.rowcount
    except Exception as e:
        print("User failed to update")
        print(e)


# delete query:

def delete_user():
    del_id=int(input("\nEnter the ID to be deleted: "))

    delete_user_query="""
        DELETE FROM cli where ID=?;
    """
    try:
        cursor.execute(delete_user_query, (del_id,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"\nData with ID {del_id} deleted successfully.")
        else:
            print(f"\nNo user found with ID {del_id}.")

    except Exception as e:
        print("Error printing")
        print(e)
