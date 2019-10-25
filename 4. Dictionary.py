#Creating a dictionary:

# First way
dictionary = {'key_1': 1, 'key_2': 2}
# Second way
dictionary = {}
dictionary['key_1'] = 1
dictionary['key_2'] = 2

#Retrieving individual dictionary values:

dictionary = {'key_1': 100, 'key_2': 200}
dictionary['key_1']  # Outputs 100
dictionary['key_2']  # Outputs 200

#Checking whether a certain value exist in the dictionary as a key:

dictionary = {'key_1': 100, 'key_2': 200}
'key_1' in dictionary  # Outputs True
'key_5' in dictionary  # Outputs False
100 in dictionary  # Outputs False

#Updating dictionary values:

dictionary = {'key_1': 100, 'key_2': 200}
dictionary['key_1'] += 600  # This will change the value to 700

#Creating a frequency table for the unique values in a column of a data set:

frequency_table = {}
for row in a_data_set:
    a_data_point = row[5]
    if a_data_point in frequency_table:
        frequency_table[a_data_point] += 1
    else:
        frequency_table[a_data_point] = 1
        
#Creating a function with a single parameter:

def square(number):
    return number**2

#Creating a function with more than one parameter:

def add(x, y):
    return x + y

#Reusing a function within another function's definition:

def add_to_square(x):
    return square(x) + 1000  # we defined square() above