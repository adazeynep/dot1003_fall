##task80
import random
size = int(input("List Size: "))
elem_type = input("Element Type (integer/float): ")
my_list = []
if elem_type == "integer":
    for i in range(size):
        num = random.randint(0, 999999)
        my_list.append(num)
elif elem_type == "float":
    for i in range(size):
        num = random.uniform(0, 999999)
        my_list.append(num)
    else:
        print("Only integer or float.")
    if len(my_list) > 0:
       print("Here is your random list you asked for:")
    print(my_list)

##task81
def biggest_in_list(new_list,list):
    ans=max(new_list)
    return ans

def sorted_list(unsorted_list):
    ans=sorted(unsorted_list)
    return ans

my_list=[695735, 169439, 41406, 112517, 457053]
print(my_list)
print(biggest_in_list(my_list,list))
print(sorted_list(my_list))

##task82
import random

def dice_rolller(dice_type):
    ans=random.randint(1, dice_type)
    return ans
my_dice=int(input("Select dice: "))

print(f"{dice_rolller(my_dice)}")

##task83
with open ("quotes_from_bane.txt","r") as my_file:
    content=my_file.read()
    my_file(0)
print(content)

##task84


