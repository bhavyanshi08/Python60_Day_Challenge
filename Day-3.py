N=int(input("Enter the number of students:"))
marks=[0]*N
for i in range(N):
    marks[i]=int(input())
valid=0
failed=0
reg_no=10790
for m in marks:
    if 90<=m<=100:
        print(m,"->Excellent")
        valid+=1
    elif 75<=m<=89:
        print(m,"->Very Good")
        valid += 1
    elif 60<=m<=74:
        print(m,"->Good")
        valid += 1
    elif 40<=m<=59:
        print(m,"->Average")
        valid += 1
    elif 0<=m<=39 :
        if reg_no%10==0:
          print(m,"-> Grace marks(Personalised Rule)")
        else:
           print(m,"-> Fail")
        failed+=1
        valid+=1
    else:
        print(m,"->Invalid")

print("Total Valid Students:",valid)
print("Total Failed Students:",failed)
