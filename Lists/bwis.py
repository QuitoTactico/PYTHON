def suma(i,nums,k):
    if(k==0):
        return ("YES")
    if(k<0 or i>= len(nums)):
        return ("NO")
    return(suma (i+1,nums,k-nums[i])or suma(i+1,nums,k))
recib=list(input())
j,k = map(int,input().split())
i=0
nums=list(input())
print(suma(i,nums,k))