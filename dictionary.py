# #Dictionary
# -Indexed
# -ordered
# -Duplicate
# -mutable


# d = {<key>:<value>,<key>:<value>}

# d = {"a":"apple","b":"ball","c":"cat"}
# print(type(d))
# print(d)


# d = {"1":"apple","3":"ball","4":"cat"}
# print(type(d))
# print(d)

# d = {"a":"apple","b":"ball","c":"cat"}
# print(d["a"])
# print(len(d))

# # d = {}
# d = dict()
# print(d)

# d = {}
# d["a"] = "apple"
# d["b"] = "ball"
# d["d"] = "dog"
# d["c"] = "cat"
# print(d)

# d = {}
# n = int(input("enter n ="))
# for i in range(n):
#     name = (input("enter name= "))
#     phone = int(input("enter the phone number "))
#     d[name] = phone
# print(d)


# d = {"ram":"551544","shyam":"254657","ram":"54654164"}
# # # we cannot take the same key in dictionary if there is same the last will ext
# for i in d:
#     print(i)

# d = {"ram":"551544","shyam":"254657"}
# for i in d:
#     print(i)

# d = {"ram":"551544","shyam":"254657"}
# for i in d.values():
#     print(i)

# d = {"ram":"551544","shyam":"254657"}
# for i in d.items():
#     print(i)


# i = []
# d = {"ram":"551544","shyam":"254657"}
# for i in d.items():
#     l.append(i)
# print(l)


# d = {"ram":"551544","shyam":"254657"}
# d["ram"]= 1250000
# print(d)

# # del 
# d = {"ram":"551544","shyam":"254657"}
# del d["ram"]
# print(d)


# pop
# d = {"ram":"551544","shyam":"254657"}
# d.pop("ram")
# print(d)

# d = {"ram":"551544","shyam":"254657"}
# c = d.pop("ram")
# print(c)
# print(d)

# d = {"ram":"551544","shyam":"254657"}
# d.clear()
# print(d)

# d = {"ram":"551544","shyam":"254657"}
# c = {"a":"apple","b":"ball","c":"cat"}
# d.update(c)
# print(d)


# # list inside dictionary
# d = {"ram":["551544","25514815"],"shyam":["254657","6232321623"]}
# print(d)


# d = {}
# n = int(input("enter n ="))
# for i in range(n):
#     name = (input("enter name= "))
#     ntc_phone = int(input("enter the phone number "))
#     ncell_phone = int(input("enter the phone number "))
#     d[name] = [ntc_phone,ncell_phone]
# print(d)


# info ={'ram': ['551544', '25514815'], 'shyam': ['254657', '6232321623']}
# info["ram"][0] = 584877847
# print(info)

# info ={'ram': ['551544', '25514815'], 'shyam': ['254657', '6232321623']}
# info["ram"].append(584877847)
# print(info)

# # # dictionary inside list
# info = [{"Name":"Ram","ntc_phone":145412421,"ncell":5845457454},
#         {"Name":"shyam","ntc_phone":6596568,"ncell":555686}]
# print(info[0])


# d = []
# n = int(input("enter n ="))
# for i in range(n):
#     name = (input("enter name= "))
#     ntc_phone = int(input("enter the phone number "))
#     ncell_phone = int(input("enter the phone number "))
#     info = {"Name":name,"ntc_number":ntc_phone,"ncell":ncell_phone}
#     d.append(info)
# print(d)

# # update and delet
# a = [{'Name': 'jhj', 'ntc_number': 5665, 'ncell': 6595}, {'Name': 'kk', 'ntc_number': 6565, 'ncell': 56484}]
# del a["name"]
# print(a)






# dict inside dict
# d = {"ram":{"ntc":6568465,"ncell":56654},"shyam":{"ntc":58955656,"ncell":45865465}}
#  print(d)
# print(d["ram"])

# for i in d:
#     print(i)

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)


# d = {}
# n = int(input("enter n ="))
# for i in range(n):
#     name = (input("enter name= "))
#     ntc_phone = int(input("enter the ntc phone number "))
#     ncell_phone = int(input("enter the ncell phone number "))
#     d[name] = {"Name":name,"ntc_number":ntc_phone,"ncell":ncell_phone}

# print(d)
# # add dict inside dict
# d = {"ram":{"ntc":6568465,"ncell":56654},"shyam":{"ntc":58955656,"ncell":45865465}}
# d["hari"] = {"ntc":585685,"ncell":548487454}
# print(d)




