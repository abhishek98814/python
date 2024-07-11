import sys

# try:
#    print("hello, my name is", sys.argv[1])
# except IndexError:
#    print("Too few argument")   

# if len(sys.argv) < 2:
#     print("Too few argumenr")
# elif len(sys.argv) > 2:
#     print("Too many argumentd")
# else:
#     print("Hello, my name is ", sys.argv[1])    


# if len(sys.argv) < 2:
#     print("Too few argumenr")
# elif len(sys.argv) > 2:
#     print("Too many argumentd")

# print("Hello, my name is ", sys.argv[1]) 


if len(sys.argv) < 2:
    sys.exit("Too few argumenr")

# for arg in sys.argv[1]:
#   print("Hello, my name is ", arg)    

for arg in sys.argv[1:-1]:
  print("Hello, my name is ", arg)    
