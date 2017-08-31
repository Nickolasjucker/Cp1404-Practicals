COLOUR_HEX = {"Cadet blue": "#5f9ea0", "Coral": "#ff7f50", "Gray": "#bebebe", "Green": "#00ff00",
              "Khaki": "#f0e68c", "Lavender": "#e6e6fa", "Magenta": "#ff00ff", "Purple": "#a020f0",
              "Red": "#ff0000", "Yellow": "#ffff00"}

print("You can check the hex from these colors:")
for colors in COLOUR_HEX.items():
    print("- {}".format(colors[0]))

color = input("Enter color: ").capitalize()
while color != "":
    if color in COLOUR_HEX:
        print("The hex for", color, "is", COLOUR_HEX[color])
    else:
        print("Invalid color")
    colors = input("Enter color: ").capitalize()

