import random
MAX_INCREASE = 0.25
MAX_DECREASE = 0.1


open_file = open("sumnumbers.txt", "w")
number = 1
while number <= 100:
    number_change = 0
    if random.randint(1, 2) == 1:
        number_change = random.uniform(0, MAX_INCREASE)
    else:
        number_change = random.uniform(-MAX_DECREASE, 0)

    number *= (1 + number_change)
    open_file.write("{}\n".format(int(number)))
open_file.close()