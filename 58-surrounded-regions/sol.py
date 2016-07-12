class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        if len(board[0])==0:
            return
        regions = []
        links = {}
        bordered_regions = {}
        width = len(board)
        height = len(board[0])

        def key(i,j):
            return ",".join((str(i),str(j)))

        def get_region(i,j):
            region_id = links.get(key(i,j),None)
            if region_id is None:
                return None
            while regions[region_id] != region_id:
                region_id = regions[region_id]
            return region_id

        for i in range(width):
            for j in range(height):
                if board[i][j]=='X':
                    continue
                top = get_region(i-1,j)
                left = get_region(i,j-1)
                if top is None and left is None:
                    # new region
                    regions.append(len(regions))
                    region_id = len(regions) - 1
                if (not top is None) and (not left is None):
                    # merging if needed
                    if top != left:
                        regions[top] = left
                    region_id = left
                if (top is None) and (not left is None):
                    region_id = left
                if (not top is None) and (left is None):
                    region_id = top
                links[key(i,j)] = region_id
                if i==0 or i==width-1 or j==0 or j==height-1:
                    bordered_regions[region_id] = True

        # print 'regions: ',regions
        # print 'boarded regions: ', links
        # print 'boarded regions: ', bordered_regions

        border_regions = bordered_regions.keys()
        for region_id in border_regions:
            while regions[region_id] != region_id:
                region_id = regions[region_id]
            bordered_regions[region_id] = True

        for i in range(width):
            for j in range(height):
                region_id = get_region(i,j)
                if region_id is None:
                    continue
                if region_id in bordered_regions:
                    continue
                board[i][j] = 'X'


board = [['X', 'X', 'X', 'X'],['X', 'O', 'O', 'X'],['X', 'X', 'O', 'X'],['X', 'O','X', 'X']]
print board
Solution().solve(board)
print board
