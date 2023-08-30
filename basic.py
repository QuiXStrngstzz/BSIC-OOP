import os

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name  = last_name.capitalize()
    
    def intro(self):
        return "I'am " + self.first_name + " " + self.last_name
    
size = int(input("HOW MANY NAMES: "))
list_of_names = []

print("ENTER FULL NAME BELOW")
print("_____________________")

for _ in range(size):
    full_name = input(": ").split()
    
    First_name = full_name[0]
    Last_name  = full_name[1]
    
    casey = Person(First_name, Last_name)
    list_of_names.append(casey)

os.system("cls" if os.name == "nt" else "clear")

for person in list_of_names:
    print(person.intro())