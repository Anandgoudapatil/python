def cap(ele):
 ele2=ele.upper()
 if(ele2[0]=='C'):
    return True
print("Enter a no of element of list = ")
n=int(input())
listc=[]
for i in range(0,n):
  ele=input()
  listc.append(ele)
print(listc)
list2=list(filter(cap,listc))
print(list2)
  
