# <<-------------------- Excersice 3 --------------------->>
"""
poem.txt Contains famous poem "Road not taken"
by poet Robert Frost. You have to read this file in python and print 
every word and its count as show below. Think about the best data
structure that you can use to solve this problem and
figure out why you selected that specific data structure.

'diverged': 2,
 'in': 3,
 'I': 8

"""

poem_path = "/home/yking19/practice/Codebasics/py_master_repo/DataStructures/4_HashTable_2_Collisions/Solution/poem.txt"


def count_words(file_name):
    word_count = {}
    with open(file_name, "r") as file:
        for line in file:
            tokens = ( (line.lower()).replace(',', "") ).split(" ")
            for word in tokens:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count
        

if __name__ == "__main__":
    print(count_words(file_name=poem_path))
