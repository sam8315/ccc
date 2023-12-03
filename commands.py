import constants, helpers, json
import datetime as dt


def load_employee():
    employees = {}
    try:
        with open(constants.EMPLOYEE_FILE, "r") as f:
            employees = json.load(f)
    except FileNotFoundError:
        pass
    return employees


def save_employee(employee):
    with open(constants.EMPLOYEE_FILE, "w") as f:
        json.dump(employee, f, indent=2)


def add_employee(employees, employee_id, employee_name):
    employee_id = str(employee_id)
    if employee_id in employees:
        print(f"Employee ID ({employee_id}) already exists!")
    else:
        employees[employee_id] = {"name": employee_name}
        save_employee(employees)


def remove_employee(employees, employee_id):
    employee_id = str(employee_id)
    try:
        del employees[employee_id]
    except:
        print(f"Employee ID ({employee_id}) not exists!")
    else:
        save_employee(employees)
        print(f"Employee ID ({employee_id}) Removed!")


def list_employee(employees):
    print(" Employee List ".center(50, "-"))
    for i in employees:
        print(f" [{i}] {employees[i]['name']}")


def load_daily_log(date_str):
    contents = {}
    try:
        with open(f"{constants.LOGS_DIR}/{date_str}.json", "r") as f:
            contents = json.load(f)
    except FileNotFoundError:
        pass
    return contents


def employee_start_day(employees, employee_id, date_str):
    employee_id = str(employee_id)
    if employee_id not in employees:
        print("Invalid Employee ID !")
        return

    log = load_daily_log(date_str)
    if employee_id in log:
        print(f"Employee ID ({employee_id}) Already started a day")
    else:
        log[employee_id] = {"start_time": dt.datetime.now().strftime("%H:%M:%S")}
        save_daily_log(date_str, log)


def save_daily_log(date_str, log):
    with open(f"{constants.LOGS_DIR}/{date_str}.json", "w") as f:
        json.dump(log, f, indent=2)


def employee_end_day(employees, employee_id, date_str):
    employee_id = str(employee_id)
    if employee_id not in employees:
        print("Invalid Employee ID !")
        return

    log = load_daily_log(date_str)
    if employee_id not in log:
        print(f"Employee ID ({employee_id}) has not started the day yet !")
    elif "end+time" in log[employee_id]:
        print(f"Employee ID ({employee_id}) Already ended a day")
    else:
        log[employee_id]["end_time"] = dt.datetime.now().strftime("%H:%M:%S")
        save_daily_log(date_str, log)


def save_daily_log(date_str, log):
    with open(f"{constants.LOGS_DIR}/{date_str}.json", "w") as f:
        json.dump(log, f, indent=2)


def get_employee_day_report(log, id):
    try:
        start_time_message = log[id]["start_time"]
        end_time_message = "Not Ended Yet"
        if "end_time" in log[id]:
            end_time_message = log[id]["end_time"]
        print(
            id,
            " " * 8,
            start_time_message,
            " " * 6,
            end_time_message,
            " " * 7,
            calculate_working_time(log[id]),
            "\n",
            "-" * 70,
        )
    except:
        print("No Record")


def see_today_log(date_str):
    log = load_daily_log(date_str)
    print(f"Report {date_str}".center(70, "*"))
    print("ID", " " * 10, "Start", " " * 10, "End", " " * 10, "Total")
    print("-" * 70)
    for id in log:
        get_employee_day_report(log, id)


def calculate_working_time(employee_log):
    if "end_time" not in employee_log:
        return None
    start_time = dt.datetime.strptime(employee_log["start_time"], "%H:%M:%S")
    end_time = dt.datetime.strptime(employee_log["end_time"], "%H:%M:%S")
    total_working_time = end_time - start_time
    return total_working_time


def see_week_log(date_str, employee_id):
    employee_id = str(employee_id)
    date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    print("Date", " " * 10, "ID", " " * 10, "Start", " " * 10, "End", " " * 10, "Total")
    for i in range(10):
        current_date = date + dt.timedelta(days=i)
        current_date_str = current_date.strftime("%Y-%m-%d")
        print(current_date_str + "     ", end="")
        log = load_daily_log(current_date_str)
        get_employee_day_report(log, employee_id)
