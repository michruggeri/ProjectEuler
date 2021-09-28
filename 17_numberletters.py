#!/usr/bin/env python3

"""
Project Euler, problem 17
 
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with 
British usage.

"""
tens = {9:'ninety', 8:'eighty', 7:'seventy',6:'sixty',5:'fifty',4:'forty',3:'thirty',2:'twenty'}
nbase = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'',10:'ten',11:'eleven',12:'twelve',
        13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
def num_to_word(num):
    word = ''
    if num > 999:
        word += nbase[num//1000] + 'thousand'
        num = num % 1000
    if num > 99:
        word += nbase[num//100] + 'hundred'
        if num % 100 != 0:
            word += 'and'
        num = num % 100
    if num > 19:
        word += tens[num//10]
        word += nbase[num%10]
    else:
        word += nbase[num]
    return word

total = 0
for i in range(1,1001):
    total += len(num_to_word(i))
print(total)
