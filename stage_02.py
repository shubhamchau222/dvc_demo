
# read the file

with open('Artifact01.txt' , mode='r') as f:
    data = f.read()
    f.close()

print(data)