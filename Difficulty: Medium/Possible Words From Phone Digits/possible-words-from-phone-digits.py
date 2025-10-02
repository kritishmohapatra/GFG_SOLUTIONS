
class Solution:
    def possibleWords(self, numbers):
        # code here
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Convert the array of integers into a string of digits.
        digits = ''.join(map(str, arr))
        
        # If the input is empty, return an empty list.
        if not digits:
            return []
            
        result = []

        def backtrack(index, current_combination):
            # Base case: if the current combination has the same length as the digits string,
            # it's a complete word.
            if index == len(digits):
                result.append(current_combination)
                return

            digit = digits[index]
            
            # Check if the digit exists in our mapping (e.g., handles '0' and '1').
            if digit in mapping:
                letters = mapping[digit]
                for letter in letters:
                    # Recursive step: explore all possible letters for the current digit.
                    backtrack(index + 1, current_combination + letter)
            else:
                # If the digit is not in the mapping (like '0' or '1'), skip it
                # and move to the next digit.
                backtrack(index + 1, current_combination)

        # Start the backtracking process from the first digit with an empty string.
        backtrack(0, "")
        return result

        
        
