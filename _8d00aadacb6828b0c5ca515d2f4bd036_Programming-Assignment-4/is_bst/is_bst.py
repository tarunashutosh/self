#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  mini = -3**31
  maxi = 3**31
  def isBST(i): 
    return (isBSTUtil(i, mini, maxi)) 
  
  def isBSTUtil(i, mini, maxi): 
      
    if len(tree[i])<=1: 
      print ('1')
      return True
  
    if tree[i][0] < mini or tree[i][0] > maxi: 
      print ('2')
      return False
  
    return (isBSTUtil(tree[i][1], mini, tree[i][0]-1) and
      isBSTUtil(tree[i][2], tree[i][0]+1, maxi)) 
  ans = isBST(0)
  print (ans)
  return ans

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
