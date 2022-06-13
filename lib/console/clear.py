"""Simple clear function"""

def clear():
    import sys
    from .execute import execute_command
    if sys.platform == "win32" or sys.platform == "win64":
        execute_command("cls")
    else:
        execute_command("clear")
