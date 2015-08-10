__author__ = 'fumandito'

my_dict = {
    "nome": "Fernando",
    "cognome": "Aspiazu",
    "eta": 28,
    "sesso": "M"
}

print my_dict.items()

print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print key, my_dict[key]
