UPPER = 127
LOWER = 33

enter_character = input("Enter a character: ")
ascii_convert_char = ord(enter_character)
print("The ASCII code for {} is {}".format(enter_character, ascii_convert_char))
enter_number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while enter_number > 33 < 127:
    ascii_convert_num = chr(enter_number)
    print("The character for {} is {}".format(enter_number, ascii_convert_num))
    break
else:
    print("Invalid")
    enter_number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
for i in range(LOWER, UPPER):
    ascii_convert_num = chr(i)
    print("{0:>5} {1:>5}".format(LOWER, ascii_convert_num))
    LOWER += 1