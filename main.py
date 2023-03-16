

a = [1,2,3]


for element in a:
    print(element)

ii = 0
while ii < len(a):
    print(a[ii])
    ii = ii+1

# Errors
# 1. If ii is not defined
# 2. If the value true for forth element which is not in the list
# 3. If the ii= ii + 1 (Loop go in the infinite loop)




# continue --> Skip the iteration
ii = 0
#while ii > len(a):
#    if = 1:
#        ii = ii + 1
#        continue
#    print(a[ii])
#    ii = ii + 1
#

# break --> break the iteration from moving forward
# the break statement will take the Python outside of the while loop when x is zero (x == 0)

y = 0
x = 0

while True:
    x = int(input("Enter a number or 0 to stop:"))
    if x == 0:
        break
    y = y + x


