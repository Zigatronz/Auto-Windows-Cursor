
import win32con
import win32gui
import ctypes
import os

SystemCursor = {
    "OCR_APPSTARTING" : "32650",
    "OCR_NORMAL" : "32512",
    "OCR_CROSS" : "32515",
    "OCR_HAND" : "32649",
    "OCR_HELP" : "32651",
    "OCR_IBEAM" : "32513",
    "OCR_NO" : "32648",
    "OCR_SIZEALL" : "32646",
    "OCR_SIZENESW" : "32643",
    "OCR_SIZENS" : "32645",
    "OCR_SIZENWSE" : "32642",
    "OCR_SIZEWE" : "32644",
    "OCR_UP" : "32516",
    "OCR_WAIT" : "32514"
}

def ChangeSystemCursor(img : str, id : int):
    cursor = win32gui.LoadImage(0, img, win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE)
    ctypes.windll.user32.SetSystemCursor(cursor, id)
    ctypes.windll.user32.DestroyCursor(cursor)

totalApplied = 0
if os.path.exists('Cursor'):
    for filename in os.listdir('Cursor'):
        for i, name in enumerate(SystemCursor):
            if name in filename:
                ChangeSystemCursor(os.path.join('Cursor', filename), int(SystemCursor[name]))
                print('Cursor for', name, 'applied with image', filename, 'and ID', SystemCursor[name])
                totalApplied += 1
else:
    os.makedirs('Cursor')
    print('Cursur folder created.')
    print('Please read README.md first before use this program.')
print('Program complete. with', totalApplied, 'cursor of total applied.')
exit
