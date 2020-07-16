import re
from collections import deque


class Stack:
    """
    Simple container class for deque
    """
    def __init__(self):
        self.container = deque()
    
    def __str__(self):
        return "Simple container class for deque"
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


# Problem 1: Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
def __reverse_string(string):
    stack_obj = Stack()
    for elements in string:
        stack_obj.push(elements)

    new_string = ""
    for elements in range(len(string)):
        new_string += stack_obj.pop()
    return new_string

# Problem 2 : Write a function in python that checks if paranthesis in the string are balanced or not.
# Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# For example:

# is_balanced( "({a+b})" )          --> True
# is_balanced( "))((a+b}{" )        --> False
# is_balanced("((a+b))")            --> True
# is_balanced( "))" )               --> False
# is_balanced( "[a+b]*(x+2y)*{gg+kk}" ) --> True    


def _is_balanced(string):
    stack_obj = Stack()
    __paranthesis = ['[', ']', '{', '}', '(', ')']
    arr = []
    test_string = ""
    # filter out operands and operators from string 
    for element in string:
        for i in range(len(__paranthesis)):
            if element ==  __paranthesis[i]:
                arr.append(element)
                test_string += element
            else:
                pass
    #print(arr)
    print(test_string)
    for i in arr:
        stack_obj.push(i)
    
    balanced = 0
    for i in range(stack_obj.size()):
        x = stack_obj.pop()    
        print(arr[i] , " == ", x )
        if arr[i] != x:
            #print(arr[i] , " == ", x )
            balanced += 1 
    
    #print(balanced)
    if balanced == len(arr):
        print("balanced")
    else:
        print("not balanced")


def __is_balanced(string):
    # Using hash map
    __paranthesis = ['[', ']', '{', '}', '(', ')']
    match = {}
    match['right_square'] = 0
    match['left_square'] = 0
    match['right_curly'] = 0
    match['left_curly'] = 0
    match['right_bracks'] = 0
    match['left_bracks'] = 0

    test_string = ""
    # filter out operands and operators from string 
    for element in string:
        for i in range(len(__paranthesis)):
            if element == '[':
                match['right_square'] += 1
            elif element == ']':
                match['left_square'] += 1
            elif element == '{':
                match['right_curly'] += 1
            elif element == '}':
                match['left_curly'] += 1
            elif element == '(':
                match['right_bracks'] += 1
            elif element == ')':
                match['left_bracks'] += 1
        
    if match["right_bracks"] == match["left_bracks"] and match["left_curly"] == match["right_curly"] and match["right_square"] == match["left_square"]:
        print("balanced")
    else:
        print("Not balanced")



    
 # ( {  } )

 # [ ] ( ) {  }


js = """var whoIsHere;



if (whoIsHere == "user") {
    console.log('welcome user');
} else if(whoIsHere === 'notActive') {
    console.log('Welcome back');
} else if(whoIsHere === 'teacher'){
    console.log('Welcome teacher');

} else if(whoIsHere === 'admin') {
    console.log('welcome back sir');
} else{
    console.log('Unknown access... Security breach');
}



var marks = 45;

if (marks >=33 && marks<=69 ) {
    console.log("Just pass");
}   
    else{
        console.log("pass with distinction")
    }}

"""

# ( ) { [] ( {}{} ) }

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0



if __name__ == "__main__":
    
#   string = __reverse_string( "Data structure tutorial exercise: Stack" )
#   print(string)

    # is_balanced( js )
    # __is_balanced(js)
    
    print(is_balanced(js))


    

    



    

    
        