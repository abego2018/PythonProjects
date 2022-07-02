#greeting function
def hello ():
    print("Hello user")

def pack(item1, item2, item3):
    packList = []
    packList.append(item1)
    packList.append(item2)
    packList.append(item3)

    return packList

print(pack("tent", "cooler", "propane"))

def eat_lunch(*lunch_lst):
    if len(lunch_lst) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(lunch_lst)):
            if i == 0:
                print(f"First I eat {lunch_lst[0]}")
            else:
                print(f"Next I eat {lunch_lst[i]}")         

eat_lunch([])
eat_lunch("Pizza")
eat_lunch("rice","meat", "veggies", "dessert")