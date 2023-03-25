'''
num2 = int(input("Enter a number : "))
result = 20/num2
print(result)
print("Done")


text = "Zerin"
print(text[5])
print("Done")
'''

try:
    list = [20,0,30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing bt zero is not possible")

finally:
    print("Successful")

    '''
    ata finally na thkle finallyr age hbe
    except IndexError:
        print("Index Error")
    '''