# python3

import re
from array import *


def compute_height(parArr):
    attendancy = array('i') 
    max_height = 0
    i=0
    while i<len(parArr):
       parent = parArr[i]
    
    if parent == -1:
             attendancy[i] = 1
    elif parArr[parent] != -1:
            if parArr[parent] in attendancy:
                path = path + attendancy[parArr[parent]]
                attendancy[i] = path 
                if path > max_height:
                 max_height = path
                 path = 1
                        
                parent = parArr[parent]
                path += 1
                print(attendancy)
    else:
             attendancy[i] = path 
             if path > max_height:
                max_height = path
                path = 1
                print(attendancy)
                        
    i += 1
    print(attendancy)
    return max_height      
    


def main():
    command=input()
    parArr=array('i')
    
    if 'I' in command:
        # nodeCount=int(input())
        parents=input()
        a=re.split(' ',parents)
        for x in a: 
             parArr.append(int(x))

    
    if 'F' in command:
        file=input()
        name="test/"+file
        if 'a' in file:
            print("wrong file name")
        else:
            with open(name,"r") as file:
                # node_Count=file.readline()
                lines=file.readlines()
                nodes=lines[1:]
                for nodes in lines:
                    a=re.split(' ',nodes)
                    for x in a:
                     parArr.append(int(x))
    
    height=compute_height(parArr)
    print(height)

if __name__ == "__main__":
     main()
    
   


