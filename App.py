# import this
# print("Hello World")
# print(5*7)

# myAge= 32
# print(myAge)

# recLength = 10
# recBreadth = 5
# recArea = recLength * recBreadth
# print(recArea)

# myName = "Adefemi"
# myAge = 20

# print(type(myName))
# print(type(myAge))

# msg = 'He said, "Aren\'t cant\'t shouldn\'t wouldn\'t."'
# msg1 = '''He said, "Aren't cant't shouldn't wouldn't."'''
# print(msg)
# print(msg1)

# print("Python" + 'n' + 'Programming')
# print("Python " * 4)

# myAge = 25
# myMsg = 'I am %s years old'
# print(myMsg % myAge) #I am 25 years old

# myAge1 = 25
# myName = 'My name is Adefemi'
# myMsg1 = '%s I am %s years old'
# print(myMsg1 % (myName, myAge1)) #My name is Adefemi I am 25 years old

# myAge1 = 25
# myName = 'My name is Adefemi,'
# myMsg1 = f'{myName} I am {myAge1} years old'
# print(myMsg1) #My name is Adefemi I am 25 years old

# text = 'Welcome to IGEM'
# print(len(text))
# print(text.upper())
# print(text.lower())
# print(text.count('m'))
# # print(text.count('w', 't'))
# print(text.index('t'))
# print(text.replace('l', 'j'))
# print(text.split(' '))
# print(text.center(6))

# #LIST

# primeNumbers = [2, 3, 5, 7, 11]
# print(primeNumbers)
# names = ['Ade', 'Ayo', 'Tola', 'Kola', 'Jide']
# newList = primeNumbers + names
# print(names)
# print(newList) # [2, 3, 5, 7, 11, 'Ade', 'Ayo', 'Tola', 'Kola', 'Jide']
# print(newList[5]) #Ade

# primeNumbers.append(13)
# primeNumbers.remove(5) #[2, 3, 7, 11, 13]
# print(primeNumbers) #[2, 3, 7, 11, 13]

#TUPLE
# tuple1 = (5, 15, 'Adekunle', 4.6)
# num = [1, 2, 3, 4, 5, 6]
# print(tuple1)
# print(type(tuple1)) #<class 'tuple'>
# print(tuple1[2]) #Adekunle
# print(tuple1.index(4.6)) #3
# print(tuple1.count(4.6)) #1
# tupleToList = list(tuple1)
# listToTuple = tuple(num)

# print(tupleToList) #[5, 15, 'Adekunle', 4.6]
# print(listToTuple) #(1, 2, 3, 4, 5, 6)

# # COMPARISON OPERATION
# # <, >, !=, ==, <=, >=
# #CONDITIONAL STATEMENTS
# cash = 6
# if cash > 10:
#     print('Buy Chocolate')
# elif cash == 4:
#     print('I don port by Saka')
# else:
#     print('Book')

# money = 80
# if money == 100 or money == 80 or money == 60:
#     print('I am rich')
# else:
#     print('I am cashless')

# # FOR LOOPS
# for x in range(0, 5):
#     print(f'{x} Hello')

# dog = [1, 2, 3, 4]
# for x in dog:
#     print(f'{x} Hello')

# name = 'Adefemi'
# nameList = ('Adefemi', 'Kola', 'Joy', 'Kemi')
# for x in nameList:
#     print(f'Hello {x}')

# # WHILE LOOPS
# num = 7
# while num < 10:
#     print('My endless loop')

# while num < 10:
#     num = num + 1
#     print('goooop')

# # NESTED FOR LOOPS
# items = [['red', 'pink'], ['berry', 'grapes'], ['cat', 'dog']]

# for item in items:
#     for x in item:
#         print(x)

# for i in range(1, 13):
#     for x in range(1, 13):
#         print(f'{i} X{x} = {i * x}')

#     print('===========================')

# def get_milk(amount, destination):
#     print('Open the door')
#     print(f'Walk to the {destination} ')
#     print(f'Buy ${amount} Milk')
#     print('Return home with milk')

# get_milk(7, 'Main store')
# get_milk(destination= 'Main store', amount=7)

# def times(a, b):
#     return a * b

# print(times(3, 5))

import Life
# import Life as calc
from Life import theAnswer
from Life import name
# import pandas as pd
import datetime
import random
import math



# value = Life.theAnswer
# piValue = math.pi
# print(type(Life))
# print((value))
# print((piValue))
# print((math.e))
# print(theAnswer)
# # print(calc)
# print(name)
Life.quote_albert()
# hmm = Life.square_root(225)

print(Life.square_root(225))