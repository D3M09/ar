import os, platform
os.system("cd $HOME/")
#os.system("termux-setup-storage")
os.system("xdg-open https://www.facebook.com/groups/660205018582939")

try:
    import requests
except(ImportError):
    os.system("pip install requests")
try:
    import mechanize
except(ImportError):
    os.system("pip install mechanize")
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")

rana=platform.architecture()[0]
try:
    if rana=="32bit":
        __import__("pro32").main_menu()
    elif rana=="64bit":
        __import__("pro").main_menu()
    else:
        print(" You have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if rana == "32bit":
        import pro32
        pro32.main_menu()
    elif rana == "64bit":
        import pro
        pro.main_menu()
    else:
        print(" You have issue to launch script")
        exit()
