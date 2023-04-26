print('welcome to the Zakat Calculator.\n')
print("")
#make this alot user friendly and neat
option1 = input("Feel free to use this calculator at any time during the year. However before use, would you like a short reading on how this program works?: (y/n) \n")
if option1 == 'y':
    print("    - This calculator will take into consideration the physical money that you have available, excluding value of owned properties and the value of businesses etc.")
    print("    - This calculator deals in only GBP (great british pounds) as the financial currency. Please convert the money before hand")
    print("    - This calculator has the option of calculating the threshold (nisaab) for the Zakat of Gold, however it is preffered by a scholarly consensus to take the nisaab of silver instead as it is lower, granting more people the ability to pay Zakat.\n")
else:
    print("")

def silhold():
    #price of silver - changes in stocks
    silver = input("Please type the current price of silver per gram - remember to use GBP:\n")
    try:
        #threshold calc according to Musnad Ahmad 1233
        nisaab = 595*float(silver) 
    except:
        print("Please type a number.")
        silhold()

    print('The nisaab (threshold) of Zakat at this price of silver is £',nisaab)
    print("")
    print('Now we ask some questions to see if you are eligible to pay Zakat:')
    print("")
    def elg():
        umoney = input('How much money do you currently have in your account, combining all savings and current accounts?\n')
        try:
            if float(umoney) < nisaab:
                #broke
                print("You have not earned enough money to exceed the threshold")
                thanks = 'Thank you for using the Zakat Calculator!'
                print(thanks)
            else:
                #not broke - has zakat money; below is zakat calc according to Musnad Ahmad 1233
                zak = float(umoney)/40
                def elg2():
                    thanks = 'Thank you for using the Zakat Calculator!'
                    elg2 = input("Have you had £" ,nisaab, " for over a year? (y/n)\n")
                    if elg2 == 'n':
                        print('You are not eligible to pay Zakat.')
                        print("")
                        print(thanks)
                    elif elg2 == 'y':
                        print('The amount that you are to pay this year is £',zak)
                        print('')
                        tips = input('Would you like some tips on how to spend this Zakat? (y/n)\n')
                        try:
                            #bug - any other input SHOULD go to except - FIXED
                            if str(tips) == 'y':
                                print('A great way to donate this money is spending it back home. Helping out your home village or area that have poor people is a great way of ensuring that the money is going to the right people. It is best to stay away from online websites - especially during the month of Ramadan to avoid money going to the wrong place.')
                                print("")
                                print("As mentioned, paying Zakat during the month of Ramadan is a great way of gaining maximum reward. Throw a bit more money on top during the last ten nights, and just spend the days (and nights) making du'a to Allah for it to be accepted In'sha'Allah.")
                                print("")
                                print(thanks)
                            else:
                                print(thanks)
                        except:
                            #bug - FIXED
                            print(thanks)
                        
                    else:
                        print("Please answer with 'y' or 'n' \n")
                        elg2()
                elg2()
        except:
            print('please enter a number below:\n')
            elg()

    elg()
silhold()



    
