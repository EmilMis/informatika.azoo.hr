import User
import threading
import pickle
import time
from User import Error

limit = int(input("How many users do you want to load? "))
number_of_threads = 300

database = []


def do(start_n):
    while start_n <= limit:
        try:
            if start_n % 1000 == 0:
                print(f"iterations: {start_n}")
            user = User.User(start_n)
            if user.name == Error.error_message:
                start_n += number_of_threads
                continue
            database.append(user)
            start_n += number_of_threads
        except:
            time.sleep(0.5)

threads = []

for i in range(number_of_threads):
    th = threading.Thread(target=do, args=(i,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

datafile = open("database.users", "ab")
pickle.dump(database, datafile)
datafile.close()
