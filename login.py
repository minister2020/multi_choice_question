#database
"""
users = 'ade'
password = 123
username = input('pls enter your username here:')
password = input('pls enter your password here:')
if username == users and password == 123:
    print('welcome')
    


if username == 'users':
   password = input('pls enter your password here:') 
   if password == 'password':
          print('looged in successfully') + users
   else:
        print('password incorrect')    
else:
    print('username incorrect')
# fix the error here

age = input('pls enter your age here:')
if int(age) >= 18:
    print('you are eligible to vote')
    print('lets go and vote')
else:
    print('you are not eligible to vote')


for index in range(10):
    print(index)

for index in range(1, 20):
    print(index)    

for index in range(1, 7, 2):
    print(index)
    

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers[2] = 'coba'
numbers.append(100)
numbers.insert(2,'coke')
del numbers[4]
numbers.pop()
numbers.remove('coke')
numbers.remove('coba')



guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort(reverse = True)

print(guests)


companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]  


def sort_key(company):
    return company[2]   

companies.sort(key = sort_key, reverse = True)  


print(companies)





def multiply(x,y):
    return x*y
for index, index1 in enumerate( range(5,65,5), 1):
    print(f" 5 * {index} = {index1}")
   # print(multiply(index,2))


def multiply(x,y):
    x = input('pls enter your first number here:')
    y = input('pls enter your second number here:')
for x, y in enumerate(range(), ):
    print(f"  * {x} = {y}")





num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 13):
   print(num,"X",i,"=",num * i)
"""

def multiplacation_table (num):
    num = int(input("Enter the number: "))
    for i in enumerate(range(num, num * 13), 1)        
      print 




multiplacation_table('num')