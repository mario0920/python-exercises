def wrap_brackets ( text ):
    return "(" + text + ")"

def wrap_square ( text ):
    return "[" + text + "]"

def wrap_minimax ( text ):
    return "<" + text + ">"
r = "12345"
r = wrap_brackets(r)
r = wrap_square(r)
r = wrap_square(r)
r = wrap_square(r)
r = wrap_minimax(r)
r = wrap_minimax(r)
r = wrap_minimax(r)
print(r)


