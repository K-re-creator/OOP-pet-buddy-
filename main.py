from Pet import Pet

# Creating my pet
my_pet = Pet("Buddy")

# Interacting with the pet
my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("sit")
my_pet.train("roll over")

# Showing updated status and tricks
my_pet.get_status()
my_pet.show_tricks()