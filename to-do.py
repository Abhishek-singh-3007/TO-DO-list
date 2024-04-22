import sqlite3

connection  = sqlite3.connect('to-do_list_db')
curs = connection.cursor()
curs.execute('''
    CREATE TABLE IF NOT EXISTS to_do (
        id INTEGER PRIMARY KEY,
        task TEXT NOT NULL,
        time TEXT NOT NULL,
        date TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')
def show_all():
    curs.execute("SELECT * FROM to_do")
    for row in curs.fetchall():
        print(row)

def add_task(task, time, date, description):
    curs.execute("INSERT INTO to_do (task, time, date, description) VALUES (?, ?, ?, ?)", (task, time, date, description))
    connection.commit()

def update_task(task_id ,task ,time ,date ,description ):
    curs.execute("Update to_do SET task = ?, time = ?, date = ?, description = ? WHERE id = ?", (task ,time ,date ,description ,task_id ))
    connection.commit()

def del_task(task_id):
    curs.execute("DELETE FROM to_do WHERE id = ?", (task_id,))
    connection.commit()

def main():
    while True:
        print("\n HI Dear ! Here is your TO-DO List ")
        print(" 1. Show all Task ")
        print(" 2. Add Task in To-Do list ")
        print(" 3. Update Task in To-Do List ")
        print(" 4. Delete Task in To-Do List ")
        print(" 5. Exit the App ")
        option = input("Enter your Choice: ") 

        if  option == '1':
            show_all()
        elif option == '2':
            task = input(" Enter the task name : ")
            time = input(" Enter the task duration : ")
            date = input(" Enter the task dtae : ")
            description = input(" Description of task in Few words : ")

            add_task(task, time, date, description)

        elif option == '3':
            task_id = input(" Enter the task Id want to update : ")
            task = input(" Enter the task name : ")
            time = input(" Enter the task duration : ")
            date = input(" Enter the task date : ")
            description = input(" Description of task in Few words : ")

            update_task(task_id ,task ,time ,date ,description )

        elif option == '4':
            task_id = input(" Enter the task Id want to delete : ")
            del_task(task_id)

        elif option == '5':
            break
        else:
            print("Invalid option !  | Please Try Again ")

    connection.close()


if __name__ == '__main__':
    main()






