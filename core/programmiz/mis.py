# file read and write

'''f = open('msg.txt', 'w')
f.write('nitesh sahu')

f = open('msg.txt', 'a')
f.write(' APPENDED')

f = open('msg.txt', 'r')
msg = f.read()
print(msg)

f.close()'''

'''try:
    f = open('msg.txt', 'w')
    f.write('nitesh sahu')

    f = open('msg.txt', 'a')
    f.write(' APPENDED')

    f = open('msg.txt', 'r')
    msg = f.read()
    print(msg)
finally:
    f.close()'''

with open('text_files/msg.txt','w') as f:
    f.write('Nitesh Sahu')
with open('text_files/msg.txt','r') as f:
    msg = f.read()
    print(msg)