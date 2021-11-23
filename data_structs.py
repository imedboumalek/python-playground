from typing import List


_list = [17, 28, 30, 40, 50, 60, 70, 80, 90, 100]

# add a new element to the end of the list


def add_element(list: List, element):
    list.append(element)

# sort the list


def sort_list(list):
    list.sort()

# remove an element from the list


def remove_element(list: List, element):
    list.remove(element)
    print(list)


# add and print the list
# to the start of the list

def add_and_print(list: List, element):
    list.insert(0, element)
    print(list)


# find index of an element in the list
def find_index(list: List, element):
    return list.index(element)


# print sublist from index to index
def print_sublist(list: List, start_index: int, end_index: int):
    print(list[start_index:end_index])


# print last element using negative index
def print_last_element(list: List):
    print(list[-1])


# float list with random ints
_machine = [17.2, 28.3, 30.4, 40.5, 50.6, 60.7, 70.8, 80.9, 90.1, 100.2]


# prints ints from index to index
def print_int_sublist(list: List, start_index: int, end_index: int, step: int):
    for i in list[start_index:end_index:step]:
        if type(i) == int:
            print(i)


def add_int_to_sublist_members(list: List, start_index: int, end_index: int, step: int, int_to_add: int):
    print(list)
    for i in list[start_index:end_index:step]:
        if type(i) == int:
            i += int_to_add
    print(list)
