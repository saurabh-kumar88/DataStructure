from collections import deque


# url_stack = []
# url_stack.append('https://www.youtube.com/results?search_query=codebasics+data+structures')
# url_stack.append('https://github.com/codebasics/py/blob/master/DataStructures/4_HashTable_2_Collisions/4_hash_table_exercise.md')
# url_stack.append('https://www.guru99.com/python-interview-questions-answers.html')


orders = ['pizza','samosa','pasta','biryani','burger']

if __name__ == "__main__":
    # print(  url_stack.pop()  )
    # print(  url_stack.pop()  )
    # print(  url_stack.pop()  )
    stack = deque()
    for order in orders:
        stack.append(order)

    print(stack.popleft() )
    
    # stack.appendleft('https://www.guru99.com/python-interview-questions-answers.html')
    # stack.insert(0, "hello stack")
    # stack.remove('https://www.guru99.com/python-interview-questions-answers.html')
    # itr = stack.__iter__()
    # print(itr )
    # stack.clear()
    # print(stack.count('https://www.guru99.com/python-interview-questions-answers.html'))


"""
__add__
__bool__
__class__
__contains__
__copy__
__delattr__
__delitem__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__gt__
__hash__
__iadd__
__imul__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__reversed__
__rmul__
__setattr__
__setitem__
__sizeof__
__str__
__subclasshook__
append
appendleft
clear
copy
count
extend
extendleft
index
insert
maxlen
pop
popleft
remove
reverse
rotate
"""
    

