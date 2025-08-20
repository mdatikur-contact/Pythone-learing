# import datetime
# x= datetime.datetime.now()
# print(x.strftime("%A"))
# print(x.strftime("%d"))
# print(x.strftime("%B"))
# print(x.strftime("%Y"))
# print(x.strftime("%c"))
# print(x.strftime("%D"))
# print(x.strftime("%X"))
# print(x.strftime("%x"))


# import math
# a =9
# print(math.sqrt(a))
# print(math.pi)

# import json
# x = {"name": "Atikur","age": 25,"dept": "CSE"}

# print(json.dumps(x, indent = 4) )

# import re
# txt ="this is atikur Rahmna atik issdfsd good is"
# x = re.search(r"\bis\w+", txt)
# print(x.group())

# with open("b.txt", "a") as f:
#     f.write("file is empty")
# with open("a.txt") as f:
#     # print(f.readline())
#     # print(f.readline())
#     for x in f:
#         print(x)

import os
os.remove("a.txt")