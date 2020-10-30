def fourNumberSum(array, targetSum):
  ans=[]
  for i in range(len(array)-3):
    for j in range(i+1,len(array)-2): 
      sum=targetSum-array[i]-array[j]
      temp=array[j+1:]
      temp.sort()
      l=0
      r=len(temp)-1
      while l<r:
        if temp[l]+temp[r]==sum:
          result=[]
          result.append(array[i])
          result.append(array[j])
          result.append(temp[l])
          result.append(temp[r])
          ans.append(result)
          l+=1
          r-=1
        elif temp[l]+temp[r]<sum:
          l+=1
        else:
          r-=1
          
  return ans

  
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  
