n=int(input("how many numbers you need to add"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print(sum)
#string
string=input("which word you need to reverse")
string2=('')
for i in string:
    string2=i+string2
    print("The reversed version of your word is", string2)