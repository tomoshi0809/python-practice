#!/usr/bin/python
#coding:utf-8

from threading import Thread
from Synchronized import Synchronized

class Counter(object):
    def __init__(self):
        self._counter = 0

    @Synchronized()
    def countup(self):
        print ":" + str(self._counter)
        self._counter += 1


class Test(Thread):
    def __init__(self, n, cntr):
        super(Test, self).__init__()
        self._n = n
        self.cntr = cntr

    def run(self):
        for i in range(self._n):
            self.cntr.countup()

def main():
    cntr = Counter()
    th1 = Test(100, cntr)
    th1.start()
    th2 = Test(100, cntr)
    th2.start()
    th1.join()
    th2.join()

if __name__ == "__main__":
    main()