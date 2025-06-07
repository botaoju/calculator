#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
移动端计算器 - 适配Android平台
基于Kivy框架开发，支持触摸操作
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
import math
import re

class CalculatorApp(App):
    def build(self):
        self.title = '科学计算器'
        
        # 设置窗口背景色
        Window.clearcolor = (0.17, 0.24, 0.31, 1)  # #2c3e50
        
        # 计算器状态
        self.current_input = ""
        self.history = []
        self.just_calculated = False
        self.decimal_places = 4
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 显示区域
        display_layout = BoxLayout(orientation='vertical', size_hint_y=0.3, spacing=5)
        
        # 输入显示
        self.input_label = Label(
            text='0',
            font_size='18sp',
            color=(0.93, 0.94, 0.95, 1),  # #ecf0f1
            text_size=(None, None),
            halign='right'
        )
        display_layout.add_widget(self.input_label)
        
        # 结果显示
        self.result_label = Label(
            text='0',
            font_size='32sp',
            color=(0.93, 0.94, 0.95, 1),
            text_size=(None, None),
            halign='right',
            bold=True
        )
        display_layout.add_widget(self.result_label)
        
        main_layout.add_widget(display_layout)
        
        # 设置区域
        settings_layout = BoxLayout(orientation='horizontal', size_hint_y=0.08, spacing=10)
        
        decimal_label = Label(
            text='小数位数:',
            font_size='16sp',
            color=(0.93, 0.94, 0.95, 1),
            size_hint_x=0.4
        )
        settings_layout.add_widget(decimal_label)
        
        self.decimal_spinner = Spinner(
            text=str(self.decimal_places),
            values=['0', '1', '2', '3', '4'],
            size_hint_x=0.2,
            font_size='16sp'
        )
        self.decimal_spinner.bind(text=self.update_decimal_places)
        settings_layout.add_widget(self.decimal_spinner)
        
        # 历史记录按钮
        history_btn = Button(
            text='历史',
            size_hint_x=0.2,
            font_size='16sp',
            background_color=(0.52, 0.73, 0.4, 1)  # #85bb65
        )
        history_btn.bind(on_press=self.show_history)
        settings_layout.add_widget(history_btn)
        
        # 清除历史按钮
        clear_history_btn = Button(
            text='清除历史',
            size_hint_x=0.2,
            font_size='16sp',
            background_color=(0.91, 0.3, 0.24, 1)  # #e74c3c
        )
        clear_history_btn.bind(on_press=self.clear_history)
        settings_layout.add_widget(clear_history_btn)
        
        main_layout.add_widget(settings_layout)
        
        # 按钮区域
        button_layout = GridLayout(cols=5, spacing=5, size_hint_y=0.62)
        
        # 按钮配置
        buttons = [
            # 第一行 - 函数按钮
            ('sin', self.add_function), ('cos', self.add_function), ('tan', self.add_function), ('√', self.add_function), ('C', self.clear),
            # 第二行 - 操作按钮
            ('(', self.add_operator), (')', self.add_operator), ('x²', self.square), ('1/x', self.reciprocal), ('CE', self.clear_entry),
            # 第三行 - 数字和运算符
            ('7', self.add_number), ('8', self.add_number), ('9', self.add_number), ('÷', self.add_operator), ('±', self.toggle_sign),
            # 第四行
            ('4', self.add_number), ('5', self.add_number), ('6', self.add_number), ('×', self.add_operator), ('%', self.add_operator),
            # 第五行
            ('1', self.add_number), ('2', self.add_number), ('3', self.add_number), ('-', self.add_operator), ('π', self.add_constant),
            # 第六行
            ('0', self.add_number), ('.', self.add_number), ('=', self.calculate), ('+', self.add_operator), ('e', self.add_constant),
        ]
        
        for text, callback in buttons:
            btn = Button(
                text=text,
                font_size='20sp',
                bold=True
            )
            
            # 设置按钮颜色
            if text in ['C', 'CE']:
                btn.background_color = (0.91, 0.3, 0.24, 1)  # 红色
            elif text in ['=']:
                btn.background_color = (0.2, 0.6, 0.86, 1)  # 蓝色
            elif text in ['+', '-', '×', '÷', '%', '±', 'x²', '1/x', '(', ')']:
                btn.background_color = (0.2, 0.29, 0.37, 1)  # 深灰色
            elif text in ['sin', 'cos', 'tan', '√', 'π', 'e']:
                btn.background_color = (0.61, 0.35, 0.71, 1)  # 紫色
            else:
                btn.background_color = (0.44, 0.5, 0.56, 1)  # 浅灰色
            
            btn.bind(on_press=lambda x, t=text, c=callback: c(t))
            button_layout.add_widget(btn)
        
        main_layout.add_widget(button_layout)
        
        return main_layout
    
    def format_number(self, number):
        """格式化数字显示"""
        if isinstance(number, (int, float)):
            if self.decimal_places == 0:
                return str(int(round(number)))
            else:
                formatted = f"{number:.{self.decimal_places}f}"
                formatted = formatted.rstrip('0').rstrip('.')
                return formatted if formatted else '0'
        return str(number)
    
    def update_display(self):
        """更新显示"""
        self.input_label.text = self.current_input if self.current_input else '0'
        
        if self.current_input:
            try:
                if not any(func in self.current_input for func in ['sqrt(', 'sin(', 'cos(', 'tan(']) or self.current_input.count('(') == self.current_input.count(')'):
                    preview = self.safe_eval(self.current_input)
                    if preview is not None:
                        self.result_label.text = self.format_number(preview)
            except:
                pass
        else:
            self.result_label.text = '0'
    
    def add_number(self, number):
        """添加数字"""
        if self.just_calculated:
            self.current_input = ""
            self.just_calculated = False
        
        self.current_input += number
        self.update_display()
    
    def add_operator(self, operator):
        """添加运算符"""
        if self.just_calculated:
            self.just_calculated = False
        
        # 转换显示符号为计算符号
        operator_map = {'×': '*', '÷': '/', '%': '%'}
        calc_operator = operator_map.get(operator, operator)
        
        self.current_input += calc_operator
        self.update_display()
    
    def add_function(self, func):
        """添加函数"""
        if self.just_calculated:
            self.current_input = ""
            self.just_calculated = False
        
        func_map = {
            'sin': 'sin(',
            'cos': 'cos(',
            'tan': 'tan(',
            '√': 'sqrt('
        }
        
        if func in func_map:
            self.current_input += func_map[func]
            self.update_display()
    
    def add_constant(self, constant):
        """添加常数"""
        if self.just_calculated:
            self.current_input = ""
            self.just_calculated = False
        
        if constant == 'π':
            self.current_input += str(math.pi)
        elif constant == 'e':
            self.current_input += str(math.e)
        
        self.update_display()
    
    def calculate(self, *args):
        """执行计算"""
        if self.current_input:
            result = self.safe_eval(self.current_input)
            if result is not None:
                formatted_result = self.format_number(result)
                
                # 添加到历史记录
                history_item = f"{self.current_input} = {formatted_result}"
                self.history.append(history_item)
                
                # 更新显示
                self.result_label.text = formatted_result
                self.current_input = formatted_result
                self.just_calculated = True
                self.update_display()
    
    def safe_eval(self, expression):
        """安全计算表达式"""
        try:
            # 替换函数名
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            
            # 安全的命名空间
            safe_dict = {
                '__builtins__': {},
                'math': math
            }
            
            result = eval(expression, safe_dict)
            return result
        except:
            return None
    
    def clear(self, *args):
        """清除所有"""
        self.current_input = ""
        self.result_label.text = '0'
        self.just_calculated = False
        self.update_display()
    
    def clear_entry(self, *args):
        """清除当前输入"""
        if self.current_input:
            self.current_input = self.current_input[:-1]
            self.just_calculated = False
            self.update_display()
    
    def square(self, *args):
        """平方运算"""
        if self.current_input:
            result = self.safe_eval(self.current_input)
            if result is not None:
                result = result ** 2
                formatted_result = self.format_number(result)
                self.current_input = formatted_result
                self.just_calculated = True
                self.update_display()
    
    def reciprocal(self, *args):
        """倒数运算"""
        if self.current_input:
            result = self.safe_eval(self.current_input)
            if result is not None and result != 0:
                result = 1 / result
                formatted_result = self.format_number(result)
                self.current_input = formatted_result
                self.just_calculated = True
                self.update_display()
    
    def toggle_sign(self, *args):
        """正负号切换"""
        if self.current_input:
            result = self.safe_eval(self.current_input)
            if result is not None:
                result = -result
                formatted_result = self.format_number(result)
                self.current_input = formatted_result
                self.just_calculated = True
                self.update_display()
    
    def update_decimal_places(self, spinner, text):
        """更新小数位数"""
        try:
            self.decimal_places = int(text)
            if self.result_label.text != '0':
                try:
                    current_value = float(self.result_label.text)
                    self.result_label.text = self.format_number(current_value)
                except:
                    pass
        except ValueError:
            pass
    
    def show_history(self, *args):
        """显示历史记录"""
        if self.history:
            history_text = '\n'.join(self.history[-10:])  # 显示最近10条
            print(f"计算历史:\n{history_text}")
        else:
            print("暂无计算历史")
    
    def clear_history(self, *args):
        """清除历史记录"""
        self.history.clear()
        print("历史记录已清除")

if __name__ == '__main__':
    CalculatorApp().run()