# Python function to remove a given word from a my_list as strip at the same time 

my_list = ["Ramesh", "Mahesh", "Fourty"]

def remove_item(item):
    if item in my_list:
        my_list.remove(item)
        print(item.strip())
    else:
        return "Item not found in list!"
    return my_list


print(remove_item("Mayuresh"))