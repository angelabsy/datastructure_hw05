from Node_05 import Node
from Tree_05 import RBT

import os

def search():
    filenames = os.listdir('./input/')
    return filenames

def fileData(files):
    data = []

    for file in files:
        f = open('./input/'+ file, 'r')
        lines = f.readlines()
        tmpData = []
        for line in lines:
            inputNumber = int(line.strip())
            tmpData.append(inputNumber)

        data.append(tmpData)
        f.close()
    return data 

def main():
    fileNames = search()
    datas = fileData(fileNames)
    case = 0

    for data in datas:
        rbt = RBT()
        
        #read data for input 
        for i in data:
            if i > 0:
                rbt.insert(i)
            elif i < 0:
                rbt.delete(-i)
            else:
                break


        print("filename = " + fileNames[case])

        rbt.printTotalNode(rbt.root)

        rbt.printInsertedNode(rbt.root)

        rbt.printDeletedNode(rbt.root)

        rbt.printMissedNode(rbt.root)

        rbt.printBlackNode(rbt.root)

        rbt.printBlackHeight(rbt.root)

        print("Inorder Traversal: ")
        rbt.inOrderTraversal(rbt.root)

        print("\n")

        case += 1 

main()
