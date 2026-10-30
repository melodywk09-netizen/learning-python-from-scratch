c=["cap", "Iron man","Thor","Hulk","Gamora","Star lord","Nebula","Nat","Loki","Doom",]

#append
print("appending")
c.append("hawkeye")
print(c)

#insert
print("inserting")
c.insert(-4, "drax")
print(c)

#extend
print("extend")
y=["wanda","vision","peter","MJ"]
c.extend(y)
print(c)

#concattenate
print("concattenate")
x=c+y
print(x)