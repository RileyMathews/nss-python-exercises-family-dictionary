# declare dictionary for family
my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}

# define function to print out family report
# using nested dictionaries in a comprehension
def family_set(family):
    return (f'{info["name"]} is my {relative} and is {info["age"]} years old' for relative, info in family.items())

def print_family(family):
    for person in family:
        print(person)

# call function and pass it the dictionary of family information
# function returns a set of strings to be printed
family = family_set(my_family)

# pass that set to a function which will print
# out each item in the set
print_family(family)
