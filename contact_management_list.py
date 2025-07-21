# Contact List Management

#READING CONTACTS !
import json
with open("contacts.json", "r") as f:
    people =json.load(f)["contacts"]

#ADDING CONTACTS !
def add_person():
        name = input("Name: ")
        age = int(input("Age: "))
        emailId = input("Email Id: ")
        person = {"name": name, "age": age, "Email": emailId}
        people.append(person)
        print('Successfully Added!')

#DELETING CONTACTS !
def del_person(people):
    for i, person in enumerate(people):
          print(f'{i+1} - {person["name"]} | {person["age"]} | {person["Email"]}')
    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <=0 or number > len(people):
                 print("Invalid Number, Out of range!")
            else:
                break
        except:
            print("Don't enter strings!")
    people.pop(number - 1)
    print("Deleted Successfully")

#SEARCHING CONTACTS !   
def search(people):
     serach_name = input("Search for a name: ").lower()
     result = []
     for person in people:
          name = person["name"]
          if serach_name in name.lower():
            result.append(person["name"])
            result.append(person["age"])
            result.append(person["Email"])
          
     print("Results: ",result)

#MAIN CONTENTS !
while True:
    print()    
    print(f"Contact List Management Portal - Total contacts is {len(people)}")
    print()
    cmd = input("You can 'Add', 'Delete', 'search' or 'quit' for contacts : ").lower()

    if cmd == 'add':
        add_person()
           
    elif cmd == 'delete':
        del_person(people)

    elif cmd == 'search':
        search(people)

    elif cmd =='quit':
         break
    else:
        print("Enter the valid Request !")

#WSAVING CONTACTS
with open("contacts.json", "w") as f:
    json.dump({"contacts": people},f)





        





