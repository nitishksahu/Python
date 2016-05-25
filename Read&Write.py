myFile = open('Sample.txt', 'w')
myFile.write('This is pretty cool! And this look awesome')
myFile.close()

reader = open('Sample.txt', 'r')
text = reader.read()
print(text)