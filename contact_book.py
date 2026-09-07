# === CONTACT BOOK ====
contact_book = []  # make empty list because add multiples contacts
def add_contact(): #make function for add new contacts
  name = input("Enter your name: ") # take input name,phone no. and email because user use input and add contact in contact book
  phone_no = int(input("Enter your phone number: "))
  email = input("Enter your Email address: ")
  data={"Name" : name , "phone no." : phone_no , "Email Address" : email } #make dictionary
  contact_book.append(data) # use append method for adding dictionary into list

def view_contact():#make view contact function for using how many contact in my contact book
  for contact_list in contact_book:
    print(contact_list)

def search_contact(): # make function of searh_contact for using serach name
  search_name = input("Enter your name: ")
  found_name = False # make variable for found_name
  for contact_name in contact_book: # using loop because bcz search name in contact book
     if contact_name ["Name"] == search_name:
      found_name = True # when condtion is true so find name and show the user
      print(contact_name)

  if found_name == False: # when condition is false so not found error show the user
   print("Name not found")
while True: # using while loof for menu create when loop is true so work and perfom while loop condition
    print("===CONTACT BOOK===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choose = input("Enter your any one option  (1-4): ") # create choose variable take input from users

    if choose == "1":   # use if ,elif ,else condition  because when user choose option so call function and show the result of user
      add_contact()

    elif choose == "2":
      view_contact()
    elif choose == "3":
      search_contact()
    elif choose == "4":
      print("Exit")
      break  # use break statment for progrmm successufully stop when use choose option no.4
    else :
      print("Invalid option")
