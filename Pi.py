continue_game = "yes"
while(continue_game=="yes"):
    user_input = input("ENTER THE DIGITS OF PI RIGHT NOW: ")
    pi = "3.1415926535897932384626433832795028841971693993751"
    
    pi_dig = pi[2:]
    digits = user_input[2:]
    length = len(digits)
    print ("YOU GUESSED PI UP TO "+ str(length) + " DIGITS")
    
    compare = pi_dig[0:length]
    
    
    if digits == compare:
        print ("YOU GOT IT CORRECT WOW")
    else:
        print ("YOU GOT IT INCORRECT YOU SUCK")
        
        for i in range (len(compare)):
            if compare[i] != digits[i]:
                break
        print ("YOURE FIRST INCORRECT DIGIT WAS AT "+ str(i+1))
        print("the correct digit was: " + compare[i])
        print("you guessed: "+ digits[i])
    continue_game=input("Do you want to play again ")
    if continue_game=="no":
        print("Thanks For Playing")
