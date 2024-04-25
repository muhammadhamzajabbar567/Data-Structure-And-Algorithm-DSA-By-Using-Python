def greetings(language):
    if language == 'english':
        return "Hello World!"
    if language == 'french':
        return "Bonjour Le Monde"
    else:
        return "Language Not Supported!"

print(greetings('english'))
print(greetings('french'))
print(greetings('urdu'))

'''
user-defined functions are objects, we can do things such as include them in other
objects, such as lists
'''

l = [greetings('english'), greetings('french'), greetings('urdu')]
print(l[1])

'''
Functions can also be used as arguments for other functions. For example, we can define the
following function:
'''
def callf(f):
    lang = 'english'
    return (f(lang))

print(callf(greetings))

def call_f(f):
    language = 'french'
    return (f(language))

print(call_f(greetings))