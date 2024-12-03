def interSection(arr1,arr2): # finding common elements

# using filter method to find identical values via lambda function
    values = list(filter(lambda x: x in arr1, arr2))
    print ("Intersection of arr1 & arr2 is: ",values)


if __name__ == "__main__":
   arr1 = [26,4,56,8,9,10,1]
   arr1.sort()
   print('First array: ',arr1)
   arr2 = [1,56,9,11,8,0]
   arr2.sort()
   print('Second array:' arr2)
   interSection(arr1,arr2)