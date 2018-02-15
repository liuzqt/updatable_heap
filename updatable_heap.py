# encoding: utf-8

'''

@author: ZiqiLiu


@file: updatable_heap.py

@time: 2018/2/15 下午1:51

@desc:
'''


class UpdatableHeap:
    def __init__(self, dic=None, minheap=True):

        self.arr = [None]
        self.pos_dict = {}
        self.dic = {}
        self.minheap = minheap
        if dic is not None:
            if not isinstance(dic, dict):
                raise Exception('dic argument must be a ' + str(dict))
            self.dic = dic
            for i, k in zip(range(1, len(dic) + 1), dic):
                self.arr.append(k)
                self.pos_dict[k] = i
            self._initializeHeap()

    def __len__(self):
        return len(self.arr) - 1

    def _initializeHeap(self):
        for i in range((len(self.arr) - 1) // 2, 0, -1):
            self._heapDown(i)

    def top(self):
        if len(self.arr) < 1:
            raise Exception('heap is empty!')
        return self.arr[1], self.dic[self.arr[1]]

    def pop(self):
        if len(self.arr) < 1:
            raise Exception('heap is empty!')
        self._switch(1, len(self.arr) - 1)
        key = self.arr.pop()
        val = self._remove_key(key)
        self._heapDown(1)
        return key, val

    def remove(self, key):
        if not key in self.dic:
            raise Exception('key %s non exist!' % str(key))
        pos = self.pos_dict[key]
        self._switch(pos, len(self.arr) - 1)
        self.arr.pop()
        val = self._remove_key(key)
        self._heapDown(pos)
        return val

    def _remove_key(self, key):
        self.pos_dict.pop(key)
        return self.dic.pop(key)

    def _switch(self, i, j):
        self.pos_dict[self.arr[i]], self.pos_dict[self.arr[j]] = j, i
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def __getitem__(self, item):
        if item not in self.dic:
            raise Exception('key %s non exist' % item)
        return self.dic[item]

    def _comp(self, i, j):

        return self.minheap and self.dic[self.arr[i]] > self.dic[
            self.arr[j]] or not self.minheap and self.dic[self.arr[i]] < \
                                                 self.dic[self.arr[j]]

    def _heapUp(self, i):
        while i > 1:
            if self._comp(i >> 1, i):
                self._switch(i >> 1, i)
                i >>= 1
            else:
                break

    def _heapDown(self, i):
        while 2 * i < len(self.arr):
            temp = i
            if self._comp(temp, 2 * i):
                temp = i << 1
            if (i << 1) + 1 < len(self.arr):
                if self._comp(temp, (i << 1) + 1):
                    temp = (i << 1) + 1
            if temp != i:
                self._switch(temp, i)
                i = temp
            else:
                break

    def __setitem__(self, key, value):
        if key not in self.dic:
            self.dic[key] = value
            self.pos_dict[key] = len(self.arr)
            self.arr.append(key)
            self._heapUp(len(self.arr) - 1)
        elif self.dic[key] == value:
            return
        else:
            origin_val = self.dic[key]
            self.dic[key] = value
            if self.minheap and value < origin_val \
                    or not self.minheap and value > origin_val:
                self._heapUp(self.pos_dict[key])
            else:
                self._heapDown(self.pos_dict[key])

    def empty(self):
        return len(self.arr) == 1

    def __iter__(self):
        return iter(self.dic)

    def __delitem__(self, key):
        self.remove(key)

    def keys(self):
        return self.dic.keys()

    def values(self):
        return self.dic.values()

    def items(self):
        return self.dic.items()


__all__ = ['UpdatableHeap']
