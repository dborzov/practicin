class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word)==0:
            return True
        height = len(board) - 1
        if height==0:
            return False
        width = len(board[0]) -1
        coordinates = {}
        for i,row in enumerate(board):
            for j,el in enumerate(row):
                coordinates.get(el,[]).append((i,j) )
        if not word[0] in coordinates:
            return False
        candidates = [{"tail": each, ",".join(each):0} for each in coordinates.[word[0]]]
        cur = 1
        def adjacent(i,j):
            results = []
            for idx,jdx in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                if i<0 or i>=height or j<0 or j>= width:
                    continue
                results.append((idx,jdx))
            return results


        while cur<len(word):
            for candidate in candidates:
                if candidate is None:
                    continue
                i,j = candidate["tail"]
                advance_to = False
                for idx, jdx in adjacent(i,j):
                    if word[cur]==board[idx][jdx]:
            cur += 1
