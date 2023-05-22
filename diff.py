import difflib
with open('update_2.0.3.bin', 'rb') as file1, open('upadte_QC_rev5.bin.gz', 'rb') as file2:
    data1 = bytearray(file1.read())
    data2 = bytearray(file2.read())
  
if data1 != data2:
    print("Files do not match.")
else:
    print("Files match.")

length = 0
newData = bytearray()

if len(data1) >= len(data2): 
     length = len(data1)
     for i in range(len(data1) - len(data2)):
        data2.append(0)
elif len(data2) > len(data1): 
     length = len(data2)
     for i in range(len(data2) - len(data1)):
        data1.append(0)
for i in range(length): 
     newData.append(data1[i]^data2[i])

with open('diff.bin', 'wb') as file3:
    file3.write(newData)
"""
d = difflib.Differ()
e = d.compare(data1,data2)        #set the compare output to a variable
print(e.__sizeof__())

for i in e:
        print(i)
        if i.startswith("-"):         #if that char start with "-" is not a match
                print(i + "index is different")
        if i.startswith("+"):         #if that char start with "-" is not a match
                print(i + "index is the same")
print("Done!")"""