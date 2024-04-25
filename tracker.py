import psutil

def check_if_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

process_names = ["pycharm64.exe", "chrome.exe", "Code.exe"]


result = check_if_process_running(process_names[0])

print(result)
