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
def task_51(): 

 sentence="The quick brown fox jumps over the lazy dog"
 print("Please enter the phhrase you want to search ")
 print("If you want to exit enter -1 ")
 my_flag= True

 while my_flag: 
     searchitem=input("WWhat are you looking for? ")
     if searchitem=="-1":
        print("Bye!")
        my_flag=False

 found_input=sentence.find(searchitem)
 if found_input!=-1:
     print(f"found it at {found_input}")
 else:
     print("not found")

task_51()
##task52
def to_two_decimal(list_2):
    new_list=[f"{num.2f}" for num in list_2 ]
    
    return new_list 
my_list=[1.2345, 2.3456, 3.4567, 4.5678]
new_list= to_two_decimal(my_list)
print(new_list)