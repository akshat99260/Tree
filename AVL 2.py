# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:40:19 2020

@author: Akshat Jain
"""

class Node(object):
    def __init__(self , data):
        self.data = data 
        self.height = 0
        self.leftchild = None
        self.rightchild = None

class AVL(object):
    def __init__(self):
        self.root = None
    
    def calcHeight(self , node):
        if not node :
            return -1
        return node.height
    
    def calcBalance(self , node):
        if not node :
            return 0
        return self.calcHeight(node.leftchild)-self.calcHeight(node.rightchild)
    
    def insert(self, data):
        self.root = self.insertNode(data , self.root)
            
    def insertNode(self , data , node):
        if not node :
            return Node(data)
        
        if data < node.data:
            node.leftchild = self.insertNode(data , node.leftchild)
        else:
            node.rightchild = self.insertNode(data , node.rightchild)
            
        node.height = max(self.calcHeight(node.leftchild) , self.calcHeight(node.rightchild))
        
        return self.settleViolation(data , node)
    
    def settleViolation(self , data , node):
        '''case-1'''
        balance = self.calcBalance(node)
        if balance > 1 and data < node.leftchild.data:
            return self.rightRotation(node)
        if balance <-1 and data > node.rightchild.data:
            return self.leftRotation(node)
        if balance > 1 and data > node.leftchild.data:
            node.leftchild = self.leftRotation(node.leftchild)
            return self.rightRotation(node)
        if balance <-1 and data < node.rightchild.data:
            node.rightchild = self.rightRotation(node.rightchild)
            return self.leftRotation(node)
        
        return node
    
    def rightRotation(self , node):
        templeftchild = node.leftchild
        t = templeftchild.rightchild
        
        templeftchild.rightchild = node
        node.leftchild = t
        
        node.height = max(self.calcHeight(node.leftchild)  , self.calcHeight(node.rightchild))+1
        templeftchild = max(self.calcHeight(templeftchild.leftchild) , self.calcHeight(templeftchild.rightchild))+1
        
    def leftRotation(self , node):
        temprightchild = node.rightchild
        t = temprightchild.leftchild
        
        temprightchild.leftchild = node
        node.rightchild = t
        
        node.height = max(self.calcHeight(node.leftchild)  , self.calcHeight(node.rightchild))+1
        temprightchild = max(self.calcHeight(temprightchild.leftchild) , self.calcHeight(temprightchild.rightchild))+1
    def traverse(self):
        if self.root:
            self.inordertraverse(self.root)
            
    def inordertraverse(self,node):
        if node.leftchild:
            self.inordertraverse(node.leftchild)
        
        print('%s'%node.data)
        
        if node.rightchild:
            self.inordertraverse(node.rightchild)
            
    def remove(self,data):
        if self.root :
            self.root = self.removeNode(data , self.root)
            
    def removeNode(self,data,node):
        if not node:
            return node
        
        if data < node.data:
            node.leftchild = self.removeNode(data , node.leftchild)
        elif data> node.data:
            node.rightchild = self.removeNode(data , node.rightchild)
        else :
            if not node.leftchild and not node.rightchild:
                print('deleting leaf node')
                del node
                return  None
            if not node.rightchild:
                print('deleting node with one leftchild')
                tempnode = node.leftchild
                del node.leftchild
                return tempnode
            elif not node.leftchild:
                print('deleting node with one rightchild')
                tempnode = node.rightchild
                del node.rightchild
                return tempnode
            print("removing node with twoo children")
            tempnode = self.getPredecessor(node.leftchild)
            node.data = tempnode.data    
            node.leftchild = self.removeNode(tempnode.data , node.leftchild)
            
        if not node:
            return node
        node.height = max(self.calcHeight(node.leftchild)  , self.calcHeight(node.rightchild))+1
        
        balance = self.calcBalance(node)
        
        if balance> 1 and self.calcBalance(node.leftchild)>=0:
            return self.rightRotation(node)
        if balance<-1 and self.calcBalance(node.rightchild)<=0:
            return self.leftRotation(node)
        if balance> 1 and self.calcBalance(node.leftchild)<0:
            node.leftchild = self.leftRotation(node.leftchild)
            return self.rightRotation(node)
        if balance<-1 and self.calcBalance(node.rightchild)>0:
            node.rightchild = self.rightRotation(node.rightchild)
            return self.leftRotation(node)
        return node
            
    def getPredecessor(self , node):
        if node.rightchild:
            return self.getPredecessor(node.rightchild)
        
        return node
if __name__ == "__main__":
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.remove(20)
    avl.traverse()
    avl.search(40)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    