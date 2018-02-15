# encoding: utf-8

'''

@author: ZiqiLiu


@file: test.py

@time: 2018/2/15 下午5:24

@desc:
'''

from updatable_heap import UpdatableHeap

if __name__ == '__main__':
    testcase = {'a': 4, 'b': 3, 'c': 6, 'd': 2, 'e': 9}
    heap = UpdatableHeap(testcase)
    print(heap.top())
    heap['b'] = 1
    print(heap.top())
    while not heap.empty():
        print(heap.pop())

    print('*' * 30)

    testcase = {'a': 4, 'b': 3, 'c': 6, 'd': 2, 'e': 9}
    heap = UpdatableHeap(testcase, minheap=False)
    print(heap.top())
    heap['b'] = 13
    print(heap.top())
    while not heap.empty():
        print(heap.pop())
