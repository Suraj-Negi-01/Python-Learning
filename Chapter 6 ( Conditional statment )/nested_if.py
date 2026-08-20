marks = int ( input("Enter your marks :"))


if (marks >= 1) and (marks < 101):

    # nested if starts from here 
    
    if marks >= 80 :
        print("you got A+ grade")

    elif marks >= 75 :
        print("you got A grade ")

    elif marks >= 65 :
        print("you got B grade ")

    elif marks >= 55 :
        print("you got C grade ")

    elif marks >= 45 :
        print("you got D grade ")

    else :
        print("Sorry you are fail, try next year !")


else :
    print("You entered invalid marks !")