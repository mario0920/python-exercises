# App where:
# IN money amount
# IN currency
# OUT money amount

input_currency = ("choose currency: MLD/RON: ") # "MLD"
input_amount   = float(input("enter amount: ")) 

rate_MLD_to_RON = condition_1 = 1
rate_RON_to_MLD = condition_2 = 0.26

if input_currency == "MLD":
    moneyRON = input_amount / condition_1
    print("you've got: ", moneyRON, "RON")
else:
    moneyMLD = input_amount / condition_2
    print("you've got: ", moneyMLD, "MLD")
