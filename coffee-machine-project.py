import sys
import time

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


machineStart = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(machineStart):
    print("\n")
    x = 0
    for y in machineStart:
        if x == 2:
            print("Coffee: " + str(machineStart[y]) + "G")
        elif x == 1:
            print("Milk: " + str(machineStart[y]) + "ML")
            x += 1
        elif x == 0:
            print("Water: " + str(machineStart[y]) + "ML")
            x += 1
    print("\n")

def makeCoffee(machineStart):
    y = 0
    wantsCoffee = True
    for x in machineStart:
        if machineStart[x] > mList[y]:
            machineStart[x] -= mList[y]
            y += 1
        elif machineStart[x] < mList[y]:
            machineStart[x] -= mList[y]
            y += 1
        wantsCoffee = True
    keys = [k for k, v in machineStart.items() if v < 0]
    if len(keys) > 0:
        w = 0
        for z in keys:
            print("Sorry, there is not enough " + keys[w] + ".")
            w += 1
        wantsCoffee = False
    return machineStart, wantsCoffee

def makePayment(order, menu):
    quarter = float(int(input("How many quarters?: ")) * 0.25)
    dimes = float(int(input("How many dimes?: ")) * 0.1)
    nickles = float(int(input("How many nickles?: ")) * 0.05)
    pennies = float(int(input("How many pennies?: ")) * 0.01)
    total = float(quarter + dimes + nickles + pennies)
    if total < menu[order]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        time.sleep(1.5)
        wantsCoffee = False
    elif total > menu[order]["cost"]:
        change = round(total - menu[order]["cost"], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {order}" + "☕" + ". Enjoy!")
        wantsCoffee = True
    return wantsCoffee        

wantsCoffee = True
while wantsCoffee == True:
    order = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if order == "report":
        report(machineStart)
    if order in menu:
        mList = []
        for x in menu[order]["ingredients"]:
            mList.append(int(menu[order]["ingredients"][x]))
        if len(mList) == 2:
            mList.insert(1, 0)
        machineStart, wantsCoffee = makeCoffee(machineStart)
        if wantsCoffee == True:
            print("Please insert coins.")
            wantsCoffee = makePayment(order, menu)
    if order not in menu or wantsCoffee == False:
        print("Turning coffee machine off...")
        time.sleep(1.5)
        sys.exit()