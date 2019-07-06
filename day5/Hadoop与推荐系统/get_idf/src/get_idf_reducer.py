#!/usr/bin/env python
#coding=utf-8
import sys
import os
#输出唯一的ans

current_word = None
current_word_value_list = []


def process_value_list(value_list):
    value = 0
    for item in value_list:
        value += int(item)
    return str(value)


for line in sys.stdin:
    line = line.strip()
    word,count = line.split("\t")

    if current_word == word:#如果词没有变，则累加
        current_word_value_list.append(count)
    else:#如果词发生变化了,则输出
        if current_word != None:
            #如果读的是第一行，和 None不一致,但不输出，不是第一行才输出
            #输出上一个词
            value = process_value_list(current_word_value_list)
            print(current_word + "\t" + value)
        #初始化current_word，current_count为当前词
        current_word = word
        current_word_value_list = []
        current_word_value_list.append(count)

#最后一行处理，如果是和前面一行的词，后续没有词了，则前面没有输出
if current_word:
    value = process_value_list(current_word_value_list)
    print(current_word + "\t" + value)
