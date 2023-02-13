import datetime
from datetime import date
import re
user_registeration=[]
print("welcome to application!")
option=int(input("if new here register yourself first enter 1\nIF Already registered Login yourself by entering 2\n"))
def registeration():
    register={
              "first name":"",
              "last name":"",
              "date of birth":"",
              "email id":"",
              "password":"",
             }
    first_name=input("please enter your first name\n")
    last_name=input("enter your last name")
    date_of_birth=input("enter your date of birth(dd/mm/yyyy)")
    email_id=input("enter your valid email id")
    password=input("enter a password")
    age=today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
    print(f'your age is:{age}')
    register.update({"first name":first_name,"last name":last_name,"date of birth":date_of_birth,"email id":email_id,"password":password})
    user_registeration.append(register)

def email_validation(email_id):
    reg_exp = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(reg_exp,email_id):
        print("Valid email ")
    else:
        print("Invalid Email please enter a valid email address \n")
        
def password_validation(inp_pswd):
    pswd_lower = 0
    pswd_upper = 0
    pswd_digit = 0
    pswd_special_char = 0
    if len(inp_pswd)>= 8:
        for i in inp_pswd:
            if i.islower():                
                pswd_lower += 1
            
            if i.isupper():
                pswd_upper += 1 
            
            if i.isdigit():
                pswd_digit += 1
            
            if (i == '@' or i == '$' or i == "_"):
                pswd_special_char += 1
    else:
        print("At least 8 digit passwprd is required!")

    if pswd_lower >=1 and pswd_upper >= 1 and pswd_digit >= 1 and pswd_special_char >=1 and pswd_lower+pswd_upper+pswd_digit+pswd_special_char == len(inp_pswd):
        print("valid Password")
    else:
        print("Invalid Password")
             
if option==1:
    #taking inputs for registeration
    registeration()

elif option==2:
    registered_email=input("enter your registered email id")
    enter_password=input("enter your password")
    for i in user_registeration:
        if i['email id'] == registered_email:
            if i['password'] == enter_password:
               print("login successful!!")

    else:
        print("your login was unsuccessful")
        inp_option=print("1.register yourself\n2.exit")
        if inp_option==1:
            registeration()
        else:
            exit()    


