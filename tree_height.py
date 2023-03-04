import sys
import threading
import re
from array import *
import numpy as np

def compute_height(n, parents):
    heights = np.zeros(n,dtype=int)
    tree_height = 0
    
    for i in range(n):
        height = 0
        par_of_i = i
        while par_of_i != -1:
            if heights[par_of_i] != 0:
                height += heights[par_of_i]
                break 
            else:
                height += 1
                par_of_i = parents[par_of_i]
                
        heights[i] = height
        
        if height > tree_height:
            tree_height = height

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


