import tkinter as tk
from tkinter import ttk, messagebox
import math
import re

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("山哥专用计算器")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # 计算器状态
        self.current_input = ""
        self.result_var = tk.StringVar(value="0")
        self.history = []
        self.just_calculated = False  # 标记是否刚完成计算
        self.decimal_places = 4  # 默认小数位数
        
        # 创建界面
        self.create_widgets()
        
    def create_widgets(self):
        # 主框架
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 显示屏框架
        display_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        display_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 当前输入显示
        self.input_label = tk.Label(display_frame, text="", font=('Arial', 12), 
                                   bg='#34495e', fg='#bdc3c7', anchor='e')
        self.input_label.pack(fill=tk.X, padx=10, pady=(10, 0))
        
        # 结果显示
        result_display = tk.Label(display_frame, textvariable=self.result_var, 
                                 font=('Arial', 24, 'bold'), bg='#34495e', 
                                 fg='#ecf0f1', anchor='e')
        result_display.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # 历史记录框架
        history_frame = tk.Frame(main_frame, bg='#2c3e50')
        history_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # 历史记录标签
        history_label = tk.Label(history_frame, text="历史记录", font=('Arial', 14, 'bold'),
                                bg='#2c3e50', fg='#ecf0f1')
        history_label.pack()
        
        # 历史记录列表框
        self.history_listbox = tk.Listbox(history_frame, font=('Arial', 10),
                                         bg='#34495e', fg='#ecf0f1', 
                                         selectbackground='#3498db',
                                         height=6)
        self.history_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.history_listbox.bind('<Double-Button-1>', self.use_history_item)
        
        # 按钮框架
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(fill=tk.X, pady=(0, 0))
        
        # 设置框架
        settings_frame = tk.Frame(main_frame, bg='#2c3e50')
        settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 小数位数设置
        decimal_label = tk.Label(settings_frame, text="小数位数:", font=('Arial', 12),
                                bg='#2c3e50', fg='#ecf0f1')
        decimal_label.pack(side=tk.LEFT, padx=(5, 5))
        
        self.decimal_var = tk.StringVar(value=str(self.decimal_places))
        decimal_spinbox = tk.Spinbox(settings_frame, from_=0, to=4, width=5,
                                   textvariable=self.decimal_var, font=('Arial', 12),
                                   command=self.update_decimal_places,
                                   bg='#34495e', fg='#ecf0f1', buttonbackground='#3498db')
        decimal_spinbox.pack(side=tk.LEFT, padx=(0, 10))
        
        # 创建按钮
        self.create_buttons(button_frame)
        
    def create_buttons(self, parent):
        # 按钮配置
        button_config = {
            'font': ('Arial', 14, 'bold'),
            'width': 5,
            'height': 2,
            'relief': tk.RAISED,
            'bd': 2
        }
        
        # 数字按钮样式
        number_style = {**button_config, 'bg': '#3498db', 'fg': 'white', 
                       'activebackground': '#2980b9'}
        
        # 运算符按钮样式
        operator_style = {**button_config, 'bg': '#e67e22', 'fg': 'white',
                         'activebackground': '#d35400'}
        
        # 功能按钮样式
        function_style = {**button_config, 'bg': '#95a5a6', 'fg': 'white',
                         'activebackground': '#7f8c8d'}
        
        # 特殊按钮样式
        special_style = {**button_config, 'bg': '#e74c3c', 'fg': 'white',
                        'activebackground': '#c0392b'}
        
        # 按钮布局
        buttons = [
            [('C', special_style, self.clear), ('CE', special_style, self.clear_entry), 
             ('⌫', special_style, self.backspace), ('÷', operator_style, lambda: self.add_operator('/'))],
            [('√', function_style, lambda: self.add_function('sqrt(')), ('x²', function_style, self.square), 
             ('1/x', function_style, self.reciprocal), ('×', operator_style, lambda: self.add_operator('*'))],
            [('7', number_style, lambda: self.add_number('7')), ('8', number_style, lambda: self.add_number('8')), 
             ('9', number_style, lambda: self.add_number('9')), ('-', operator_style, lambda: self.add_operator('-'))],
            [('4', number_style, lambda: self.add_number('4')), ('5', number_style, lambda: self.add_number('5')), 
             ('6', number_style, lambda: self.add_number('6')), ('+', operator_style, lambda: self.add_operator('+'))],
            [('1', number_style, lambda: self.add_number('1')), ('2', number_style, lambda: self.add_number('2')), 
             ('3', number_style, lambda: self.add_number('3')), ('=', operator_style, self.calculate)],
            [('±', function_style, self.toggle_sign), ('0', number_style, lambda: self.add_number('0')), 
             ('.', number_style, lambda: self.add_number('.')), ('清除历史', special_style, self.clear_history)]
        ]
        
        for i, row in enumerate(buttons):
            for j, (text, style, command) in enumerate(row):
                if text == '清除历史':
                    btn = tk.Button(parent, text=text, command=command, **style)
                    btn.grid(row=i, column=j, columnspan=2, sticky='nsew', padx=2, pady=2)
                else:
                    btn = tk.Button(parent, text=text, command=command, **style)
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
        
        # 配置网格权重
        for i in range(6):
            parent.grid_rowconfigure(i, weight=1)
        for j in range(4):
            parent.grid_columnconfigure(j, weight=1)
    
    def add_number(self, number):
        # 如果刚完成计算，清除上一次结果开始新输入
        if self.just_calculated:
            self.current_input = ""
            self.just_calculated = False
        
        if self.current_input == "0" and number != ".":
            self.current_input = number
        else:
            self.current_input += number
        self.update_display()
    
    def add_operator(self, operator):
        # 运算符输入时不清除结果，允许连续计算
        self.just_calculated = False
        if self.current_input and self.current_input[-1] not in "+-*/":
            self.current_input += operator
            self.update_display()
    
    def add_function(self, func):
        self.current_input += func
        self.update_display()
    
    def format_number(self, number):
        """格式化数字显示，控制小数位数"""
        if isinstance(number, (int, float)):
            if self.decimal_places == 0:
                return str(int(round(number)))
            else:
                # 格式化为指定小数位数，去除末尾的0
                formatted = f"{number:.{self.decimal_places}f}"
                # 去除末尾的0和小数点
                formatted = formatted.rstrip('0').rstrip('.')
                return formatted if formatted else '0'
        return str(number)
    
    def update_display(self):
        self.input_label.config(text=self.current_input)
        if self.current_input:
            try:
                # 预览计算结果（不包含未完成的函数）
                if not any(func in self.current_input for func in ['sqrt(', 'sin(', 'cos(', 'tan(']) or self.current_input.count('(') == self.current_input.count(')'):
                    preview = self.safe_eval(self.current_input)
                    if preview is not None:
                        self.result_var.set(self.format_number(preview))
            except:
                pass
    
    def calculate(self):
        if not self.current_input:
            return
        
        try:
            result = self.safe_eval(self.current_input)
            if result is not None:
                # 格式化结果
                formatted_result = self.format_number(result)
                
                # 添加到历史记录
                history_item = f"{self.current_input} = {formatted_result}"
                self.history.append(history_item)
                self.history_listbox.insert(tk.END, history_item)
                
                # 更新显示
                self.result_var.set(formatted_result)
                self.current_input = formatted_result
                self.just_calculated = True  # 标记刚完成计算
                self.update_display()
        except Exception as e:
            messagebox.showerror("错误", f"计算错误: {str(e)}")
    
    def safe_eval(self, expression):
        # 替换显示符号为Python运算符
        expression = expression.replace('×', '*').replace('÷', '/')
        
        # 处理数学函数
        expression = expression.replace('sqrt(', 'math.sqrt(')
        
        # 安全的数学表达式评估
        allowed_names = {
            "__builtins__": {},
            "math": math,
            "abs": abs,
            "round": round,
            "pow": pow
        }
        
        try:
            return eval(expression, allowed_names)
        except:
            return None
    
    def clear(self):
        self.current_input = ""
        self.result_var.set("0")
        self.input_label.config(text="")
        self.just_calculated = False
    
    def clear_entry(self):
        self.current_input = ""
        self.just_calculated = False
        self.update_display()
    
    def backspace(self):
        if self.current_input:
            self.current_input = self.current_input[:-1]
            self.update_display()
    
    def square(self):
        if self.current_input:
            try:
                result = self.safe_eval(self.current_input)
                if result is not None:
                    result = result ** 2
                    formatted_result = self.format_number(result)
                    self.current_input = formatted_result
                    self.just_calculated = True  # 标记刚完成计算
                    self.update_display()
            except:
                messagebox.showerror("错误", "无法计算平方")
    
    def reciprocal(self):
        if self.current_input:
            try:
                result = self.safe_eval(self.current_input)
                if result is not None and result != 0:
                    result = 1 / result
                    formatted_result = self.format_number(result)
                    self.current_input = formatted_result
                    self.just_calculated = True  # 标记刚完成计算
                    self.update_display()
                else:
                    messagebox.showerror("错误", "除零错误")
            except:
                messagebox.showerror("错误", "无法计算倒数")
    
    def toggle_sign(self):
        if self.current_input:
            try:
                result = self.safe_eval(self.current_input)
                if result is not None:
                    result = -result
                    formatted_result = self.format_number(result)
                    self.current_input = formatted_result
                    self.just_calculated = True  # 标记刚完成计算
                    self.update_display()
            except:
                messagebox.showerror("错误", "无法改变符号")
    
    def update_decimal_places(self):
        """更新小数位数设置"""
        try:
            self.decimal_places = int(self.decimal_var.get())
            # 重新格式化当前显示的结果
            if self.result_var.get() != "0":
                try:
                    current_value = float(self.result_var.get())
                    self.result_var.set(self.format_number(current_value))
                except:
                    pass
        except ValueError:
            self.decimal_var.set(str(self.decimal_places))
    
    def clear_history(self):
        self.history.clear()
        self.history_listbox.delete(0, tk.END)
        messagebox.showinfo("提示", "历史记录已清除")
    
    def use_history_item(self, event):
        selection = self.history_listbox.curselection()
        if selection:
            item = self.history_listbox.get(selection[0])
            # 提取表达式部分
            expression = item.split(' = ')[0]
            self.current_input = expression
            self.just_calculated = False  # 重置计算状态
            self.update_display()
    
    def run(self):
        # 键盘绑定
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
        self.root.mainloop()
    
    def on_key_press(self, event):
        key = event.char
        if key.isdigit():
            self.add_number(key)
        elif key in '+-*/':
            self.add_operator(key)
        elif key == '.':
            self.add_number(key)
        elif key == '\r':  # Enter键
            self.calculate()
        elif key == '\x08':  # Backspace键
            self.backspace()
        elif key.lower() == 'c':
            self.clear()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()