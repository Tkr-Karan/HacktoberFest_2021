def Selection_Sort(lst):
    for i in range(0,len(lst)):
        min_idx = i
        for j in range(i+1,len(lst)):
            if(lst[min_idx] > lst[j]):
                min_idx = j
        
        lst[i],lst[min_idx] = lst[min_idx],lst[i]
    
    return lst

print('Enter the Elements')
my_lst = [int(ele) for ele in input().split()]

print('Unsorted Elements',my_lst)
print('Sorted Elements',Selection_Sort(my_lst))
