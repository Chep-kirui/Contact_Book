#let us create a simple contact book
#Collect contacts
names =[]
phone_numbers=[]
num= 3
for i in range(num):
    name=input("Name ")
    phone_number=input("Phone Number: ") #f0r convert to int=> int(input("Phone Number: "))

    names.append(name)
    phone_numbers.append(phone_number)
#Display contact list
print("{:<15} {:<15}".format("Name", "Phone Number"))
#print("\nName\t\t\tPhone Number\n")

for i in range(num):
    #print( {phone_numbers[i]}")
    print("{:<15} {:<15}".format(names[i], phone_numbers[i]))

#Search contacts
search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
if search_term.lower() in [n.lower() for n in names]: #allows for either case of searched term
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))
else:
    print("Name Not Found")