class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def check_binary_search_tree_(root):
    lst=[]
    if root==None:
        return False
    def helper(root, lst):
        if root==None:
            return
        helper(root.left, lst)
        lst.append(root.data)
        helper(root.right, lst)
        return lst
    helper(root, lst)
    p=set(lst)
    if lst==sorted(p):
        return True
    else:
        return False