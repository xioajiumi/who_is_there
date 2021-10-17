#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Site    : 
# @File    : name_store.py
import os
import json

cwd = os.getcwd()


def writer(dict_data):
    with open(cwd + "\\stu_info.json", "w", encoding="UTF-8") as file:
        json_data = json.dump(dict_data, file)


def inputer():
    print("请以‘2019xxxxxxxxxx XXX’的格式输入学生信息\n退出请回车或输入‘可以了’", )
    data = {}
    while True:
        text = input()
        if text not in ["可以了", ""]:
            id, name = text.split()
            data[id] = name
        else:
            break
    writer(data)


def reader():
    with open(cwd + "\\stu_info.json", "r", encoding="UTF-8") as file:
        dict_data = json.load(file)
        return dict_data
