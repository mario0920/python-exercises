born_year = int (input( "Write your born-year to know the status: " ) ) #status old, adult, yound, teen, kid, baby;

if 1900 <= born_year <= 2024:
    
    if 1900 <= born_year < 1929:
        print("your status is: old")
    if 1929 <= born_year < 1979:
        print("your status is: adult")
    if 1979 <= born_year < 1997:
        print("your status is: young")
    if 1997 <= born_year < 2012:
        print("your status is: teen")
    if 2012 <=  born_year <2021:
        print("your status is: kid")
    if 2021 <= born_year <= 2024:
        print("your status is: baby")
        
else:
    print("error - input a valid year")
    

            