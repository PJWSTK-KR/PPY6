from Element import Element


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        all_elements = ""
        current_element = self.head
        while current_element is not None:
            all_elements += str(current_element) + " "
            current_element = current_element.nextE
        return all_elements

    def get(self, e: Element):
        current_element = self.head
        while current_element is not None:
            if current_element == e:
                return current_element
            current_element = current_element.nextE
        return None

    def delete(self, e: Element):  # [1, 2, 3, 4], [1, 2, 3], [1, 2], [1], []
        if self.head is None:
            return
        former_element = None
        current_element = self.head
        while current_element is not None:
            if current_element == e:
                if former_element is not None:
                    former_element.nextE = current_element.nextE
                else:
                    current_element = current_element.nextE
                return
            former_element = current_element
            current_element = current_element.nextE

    # def append(self, e, func=None):
    def add(self, e):
        if self.tail is None:
            self.head = self.tail = e
            return
        self.tail.nextE = e
        self.tail = self.tail.nextE


