open_file = open("name.txt", "r")
user_name = open_file.read().strip()
print("Your name is {}".format(user_name))
open_file.close()