class Solution:
    def maxHistogramArea(self, heights):
        # Largest rectangle in histogram using stack
        stack = []
        max_area = 0
        heights.append(0)  # sentinel for cleanup
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()  # restore
        return max_area

    def maxArea(self, mat):
        if not mat or not mat[0]:
            return 0
        
        rows, cols = len(mat), len(mat[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            # compute largest rectangle for this row as histogram
            max_area = max(max_area, self.maxHistogramArea(heights))
        
        return max_area

