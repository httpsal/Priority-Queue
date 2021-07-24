import math
from math import log2


class Node:
    """A single node containing the priority and the actual data"""

    def __init__(self, priority: float, data=None):
        self.priority = priority
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.priority == other.priority and self.data == other.data

    def __hash__(self):
        return hash((self.priority, self.data))

    def __str__(self):
        """Return the representation of the object"""
        if self.data:
            return f"[{self.priority} {self.data}]"
        else:
            return f"{self.priority}"


class PriorityQueue:
    """Priority queue where the min value is at the top"""

    def __init__(self) -> None:
        self.__heap = []

    @staticmethod
    def get_children(x: int):
        """Return the left and right child's index"""
        return (2 * x) + 1, (2 * x) + 2

    @staticmethod
    def get_parent(x: int) -> int:
        """Return the index of the parent of a node"""
        return (x - 1) // 2

    def copy_list(self):
        """Return a copy of the heap"""
        return self.__heap[:]

    def is_empty(self) -> bool:
        """Return True if the list is empty"""
        return len(self.__heap) == 0

    def len(self) -> int:
        """Return the length of the heap"""
        return len(self.__heap)

    def heapify(self, index: int) -> None:
        """Transform the list into a heap"""
        heap = self.__heap
        left, right = self.get_children(index)

        if left < len(heap) and (heap[left].priority < heap[index].priority):
            minimum = left
        else:
            minimum = index

        if right < len(heap) and (heap[right].priority < heap[minimum].priority):
            minimum = right

        if minimum != index:
            # Swap the nodes
            heap[index], heap[minimum] = heap[minimum], heap[index]
            self.heapify(minimum)

    def print(self) -> None:
        """Print the list"""
        for node in self.__heap:
            print(f"{node}", end="\t")

    def print_as_tree(self, index=0, depth=0) -> None:
        """Print the heap in a 'binary tree' style"""
        if index >= len(self.__heap):
            return

        left, right = self.get_children(index)

        self.print_as_tree(right, depth + 1)
        print("\t" * depth + str(self.__heap[index]))
        self.print_as_tree(left, depth + 1)

    def min(self):
        """Return the head of the heap (the node with the minimum priority) without removing it from the list"""
        if self.is_empty():
            return None
        else:
            return self.__heap[0]

    def max(self):
        """Return the Node with the max priority without removing it from the list"""
        if self.is_empty():
            return None

        height = int(log2(len(self.__heap)))
        start_index = (2 ** height) - 1  # 2^height - 1

        max_priority = -math.inf
        node = None

        for i in range(start_index, len(self.__heap)):
            if max_priority < self.__heap[i].priority:
                max_priority = self.__heap[i].priority
                node = self.__heap[i]

        return node

    def append(self, elem: Node):
        """Add a new node at the end of the heap"""
        self.__heap.append(elem)

        index = len(self.__heap) - 1
        # If necessary, push the new value to the top
        self.__restore_heap(index)

    def clear(self):
        """Remove all elements from the list"""
        self.__heap.clear()

    def __restore_heap(self, index: int):
        """Restore the heap property"""
        h = self.__heap  # Just to write less things

        while index > 0 and h[self.get_parent(index)].priority > h[index].priority:
            # Swap parent with its child
            h[self.get_parent(index)], h[index] = h[index], h[self.get_parent(index)]

            index = self.get_parent(index)

    def search(self, node: Node):
        """Return the index of the searched node or None if i doesn't exists"""
        for i in range(0, len(self.__heap)):
            if self.__heap[i] == node:
                return i
        return None

    def pop(self):
        """Pop the first element of the heap"""
        if self.is_empty():
            # Empty heap
            return None

        head = self.__heap.pop(0)
        self.heapify(0)

        return head

    def increase_priority(self, index: int, new_value: float):
        """Increase the value of the priority for a given Node"""
        if index >= self.len() or index < 0:
            return False

        if new_value <= self.__heap[index].priority:
            return False

        self.__heap[index].priority = new_value
        self.heapify(index)
        return True

    def decrease_priority(self, index: int, new_value: float):
        """Decrease the value of the priority for a given Node"""
        if index >= self.len() or index < 0:
            return False

        if new_value >= self.__heap[index].priority:
            return False

        self.__heap[index].priority = new_value
        self.__restore_heap(index)

        return True
