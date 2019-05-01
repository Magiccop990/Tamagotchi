om tkinter import *
from tkinter import messagebox
global name, photo


name = "cat"
photo = "(=^o.o^=)"


window = Tk()
window.geometry("1920x1080")
window.title("PyPet")
host_nme_lbl = Label(text = "Name:")
host_pht_lbl = Label(text = "Photo:")
host_nme_lbl.grid(row = 0, column = 0)
host_pht_lbl.grid(row = 2, column = 0)
host = StringVar()
nme_entry = Entry(window, textvariable = name)
pht_entry = Entry(window, textvariable = photo)
nme_entry.grid(row = 1, column = 0)
pht_entry.grid(row = 3, column = 0)
#------------------------------------------------------------------------
cat = {
"name": "Fluffy",
"age": 5,
"weight": 9.5,
"hungry": True,
"photo": '(=^o.o^=)',
}

#-----------------------------------------------------------------------
def feed(pet):
	if pet['hungry'] == True:
		pet["hungry"] = False
		pet['weight'] = pet['weight'] + 1.1
	else:
		print("Pypet is not hungry")
	
def feeding(pet):
	if input("Feed your cat? ") == "yes":
		feed(pet)
		print("Feeding your %s") % ( cat.get("name") )
	else:
		print("So you want your cat to starve? ")
#----------------------------------------------------------------------


feeding(cat)


	
print("Welcome to Pypet")
print("Hello " + cat.get("name"))
print("Am I hungry? " + str(cat.get("hungry")))
print(cat.get("photo"))
print( "Weight " + str(cat.get("weight")))
