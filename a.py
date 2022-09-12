d = {'names': ["Anil", "Bhushan"], "sal":400, "disc": 300}
d['movie'] = "Liger"
d["director"] = "Poori"
# d[3] = 300
# d[1] = 1000
print(d['sal'])
# print(dir(d))
print(d.keys())
print(d.values())
print(d.items())
print(d['disc'])
print(d.get('sals'))
print(d.popitem())
print(d)

# 'clear', 'copy', 'fromkeys', 'get', 'items', 
# 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'