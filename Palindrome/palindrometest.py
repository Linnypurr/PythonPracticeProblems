import unittest

import palindrome

class PalindromeTest(unittest.TestCase):

    def setUp(self):
        self.palindrome_linked_list = palindrome.LinkedList()
        self.non_palindrome_linked_list = palindrome.LinkedList()
        first_node = palindrome.Node(1)
        non_first_node = palindrome.Node(1)
        second_node = palindrome.Node(2)
        non_second_node = palindrome.Node(2)
        third_node = palindrome.Node(3)
        non_third_node = palindrome.Node(3)
        fourth_node = palindrome.Node(4)
        second_to_last_node = palindrome.Node(2)
        last_node = palindrome.Node(1)
        self.palindrome_linked_list.head = first_node
        self.non_palindrome_linked_list.head = non_first_node
        first_node.next_node = second_node
        non_first_node.next_node = non_second_node
        second_node.next_node = third_node
        non_second_node.next_node = non_third_node
        third_node.next_node = second_to_last_node
        non_third_node.next_node = fourth_node
        second_to_last_node.next_node = last_node

    #
    # def test_print_list_palindrome(self):
    #     self.palindrome_linked_list.print_list()
    #
    # def test_print_list_non_palindrome(self):
    #     self.non_palindrome_linked_list.print_list()

    def test_list_length_palindrome(self):
        length = self.palindrome_linked_list.list_length()
        self.assertEqual(length, 5)

    def test_list_length_non_palindrome(self):
        length = self.non_palindrome_linked_list.list_length()
        self.assertEqual(length, 4)

    def test_return_last_node_palindrome(self):
        last_node = self.palindrome_linked_list.return_last_node()
        self.assertEqual(last_node.data, 1)

    def test_return_last_node_non_palindrome(self):
        last_node = self.non_palindrome_linked_list.return_last_node()
        self.assertEqual(last_node.data, 4)

    def test_return_kth_to_last_palindrome(self):
        second_to_last_node = self.palindrome_linked_list.return_kth_to_last_node(2)
        self.assertEqual(second_to_last_node.data, 3)

    def test_return_kth_to_last_non_palindrome(self):
        second_to_last_node = self.non_palindrome_linked_list.return_kth_to_last_node(2)
        self.assertEqual(second_to_last_node.data, 2)

    def test_return_kth_node_palindrome(self):
        second_to_last_node = self.palindrome_linked_list.return_kth_node(2)
        self.assertEqual(second_to_last_node.data, 3)

    def test_return_kth_node_non_palindrome(self):
        second_to_last_node = self.non_palindrome_linked_list.return_kth_node(2)
        self.assertEqual(second_to_last_node.data, 3)

    def test_is_palindrome_palindrome(self):
        self.assertTrue(self.palindrome_linked_list.identify_palindrome())

    def test_is_palindrome_non_palindrome(self):
        self.assertFalse(self.non_palindrome_linked_list.identify_palindrome())


if __name__ == '__main__':
    unittest.main()
