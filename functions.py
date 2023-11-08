import psutil
import time
import sys
import subprocess
import os
import ctypes
import pygetwindow as gw
import automation



both_clients_running = True
directory = r'D:\P99'
command = ['cmd', '/c', 'start', 'eqgame.exe', 'patchme']

def title_change(server):
    HWND_BROADCAST = 0xFFFF
    WM_SETTEXT = 0x000C
    hwnd = ctypes.windll.user32.FindWindowW(None, "Everquest")
    ctypes.windll.user32.SendMessageW(hwnd, WM_SETTEXT, 0, server)
def client_launch():
    global both_clients_running
    subprocess.Popen(command, cwd=directory)
    time.sleep(6)
    title_change('Blue')
    move_window('Blue')

    time.sleep(2)
    call_login("Blue")

    subprocess.Popen(command, cwd=directory)
    time.sleep(8)
    title_change('Green')
    move_window('Green')
    call_login("Green")


def move_window(color):
    app = gw.getWindowsWithTitle(color)
    window = app[0]
    window.moveTo(0, 0)

def call_login(color):
    automation.login(color)

def client_launch_single(color):
    subprocess.Popen(command, cwd=directory)
    time.sleep(6)
    title_change(color)
    move_window(color)
    call_login(color)

def client_alive_check(title):
    alive = ctypes.windll.user32.FindWindowW(None, title)
    return bool(alive)

def kill_clients_single(color):
    print("Kill Clients Called.")
    if color == "Blue":
        blue_hwnd = ctypes.windll.user32.FindWindowW(None, "Blue")
        ctypes.windll.user32.PostMessageW(blue_hwnd, 0x0010, 0, 0)

    else:
        green_hwnd = ctypes.windll.user32.FindWindowW(None, "Green")
        ctypes.windll.user32.PostMessageW(green_hwnd, 0x0010, 0, 0)

def kill_clients_all():
    print("Kill Clients Called.")

    blue_hwnd = ctypes.windll.user32.FindWindowW(None, "Blue")
    green_hwnd = ctypes.windll.user32.FindWindowW(None, "Green")

    if blue_hwnd != 0:
        ctypes.windll.user32.PostMessageW(blue_hwnd, 0x0010, 0, 0)  # 0x0010 is the code for WM_CLOSE
    else:
        print("Blue window not found.")

    if green_hwnd != 0:
        ctypes.windll.user32.PostMessageW(green_hwnd, 0x0010, 0, 0)  # 0x0010 is the code for WM_CLOSE
    else:
        print("Green window not found.")

def error_window():
    if ctypes.windll.user32.FindWindowW(None, 'Everquest'):
        kill_clients_all()
        print('Error window found, terminating clients and starting over.')
        time.sleep(120)
        client_launch()