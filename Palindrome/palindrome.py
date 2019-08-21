import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

    def list_length(self):
        current_node = self.head
        list_length_couter = 1
        while current_node.next_node is not None:
            list_length_couter = list_length_couter + 1
            current_node = current_node.next_node
        return list_length_couter

    def return_last_node(self):
        return self.return_kth_to_last_node(0)

    def return_kth_to_last_node(self, kth):
        kth_to_last_node = self.head
        runner_node = self.return_kth_node(kth)
        while runner_node.next_node is not None:
            runner_node = runner_node.next_node
            kth_to_last_node = kth_to_last_node.next_node
        return kth_to_last_node

    def return_kth_node(self, kth):
        kth_node = self.head
        for index in range(kth):
            kth_node = kth_node.next_node
        return kth_node

    def identify_palindrome(self):
        is_palindrome = True
        list_length = self.list_length()
        half_of_list = math.floor(list_length / 2)
        current_from_beginning_node = self.head
        for index in range(half_of_list):
            current_from_end_node = self.return_kth_to_last_node(index)
            if current_from_beginning_node.data == current_from_end_node.data:
                current_from_beginning_node = current_from_beginning_node.next_node
            else:
                is_palindrome = False
        return is_palindrome

if __name__== '__main__':
    # head_node = Node(1)
    # linked_list = LinkedList()
    # linked_list.head = head_node
    # second_node = Node(2)
    # third_node = Node(3)
    # fourth_node = Node(4)
    # fourth_to_last_node = Node(4)
    # third_to_last_node = Node(3)
    # second_to_last_node = Node(2)
    # last_node = Node(1)
    #
    # linked_list.head.next_node = second_node
    # second_node.next_node = third_node
    # third_node.next_node = fourth_node
    # fourth_node.next_node = fourth_to_last_node
    # fourth_to_last_node.next_node = third_to_last_node
    # third_to_last_node.next_node = second_to_last_node
    # second_to_last_node.next_node = last_node
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
    #linked_list.print_list()
    print(linked_list.identify_palindrome())
