# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# import csv
# with open('ciphertext.txt', 'r') as myCipther:
#     lines = csv.DictReader(myCipther, delimiter=',')
#     for line in lines:
#         print(lines)

with open('ciphertext.txt') as file:
    ciphertext = file.read()
c_key = {
     'E' : 'W',
     'T' : 'J',
     'A' : 'M',
     'O' : 'X',
     'H' : 'C',
     'N' : 'D',
     'R' : 'K',
     'I' : 'I',
     'S' : 'N',
     'D' : 'U',
     'L' : 'S',
     'W' : 'O',
     'U' : 'G',
     'G' : 'Q',
     'F' : 'B',
     'B' : 'Y',
     'M' : 'E',
     'Y' : 'F',
     'C' : 'A',
     'P' : 'Z',
     'K' : 'P',
     'V' : 'H',
     'Q' : 'V',
     'J' : 'T',
     'X' : 'L',
     'Z' : 'R'
}

decode_table = {value:key for key, value in c_key.items()}

# 1st PASS:
def decrypt(s):
    res = ''

    for c in s:
        c = c.upper()

        if c.isalpha():
            res += decode_table[c]
        else:
            res += c

    return res

print(decrypt(ciphertext))


# 2nd PASS
# 
# from collections import defaultdict

# counts = defaultdict(int)

# for c in ciphertext:
#     if c.isupper():
#         counts[c] += 1

# freq_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
#              'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# cipher_freq = [item[0] for item in sorted(counts.items(),
#                                           key=lambda x: x[1],
#                                           reverse=True)]

# lookup = {cipher: plain for cipher, plain in zip(cipher_freq, freq_list)}
# print(f'FREQ LIST {cipher_freq}')
# # print(ciphertext.translate(str.maketrans(lookup)))


