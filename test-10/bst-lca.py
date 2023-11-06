class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           
def lca(root, v1, v2):
  #Enter your code here
    if root==None:
        return root
    if v1<=root.info and v2>=root.info:
        return root
    elif v1>=root.info and v2<=root.info:
        return root
    if v1<root.info and v2<root.info:
        return lca(root.left, v1, v2)
    elif v1>root.info and v2>root.info:
        return lca(root.right, v1, v2)