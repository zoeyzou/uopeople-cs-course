
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
      print(letter + suffix)

print('------------------- this is a seperator ---------------------')
# Give at least three examples that show different features of string slices. Describe the feature illustrated by each example. 
str = 'clearly this is a string'
print('the value of str: ' + str)

# Basic feature of string slices: use [n:m] to select a slice of a string from index n to m, including n but excluding m

# when the both n and m are given values, it will select characters from index n to m
print('result of str[8:12]: ')
print(str[8:12]) # output: this

# when n is omitted, it selects from index 0 to index m (excluding m)
print('result of str[:12]: ')
print(str[:12])

# when m is ommited, it selects from index n to the last index of the string
print('result of str[8:]: ')
print(str[8:])

# when both m and n are omitted, it selects the whole string
print('result of str[:]: ')
print(str[:])