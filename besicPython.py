#set
animals = {"dog","cat","lion","tiger",True,100}
animals.add("duck")
animals.update(("pig","yiraf"))

pets = set(("dog","cat","rabbit","pocupine"))

print(animals)
print(pets)

data =animals.difference(pets)
print(data)