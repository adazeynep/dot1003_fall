##task40
city=input("City name: ")
rep=int(input("How many repetition for li : "))
word= city+rep*"li"+"lerle"
print(word)
##task41
arguman1= input("First word: ")
arguman2=input("second word: ")
len1=len(arguman1)
len2=len(arguman2)
if len1 > len2:
    print(arguman1)
elif len2 > len1:
    print(arguman2)
else:
    print("their lenght are same")
##task42
name=input("Your input: ")
result="*"+name+"*"
print(result)
##task43
name=input("Your input: ")
result=len(name)
print(name)
print(result*"_")
##task44
name=input("Your input: ")
if len(name) <18:
    print(18*"_")
##task45
name=input("Please enter string: ")
num1=int(input("Please enter first integer. "))
num2=int(input("Please enter last integer: "))
result=(name[num1:num2])
print(result)
##task46
name=input("Please enter string: ")
number=int(input("Please enter integer: "))
result=(name[:number])
print(result)
##task47
userinput=input("Please enter string: ")
number=int(input("Please enter integer: "))
result=(userinput[number: ])
print(result)
##task48
user_input=input("Please enter string: ")
if "a" in user_input:
    print("found")
else: 
    print("not found")
##task49
main_input=input("Please enter string: ")
main_item=input("Please enter search item: ")
if main_item in main_input :
    print("found")
else:
    print("not found")
##task50
userinput=input("Please enter string: ")
search_item=input("Please enter search item: ")
indeks=userinput.find(search_item)
if indeks==-1 :
    print("not found")
else:
    print("found it at {indeks}")
##task51





