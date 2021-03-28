def solution(input):
    #split input to different parameters
    s= input[0][1:-1]
    arr = [i for i in s.split(",")]
    n1= input[1]
    n2= input[2]
    
    #find liost length and create binary tree with list
    l = len(arr)
    root =None
    root = createBinTree(arr,root,l,0)
    #find lca element
    lca = findlca(root,n1,n2).key
    return lca

#change list to binary tree
def createBinTree(arr,root,n,i):
    if i < n :
        root = Node(arr[i])
        root.left = createBinTree(arr,root.left,n,2*i+1)
        root.right = createBinTree(arr,root.right,n,2*i+2)
    return root

#find lowest common ancestor
def findlca(root,n1,n2):
    #no node further
    if root is None:
        return None
    #no node represented in # form
    if root.key == '#':
        return None
    #if current node is in any of the number return current node
    if root.key == n1 or root.key ==n2:
        return root
    #if none of above satisfies - check if search numbers are in right or left node
    #it will set left/right nodes respectively if found.
    left_lca = findlca(root.left,n1,n2)
    right_lca = findlca(root.right,n1,n2)
    
    #If both numbers found on left side - first left node is LCA and left_lca is not null and right_lca will be null and vice versa
    #if one number found on left and other on right - left_lca and right_lca is not null and hence should return root
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca
    
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
