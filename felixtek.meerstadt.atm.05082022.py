#FELIXTEK 2022
#PROJECT MEERSTADT - AUTOMATIC TELLER MACHINE SIMULATOR
#BUILD DATE: AUGUST 4TH AND 5TH, 2022 ANNO DOMINI

argument = ""

def sorting():
    thousandbahtnotes = 0
    fivehundredbahtnotes = 0
    onehundredbahtnotes = 0
    remainingmoney = 0
    moneyinput = int(input("Insert amt. > "))
    if moneyinput % 100 != 0:
        print("\nValue error. Please use numbers dividable by 100 only.")
        sorting()
    elif moneyinput % 1000 != 0:
        thousandbahtnotes = int(moneyinput / 1000)
        remainingmoney = moneyinput - (thousandbahtnotes * 1000)
    elif moneyinput % 1000 == 0:
        thousandbahtnotes = int(moneyinput / 1000)
        remainingmoney = 0
    elif moneyinput < 1000: 
        thousandbahtnotes = 0
        remainingmoney = moneyinput
    print("You have %d 1000 banknotes." % (thousandbahtnotes))
    if moneyinput % 500 != 0:
        fivehundredbahtnotes = int(remainingmoney / 500)
        remainingmoney = remainingmoney - (fivehundredbahtnotes * 500)
    elif moneyinput % 500 == 0:
        fivehundredbahtnotes = int(remainingmoney / 500)
        remainingmoney = 0
    print("You have %d 500 banknotes." % (fivehundredbahtnotes))
    if moneyinput % 100 == 0:
        onehundredbahtnotes = int(remainingmoney / 100)
        remainingmoney = 0
    print("You have %d 100 banknotes." % (onehundredbahtnotes))

    runagain()

def runagain():
  global argument
  argument = input("Run again? (Y/N)\n> ").capitalize()
  if argument == "Y":
    sorting()
  elif argument == "N":
    print("Bye.")
    quit()
  else:
    print("Invalid response.")
    runagain()

if __name__ == "__main__": #main function
  while True:
    sorting()
    if argument == "N":
      break