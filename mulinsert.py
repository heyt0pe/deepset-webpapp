class Solution(object):

    def isValid(self, s):
        max = 0
        count = 0
        i = 0
        opens = []
        while i < len(s):
            char = s[i]
            if char == ')':
                if(len(opens) == 0):
                    if count > max:
                        max = count
                    count = 0
                elif(opens[len(opens) - 1]) == '(':
                    opens = opens[:-1]
                    count += 2
                    if count > max:
                        max = count
                else:
                    if count > max:
                        max = count
                    count = 0
                
            else:
                opens.append(char)
            i += 1
        return max


solution = Solution()

print(solution.isValid('(())'))
