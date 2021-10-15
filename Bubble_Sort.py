def Bubble_Sort(lst):
    N = len(lst)

    for i in range(0,N):
        for j in range(0,N-i-1):
            if(lst[j] > lst[j+1]):
                lst[j],lst[j+1] = lst[j+1],lst[j]

    return lst

print('Enter the Elements')
my_lst = [int(ele) for ele in input().split()]

print('Unsorted Elements',my_lst)
print('Sorted Elements',Bubble_Sort(my_lst))
