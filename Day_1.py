name=input("Full Name:")
email=input("Email:")
mobile=input("Mobile:")
age=int(input("Age:"))
length = len(name)
validN=(name.find(' ')!=0 and name.find(' ')!=length-1 and name.count(' ')>=1)
validE=(email[0]!='@' and email.find('@')>0 and email.find('.')!=-1)
validM=(len(mobile)==10 and mobile.isdigit() and mobile[0]!='0')
validA= age>=18 and age<=60
if validN and validE and validM and validA:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
