import os
import datetime


class Logger():

    def __init__(self, path, log_file):
        self.new_dir_path = path
        self.new_name = log_file
        self.full_path = "{}//{}".format(self.new_dir_path, self.new_name)

    def create_log_entry(self, msg):
        if not os.path.exists(self.new_dir_path):
            os.makedirs(self.new_dir_path)
        try:
            f = open(self.full_path, "a+")
        except Exception as e:
            print(e)

        else:
            date = datetime.datetime.now()
            try:
                f.write(date.strftime("%y/%m/%Y, %H:%M:%S") + "{} \n".format(msg))
            except Exception as e:
                print(e)
            else:
                "Good job".format(self.new_dir_path)
            f.close()


log = Logger("logs", "log_file.txt")
log.create_log_entry("A text message")
