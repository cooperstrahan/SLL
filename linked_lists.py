class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class SLList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.val)
            runner = runner.next
        return self
    
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = Node(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self
    
    def remove_from_front(self):
        if self.head == None:
            print("There is no linked list yet!")
            return None
        runner = self.head
        self.head = runner.next
        print(f"deleted: {runner.val}")
        return self

    def remove_from_back(self):
        if self.head == None:
            print("There is no linked list yet!")
            return None
        runner = self.head
        second_to_last = None
        while runner.next != None:
            second_to_last = runner
            runner = runner.next  
        print(f"deleted: {runner.val}")
        second_to_last.next = None
        return self
    
    def remove_val(self, val):
        if self.head == None:
            print("There is no linked list yet!")
            return None

        if val == self.head.val:
            self.remove_from_front()
            return self
        
        runner = self.head
        prevRun = None
        while runner.next != None:
            if runner.val == val:
                prevRun.next = runner.next
                print(f"deleted: {runner.val}")
                return self
            prevRun = runner
            runner = runner.next

        if runner.next == None:
            self.remove_from_back()
        return self        
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self

        runner = self.head.next
        count = 1
        prev_run = self.head
        insert = Node(val)

        while runner != None:
            if count == n:
                prev_run.next = insert
                insert.next = runner
                return self
            count += 1
            prev_run = runner
            runner = runner.next
        
        if runner == None:
            self.add_to_back(val)
            return self
my_list = SLList()
my_list.add_to_front("are").add_to_back("fun!").add_to_front("lists").add_to_front("Linked").add_to_front("facebook").add_to_back("twitter")
my_list.remove_val("facebook").print_values()

# my_list.print_values()