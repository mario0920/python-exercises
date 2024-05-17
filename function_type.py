"""
a_int = int(input("itn"))
a_float = float(input("float"))
a_bool = bool(input("bool"))
"""

def inputInt(message):
    return int(input(message))

def inputFloat(message):
    return float(input(message))

def inputBoolean(message):
    return bool(input(message))

n = inputInt("primul numar: ")
m = inputInt("al doilea numar: ")

print(n + m)