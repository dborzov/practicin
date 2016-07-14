class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        if len(matrix[0])==0:
            return 0
        topological = []
        visited = {}
        def adjacent(i,j):
            matches = []
            for nbr_i, nbr_j in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                if nbr_i<0 or nbr_i>= len(matrix):
                    continue
                if nbr_j<0 or nbr_j>= len(matrix[0]):
                    continue
                if matrix[i][j] < matrix[nbr_i][nbr_j]:
                    matches.append( (nbr_i, nbr_j) )
            return matches


        def key(i,j):
            return ",".join((str(i),str(j)))

        def visit(i,j):
            visited[key(i,j)] = 0
            for a_i, a_j in adjacent(i,j):
                if not key(a_i,a_j) in visited:
                    visit(a_i,a_j)
            topological.append( (i,j) )

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if key(i,j) in visited:
                    continue
                visit(i,j)
        longest_strike = 0
        for k_i, k_j in topological:
            max_before = 0
            for a_i, a_j in adjacent(k_i,k_j):
                if visited[key(a_i,a_j)] > max_before:
                    max_before = visited[key(a_i,a_j)]
            visited[key(k_i,k_j)] = max_before + 1
            if visited[key(k_i,k_j)] > longest_strike:
                longest_strike = visited[key(k_i,k_j)]
        return longest_strike


matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]

labels = [
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','J']
]
print  Solution().longestIncreasingPath(matrix)
