import csv


class Filehandler:

    def load_from_cvs(self, file_name):
        try:
            with open(file_name, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    print(line)

        except Exception as error:
            print("Hi Error, Welcome!" + str(error))

file = Filehandler()
file.load_from_cvs("/Users/selimmizrahi/Desktop/Python_Mini_Project/cvs_file/user.csv")
