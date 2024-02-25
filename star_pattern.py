'''
*
**
***
****
*****
****
***
**
*
'''

#this code aims to print above pattern just with one for loop
pattern=""
# 9 rows, i starts from 0. 
for i in range(9): 
    if i<5:
        pattern+="*"
    else:
        pattern="*" * (9-i)
    print(pattern)
    