from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Get number of rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Initialize a (ROWS+1) x (COLS+1) matrix filled with zeros for prefix sums
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Compute prefix sum matrix
        for r in range(ROWS):
            prefix = 0  # running sum of current row
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]  # value from row above at same column
                # Store sum of submatrix from (0,0) to (r,c)
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Adjust indices to match the prefix sum matrix (1-based indexing)
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        # Use inclusion-exclusion principle to get sum of the submatrix
        bottomright = self.sumMat[row2][col2]
        left = self.sumMat[row2][col1 - 1]
        above = self.sumMat[row1 - 1][col2]
        topleft = self.sumMat[row1 - 1][col1 - 1]
        
        return (bottomright - left - above) + topleft

if __name__ == "__main__":  
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    numMatrix = NumMatrix(matrix)
    print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
    print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
    print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12
