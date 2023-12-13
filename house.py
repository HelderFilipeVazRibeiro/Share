name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")



"""
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")
"""

"""
if name == "Harry":
    print("Grynffindor")
elif name == "Hermione":
    print("Grynffindor")
elif name == "Ron":
    print("Grynffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")
"""
"""
2ª option

if name == "Harry" or name == "Herminone" or name == "Ron":
    print("Grynffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")
"""