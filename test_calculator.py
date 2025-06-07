#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
计算器功能测试脚本
用于验证计算器的各项功能是否正常工作
"""

import sys
import math
from calculator import Calculator

def test_safe_eval():
    """测试安全计算功能"""
    print("\n=== 测试安全计算功能 ===")
    calc = Calculator()
    
    test_cases = [
        ("2+3", 5),
        ("10-4", 6),
        ("6*7", 42),
        ("15/3", 5),
        ("2.5+3.7", 6.2),
        ("math.sqrt(16)", 4.0),
        ("2**3", 8),
        ("abs(-5)", 5),
        ("round(3.14159, 2)", 3.14)
    ]
    
    passed = 0
    total = len(test_cases)
    
    for expression, expected in test_cases:
        try:
            result = calc.safe_eval(expression)
            if abs(result - expected) < 0.0001:  # 浮点数比较
                print(f"✅ {expression} = {result} (期望: {expected})")
                passed += 1
            else:
                print(f"❌ {expression} = {result} (期望: {expected})")
        except Exception as e:
            print(f"❌ {expression} 出错: {e}")
    
    print(f"\n安全计算测试结果: {passed}/{total} 通过")
    return passed == total

def test_error_handling():
    """测试错误处理"""
    print("\n=== 测试错误处理 ===")
    calc = Calculator()
    
    error_cases = [
        "1/0",  # 除零错误
        "math.sqrt(-1)",  # 负数开方
        "invalid_expression",  # 无效表达式
        "2+",  # 不完整表达式
        "(2+3",  # 括号不匹配
    ]
    
    passed = 0
    total = len(error_cases)
    
    for expression in error_cases:
        try:
            result = calc.safe_eval(expression)
            if result is None:
                print(f"✅ {expression} 正确返回 None")
                passed += 1
            else:
                print(f"❌ {expression} 应该返回 None，但返回了 {result}")
        except Exception as e:
            print(f"✅ {expression} 正确抛出异常: {type(e).__name__}")
            passed += 1
    
    print(f"\n错误处理测试结果: {passed}/{total} 通过")
    return passed == total

def test_display_conversion():
    """测试显示符号转换"""
    print("\n=== 测试显示符号转换 ===")
    calc = Calculator()
    
    conversion_cases = [
        ("2×3", "2*3", 6),
        ("10÷2", "10/2", 5),
        ("5×6÷2", "5*6/2", 15),
    ]
    
    passed = 0
    total = len(conversion_cases)
    
    for display_expr, python_expr, expected in conversion_cases:
        try:
            result = calc.safe_eval(display_expr)
            if abs(result - expected) < 0.0001:
                print(f"✅ {display_expr} -> {python_expr} = {result}")
                passed += 1
            else:
                print(f"❌ {display_expr} = {result} (期望: {expected})")
        except Exception as e:
            print(f"❌ {display_expr} 出错: {e}")
    
    print(f"\n符号转换测试结果: {passed}/{total} 通过")
    return passed == total

def test_mathematical_functions():
    """测试数学函数"""
    print("\n=== 测试数学函数 ===")
    calc = Calculator()
    
    math_cases = [
        ("math.sqrt(25)", 5.0),
        ("math.sqrt(2)", math.sqrt(2)),
        ("pow(2, 3)", 8),
        ("abs(-10)", 10),
        ("round(3.14159, 3)", 3.142),
    ]
    
    passed = 0
    total = len(math_cases)
    
    for expression, expected in math_cases:
        try:
            result = calc.safe_eval(expression)
            if abs(result - expected) < 0.0001:
                print(f"✅ {expression} = {result}")
                passed += 1
            else:
                print(f"❌ {expression} = {result} (期望: {expected})")
        except Exception as e:
            print(f"❌ {expression} 出错: {e}")
    
    print(f"\n数学函数测试结果: {passed}/{total} 通过")
    return passed == total

def test_complex_expressions():
    """测试复杂表达式"""
    print("\n=== 测试复杂表达式 ===")
    calc = Calculator()
    
    complex_cases = [
        ("2+3*4", 14),  # 运算优先级
        ("(2+3)*4", 20),  # 括号
        ("2**3+1", 9),  # 幂运算
        ("math.sqrt(16)+2*3", 10.0),  # 函数和运算混合
        ("abs(-5)+math.sqrt(9)", 8.0),  # 多个函数
    ]
    
    passed = 0
    total = len(complex_cases)
    
    for expression, expected in complex_cases:
        try:
            result = calc.safe_eval(expression)
            if abs(result - expected) < 0.0001:
                print(f"✅ {expression} = {result}")
                passed += 1
            else:
                print(f"❌ {expression} = {result} (期望: {expected})")
        except Exception as e:
            print(f"❌ {expression} 出错: {e}")
    
    print(f"\n复杂表达式测试结果: {passed}/{total} 通过")
    return passed == total

def run_all_tests():
    """运行所有测试"""
    print("开始计算器功能测试...")
    print("=" * 50)
    
    tests = [
        test_safe_eval,
        test_error_handling,
        test_display_conversion,
        test_mathematical_functions,
        test_complex_expressions
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test_func in tests:
        if test_func():
            passed_tests += 1
    
    print("\n" + "=" * 50)
    print(f"总体测试结果: {passed_tests}/{total_tests} 测试组通过")
    
    if passed_tests == total_tests:
        print("🎉 所有测试通过！计算器功能正常。")
        return True
    else:
        print("⚠️  部分测试失败，请检查计算器实现。")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)