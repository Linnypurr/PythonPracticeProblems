#0 -> 2 -> 3 -> 5 -> 10 -|
#              ^---------

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    # def get_data(self):
    #     return self.get_data
    #
    # def get_next(self):
    #     return self.next_node
    #
    # def set_next(self, new_next):
    #     self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    # def insert(self, data):
    #     new_node = Node(data)
    #     new_node.set_next(self.head)
    #     self.head = new_node
    #
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def list_length(self):
        current_node = self.head
        current_number = current_node.data
        list_set = set()
        while current_number not in list_set:
            list_set.add(current_number)
            current_node = current_node.next_node
            current_number = current_node.data

        return len(list_set)



def set_up():
    head_node = Node(1)
    linked_list = LinkedList()
    linked_list.head = head_node
    second_node = Node(2)
    third_node = Node(3)
    fifth_node = Node(5)
    tenth_node = Node(10)

    linked_list.head.next_node = second_node
    second_node.next_node = third_node
    third_node.next_node = fifth_node
    fifth_node.next_node = tenth_node
    tenth_node.next_node = fifth_node
    find_links_in_list(linked_list)

def find_links_in_list(linked_list):
    linked_dictionary = {}
    current_node = linked_list.head
    next_node = current_node.next_node
    length = linked_list.list_length()
    for index in range(length):
        linked_dictionary[current_node.data] = next_node.data
        current_node = current_node.next_node
        next_node = current_node.next_node

    detect_loop(linked_dictionary)

def detect_loop(linked_dictionary):
    for current_key in linked_dictionary.keys():
        current_value = linked_dictionary.get(current_key)
        if linked_dictionary.get(current_value) == current_key:
            print('Loop between {} and {}'.format(current_key, current_value))



if __name__== '__main__':
    set_up()
