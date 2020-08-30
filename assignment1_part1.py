


#Create a function named listDivide that takes in two parameters
def listDivide(numbers, divide):
    divide=2
    noe = 0
    for i in numbers:
        if i%divide == 0:
            noe += 1
    else:
        continue
    return noe
# Create a custom exception class called ‘ListDivideException’. This should be two lines of Python code   

class ListDivideException(Exception):
    pass

#Write another function called testListDivide that performs the following tests on listDivide:

def testListDivide(numbers, divide):

print(listDivide([1,2,3,4,5]) #should return 2
print(listDivide([2,4,6,8,10]) #should return 5
print(listDivide([30, 54, 63,98, 100], divide=10) #should return 2
print(listDivide([]) #should return 0
print(listDivide([1,2,3,4,5], 1) #should return 5

if noe == 0:
    ListDivideException:
        print("No numbers to divide")