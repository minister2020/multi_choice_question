# mult table

# No parameter
def greet():
    return "Welcome to the world of Python"

# one postional parameter
def n_table(num):
    # enumerate
    for index, value in enumerate(range(num, num*13,num),1):
        print(f"{num} x {index} = {value}")

# n_table(709)

# two postional parameter
def login(username,password):
    return f"{username.upper()}, welcome to the world of Python, your password is {password}"

login('ade', 123)    
    