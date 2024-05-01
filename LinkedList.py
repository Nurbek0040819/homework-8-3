class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise ValueError("Invalid position")

        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Position out of bounds")

        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return
        deleted_node = self.head
        self.head = self.head.next
        deleted_node.next = None  

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        deleted_node.next = None  

    def delete_at_position(self, position):
        if position < 0:
            raise ValueError("Invalid position")

        if self.head is None:
            return

        if position == 0:
            self.delete_at_beginning()
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            raise IndexError("Position out of bounds")

        deleted_node = current.next
        current.next = deleted_node.next
        deleted_node.next = None  

    def get_sum(self):
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total

    def get_mean(self):
        total_sum = self.get_sum()
        if total_sum == 0:
            raise ZeroDivisionError("List is empty")
        return total_sum / self.get_length()

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def remove_duplicates(self):
        current = self.head
        while current:
            next_node = current.next
            while next_node and next_node.data == current.data:
                next_node = next_node.next
            current.next = next_node
            current = current.next

    def create_from_list(self, data_list):
        for data in data_list[::-1]:  
            self.insert_at_beginning(data)

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "None"
        return result

    # 8-3 uyga vazifa methodlari
    def count_type(self, type_name):
        count = 0
        current = self.head
        while current:
            if isinstance(current.data, type_name):
                count += 1
            current = current.next
        return count

    def find_string_occurrences(self, target):
        occurrences = []
        index = 0
        current = self.head
        while current:
            if isinstance(current.data, str):
                if target in current.data:
                    index = current.data.index(target)
                    occurrences.append((current.data, index))
            current = current.next
        return occurrences
    
    def remove_zero_nodes(self):
        current = self.head
        prev = None

        while current:
            if current.data == 0:
                if current == self.head:
                    self.head = current.next
                    current = self.head
                else:
                    prev.next = current.next
                    current = current.next
            else:
                prev = current
                current = current.next

    def to_list(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.data)
            current = current.next
        return lst

    def to_tuple(self):
        tpl = ()
        current = self.head
        while current:
            tpl += (current.data,)
            current = current.next
        return tpl
    

    def reverse_alternate(self):
        current = self.head
        prev = None

        while current and current.next:
            next_node = current.next
            current.next = next_node.next
            next_node.next = current
            if prev:
                prev.next = next_node
            else:
                self.head = next_node
            prev = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

linkedlist = LinkedList()
linkedlist.append(1)
linkedlist.append("hello")
linkedlist.append(True)
linkedlist.append(3.14)
linkedlist.append(["a", "b", "c"])

linkedlist.append("apple")
linkedlist.append("banana")
linkedlist.append("orange")
linkedlist.append("grape")

linkedlist.append(1)
linkedlist.append(0)
linkedlist.append(2)
linkedlist.append(0)
linkedlist.append(3)
linkedlist.append(0)

linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(6)
linkedlist.append(7)
linkedlist.append(8)

target = "ra"
occurrences = linkedlist.find_string_occurrences(target)

if occurrences:
    print(f"'{target}' stringi mavjud.")
    print(f"'{target}' stringi {len(occurrences)} marta quyidagi indekslarda uchraydi:")
    for item in occurrences:
        print(f"    - LinkedListdagi element: '{item[0]}', Indeks: {item[1]}")
else:
    print(f"'{target}' stringi mavjud emas.")

print(linkedlist.count_type(int))
print(linkedlist.count_type(str))
print(linkedlist.count_type(bool))
print(linkedlist.count_type(list))

print("Boshlang'ich LinkedList:")
linkedlist.display()

# Qiymati nolga teng tugunlarni o'chirish
linkedlist.remove_zero_nodes()

print("Tugunlardagi qiymati nolga teng bo'lgan elementlar o'chirilgan LinkedList:")
linkedlist.display()

linked_list_as_list = linkedlist.to_list()
print("LinkedListdan listga aylantirilgan ro'yxat:", linked_list_as_list)

# LinkedListdan tuplega aylantirish
linked_list_as_tuple = linkedlist.to_tuple()
print("LinkedListdan tuplega aylantirilgan tuple:", linked_list_as_tuple)


linkedlist.display()

# Yonma yon almashtirish
linkedlist.reverse_alternate()

print("Yonma yon almashtirilgan LinkedList:")
linkedlist.display()