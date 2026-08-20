p1 = "get free gift"
p2 =  "you won"
p3 = "click this"
p4 = "open now"

msg = input("Enter your comment :")

if (p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg) :
    print("spam alert !")

else :
    print("safe comment !")