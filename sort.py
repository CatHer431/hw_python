def sort_list(oneList):
 n=len(oneList)
 i=0
 while i<n:
  j=0
  while j<n-i-1:
   if oneList[j]>oneList[j+1]:
    temp=oneList[j]
    oneList[j]=oneList[j+1]
    oneList[j+1]=temp
   j=j+1
  i=i+1
 return oneList

x=[1,3,2,7]
print(sort_list(x))
