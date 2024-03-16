
dict = {"1":"java","2":"python","3":"sql","2":"node"}

# print(dict)

# for key in dict:
#     print(key+" "+dict[key])

# dt = dict.copy()
# print(dt)

dt = {"5":"react"}

dt.update(dict)
print(dt.values())
print(dt.keys())
print(dt.items())
dt.clear()
print(dt)