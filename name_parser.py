#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Site    : 
# @File    : name_parser.py


def inputer():
    print("复制并粘贴今日未上报的通知信息，然后在末尾换行输入‘ok’\n")
    stopword = 'ok'
    context = ''
    for line in iter(input, stopword):
        context += line + '\n'
    context = context.strip()
    return context


def parser():
    text = inputer()
    text = text.split("单位")[-1].strip()
    return text
