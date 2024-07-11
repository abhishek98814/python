# x =  int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


def main():
    y = int(input("Whats x? "))
    if is_even(y):
        print("Even")
    else:
        print("Odd") 

def is_even(n):
    #  return True if n % 2 == 0 else False
     return n % 2 == 0




# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


main()           