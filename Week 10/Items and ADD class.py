

class Item():
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def set_price(self, new_price):
        self.__price = new_price

    def get_price(self):
        return self.__price

    def total_price(self):
        return self.__price * self.__quantity

    def __str__(self):
        return "{} cost {} and we currently have {} in stock".format(self.__name, self.__price, self.__quantity)


def Fruits():
    fruits = {'apples', 'oranges'}
    print('The fruits we have available are:')
    print('1: Apples')
    print('2: Oranges')
    print('Please select which you would like to see')
    choice = input('')
    if choice == 'Apples' or choice == 'apples':
        print(Apples)
    else:
        print(Oranges)
    return


#Main
exiting = 0
Apples = Item('Apples', 6, 0.50)
Oranges =Item('Oranges', 8, 0.75)



while exiting != '4':
    print('Press 1 to see Fruits')
    print('Press 2 to see Vegetables')
    print('Press 4 to leave')
    exiting = input('')

    if exiting == '1':
        Fruits()

