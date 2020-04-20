from FileHandler import File_handler


class User:
    def __init__(self):
        self.handler = File_handler()

    def user_auth(self, username, password):
        self.handler.load_from_csv('/Users/selimmizrahi/Desktop/Python_Mini_Project/user.csv')
        print(self.handler.list)

        access = False
        user_role = ' '

        for row in self.handler.list:
            if username == row["first_name"] and password == row["password"]:
                access = True
                user_role = str(row["role"])

            if access:
                print('Access Granted')
                print(f'Your role is {user_role}')
                return access

            else:
                print('Access Denied')
                return access

User.__init__(User)
User.user_auth(User, "Amir", '12345678')