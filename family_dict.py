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
# using nested dictionaries in a loop
def family_report(family):
    for relative, info in family.items():
        print(f'{info["name"]} is my {relative} and is {info["age"]} years old')


# call function and pass it the dictionary of family information
family_report(my_family)
