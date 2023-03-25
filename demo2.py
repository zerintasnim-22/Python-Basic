#xargs
'''
def student(*details):
    print(details[0])

student(101,"Zerin")
student(102,"Zerin", 3.52)


def add(*number):
    sum = 0
    for num in number:
        sum = sum + num
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)
'''

#xxarg

def student(**details):
    print(details["name"])

student(id=101,name="Zerin")



