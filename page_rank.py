#program to implement the algorithm of page rank

#to get the user input for the matrix
#number of rows are equal to the number of columns i.e square matrix.
n = int(input("Enter the number of rows in a matrix\n"))
a = [[0 for x in range (n)] for y in range(n)]
for i in range (n):
    for j in range(n):
        a[i][j]=int(input())

iteration=input("Enter the number of iterations\n")
#to get the user input for the number of iterations which has to be performed


value=float(1.0/n);
#the rank_array is initially assigned with the value 1/n where n is the number of nodes.

rank_array=[value] * n;
#all the array elements are initialised with the value which was calculated.

print(rank_array)
#printing the array matrix


def update_matix(rank_array):
#function which updates the rank values of each page.
   new_rank_array=[0] * n;
   #the array elemnets are initialised with the value zero. 
   for i in range (n):
      for j in range(n):
         if(a[j][i]==1):
         #if there is incomming link from the node from jth node to ith node.
            num=number_of_outlinks(j,i);
            #function is called which gives the number of outlinks from the ith node.
            new_rank_array[i]+=float(rank_array[j]/num);
            #new rank value is calculated.

   print(new_rank_array)
   #array which is contains updated rank is printed.
   return new_rank_array;
   #the array which contains the updated rank is returned.


count=[0]
def number_of_outlinks(j,i):
#function to calculate the number of outlinks of the ith node
   count[0]=0;
   for i in range (n):
      if(a[j][i]==1):
      #when there is link between the nodes the count is incremented by one.
         count[0]+=1;
   
   return count[0];
   #the calculated value of count is returned.

x=[0]
while(x[0]!=iteration):
#new rank is updated until the value in the iteration is satisfied.
   new_rank_array=update_matix(rank_array);
   #function to update the matrix is called.
   x[0]+=1;
   #the value of x[0] is incremented by one.
   rank_array=new_rank_array
   #rank_array is initialised with the array which contains the updated rank value.
   

