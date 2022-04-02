import pickle
print("Loading users...")
database = pickle.load(open("database.users", "rb"))

for user in database:
    print("")
    user.info()
    print("")
