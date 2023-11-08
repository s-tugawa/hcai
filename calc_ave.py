c_hash={}
val_hash={}
while True:
    try:
        line = input()
        key,val=line.split(" ")
        key=int(key)
        val=int(val)
        if key in val_hash:
            val_hash[key]+=val
            c_hash[key]+=1
        else:
            val_hash[key]=val
            c_hash[key]=1
    except EOFError:
        break

for key, val in sorted(val_hash.items()):
    val=val/c_hash[key]
    print (key,val)
