"""
@author: Shubham Prajapati

Problem:Spiral
Input:
arr=[[1,2,3],[4,5,6],[7,8,9]]
Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]   

"""
lst=[]         #declaring empty list 
def spiral(arr,row,col): #declaring and defining a spiral function 
    for i in range(0,1):
     for j in range(0,col):
      lst.append(arr[i][j])
    lst.append(arr[1][col-1])
    for i in range(len(arr)-1,1,-1):
     for j in range(col-1,-1,-1):
      lst.append(arr[i][j])
    for i in range(row-2,0,-1):
     for j in range(0,col-1):
      lst.append(arr[i][j])
    return lst #it will reurn a list

row=int(input("Enter no of rows:")) #It will take no of rows of a matrix
col=int(input("Enter no of coloumns:")) #it will take no of columns in a matrix
arr=eval(input("Enter an elements in the array:"))
print("Spiral matrix is:",spiral(arr,row,col))  #whenever our function is return something then we have to call using print() function
