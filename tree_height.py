import sys
import threading
import re
from array import *
import numpy as np

def compute_height(n, parents):
    
    heights = np.zeros(n, dtype=int)
    tree_height = 0

    def calculate_height(n):
        if heights[n] != 0:
            return heights[n]

        if parents[n] == -1:
            heights[n] = 1
            return 1
        parent_height = calculate_height(parents[n])
        height = parent_height + 1
        heights[n] = height
        return height
    for j in range(n):
        node_height = calculate_height(j)
        if node_height > tree_height:
            tree_height = node_height

    return tree_height

def main():
    command=input()
    parents=array('i')
    if 'I' in command:
        n=int(input())
        par=input()
        a=re.split(' ',par)
        for x in a: 
             parents.append(int(x))

    
    if 'F' in command:
        file=input()
        name="test/"+file
        if 'a' in file:
            print("wrong file name")
        else:
            with open(name,"r") as file:
                n=int(file.readline())
                lines=file.readlines()
                nodes=lines[1:]
                for nodes in lines:
                    a=re.split(' ',nodes)
                    for x in a:
                     parents.append(int(x))
                   
    
    height=compute_height(n,parents)
    print(height)
    
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


