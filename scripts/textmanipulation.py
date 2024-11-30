# This script is to verify all the fields of license file for adapters used in project 
# This script was written by me and hence I am adding it here 
import re
import itertools
import datetime
import sys

#reading the license.txt provided by Avtex
file = open('./license.txt','r')
mylines=list( file)
file.close()
mylines = list(map(lambda a:a.strip(),mylines))
#print(mylines)
  
list2 = []
list3 = []


'''for list in mylines:
  string = list
  list3.append(string.replace("=",","))
  if list == "":
    break

print(list3)'''
#chopping off the key and values from the list
for list in mylines:
  up_to_word = "="
  rx_to_first = r'^.*?{}'.format(re.escape(up_to_word))
  rx_to_last = r'^.*{}'.format(re.escape(up_to_word))
  list2.append(re.sub(rx_to_first,'',list))
  if list == "":
    break
#user input
input1 = input("tenant id:")
input2 = input("primary or backup Adapter:")
#input4 = int(input("Give todays date in the format: 2024,12,9:"))

#print(list2) 

'''def convert(list3):
    res_dict = {}
    for i in range(0, len(list3), 2):
        res_dict[list3[i]] = list3[i + 1]
    return res_dict
print(convert(list3))


df=pd.read_csv('license_old.txt')
print(df)'''

#defining the Key values in separate list
list4 = [ 'Signature','Hostname','NumPlaces','CmeAppName','ExpiryDate','ExpiryTimestamp','WfmVendor','Customer' ]

'''def addyears(d,years):
  try:
      return d.replace(year=d.year + years)
  except ValueError:
      return d + (date(d.year + years, 1, 1) - date(d.year,1,1))
expiry_year = addyears(datetime.date(input4),1)
print(expiry_year)'''

#print(datetime.date.today().year + 1)

#creating dictionary out of two list
dictionary = dict(zip(list4, list2))	
print(f'The Key-value pair of license file is: {dictionary}')
#print(dictionary.keys())
print('The output of the license file analysis as follows:-')
#checking the conditions to match for each of the key in dictionary
dict_values = dictionary.get(list4[0])
if(dict_values.isascii()):
  print("******Signature is valid******.")
else:
  print("==========>Signature is invalid=======>Please take neccessary action.")

dict_values = dictionary.get(list4[1])
#print(dict_values)
input3 = ""
if(input2 == "primary"):
  input3 = ""
elif(input2 == "backup"):
  input3 = "-backup"
 # print(input3)
 # print(f"gpluswfm-{input1}-aspect1{input3}-0")
if(dict_values == f"xyz-{input1}-aspect1{input3}-0"):
  print("******Hostname is valid******.")
else:
  print("==========>Hostname is invalid=======>Please take neccessary action.")	

dict_values = dictionary.get(list4[2])
#print(dict_values)
if(dict_values.isnumeric()):
  print("******Numplaces is valid******.")
else:
  print("==========>Numplaces is invalid=======>Please take neccessary action.")


dict_values = dictionary.get(list4[3])
#print(dict_values)
input3 = ""
if(input2 == "primary"):
  input3 = ""
elif(input2 == "backup"):
  input3 = "-backup"
 # print(input3)
if(dict_values == f"xyz-{input1}-aspect1{input3}"):
  print("******CmeAppName is valid******.")
else:
  print("==========>CmeAppName is invalid=======>Please take neccessary action.")

dict_values = dictionary.get(list4[4])
#print(dict_values)
expiry_year = int(datetime.date.today().year + 1)
exist_dot_pos1 = dict_values.find('.')
exist_dot_pos2 = dict_values.rfind('.')
exist_year = int(dict_values[slice(4)])
exist_month = dict_values[slice(5,8)]
exist_day = dict_values[slice(9,11)]
exist_year_pos = dict_values.rfind(f'{exist_year}')
print(f'The expiry date in license file : year:{exist_year},month:{exist_month},day:{exist_day}')
print(f'Position of year: {exist_year_pos} and  position of dot are {exist_dot_pos1},{exist_dot_pos2}')
if(exist_year_pos != -1 and exist_dot_pos1 == 4 and exist_dot_pos2 == 8 and exist_year >= expiry_year):
  print("******Expirydate is in correct format******.")
else:
  print("==========>Expirydate is not in correct format=======>Please take neccessary action.")

dict_values = dictionary.get(list4[5])
if(dict_values.isnumeric()):
  print("******Timestamp is valid******.")
else:
  print("==========>Timestamp is invalid=======>Please take neccessary action.")

dict_values = dictionary.get(list4[6])
if(dict_values == "Aspect"):
  print("******Wfmvendor is valid******.")
else:
  print("==========>Wfmvendor is invalid.")

dict_values = dictionary.get(list4[7])
if(dict_values == "Amazon"):
  print("******Customer is valid******.")
else:
  print("==========>Customer is invalid=======>Please take neccessary action.")