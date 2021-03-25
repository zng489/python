# Python


```
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
i = 0
new_list = []

while i < len(names): # "len(names) 5 # while i < 5:"
    if len(names[i]) >= 6:
        new_list.append(names[i])  
    i += 1 # i = i + 1
    
print(new_list)

-> 'While' is a loopping process for every time, when you wanna repeat the code, modifying only the arguments. 
![alt text](http://url/to/img.pn
               _________
              |        |
              |        |
              |        |
              |        |
            while      |
              |        |
              |        |
              |________|

```

```
```

```
nums = range(6)
-> range is not a list range(0, 6)

type(nums)
<class 'range'>

nums_list = list(nums)
print(nums_list)
[0, 1, 2, 3, 4, 5]

nums_list2 = [range(1,12,2)]
print(nums_list2)
[range(1, 12, 2)]

nums_list2 = [*range(1,12,2)]
-> [*range(incial,end,steps)]
print(nums_list2)
[1, 3, 5, 7, 9, 11]


```
