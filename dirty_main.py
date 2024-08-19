from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    print(datetime.now())
    get_employees()
    calculate_salary()