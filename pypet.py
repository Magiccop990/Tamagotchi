

weight = cat.get("weight")
cat = {
"name": "Fluffy",
"age": 5,
"weight": 9.5,
"hungry": False,
"photo": '(=^o.o^=)',
}
def feed(pet):
	pet['hungry'] = False 
	pet['weight'] = pet['weight'] + 1.0
feed(cat)
# now some printing

print("Welcome to Pypet")
print("Hello " + cat.get("name"))
print(cat.get("photo"))

print(weight)

print(cat.get("hungry"))
#
