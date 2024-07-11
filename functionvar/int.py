# +
# -
# *
# / 
# %


# x = 1
# y = 2
 
# z= x+y
# print(z)

# x = input("What's x? ")
# y = input("what's y? ")

# z = int(x) + int(y)

# print(z)

# x = int(input("What's x? "))
# y = int(input("what's y? "))

# z = x + y

# print(z)


# float 

# x = float(input("What's x? "))
# y = float(input("what's y? "))

# z = round(x + y)
# z = x / y

# print(f"{z:,}")
# this is how we put commas by us system 

# print(f"{z:.2f}")
# this is how we xcontrol float 



def main():
    x = int(input("what is the value of x"))
    print("x square is", square(x))


def square(n):
    # return n*n
    # return n **2
    return pow(n, 2)

# we can also do like this for power solving 


main()
