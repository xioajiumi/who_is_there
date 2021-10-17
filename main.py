#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Site    : 
# @File    : main.py

import os
from name_store import inputer, reader
from name_parser import parser


def main():
    order = input("是否需要重新输入班级信息（Y/N）：")
    if order in ["y", "Y"]:
        inputer()
    info = parser()
    students = reader()
    for k, v in students.items():
        if k in info:
            print(k, v)


if __name__ == "__main__":
    main()
    os.system("pause")
