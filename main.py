from commands import *


def main():
    helpers.make_folder_if_not_exist(constants.LOGS_DIR)

    employees = load_employee()
    # # employee["1"] = {"name": "ahmad hosseini"}
    # add_employee(employees, 1, "ahmad hosseini")
    # add_employee(employees, 3, "zahra")
    # save_employee(employees)
    # print(employees)
    # remove_employee(employees, 2)
    # list_employee(employees)
    today_str = dt.datetime.now().strftime("%Y-%m-%d")
    # employee_start_day(employees, 3, today_str)
    # employee_end_day(employees, 3, today_str)
    # see_today_log(today_str)
    # see_week_log(today_str, 1)
    print(constants.MENU_MESSAGE)
    while True:
        choice = input("Select an Option (1-9) :  ")
        if choice == "1":
            employee_id = input("Employee Id : ")
            employee_start_day(employees, employee_id, today_str)
            continue
        if choice == "2":
            employee_id = input("Employee Id : ")
            employee_end_day(employees, employee_id, today_str)
            continue
        if choice == "3":
            employee_id = input("Employee Id : ")
            date = input("Date(YYYY-MM-DD)")
            see_week_log(date,employee_id)
            continue
        if choice == "4":
            date = input("Date(YYYY-MM-DD)")
            see_today_log(date)
            continue
        if choice == "5":
            id = input("ID : ")
            name = input("Name")
            add_employee(employees,id,name)
            continue
        if choice == "6":
            id = input("ID : ")
            remove_employee(employees,id)
            continue
        if choice == "7":
            list_employee(employees)
            continue
        if choice == "8":
            print("Good Bye")
            break
        if choice == "0":
            print(constants.MENU_MESSAGE)

    


if __name__ == "__main__":
    main()
