#program to implement the algorithm of page rank

#to get the user input for the matrix
#number of rows are equal to the number of columns i.e square matrix.
n = int(input("Enter the number of rows in a matrix"))
a = [[0 for x in range (n)] for y in range(n)]
for i in range (n):
    for j in range(n):
        a[i][j]=int(input())

#intialising an array which contains rank as its elements
#int rank_array=[];

#the rank_array is initially assigned with the valu 1/n where n is the number of nodes
value=float(1.0/n);
rank_array=[value] * n;

print(rank_array)
#printing the array matrix

new_rank_array=[0] * n;

def update_matix():
   for i in range (n):
      for j in range(n):
         if(a[j][i]==1):
            count=float(number_of_outlinks(j,i));
            #print(count)
            new_rank_array[j]+=(rank_array[j]/count);
            #print(new_rank_array)



count=0;
def number_of_outlinks(j,i):
   for i in range (n):
      if(a[j][i]==1):
         count+=1;
   return count;

print(new_rank_array)
