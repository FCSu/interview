def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if traverse(board, i, j, word):
                return True               
    return False

def traverse(board, i, j, word):
    if len(word) == 0:
        return True
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
        return False

    if word[0] == board[i][j]:
        temp = board[i][j]
        board[i][j] = ''
        ans = traverse(board, i + 1, j, word[1:]) or traverse(board, i - 1, j, word[1:]) or traverse(board, i, j + 1, word[1:]) or traverse(board, i, j - 1, word[1:])
        board[i][j] = temp
        return ans
    else:
        return False
