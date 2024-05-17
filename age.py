def calculate_age(birth_year): # define function
    current_year = 2024
    age = current_year - birth_year
    return(age)
  
birth_year = int( input( "enter your birth year: " ) )
age = calculate_age(birth_year)
print("Your age is:", age)