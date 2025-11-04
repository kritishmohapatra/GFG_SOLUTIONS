class Solution:
    def precedence(self, c):
        if c == '^':
            return 3
        elif c in ('*', '/'):
            return 2
        elif c in ('+', '-'):
            return 1
        else:
            return -1

    def isRightAssociative(self, c):
        return c == '^'

    def isOperator(self, c):
        return c in "+-*/^"

    def infixToPrefix(self, s):
        st = []
        result = []

        # scan from right to left
        for c in reversed(s):
            if c.isalnum():
                result.append(c)
            elif c == ')':
                st.append(c)
            elif c == '(':
                while st and st[-1] != ')':
                    result.append(st.pop())
                if st:
                    st.pop()  # remove ')'
            elif self.isOperator(c):
                while (st and self.isOperator(st[-1]) and
                       (self.precedence(st[-1]) > self.precedence(c) or
                        (self.precedence(st[-1]) == self.precedence(c) and self.isRightAssociative(c)))):
                    result.append(st.pop())
                st.append(c)

        # pop remaining operators
        while st:
            result.append(st.pop())

        # reverse at the end to get correct prefix
        return ''.join(reversed(result))
