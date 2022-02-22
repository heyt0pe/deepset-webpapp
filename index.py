# Class_Tuple = ()  # 2a

# #2b
# for i in range(10):
#     firstName = input('What is your first name: ')
#     lastName = input('What is your last anme: ')
#     matricNo = input('What is your matric Number: ')
#     new_Tuple = (firstName, lastName, matricNo)
#     Class_Tuple = Class_Tuple + (new_Tuple,)

# #2c
# print(Class_Tuple)

# while True:
#     x = int(input("Enter amount: NGN"))
#     paystackAmount = x / 0.985
#     if paystackAmount > 2500:
#         paystackAmount += 100

#     paystackTake = x * 0.015
#     if paystackAmount > 2500:
#         paystackTake += 100

#     yourTake = paystackAmount - paystackTake
#     print("You would charge {:,}".format(paystackAmount))
#     print("Paystack takes {:,}".format(paystackTake))
#     print("You take {:,}".format(yourTake))
#     print(" ")
#     print(" ")

# x = 'discuss.leetcode.com'
# s = x.split('.')
# t = x.split('.')
# for d in t:
#     cc = '.'.join(s)
#     print(cc)
#     s.remove(d)

x = """
9b2226
ae2012
bb3e03
ca6702
7f5539
606c38
283618
03045e
370617
6a040f
ee9b00
0a9396
005f73
0aff99
9d4edd
7400b8
6b705c
cb997e
a4133c
38b000
14213d
007200
7209b7
3d405b
8338ec
3a86ff
5a189a
3c096c
"""
colors = []
c = x.split('\n')
for i in c:
    cc = "Color(0XFF{})".format(i.upper());
    colors.append(cc)
print(colors);

