import csv


class Filehandler:

    def load_from_cvs(file_name):
        try:
            with open(file_name[0]) as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                        users = {
                            "id": row[0],
                            "first name": row[1],
                            "last name": row[2],
                            "password": row[3],
                            "position": row[4],
                            "salary": row[5],
                            "role": row[6],
                        }
                        self.users.append(users)

        except Exception as error:
            print("Hi Error, Welcome!" + str(error))

file = Filehandler()
file.load_from_cvs("/Users/selimmizrahi/Desktop/Python_Mini_Project/cvs_file/user.csv")
print(file.users)
