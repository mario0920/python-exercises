def drawLine( lenght, direction):
    if direction == "h":
        print("-" * lenght)
    if direction == "v":
        print("| \n" * lenght)
drawLine(5, "h")
drawLine(3, "v")
