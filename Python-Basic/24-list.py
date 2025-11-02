# daripada menuliskan 

angka1 = 10
angka2 = 20

# sangat rumit, makanya dibuatlah list

## 1. list angka ##
number_data = [10, 20, 30, 40, 50]

## 2. String ##
str_data = ['arwanzxp', 'yudi', 'rahman']

## 3. Random data ##
rndm_data = [1, "Arwanzxp", True, 10.29]


## automatic step for create list

list_range = range(1,10) # start and stop
list_range2 = range(1, 20, 3) # start, stop step
print(list(list_range))
print(list(list_range2))

print('\n')
## create list with for loop 
## LIST COMPREHENSIV
list_used_for = [i for i in range(1,10)]
print(list_used_for)

# urutan
# var for i in range
list_used_for = [i**2 for i in range(1, 10)] #
print(list_used_for)

## for and if
# delete number 5 in the list
list_usef_for_if = [i for i in range(1, 20) if i != 5]
print(list_usef_for_if)

list_usef_for_if = [i**2 for i in range(1, 10) if i % 2 == 0]
print(list_usef_for_if)

