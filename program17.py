'''
subjects = ["C","C++","Java","Python","Basic"]

#print(len(subjects))

subjects.append("TOC")
print(subjects)

subjects.insert(2,"OS")
print(subjects)

subjects.remove("Basic")
print(subjects)
'''
subjects = [5,4,6,22,768,4,4,4]
'''
subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)

subjects.clear()
print(subjects)

subjects2 = subjects.copy()
print(subjects2)

pos = subjects.index(4)
print(pos)
'''
pos = subjects.count(4)
print(pos)