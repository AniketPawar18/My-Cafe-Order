import time

Menu={'Tea':20,'Coffee':45, "Cola" : 50, 'lemon tea': 35,'Pizza': 120, "Burger": 90, 'Fries': 55, 'Roll': 80, 'Icecream': 190,'Milkshake': 95}

print('*****|| Welcome to the Cafe 🙏 || *****\n')
print("Here is our menu!!")
print(' 1. Drinks\n\tTea:20\n\tCoffee:45\n\tCola : 50\n\tlemon tea: 35\n',
      '2. Food\n\tPizza: 120\n\tBurger: 90\n\tFries: 55\n\tRoll: 80\n',
      '3. Dessert\n\tIcecream: 190\n\tMilkshake: 95\n')

tot_price1 = 0
tot_price2 = 0
item_2 = None
while True:
    item = input('What you wanna order?\n')
    if item in Menu:
        tot_price1 += Menu[item]
        print('Your order is processing......')
        time.sleep(3)
        print(f'Your order "{item}" has been placed ✅')
        break
    else:
        print('This item is not available,\n Please choose another food')

another_order = input('\nDo you wanna order Something else?\n Yes/No\n')
if another_order == 'Yes' or "yes":
    while True:
        item_2 = input('What you wanna order?\n')
        if item_2 in Menu:
            tot_price2 += Menu[item_2]
            print('Your order is processing......')
            time.sleep(3)
            print(f'\nYour order:-{item_2} has been placed\nGenerating your bill.....')
            break
        else:
            print('This item is not available,\n Please choose another food')
else:
    print('Generating your bill.....')

tot_price3 = tot_price1+tot_price2
Gst = float(tot_price3*5/100)
time.sleep(3)
print('  ----------------------------')
print(f' |**** Your total bill is ****|')
print(f' |  {item}     -  {tot_price1}          |')
if item_2 is not None:
    print(f' |  {item_2}     -  {tot_price2}          |')
print(f' |  SGST      -  2.5%         |')
print(f' |  CGST      -  2.5%         |')
print(" |----------------------------|")
print(' |  Total Bil =',tot_price3+Gst,'/-      |')
print(' |----------------------------|')
print(' |       Visit Again 🙏       |')
print('  ------------------------------')

