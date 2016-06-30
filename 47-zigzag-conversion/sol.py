class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        output = ""
        if numRows==1:
            return s
        period_size = 2*numRows - 2
        number_of_periods = 1 + len(s) / period_size
        def sym_getter(idx):
            return s[idx] if idx < len(s) else ""


        def get_row(row_idx):
            output = ""
            for p_idx in range(number_of_periods):
                output += sym_getter(p_idx * period_size + row_idx)
                if row_idx !=0 and row_idx != numRows-1:
                    output += sym_getter((p_idx + 1) * period_size -  row_idx)
            return output


        for i in range(numRows):
            output += get_row(i)
        return output
