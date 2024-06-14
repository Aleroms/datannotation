# psuedo code
# create list and object
# open file
# split line and extract number and word
# put word and number into object
# and put number as int in list
# sort list in ascending order
# use sorted_list to create pyramid of numbers
# extract last number of each pyramid level and
# join

# FILE_PATH = './coding_qual_input.txt'


def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    number_word = {}
    for line in lines:
        number, word = line.split()
        number_word[int(number)] = word

    current_number = 1
    end_nums = []
    row_len = 1

    while current_number in number_word:
        end = current_number + row_len - 1
        if end in number_word:
            end_nums.append(end)
        
        current_number += row_len
        row_len += 1
    
    result = " ".join(number_word[num] for num in end_nums)
    return result
