start_n = 5 # variabila 1
end_n = 10 # variabila 2
while start_n == 5:
    start_n = int(input("Introduceti valoarea mai mica (5, 10): " ) )
    if start_n== 5:
            for start_n in range(5,11):
                print(start_n)
                start_n += 1
                
while end_n == 10:
    end_n = int(input("Introduceti valoarea mare (5, 10): " ) )
    if end_n == 10:
            for start_n in range(5,11): 
                print(end_n)
                end_n -= 1
                
                