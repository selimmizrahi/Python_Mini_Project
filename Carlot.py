import os
from FileHandler import File_handler
from User import User
# from csv import DictWriter
import csv


class Carlot:
    def __init__(self, file_name):
        self.user = User(file_name)
        self.file_handler = File_handler(file_name)

    def update_salary_by_name(self, salary, employee_name):

        employee = {}
        newpath = os.path.join('/Users/selimmizrahi/Desktop/Python_Mini_Project/user.csv')
        self.file_handler.load_from_csv(newpath)
        for x in self.file_handler.data:
            if x["first_name"] == employee_name:
                employee = x

        if employee:
            role = self.user.user_auth(employee["first_name"], employee["password"])
            if role == "admin":
                employee["salary"] = str(salary)
                remove_value = self.file_handler.remove_from_csv(employee["id"])
                if remove_value == None:
                    add_value = self.file_handler.append_to_csv(employee)
                    if add_value == None:
                        print("updated salary of an employee")
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def add_to_fleet(self, external_file):
        try:
            with open(external_file, "r") as csv_external:
                csv_reader = csv.reader(csv_external)
                external_headers = next(csv_reader)

            with open("/Users/selimmizrahi/Desktop/Python_Mini_Project/vehicle.csv", "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                internal_headers = next(csv_reader)

            if external_headers != internal_headers:
                return False

            external_data = open(external_file, "r")
            internal_data = open("/Users/selimmizrahi/Desktop/Python_Mini_Project/vehicle.csv", "r").readlines()

            if external_data != internal_data:
                with open("/Users/selimmizrahi/Desktop/Python_Mini_Project/vehicle.csv", "a") as csv_append:
                    next(external_data)
                    for row in external_data:
                        csv_append.writelines(row)
                return True

        except Exception as error:
            print(error)
            raise

# carlot = Carlot('/Users/selimmizrahi/Desktop/Python_Mini_Project/user.csv')
carlot = Carlot('/Users/selimmizrahi/Desktop/Python_Mini_Project/vehicle.csv')
# carlot.update_salary_by_name("3000", "Hen")
carlot.add_to_fleet('/Users/selimmizrahi/Desktop/Python_Mini_Project/external_file.csv')


