def Binary_Search(lst,l,r,ele):
    if(l<=r):
        mid = l + (r-l)//2

        if(lst[mid] == ele):
            return mid

        elif(lst[mid] >= ele):
            return Binary_Search(lst,l,mid-1,ele)

        else:
            return Binary_Search(lst,mid+1,r,ele)

    return -1

print('Enter the Size of the LIST')
N = int(input())

print('Enter the List')
my_lst = [int(k) for k in input().split()][:N]

print('Your List:', my_lst)

my_lst = sorted(my_lst)
print('Enter the Value to be Searched')

ele = int(input())
result = Binary_Search(my_lst,0,N-1,ele)

if(result == -1):
    print('Element not found')

else:
    print('Element Found')
