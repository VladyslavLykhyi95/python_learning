some_list = ["one", "two", "three", "four", "five", "word"]

print(some_list[-3])

print(str(some_list[1])[0])

print(str(some_list[-1])[-1])

some_list.append("six") #return None if print (?)
print(some_list)

some_list.insert(len(some_list)//2,"three with half")
print(some_list)

some_list.pop(0) # or some_list.remove(some_list[0])
print(some_list)

some_list.remove("word")
print(some_list)