with open('artifact.txt','r') as f:
    text = f.read()

with open('artifact.txt','w') as f:
    text = f.write(text + "I have added one line")

print(text)
print('It is a end of stage 3')