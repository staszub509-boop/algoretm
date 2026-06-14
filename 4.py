
name = input('what is your name? ')

def greet(name):
    print('hello, ' + name + '!')
    greet2(name)
    print('getting ready to say bye...')
    bye()

def greet2(name):
    print('how are you, ' + name + '?')
def bye():
    print('ok bye!')

print(greet(name))
print(greet2(name))
print(bye())
