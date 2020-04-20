import csv
from csv import writer


class File_handler:

    def __init__(self):
        self.list = []

    def load_from_cvs(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    self.list.append(line)

        except Exception as error:
            print("There is an error :" + str(error))

    def append_to_csv(self, file_name, data):
        try:

            self.load_from_cvs(file_name)
            for row in self.list:
                if row.get("id") == data[0]:
                    raise Exception("This ID already exists")

            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(data)

        except Exception as error:
            print("There is an error :" + str(error))


new_data = ["1", "Selim", "Mizo", "password", "student", 100, "student"]

file = File_handler()
file.append_to_csv('/Users/selimmizrahi/Desktop/Python_Mini_Project/user.csv',new_data)
file.load_from_cvs('/Users/selimmizrahi/Desktop/Python_Mini_Project/user.csv')

