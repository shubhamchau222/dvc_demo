
with open('Artifact01.txt' , mode='r') as f:
    data = f.read()
    f.close()


# also create the New File 

with open('Artifact02.txt' , mode='a+') as file2 :
    file2.write(data + 'added SuccessFully...')
    file2.close()


print('Stage 03 Completed successfully........')
