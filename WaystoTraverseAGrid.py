#Hi, here's your problem today. This problem was recently asked by Microsoft:
#You have 2 integers n and m representing an n by m grid, determine the number of ways you can get from the
#top-left to the bottom-right of the matrix y going only right or down.



def num_ways(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(1)
        matrix.append(row)

# For the following loop, I had to use n-1 and m-1 in the range because the indexes start at 0 for the matrix,
# so if i left it the way it is then it would give 0,1,2,3,4 indexes to loop through, which is one too many.
# When making the matrix originally, it made n and m number of rows/columns to index, so 4 and 4. that's where
# my confusion was.

    for i in range(n-1):
        for j in range(m-1):
            matrix[i+1][j+1] = matrix[i][j+1]+matrix[i+1][j]

    print("There are " + str(matrix[n-1][m-1]) + " ways.")

print(num_ways(2, 2)) #should result in two because only possible routes are: right, down and down, right