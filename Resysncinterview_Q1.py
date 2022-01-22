

print("Welcome!") 
while True: 
    try: 
        #line = input()
        my_str = input("Please input the string:")
        input_str="print happy against monkey need different effect sheep paper horse parallel journey kind account opinion lock knowledge look weather join market space married who nerve responsible payment again while rhythm prison opposite special why authority rest school operation river year shake than shame push when question road waiting Zoo respect that ring then very theory water tomorrow wheel umbrella the view walk twist unit voice waste together week weight yesterday tooth you young Zibra will yellow brain verse Xray cloud adjustment between where connection branch care needle about with addition cart button control desire Xman cloth balance"
        words = [word.lower() for word in my_str.split()]
        if my_str == input_str:
           words.sort()
           print("The sorted words are:")
           for word in words:
              print(word)      
        else:
           print("Error Message: Input strings are different from provided input string")
    except EOFError: 
        break
    input('Press ENTER to exit') 



