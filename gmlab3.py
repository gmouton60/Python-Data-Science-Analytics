# -*- coding: utf-8 -*-
"""GMLab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C77isT0rRvf2gTwoh_7aBWi171q70Cld

Exerc. 1
---
#### Alphabet Slices
- Store the first ten letters of the alphabet in a list.
- Use a slice to print out the first three letters of the alphabet.
- Use a slice to print out any three letters from the middle of your list.
- Use a slice to print out the letters from any point in the middle of your list, to the end.
"""

L = list('abcdefghij')
print(L)

print(L[:3])
print(L[4:4+3])
print(L[6:])

"""#### Multiples of Ten
- Make a list of the first ten multiples of ten (10, 20, 30... 90, 100). Try to do it using a list comprehension. Print out your list.

#### Cubes
- We saw how to make a list of the first ten squares. Make a list of the first ten cubes (1, 8, 27... 1000) using a list comprehension, and print them out.
"""

L = [i*10 for i in range(1, 11)]  
print(L)
L = [i**3 for i in range(1, 11)]
print(L)

"""Exerc. 2
---
#### <a name='exercise_mountain_heights'></a>Mountain Heights
- Wikipedia has a list of the [tallest mountains in the world](http://en.wikipedia.org/wiki/List_of_mountains_by_elevation), with each mountain's elevation. Pick five mountains from this list.
    - Create a dictionary with the mountain names as keys, and the elevations as values.
    - Print out just the mountains' names, by looping through the keys of your dictionary.
    - Print out just the mountains' elevations, by looping through the values of your dictionary.
    - Print out a series of statements telling how tall each mountain is: "Everest is 8848 meters tall."
"""

M = {
    'Mount Everest':8848,
    'Kangchenjunga':8586,
    'Cho Oyu':8201,
    'Manaslu':8163
}
for k in M.keys():
    print(k)
print('--------')
for v in M.values():
    print(v)
print('--------')
for k, v in M.items():
    print('%s is %d meters tall' % (k, v))

"""#### Mountain Heights 2
- Revise your final output from Mountain Heights, so that the information is listed in alphabetical order by each mountain's name.
    - That is, print out a series of statements telling how tall each mountain is: "Everest is 8848 meters tall."
    - Make sure your output is in alphabetical order.
"""

L = [k for k in M.keys()]
L.sort()
for k in L:
    print('%s is %d meters tall' % (k, M[k]))

"""Exerc. 3
---
Write a function that accepts a sentence and calculate and print the number of letters and digits in the sentence. Suppose the following string is passed to your function: 

hello world! 123

Then, the output should be:

LETTERS 10 <br>
DIGITS 3
"""

# use isdigit() and isalpha()
print('3'.isdigit())
print('a'.isalpha())

def func1(S):
    d = 0
    a = 0
    for c in S:
        if c.isdigit():
            d+=1
        elif c.isalpha():
            a+=1
    print('LETTERS', a)
    print('DIGITS', d)
    
func1('hello world! 123')

"""Exerc. 4
---
Write a function that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following is supplied to the function:

hello world and practice makes perfect and hello world again

Then, the output should be:

again and hello makes perfect practice world
"""

# hint: a set has no duplication 

def func2(S):
    s = S.split(' ') 
    s = list(set(s))
    s.sort()
    s=' '.join(s)
    print(s)
    
func2('hello world and practice makes perfect and hello world again')

"""Exerc. 5
---
Complete the following code. Use python dictionary to implement a table (a 2d array) that provides the following operations:
    - setAt(i, j, v)  set value of entry (i, j) to be v
    - readAt(i, j)  return value at entry (i, j); if no such value, return None
    - rowHasValuesAt(i)  return the column indices where row i has some values set; if no value in the whole row, return None
    - readRow(i) return all the set values at row i
    
Note the (row and column) indices start from 0 and cannot be negative number.
"""

class Table(dict):
        
    def setAt(self, i, j, v):
        self[(i, j)] = v
             
    def readAt(self, i, j):
        return self.get((i, j), None)
    
    def rowHasValuesAt(self, i):
        L = []
        for ii, jj in self.keys():
            if ii == i:
                L.append(jj)
        if L:
            return L
        else:
            return None
    
    def readRow(self, i):
        L = []
        for ii, jj in self.keys():
            if ii == i:
                L.append(self[(ii, jj)])
        return L

t = Table()
t.setAt(1, 2, 5)
t.setAt(3, 5, 7)
t.setAt(3, 12, 21)
print(t.readAt(1, 3))
print(t.readAt(3, 5))
print(t.rowHasValuesAt(3))
print(t.rowHasValuesAt(45))
print(t.readRow(3))
print(t.readRow(45))