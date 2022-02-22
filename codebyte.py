# def CamelCase(strParam):
#     string = ''
#     for index in range(len(strParam)):
#         if strParam[index].isalpha() and len(string) == 0:
#             string += strParam[index].lower()
#         elif strParam[index].isalpha() and index > 0 and not strParam[index - 1].isalpha():
#             string += strParam[index].upper()
#         elif strParam[index].isalpha():
#             string += strParam[index].lower()
#     return string


# print(CamelCase(input()))

# def getMin(arr):
#     #get minimum value in array
#     minimum = None
#     for i in arr:
#         if minimum == None:
#             minimum = i
#         else:
#             minimum = min(minimum, i)
#     return minimum

# def LargestFour(arr):
#     sum = 0
#     maxFour = []
#     for i in arr:
#         if len(maxFour) < 4:
#             maxFour.append(i)
#         else:
#             for j in maxFour:
#                 if i > j:
#                     # if i is greater than any value in maxFour
#                     # replace i with the min value in maxFour
#                     minimum = getMin(maxFour)
#                     maxFour[maxFour.index(minimum)] = i
#                     break
#     for i in maxFour:
#         sum += i
#     return sum

# print(LargestFour(input()))

# def runLength(strParam):
#     ans = ''
#     count = 0
#     currentLetter = strParam[0]
#     for char in strParam:
#         if char == currentLetter:
#             count += 1
#         else:
#             ans += '{}{}'.format(count, currentLetter)
#             count = 1
#             currentLetter = char
#     ans += '{}{}'.format(count, currentLetter)
#     return ans


# print(runLength('aabbcde'))

# def runLength(strParam):
#     ans = ''
#     for index in range(len(strParam) - 1, -1, -1):
#         ans += strParam[index]
#     return ans


# print(runLength('Coderbyte Love I'))

# def LRUCache(strArr):
#     cache = []
#     for char in strArr:
#         if char in cache:
#             cache.remove(char)
#             cache.append(char)
#         elif len(char) < 5:
#             cache.append(char)
#         else:
#             cache.pop(0)
#             cache.append(char)
#     return '-'.join(cache[-5:])


# print(LRUCache(["A", "B", "A", "C", "A", "B"]))

# def stringPeriods(strParam):
#     lenn = len(strParam)
#     validString = None
#     for i in range(lenn):
#         if i < int(lenn / 2) + 1:
#             thisStr = strParam[:i]
#             if len(thisStr) != 0 and thisStr * int(len(strParam) / len(thisStr)) == strParam:
#                 validString = thisStr
#                 return validString
#     return -1


# print(stringPeriods('abcabcabcabc'))
