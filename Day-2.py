StudentID=input("ID:")
EmailID=input("Email:")
Password=input("Password:")
Referral=input("Referral:")
length = len(EmailID)
code=len(Referral)
SId=(StudentID[0]=='C' and StudentID[1]=='S'and StudentID[2]=='E' and StudentID[3]=='-'and StudentID[4:].isdigit() and len(StudentID)==7)
EId=(EmailID[0]!='@' and EmailID[length-1]!='@'and EmailID.count('@')==1 and EmailID.count('.')==1 and EmailID[length-4: length]==".edu")
Pass=(len(Password)>=8 and 'A'<=Password[0]<='Z' and (Password.count("0") or Password.count("1") or Password.count("2") or Password.count("3") or Password.count("4") or Password.count("5") or Password.count("6") or Password.count("7") or Password.count("8") or Password.count("9"))  )
ref=(Referral[0:3]=='REF' and Referral[3:5].isdigit() and Referral[code-1]=='@')
if SId and EId and Pass and ref:
    print("APPROVED")
else:
    print("REJECTED")

