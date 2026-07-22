contact={
    "neeraj": "123456",
    "Dheeraj": "234567",
    "feeraj": "345678"
}

new_contact=input("Enter the name to search:").strip().lower()
found=None

for i in contact:
    if i.lower()==new_contact:
        found=i
        print(found+" is the i")
        break

if found:
    print("Contact found:" + contact.get(found))
else:
    print("Contact not found. Do you wish to add it to the list(Y/N):")
    decision=input().upper()
    if (decision =="Y"):
        new_number= input("Enter the number please: ")
        contact[new_contact]= new_number
print("\n Phone book list is as follows:\n")
for i,j in contact.items():
    print(i,j)