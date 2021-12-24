file = "pong.kv"

with open(file) as f:
    content = f.readlines()

content = [line[2:] for line in content]

with open(file,'w') as f:
    f.writelines(content)