# x = int(input("What's x ? "))
# print(f"The value of x is {x} {5 + x}")

# c = 50 + x
# print(c)

# try:
#     x = int(input("What's x? "))
#     print(f" X is {x}")
# except ValueError:
#     print("X is not an integer")



# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("X is not an integer")    
# else:
#     print(f" X is {x}")


# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("X is not an integer")  
#     else:
#         break      

# print(f"x is {x}")
def main():
     x = get_int()
     print(f"x is {x}")



# def get_int():
#        while True:
#            try:       
#                x = int(input("What's x? "))
#            except ValueError:
#                print("X is not an integer")  
#            else:
#                break      
#        return x


def get_int():
       while True:
           try:       
                return int(input("What's x? "))
           except ValueError:
                 pass

main()