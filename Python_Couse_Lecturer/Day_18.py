#Message Filter

p1="Make a lot of money"
p2="Win a lottery"
p3="Buy a house"
p4="Buy a car"
p5="Get married"
p6="Go to heaven"
p7="Go to hell"
p8="Get a job"
p9="Be a rich man"
p10="Be a poor man"
message=input("Enter your message:")
#here we ae using lower() function to convert the message into lower case because some user can enter
acceptedMessage=message.lower()
print(acceptedMessage)

if acceptedMessage in p1 or p2 or p3 or p4 or p5 or p6 or p7 or p8 or p9 or p10:
    print("Your message is not safe")
else:
    print("Your message is safe")
print("Congratulations you have successfully make the spam filter program using python")