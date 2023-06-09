cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293, 38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]

result=[]
for i in cipher:
    j=0
    while (j+1)**2<=i:
        j+=1
    result.append((i-j**2,j))

result.sort(key=lambda x:x[0])

chrs=[i[1] for i in result]



for start in range(128):
    flag=[start]
    next=chrs[0]-start
    flag.append(next)
    for i in range(1,len(chrs)):
        next=chrs[i]-next
        flag.append(next)
    try:
        print(''.join([chr(start)+":"]+[chr(i) for i in flag]))
    except:
        
        pass