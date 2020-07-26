# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:25:29 2020

@author: Akshat Jain
"""

class Node(object):
    def __init__(self , data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    
    def insert(self , data):
        if not self.root:
            self.root = Node(data)
        
        else :
            self.insertNode(data,self.root)
    
    def insertNode(self , data , node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data , node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data , node.rightChild)
            else:
                node.rightChild = Node(data)
                
                
    def remove(self , data):
        if self.root:
            self.root = self.removeNode(data , self.root)
            
    def removeNode(self , data , node):
        if not node:
            return node
        
        if data < node.data:
            node.leftChild = self.removeNode(data , node.leftChild)
        
        elif data > node.data:
            node.rightChild = self.removeNode(data , node.rightChild)
            
        else:
            if not node.leftChild and not node.rightChild:
                print('removing the leaf node')
                del node
                return None
            
            if not node.leftChild:
                print('removing node with right child')
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print('removing node with left child')
                tempNode = node.leftChild
                del node
                return tempNode
            print('removing node with two children')
            tempNode = self.getPredeccor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data , node.leftChild)
        
        return node
    
    def getPredeccor(self , node):
        if node.rightChild:
            return self.getPredeccor(node.rightChild)
            
        return node
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
    
    def getMin(self , node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        
        return node.data
    
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self , node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        
        return node.data
    
    def traverse(self):
        if self.root:
            return self.inorderTraverse(self.root)
    
    def inorderTraverse(self , node):
        if node.leftChild :
            self.inorderTraverse(node.leftChild)
            
        print("%s"%node.data)
        
        if node.rightChild:
            self.inorderTraverse(node.rightChild)
            
bst = BinarySearchTree()
bst.insert(50)
bst.insert(10)
bst.insert(40)
bst.insert(30)
bst.insert(60)
bst.insert(70)
bst.insert(80)
bst.traverse()
bst.getMinValue()
bst.remove(50)
bst.getMinValue()
bst.getMaxValue()           
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
                
                
                
                