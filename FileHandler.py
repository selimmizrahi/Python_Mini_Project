import csv
from csv import writer

class Filehandler:

    def load_from_cvs(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    print(line)

        except Exception as error:
            print("Hi Error, Welcome!" + str(error))

    def append_to_csv(self, file_name, data):
        try:
            with open(file_name, 'a+', newline='') as write_obj:
                csv_writer = writer(write_obj)
                csv_writer.writerow(data)

            for row in csv_writer:
                print(row[0])

        except Exception as error:
            print("There is" + str(error))

new_data = [8, "Selim", "Mizo", "password", "student", 100, "student"]

file = Filehandler()
file.append_to_csv("/Users/selimmizrahi/Desktop/Python_Mini_Project/cvs_file/user.csv",new_data)
file.load_from_cvs("/Users/selimmizrahi/Desktop/Python_Mini_Project/cvs_file/user.csv")
