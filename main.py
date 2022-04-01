import pickle

database = pickle.load(open("database.users", "rb"))

for user in database:
    print("")
    user.info()
    print("")
