def interSection(arr1,arr2): # finding common elements

# using filter method to find identical values via lambda function
values = list(filter(lambda x: x in arr1, arr2))
print ("Intersection of arr1 & arr2 is: ",values)

# Driver program
if __name__ == "__main__":
   arr1 = ['t','u','t','o','r','i','a','l']
   arr2 = ['p','o','i','n','t']
   interSection(arr1,arr2)