from datetime import date, datetime
def star_sign(date):
    print(date)
    def date(x): 
        global 'month'
        global 'day'
        x = x.split('-')
        print(x)
        'month' = int(x[1])
        'day' =int(x[2])
        print(month)
        print(day)
    if 'month' == 1 :
        if 'day' >= 21:
            return 'Aquarious'
        else:
            return 'Capricon'
    elif month == 2 :
        if day <=19 :
            return 'Aquarious'
        else:
            return 'Pisecs'
    elif month == 3 :
        if day <=20 :
            return 'Pisces'
        else:
            return 'Aries'
    elif month == 4 :
        if day <=20 :
            return 'Aries'
        else:
            return 'Taurus'
    elif month == 5 :
        if day <=21 :
            return 'Taurus'
        else:
            return 'Gemini'
    elif month == 6 :
        if day <=21 :
            return 'Gemini'
        else:
            return 'Cancer'
    elif month == 7 :
        if day <=22 :
            return 'Cancer'
        else:
            return 'Leo'
    elif month == 8 :
        if day <=23 :
            return 'Leo'
        else:
            return 'Virgo'
    elif month == 9 :
        if day <=23 :
            return 'Virgo'
        else:
            return 'Libra'
    elif month == 10 :
        if day <=23 :
            return 'Libra'
        else:
            return 'Scorpio'
    elif month == 11 :
        if day <=22 :
            return 'Scorpio'
        else:
            return 'Sagittarius'
    elif month == 12 :
        if day <=21 :
            return 'Sagittarius'
        else:
            return 'Capricorn'
#Aqu   arius ------ 21 January - 19 February
#Pisces --------- 20 February - 20 March
#Aries ---------- 21 March - 20 April
#Taurus -------- 21 April - 21 May
#Gemini -------- 22 May - 21 June
#Cancer -------- 22 June - 22 July
#Leo ------------- 23 July - 23 August
#Virgo ----------- 24 August - 23 September
#Libra ----------- 24 September - 23 October
#Scorpio -------- 24 October - 22 November
#Sagittarius ---- 23 November - 21 December
#Capricorn ----- 22 December - 20 January


print(star_sign(date(1970, 6, 5)))
print(star_sign(date(2000, 2, 15)))
print(star_sign(date(1987, 8, 23)))

print(star_sign('2000, 2, 15'))
          
