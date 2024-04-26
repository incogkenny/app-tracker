import psutil
from _datetime import datetime


def check_if_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False


class App:

    def __init__(self):
        self.running = False
        self.start_time = datetime.now().strftime('%H:%M:%S')
        self.end_time = ''
        self.time_diff = None

    def set_end_time(self):
        self.end_time = datetime.now().strftime('%H:%M:%S')
        self.running = False

    def calculate_difference(self):
        return datetime.strptime(self.end_time, FMT) - datetime.strptime(self.start_time, FMT)

    def set_time_diff(self):
        self.time_diff = self.calculate_difference()


app_names = ["pycharm64.exe", "chrome.exe", "Code.exe"]

FMT = '%H:%M:%S'  # format : hrs:mins:secs

example = '18:15:00'

start = datetime.now()
start_time = start.strftime(FMT)

time_diff = datetime.strptime(example, FMT) - datetime.strptime(start_time, FMT)

print(time_diff)
# print(start_time)
# print(start)
result = check_if_process_running(app_names[0])

print(result)


# def main():
#     # checks if apps in list are running
#     while True:
#         if len(app_names) == 0:
#             break
#         for app in app_names:
#             check_if_process_running(app)
