#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator App - Main Entry Point.

This is the main entry point for the Calculator App.
Buildozer looks for main.py as the application entry point.

Author: Calculator App Team
License: MIT
"""

from typing import NoReturn

from calculator_mobile import CalculatorApp


def main() -> NoReturn:
    """Main function to start the Calculator App.
    
    This function creates and runs the Calculator App instance.
    It serves as the entry point for the application.
    
    Raises:
        SystemExit: When the application is closed.
    """
    app = CalculatorApp()
    app.run()


if __name__ == '__main__':
    main()