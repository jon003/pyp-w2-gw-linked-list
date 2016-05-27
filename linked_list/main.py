class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None): # jon:DONE
        self.elem = elem
        self.next = None

    def __str__(self): # jon:DONE
        return str(self.elem)

    def __eq__(self, other): # akshith: Done
        if type(self) == type(other):
            return self.elem == other.elem
        else:
            return False

    def __repr__(self): # jon:DONE
        return "Node({}, {})".format(self.elem, self.next)

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None): # jon:DONE
        #This should initialize a node for each item in the list.
        # then populate 'elem' with the element, and link up the next node.

        self.elements = elements
        self.start = None
        self.end = None

        if self.elements:
            # set up a new list of 1 item using first passed element.
            self.start = Node(self.elements[0])
            self.end = self.start
            # trim off the first item, so we don't repeat it.
            self.elements = self.elements[1:]
            # now iterate and populat ethe rest of the list.
            for item in self.elements:
                self.append(item)

    def __str__(self): # corey:DONE
        # per Line 158 of test_main, a list of items with 3 nodes 1, 2, 3
        #  should return a string representation "[1, 2, 3]"
        # This should also allow test_main lines 168+ to work.
        # However, if not, we may need to implement magic function __repr__
        string_list = []
        if self.start != None or []:
            string_list.append(self.start.elem)
            curr_node = self.start.next
            while curr_node != self.end:
                string_list.append(curr_node.elem)
                curr_node = curr_node.next
            string_list.append(self.end.elem)
        return str(string_list)
            
    def __len__(self): # jon:DONE
        # should simply return the number of nodes.
        # iterate over list, and return the number of nodes.
        # we can call count() to count up the nodes.
        return self.count()

    def __iter__(self): # jon:DONE
        # start at head.  yield item, increment to next node in list.
        current = self.start
        while current:
            yield current
            current = current.next

    def __getitem__(self, index): # jon:DONE
        # fetch item at position index
        # this is what returns self[key]
        # TODO: BOUNDS CHECKING!  RAISE OUT OF INDEX ERRORS!
        current = self.start
        count = 0
        for count in range(index):
            current = current.next

        return current

    def __add__(self, other): # akshith: Done
        res = []
        for item in self:
            res.append(item.elem)
        for item in other:
            res.append(item.elem)
        return LinkedList(res)

    def __iadd__(self, other): # akshith: Done
        return self.__add__(other)

    def __eq__(self, other): # akshith: IN PROGRESS
        if len(self) != len(other):
            return False
        else:
            return all( self[i] == other[i] for i in range(len(self)) )
 
            

    def append(self, elem): # jon:DONE
        # Append a new node to the end of the list
        newnode = Node(elem)
        if self.end:
            self.end.next = newnode
        else:
            self.start = newnode
        # remember to update the 'end' pointer to the new last item.
        self.end = newnode

    def count(self): # jon:DONE
        current = self.start
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def pop(self, index=None): # corey:IN PROGRESS
        curr_node = self.start
        if len(self) in (0, None) or index >= len(self):
            raise IndexError
        elif index==None or index==len(self):
            orig_end = self.end.elem
            new_end = curr_node
            while curr_node != self.end:
                new_end = curr_node
                curr_node = curr_node.next
            if self.start == self.end:
                self.start = None
            new_end.next = None
            self.end = new_end
            return orig_end
        elif index==0:
            orig_start = self.start
            self.start = self.start.next
            orig_start.next = None
            return orig_start.elem
        else:
            next_node = self.start.next
            prev_node = self.start
            for i in range(index):
                prev_node = curr_node
                curr_node = prev_node.next
                next_node = curr_node.next
            curr_node.next = None
            our_node = curr_node.elem
            curr_node = ''
            prev_node.next = next_node
            return our_node
        

# MISC Test Sequences below, ignore.

#ll = LinkedList([1, 2, 3, 4]) # __init__() TEST PASSED
#jj = LinkedList([5, 6, 7, "list"])
#ii = LinkedList([9])
# kk = ll + jj # Test passed
# ll += jj     # Test passed
# print(ll)
# print(jj)
# print ll.count() # count() TEST PASSED
# print len(ll) # len() TEST PASSED
#for item in ll: # __iter__() TEST PASSED
#     print item
#print ll[0]
#print str(ll)
# print ii.pop(0) 
# print len(ii)
