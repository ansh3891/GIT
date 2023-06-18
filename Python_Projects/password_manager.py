from cryptography.fernet import Fernet
mstr_pswrd=input("What's the master password (for now :'master'): ")
if mstr_pswrd!='master':
    print("Wrong Password.....Exiting program....")
    quit()
def view():
    with open('passwords.txt','r') as a:
             for line in a.readlines():
                 data=line.rstrip()
                 user,passw=data.split("|")
                 print("Username: ",user," Password: ",passw)
def add():
    usrname=input("Enter Username: ")
    pwd=input("Enter Password: ")
    with open('passwords.txt','a') as f:
        f.write(usrname+" | "+pwd+"\n")

while True:
    option=input("What would you like to do:"+"\n"+"1. Add a password(add)"+"\n"+"2. View a Password(view)"+"\n"+"3. Exit"+"\n")
    if option=='add':
        add()
    elif option=='view':
        view()
    elif option=='exit':
        quit()
    else:
        print('Invalid')
        continue
