# a python implementation of updatable heap

# Example

    In [1]: from updatable_heap import UpdatableHeap

    In [2]: testcase = {'a': 4, 'b': 3, 'c': 6, 'd': 2, 'e': 9}
       ...: heap = UpdatableHeap(testcase)
       ...: print(heap.top())
       ...: heap['b'] = 1
       ...: print(heap.top())
       ...: while not heap.empty():
       ...:     print(heap.pop())
       ...:
       ...: print('*' * 30)
       ...:
       ...: testcase = {'a': 4, 'b': 3, 'c': 6, 'd': 2, 'e': 9}
       ...: heap = UpdatableHeap(testcase, minheap=False)
       ...: print(heap.top())
       ...: heap['b'] = 13
       ...: print(heap.top())
       ...: while not heap.empty():
       ...:     print(heap.pop())
       ...:
    ('d', 2)
    ('b', 1)
    ('b', 1)
    ('d', 2)
    ('a', 4)
    ('c', 6)
    ('e', 9)
    ******************************
    ('e', 9)
    ('b', 13)
    ('b', 13)
    ('e', 9)
    ('c', 6)
    ('a', 4)
    ('d', 2)