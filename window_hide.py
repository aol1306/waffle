import win32gui

def enum_windows_callback(hwnd, windowList):
    text = win32gui.GetWindowText(hwnd)
    className = win32gui.GetClassName(hwnd)
    if className == "ConsoleWindowClass":
        windowList.append((hwnd, text, className))

def hide_console_window():
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    win32gui.ShowWindow(windows[0][0], False)