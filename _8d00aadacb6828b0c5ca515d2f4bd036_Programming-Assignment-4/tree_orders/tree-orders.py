# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    def inorder_traverse(i):
        if i==-1:
            return
        inorder_traverse(self.left[i])
        self.result.append(self.key[i])
        inorder_traverse(self.right[i])
    inorder_traverse(0)
    return self.result

  def preOrder(self):
    self.result = []
    def preorder_traverse(i):
        if i==-1:
            return
        self.result.append(self.key[i])
        preorder_traverse(self.left[i])
        preorder_traverse(self.right[i])
    preorder_traverse(0)        
    return self.result

  def postOrder(self):
    self.result = []
    def postorder_traverse(i):
        if i==-1:
            return
        postorder_traverse(self.left[i])
        postorder_traverse(self.right[i])
        self.result.append(self.key[i])
    postorder_traverse(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))
threading.Thread(target=main).start()
