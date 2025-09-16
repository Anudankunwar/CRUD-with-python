
import db

print("Welcome to Simple CRUD App!!")
db.create_table()

def display():
    print('=' *30)
    print("Simple Crud App")
    print('=' *30)
    print("1. Add User")
    print("2. Show All Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    print('=' *30)


# add_user function

def add_user():
    print("\n---Add New User ---")
    name=input("Enter Name: ")
    age=(input("Enter Age: "))
    if not age.isdigit():
        print("Error: Age must be a number!")
       
    age = int(age)
    email= input("Enter Email: ")
    return(name,age,email)

def insert_user():
    user = add_user()
    if user:
        db.insert_user_db(user)
        print(f"User {user[0]} added successfully")


# update function 

def update_user_value():
    user_id = input("\nEnter user ID to update: ")
    if not user_id.isdigit():
        print("❌ Invalid ID!")
        return None
    user_id = int(user_id)

    db.cursor.execute("SELECT NAME, AGE, EMAIL FROM cli WHERE ID=?", (user_id,))
    current = db.cursor.fetchone()

    if not current:
        print(f"\nUser with ID {user_id} not found.")
        return None

    print("Enter new information (press Enter to keep current):")
    new_name = input("New name: ") or current[0]
    new_age_input = input("New age: ")
    new_age = int(new_age_input) if new_age_input.strip() else current[1]
    new_email = input("New email: ") or current[2]

    return (new_name, new_age, new_email, user_id)



while True:

    display()

    choose= int(input("\nChoose an option (1-5): "))

    if choose==1:
       insert_user() 
       input("\nPress enter to continue")

    elif choose==2:
        print("\n----All user----")
        print("\nID | NAME | AGE | EMAIL ")
        print('-' *30)
        db.reading_query()
        print('-' *30)
        input("\nPress enter to continue")

    elif choose==3:
        print("\n----All user----")
        print("\nID | NAME | AGE | EMAIL ")
        print('-' *30)
        db.reading_query()
        print('-' *30)

        updated_user = update_user_value()
        if updated_user:
            db.update_user_db(updated_user)   # send data to db
            print("\n✅ User updated successfully!")
        input("\nPress enter to continue")

    elif choose==4:
        print("\n----All user----")
        print("\nID | NAME | AGE | EMAIL ")
        print('-' *30)
        db.reading_query()
        print('-' *30)

        db.delete_user()
        print("\n----All user----")
        print("\nID | NAME | AGE | EMAIL ")
        print('-' *30)
        db.reading_query()
        print('-' *30)
        input("\nPress enter to continue")
    
    elif choose==5:
        break 

    else:
        print("Wrong input. Enter the valid number from 1 to 5.")
       
    

