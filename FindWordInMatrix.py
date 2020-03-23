def word_search(matrix, word):
    numrows = len(matrix)
    numcols = len(matrix[0])
    for r in range(numrows):
        for c in range(numcols):
            if matrix[r][c] == 'F' and matrix[r][c+1] == 'O' and matrix[r][c+2] == 'A'and matrix[r][c+3] == 'M':
                return True
    for c in range(numcols):
        for r in range(numrows):
            if matrix[r][c] == 'F' and matrix[r+1][c] == 'O' and matrix[r+2][c] == 'A'and matrix[r+3][c] == 'M':
                return True


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))
