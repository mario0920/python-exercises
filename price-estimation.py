price = int(input("cit costa ? "))
money = 10

# x----------------------10-----------------------50------------>
if price < 0:
    print("pretul nu poate fi negativ")
elif price <= money:
    print("Ideal")
elif price <=50:
    print("ok")
else:
    print("Scump")