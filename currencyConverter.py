
with open ('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split('\t')
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter the amount \n"))
print("Enter the currency in which you want to convert."
      "available options are:")
for item in currencyDict.keys():
    print(item)

currency = input("Choose among these \n")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")
