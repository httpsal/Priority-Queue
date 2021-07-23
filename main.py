from pq_module.priority_queue import *

if __name__ == '__main__':
    # Example
    priority_queue = PriorityQueue()
    priority_queue.append(Node(5))
    priority_queue.append(Node(2))
    priority_queue.append(Node(3))
    priority_queue.append(Node(10))
    priority_queue.append(Node(10))
    priority_queue.append(Node(9))
    priority_queue.append(Node(8))

    priority_queue.print_as_tree()
    print()

    print(priority_queue.min())

    print()
