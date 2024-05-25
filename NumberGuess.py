import random
print("hi whats your name")
name = input()
randomnumber = random.randint(1,10)
print("hello "+ name + " am thinking of a number between 1-10, what do you think it is")
for i in range(7):
    number = int(input())
    if number < randomnumber:
        print("no thats too low")
    elif number > randomnumber:
        print("no too high")
    else:
        print("yes" + str(number) + "was the number i was thinking of")


if randomnumber!= number:
    print("you lose the number i was thinking of was" + str(randomnumber))
else:
    print("congratulations thats correct " +str(number) + " was the nunber i was thinking of")