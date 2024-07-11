

# for i in [0,1,2,3]:
#     print("meow")


# i = 10
# while  i !=0:
#     print(i)
#     i = i-1



# i = 0
# while i <10:
#     print(i)
#     i = i + 1


# for i in range(3):
#     print("meow")


# for _ in range(3):
#     print("Hello")


# a = int(input("What number you wanna provide??"))

# for a in range(a):
#       print("Hello")


# print("Meow\n" * 4, end="")


# a = int(input("What's the value of a"))


# i = a
# while i <10:
#     print(i)
#     i = i + 1


# value = int(input("What the value??"))

# for _ in range (value):
#            print("Hello Bruh")


# n = int(input("Whats the value of n??"))

# for _ in range(n<10):
#     n = n<10
#     print(n)


# while True:
    # n = int(input("What's n?? "))
    # if n < 0:
    #     continue
    # else:
    #     break
    # if n < 0:
        # continue


# for _ in range(n):
#     if n > 10: 
#      print(n+1)



# while True:
#     n = int(input("What's n ?"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow") 
    # if n < 0:
    #     print(n-1)   



def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
          n = int(input("What's the value of n?"))
          if n > 0:
               break
    return n


def meow(n):
        for _ in range(n):
              print("meow")


main()              