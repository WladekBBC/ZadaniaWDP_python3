def czy_ma_cyfre(haslo):
    for i in haslo:
        if i.isdigit():
            return True
    return False
def czy_ma_dlugosc(haslo):
    if len(haslo) < 9:
        return False
    return True
def czy_ma_duzy_znak(haslo):
    for znak in haslo:
        if znak.isupper():
            return True
    return False
#print(czy_ma_dlugosc(haslo))
#print(czy_ma_cyfre(haslo))
#print(czy_ma_duzy_znak(haslo))

def verification():
    haslo = str(input('Proszę wprowadzić haslo :  '))
    if czy_ma_dlugosc(haslo):
        #Hasło musi zawierać nie mniej niz 9 
        print('Very good -- ma 9 znaków!')
        if czy_ma_cyfre(haslo):
            #Hasło musi zawierać jakąś liczbę
            print('Very Good -- ma liczbę!')
            if czy_ma_duzy_znak(haslo):
                #Hasło musi zawierać duzy znak
                print('Very Good -- ma duzy znak!')
                return "Hasło odpowiada wszystkim wymaganiom"
            else:
                print('Hasło musi zawierać duzy znak')
                return "Hasło nie spełnia wymagań"
        else:
            print('Hasło musi zawierać jakąś liczbę!')
    else:
        print('Hasło musi zawierać nie mniej niz 9 znaków!')   
#print(verification())