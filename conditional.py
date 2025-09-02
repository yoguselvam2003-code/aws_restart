userReply =input(" Do you need to ship a package? (Enter yes or no)")
if (userReply =="Yes"):
    print("we can help you ship that package!")
else:
    print("please come back when you need to ship a ackage. thank you.")
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("we have many stamp desings to choose from.")
elif userReply == "envelope":
    print("we have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("how many copies would you like ? (enter a number)")
    print("here are {} copies.".format(copies))
else:
    print("thank you, please come again.")
     