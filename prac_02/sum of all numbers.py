open_file = open("sumnumbers.txt", "r")
number_total = 0
for line in open_file:
    number = int(line)
    number_total += number
print("The sum of sumnumbers.txt is {}".format(number_total))
open_file.close()