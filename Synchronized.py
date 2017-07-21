#!/usr/bin/python
#coding:utf-8


from threading import Lock

lock = Lock()
def Synchronized():
    def decorator(srcfunc):
        def dstfunc(*args, **kwargs):
            lock.acquire()
            try:
                return srcfunc(*args, **kwargs)
            finally:
                lock.release()
        return dstfunc
    return decorator
