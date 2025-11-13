print ("what is the tempurature today?")
temp = input()
temp = int(temp)
print("Will it rain today? (yes/no)")
rain = input()
if temp >20:
    print("Wear sweatpants and a sweater")
elif temp >10:
    print("Wear sweatpants and a sweater")
    print("I recommend a jumper as well")
elif temp >5:
    print("Wear sweatpants and a sweater")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
else: 
    print("Wear sweatpants and a sweater")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
else:
    print("-----------")
