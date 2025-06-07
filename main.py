#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Android计算器应用入口文件
buildozer会寻找main.py作为应用入口
"""

from calculator_mobile import CalculatorApp

if __name__ == '__main__':
    CalculatorApp().run()