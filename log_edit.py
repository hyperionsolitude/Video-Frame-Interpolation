import sys
counter =0
counterr =0
edited = ""
total=0
max = 0.0
min = 900.0
cleanedloss=[]
filepath= str(sys.argv[1])
with open(filepath) as log:
    sumlines = log.readlines()
for sumline in sumlines:
    if counter == 0:
        edited += sumline.split("[")[1].split("\n")[0]
    elif counter == len(sumlines)-1:
        edited += sumline.split("]")[0]
    else:
        edited += sumline.split("\n")[0]
    counter = counter + 1
for element in edited.split(" "):
    if element != '':
        cleanedloss.append(element)
for number in cleanedloss:
    number=float(number)
    if number > max:
        max = number
        maxindex = counterr + 1
    if number < min:
        min = number
        minindex = counterr + 1
    total += number
    counterr += 1   

print('Count:', counterr)
print('Total:', total)
print('Average:', total / counterr)
print('Minimum:',min, 'at frame',minindex*4)
print('Maximum:',max, 'at frame',maxindex*4)