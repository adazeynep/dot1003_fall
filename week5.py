##task54
yazi = "The quick brown fox jumps over the lazy dog "
user_input=input("Which item do you want to search? ")
print(f"item {user_input} appeared {yazi.count(user_input)} times.")

##task55
def aranacak_öge():
    aranacak=input("Enter input to search: ")
    item=input("Which item do you want to searvh? ")

    count=aranacak.count(item)
    print(f"Item {item} appeared {count} times. ")
aranacak_öge()

##task56
def unluleri_sil(text):
    vowels="aeiouAEIOU"
    yeni_text= ""
     
    for char in text:
        if char not in vowels:
            yeni_text +=char

    return yeni_text
user_text=input("Enter your sentence: ")
result= unluleri_sil(user_text)
print("Without vowels:" ,result)

##task57
def anarya(input_list):
    input_list.reverse()
    return input_list
game_list=["Doom", "Max Payne", "FTL"]
print(game_list)
reversed_list= anarya(game_list)
print(reversed_list)
print(game_list)

##task59
def longest_name(game_list):
    return max(game_list, key=len)
game_list=["Doom", "Max Payne", "FTL"]
print(game_list)
print(longest_name(game_list))

##task63
def tripler(input_list):
    new_list=[num*3 for num in input_list]
    return  new_list
my_lucky_numbers=[4,8,15,16,23,42]

tripled_numbers=tripler(my_lucky_numbers)
print(tripled_numbers)

##task64
inventory={"item1":3,"item2":1,"item3":5}
for k,v in inventory.items():
    print(k,v)

##task65
def add_item(item,quantity):
    if item in inventory:
        inventory[item] +=quantity
    else:
        inventory[item] = quantity
inventory={"item1":3,"item2":1,"item3":5}
add_item("item1",5)
add_item("item4",1)

for key,value in inventory.items():
    print(f"{key}:{value}")

##task66
inventory = {"item1": 3, "item2": 1, "item3": 5}

def remove_item(item, quantity):
    if quantity > 0:
        if item in inventory:
            if inventory[item] < quantity:
                inventory[item] = 0
            else:
                inventory[item] -= quantity

def add_item(item, quantity):
    if quantity > 0:
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

add_item("item1", 5)
add_item("item4", 1)

remove_item("item4", 6)
remove_item("item1", 2)

for key, value in inventory.items():
    print(f"{key}:{value}")
