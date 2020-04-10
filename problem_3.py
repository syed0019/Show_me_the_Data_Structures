import sys

def huffman_encoding(data):
    # if length of string is zero
    if len(data) == 0:
        print("Empty string. Include non-null string")
        return
    # generating frequency of the characters in string
    dict_freq = {}
    count = 1
    for char in data:
        if char in dict_freq:
            dict_freq[char] += count
        else:
            dict_freq[char] = count
    # converting the dictionary into list of frequency tuples
    list_ = []
    for items in dict_freq.items():
        list_.append(items)
    # sorting list of tuples based on the counts in ascending order
    charac_tuples = sorted(list_, key = lambda x: x[1], reverse=False)
    # making tree based on the frequency of the characters
    tree_dict = {}
    zero = '0'
    bin_str = '1'
    # iterating through tuples to create dictionary of binary tree (0,1)
    for tup in charac_tuples:
        tree_dict[tup[0]] = bin_str
        bin_str = zero + bin_str
    # generating encoded string and tree
    encoded_data = ''
    for str_ in data:
        encoded_data += tree_dict[str_]
    return encoded_data, tree_dict    


def huffman_decoding(data, tree):
    empty_str = ''  
    decoded_str = '' 
    reversed_tree_dict = {}  
    # iterating through tree to create reversed tree dictionary
    for char in tree:
        reversed_tree_dict[tree[char]] = char
    # iterating through encoded data to decode using characters in reversed tree dictionary
    for bin_num in data:
        if bin_num == '0':
            empty_str += bin_num
        else:
            decoded_str += reversed_tree_dict[empty_str + bin_num]
            empty_str = ''
    return decoded_str    

##### Test Cases ######

if __name__ == "__main__":
    codes = {}
    
    print('Test Case 1:')
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print('\n')
    
    print('Test Case 2:')
    test_sentence_2 = "yyyy"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence_2)))
    print ("The content of the data is: {}\n".format(test_sentence_2))

    encoded_data, tree = huffman_encoding(test_sentence_2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print('\n')
 
    print('Test Case 3:')
    test_sentence_3 = "ABccdddeeee"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence_3)))
    print ("The content of the data is: {}\n".format(test_sentence_3))

    encoded_data, tree = huffman_encoding(test_sentence_3)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print('\n')
    
    print('Test Case 4:')
    test_sentence_4 = "I am enjoying the course"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence_4)))
    print ("The content of the data is: {}\n".format(test_sentence_4))

    encoded_data, tree = huffman_encoding(test_sentence_4)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    print('\n')
    
    print('Test Case 5:')
    test_sentence_5 = ''

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence_5)))
    print ("The content of the data is: {}\n".format(test_sentence_5))
    huffman_encoding(test_sentence_5)

    
    
################ Expected Output ################

# Test Case 1:
# The size of the data is: 69

# The content of the data is: The bird is the word

# The size of the encoded data is: 48

# The content of the encoded data is: 100000010000000100000000000101000000001000000000100000000001000000000001000000001001000000000001000100000010000000100000000000100001000001000000000100000000001

# The size of the decoded data is: 69

# The content of the encoded data is: The bird is the word



# Test Case 2:
# The size of the data is: 53

# The content of the data is: yyyy

# The size of the encoded data is: 28

# The content of the encoded data is: 1111

# The size of the decoded data is: 53

# The content of the encoded data is: yyyy



# Test Case 3:
# The size of the data is: 60

# The content of the data is: ABccdddeeee

# The size of the encoded data is: 32

# The content of the encoded data is: 10100100100010001000100001000010000100001

# The size of the decoded data is: 60

# The content of the encoded data is: ABccdddeeee



# Test Case 4:
# The size of the data is: 73

# The content of the data is: I am enjoying the course

# The size of the encoded data is: 60

# The content of the encoded data is: 1000000000000000010100100000000000000001000000000000000100000000000001000100000000000000100001000001000000000000010000001000000000000000010000000100000000100000000000000010000000000000000100000000010000000000000010000000000100000000000100000000000010000000000000001

# The size of the decoded data is: 73

# The content of the encoded data is: I am enjoying the course


# Test Case 5:
# The size of the data is: 49

# The content of the data is: 

# Empty string. Include non-null string