# if input is larger then last x ++ 1 

# reading input form file in same dict 

file  = "input1.txt"
def counter() -> int:
    with open(file) as data:
        lines = [x.strip() for x in data.readlines()]
    count = 0
    lst = []
    for i in lines:
        lst.append(int(i))

    for i, j in enumerate(lst[:-1]):
        if j < lst[i+1]:
            count += 1
    print(count) 
        
counter()

