from FileHandler import File_handler
from User import User
import os


class Carlot:
    def __init__(self):
        self.user = User()
        self.file_handler = File_handler()

    def update_salary_by_name(self, salary, employee_name):
        employee = {}
        newpath = os.path.join('/Users/selimmizrahi/Desktop/Python_Mini_Project/user.csv')
        self.file_handler.load_from_csv(newpath)
        print(self.file_handler.data)
        for x in self.file_handler.data:
            if x["first_name"] == employee_name:
                employee = x

        if employee:
            role = self.user.user_auth(employee["first_name"], employee["password"])
            if role == "admin":
                employee["salary"] = str(salary)
                remove_value = self.file_handler.remove_from_csv(newpath, employee["id"])
                if remove_value == True:
                    add_value = self.file_handler.append_to_csv(newpath, employee)
                    if add_value == True:
                        self.log.create_log_entry("updated salary of an employee")
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

carlot = Carlot()
value = carlot.update_salary_by_name("3000", "selim")
print(value)