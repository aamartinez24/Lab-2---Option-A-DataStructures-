class Node(object):
   item = -1
   next = None

   def __init__(self, item, next):
       self.item = item
       self.next = next

def read_file(file, file_list):
    for x in file:
        # If linked list is empty, ceate list with first node of text file.
        if file_list == None:
            file_list = Node(int(x), next)
            file_tmp = file_list
        else:
            # Fills the rest of the list with the content of the file.
            file_tmp.next = Node(int(x), next)
            file_tmp = file_tmp.next
    return file_list

# Compares the content of the list one by one and tells which ID is a duplicate.
def simple_comp(file_list):
    curr_node = file_list
    while curr_node:
        if curr_node is next:
            break
        else:
            # Compares a node with the rest of the nodes after it.
            rest_node = curr_node.next
            while rest_node:
                if rest_node is next:
                    break
                else:
                    if curr_node.item == rest_node.item:
                        print("Duplicate ID: ", curr_node.item)
                    rest_node = rest_node.next
            curr_node = curr_node.next

# Checks if theres a duplicate in a sorted list by comparing a node with the node after it.
def check_dub(file_list):
    curr_node = file_list
    while curr_node:
        if curr_node.next is next:
            break
        else:
            if curr_node.item == curr_node.next.item:
                print("Duplicate ID: ", curr_node.item)
                curr_node = curr_node.next.next
            else:
                curr_node = curr_node.next
   
# Sorts the list with the bubble sort algorithm.
def bubble_sort(file_list):
    n = 6000
    tmp_list = file_list
    for i in range(n):
        # loop  will always start on the first node of the list.
        curr_node = tmp_list
        for j in range(n-1):
            next_node = curr_node.next
            # Compares the current node with the next node.
            if curr_node.item > next_node.item:
                curr_node.item, next_node.item = next_node.item, curr_node.item
            # Start iterating thru the list
            curr_node = next_node
    return file_list                        

# Divides the list into two until all lists contain one node and calls merge_sort where 
# the lists will be sorted such as in the merge sort algorithm.
def div_list(file_list, n):
    head1 = file_list
    # if theres only one node, stop.
    if n == 1:
        return head1
    else:
        # Iterate thru the list half ways.
        for i in range(n//2 - 1):
            file_list = file_list.next
        head2 = file_list.next
        # Make first half of list point to None at the end.
        file_list.next = next
        # Recursive call to keep dividng the lists into two.
        head1 = div_list(head1, n//2)
        head2 = div_list(head2, n//2)
        # Call to sort each list.
        return merge_sort(head1, head2)

def merge_sort(head1, head2):
    # If either lists are None return the other lsit.
    if head1 is next:
        return head2
    if head2 is next:
        return head1
    # Create a new lists that will contain the contents of the two lists but sorted.
    if head1.item <= head2.item:
        sorted_list = Node(head1.item, next)
        head1 = head1.next
    else:
        sorted_list = Node(head2.item, next)
        head2 = head2.next
    end = sorted_list
    # Compares each node of the two lists to determine which node to add in the sorted list.
    while head1 is not next and head2 is not next:
        if head1.item <= head2.item:
            end.next = Node(head1.item, next)
            head1 = head1.next
        else:
            end.next = Node(head2.item, next)
            head2 = head2.next
        end = end.next
    # If a list is already been iterate thru and point to None the add the other list.
    while head1 is not next:
        end.next = Node(head1.item, next)
        head1 = head1.next
        end = end.next
    while head2 is not next:
        end.next = Node(head2.item, next)
        head2 = head2.next
        end = end.next
    return sorted_list

# Creates an boolean list where if theres a duplicate ID it is true.     
def bool_array(file_list):
    bool_list = [None] * 6001
    curr_node = file_list
    for i in range(6000):
        # If it is the second time we see the ID then change to True.
        if bool_list[curr_node.item] == False:
            bool_list[curr_node.item] = True
            curr_node = curr_node.next
        else:
            # If it is the first time seeing the ID then make boolean to False.
            bool_list[curr_node.item] = False
            curr_node = curr_node.next
    # If True in index of ID then the ID is duplicate.
    for i in range(len(bool_list)):
        if bool_list[i] is True:
            print("Duplicate ID: ", i)
    

def main():
    file1 = open("activision.txt", "r")
    file2 = open("vivendi.txt", "r")
    file1_list = None
    file2_list = None
    file1_list = read_file(file1, file1_list)
    file2_list = read_file(file2, file2_list)
    
    # Merge the two lists into one.
    file_tmp = file1_list
    while file_tmp:
        # Iterate thru one linked list until we reach the end.
        if file_tmp.next is next:
            break
        else:
            file_tmp = file_tmp.next
    # Add the second list by setting it as next nodes.
    file_tmp.next = file2_list
    
    # Solution1:
    simple_comp(file1_list)
    # Solution2:
    bubble_list = bubble_sort(file1_list)
    check_dub(bubble_list)
    # Solution3:
    merge_list = div_list(file1_list, 6000)
    check_dub(merge_list)
    # Solution4:
    bool_array(file1_list)
    

    
   
main()