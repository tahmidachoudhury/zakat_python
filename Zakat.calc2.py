def silverthreshold():
    #price of silver - changes in stocks
    silver = input("Please type the current price of silver per gram - remember to use GBP:\n")
    
    #threshold calc according to Musnad Ahmad 1233
    nisaab = 595*float(silver) 
    return ("The nisaab (threshold) of Zakat at this price of silver is £ ", nisaab)
    #except:
     #   print("Please type a number.\n")
      #  silverthreshold()

def goldthreshold():
    gold = input("Please type the current price of gold per gram - remember to use GBP:\n")
    try:
        #FIX THIS
        nisaab = float(gold)
        return ("The nisaab (threshold) of Zakat at this price of gold is £ ", nisaab)
    except:
        print("Please type a number.\n")
        goldthreshold()

def greeting(x):
    if x == 'yes' or 'y':
        print("    - This calculator will take into consideration the physical money that you have available, excluding value of owned properties and the value of businesses etc.")
        print("    - This calculator deals in only GBP (great british pounds) as the financial currency. Please convert the money before hand")
        print("    - This calculator has the option of calculating the threshold (nisaab) for the Zakat of Gold, however it is preffered by a scholarly consensus to take the nisaab of silver instead as it is lower, granting more people the ability to pay Zakat.\n")
        return
    else:
        return ("")








print('welcome to the Zakat Calculator.\n')
print("")
#make this alot user friendly and neat
option1 = input("Feel free to use this calculator at any time during the year. However before use, would you like a short reading on how this program works?: (y/n) \n")
greeting(option1)
goldorsil = input("Would you like to calculate with the gold or silver threshold (we recommend silver)\n")
if goldorsil == 'gold':
    goldthreshold()
if goldorsil == 'silver':
    silverthreshold()
else:
    print('fin')
    





