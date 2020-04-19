import csv

class User:

    def inputResult(self):
        self.User = User
        self.username = str(input('Please insert your username: '))
        self.password = str(input('Please insert your password: '))

    def user_auth(username, password):
        with open("/Users/selimmizrahi/Desktop/Python_Mini_Project/cvs_file/user.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            access = False
            user_role = ' '
            for row in csv_reader:
                if username.lower() == row[1] and password.lower() == row[3]:
                    access = True
                    user_role = str(row[6])
            if access:
                print('Access Granted')
                print(f'Your role is {user_role}')
                return access
            else:
                print('Access Denied')
                return access

User.inputResult(User)
User.user_auth(User.username, User.password)