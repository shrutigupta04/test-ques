class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
      


def decodeHuff(root, s):
	#Enter Your Code Here
    i=-1
    temp=root
    while i<len(s)-1:
        i=i+1
        if s[i]=='1':
            temp=temp.right
            if temp.right==None and temp.left==None:
                print (temp.data, end="")
                temp=root
        elif s[i]=='0':
            temp=temp.left
            if temp.right==None and temp.left==None:
                print(temp.data, end="")
                temp=root