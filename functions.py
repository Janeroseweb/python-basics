 # functions
import random
# a-append w- write
with open("data.txt", "w") as file:
    #file.write("99\n")
    #file.write("68\n")
    for temp in range(100):
        x = random.randint(-10,65)
        file.write(str(x)+"\n")
with open ("data.text","r") as file:
    content =file.read() #0 params 0 args
    print(content)

    #install
    #use




