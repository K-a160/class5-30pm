# set
# - no indexing
# - on ordered
# - no duplicate data
# - mutable

# a = {1,2,3,4,}
# print(type(a))
# print(a)

# a = {"apple","ball","cat","dog"}
# print(a)    # ##it is on ordered


### - no duplicate dat
# a = {1,2,3,5,1,5,3,2,4,8,7}
# print(a)  ### - no duplicate dat


# a = [1,2,3,5,1,5,3,2,4,8,7]
# b = set(a)
# print(b)


# a = {"apple","ball","cat"}
# a.add("dog")
# print(a)


# a = {"apple","ball","cat"}
# a.add(("dog"),)
# print(a)


# a = {"apple","ball","cat"}
# a.remove("apple")
# print(a)

# a = {"apple","ball","cat"}
# for i in a:
#     print(i)

# ms = {"ram","shyam","Gita","mike"}
# apple ={"hari","ram","sita","Gita"}
# print(ms.union(apple))

# update

# ms = {"ram","shyam","Gita","mike"}
# apple ={"hari","ram","sita","Gita"}
# ms.update(apple)
# print(ms)

# # intersection
# ms = {"ram","shyam","Gita","mike"}
# apple ={"hari","ram","sita","Gita"}
# print(ms.intersection(apple))

# # difference
# ms = {"ram","shyam","Gita","mike"}
# apple ={"hari","ram","sita","Gita"}
# print(ms-apple)  #or ms.difference(apple)
# print(apple.difference(ms))  # apple-ms



# u = {'ram', 'Gita', 'shyam', 'hari', 'mike', 'sita',"nabin","sabin","ayush"}
# ms = {"ram","shyam","Gita","mike"}
# apple ={"hari","ram","sita","Gita"}
# print(ms.union(apple))
# print(u-ms.union(apple))