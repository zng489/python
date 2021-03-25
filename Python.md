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


```
# Rewrite the for loop to use enumerate
indexed_names = []

for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

index_name 
[(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]
(4, 'Newman')

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)
[(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)
[(1, 'Jerry'), (2, 'Kramer'), (3, 'Elaine'), (4, 'George'), (5, 'Newman')]
```

```
```

```
# 2-D list
nums2 = [[1,2,3], [4,5,6]]

             Columns
           [0] [1] [2]
 Rows  [0]  3   1   4
       [1]  1   5   9

nums2 = [[1,2,3], [4,5,6]]
nums2[0][1]
2
```
