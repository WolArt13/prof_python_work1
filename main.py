from application.salary import calculate_salary
import application.db.people
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    application.db.people.get_employees()
    calculate_salary()