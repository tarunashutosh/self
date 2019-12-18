#!/usr/bin/python3
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  mini = -2**31
  maxi = 2**31
  if tree==[]:
    return True
  def isBST(i): 
    return (isBSTUtil(i, mini, maxi)) 
  
  def isBSTUtil(i, mini, maxi): 
      
    if i!=-1:
      if tree[i][0] < mini or tree[i][0] > maxi: 
        return False
      ans1 = isBSTUtil(tree[i][1], mini, tree[i][0]-1)
      ans2 = isBSTUtil(tree[i][2], tree[i][0]+1, maxi)
      if ans1==None:
        ans1 = True
      if ans2==None:
        ans = True
      return ans1 and ans2
  ans = isBST(0)
  if ans==None:
    ans=True
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
