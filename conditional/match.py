name = input("What's Your name?")

# if name == "Harry":
#        print("Gryffindor")
# elif name == "Herimone":
#        print("Gryffindor")
# elif name == "Ron":
#        print("Gryffindor")
# elif name == "Dracor":                     
#      print("Slytherin")
# else:
#        print("Who?")     

# match name:
#     case "Harry":
#         print("Gryffindor") 
#     case "Hermione":
#         print("Gryffindor")   
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who") 

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor") 
    case "Draco":
        print("Slytherin")
    case _:
        print("Who") 