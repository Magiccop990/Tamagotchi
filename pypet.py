stats

cat = {

"name": "Fluffy",

"age": 5,

"weight": 9.5,

"hungry": True,

"photo": '(=^o.o^=)',

}





def feed(pet):
	if pet['hungry'] == True:
		pet["hungry"] = False
		pet['weight'] = pet['weight'] + 1.1
	else:
		print("Pypet is not hungry")
	
def feeding(pet):
	if input("Feed your cat? ") == "yes":
		feed(pet)
	else:
		pass
# now some printing

feeding(cat)

print("Welcome to Pypet")

print("Hello " + cat.get("name"))

print("Am I hungry? " + str(cat.get("hungry")))

print(cat.get("photo"))
print( "Weight " + str(cat.get("weight")))
