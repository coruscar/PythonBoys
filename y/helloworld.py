# Printing.
hello_world = True

if hello_world:
	print("Hello World!")
	print('Hello World!')

print('''
    (\_/)
    (o  o)
    This is a cute bunny.
    ... Maybe.
    ''')

print('''我们来打个中文试试？
    噢噢噢噢可以打中文！''')

# Something else.
year_born = input('What year were you born? ')
current_year = 2018
age = current_year - int(year_born)

if age > 0:
    print('You are ', age, ' years old latest by the end of the year.')
else:
    print('Error! ')

# Something else else.
print('strawberry ' * 10)
print('banana ' * 6)
