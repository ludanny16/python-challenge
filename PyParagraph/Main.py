#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:27:37 2017

@author: chao_lu
"""


#Read Text File 1
with open('paragraph_1.txt', 'r') as file:
    file_contents = file.read()

# Define global variable
num_words=len(file_contents.split())
num_sent=file_contents.count('.')
num_letter=0

# Use Loop to find number of letter
for line in file_contents:
        wordlist=line.split()
        num_letter+= len(line)

# Calculation 
average_sentence=round(float(num_words)/float(num_sent),2)

average_letters=(float(num_letter)/float(num_words))

#Output
print("----------------")
print("Paragrah Analysis #1")
print("----------------")
print("Approximate Word Count:", num_words)
print("Approximate Sentence Count:", num_sent)
print("Average Letter Count:", average_letters)
print("Average Sentence Length:", average_sentence,)
print("----------------")




#Read Text File 2
with open('paragraph_2.txt', 'r') as file:
    file_contents = file.read()

# Define global variable
num_words=len(file_contents.split())
num_sent=file_contents.count('.')
num_letter=0

# Use Loop to find number of letter
for line in file_contents:
        wordlist=line.split()
        num_letter+= len(line)

# Calculation 
average_sentence=round(float(num_words)/float(num_sent),2)

average_letters=(float(num_letter)/float(num_words))

#Output
print("Paragrah Analysis #2")
print("----------------")
print("Approximate Word Count:", num_words)
print("Approximate Sentence Count:", num_sent)
print("Average Letter Count:", average_letters)
print("Average Sentence Length:", average_sentence)