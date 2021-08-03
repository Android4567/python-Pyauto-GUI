# important  imports
import pyautogui as p
from time import sleep

# click on windows icon
p.click(37,748)

# search for notepad
p.write('Notepad')

# press enter
p.press('Enter')

# rest for 3 seconds
sleep(3)

# Write the Script
p.write('''@echo off
color 0a
:top
echo %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random%
goto top''')

# press ctrl + s for save
p.hotkey('ctrl', 's')

# take the name of file 
p.write('matrix.bat')

# press enter
p.press('Enter')

# press Alt + f4 for close the file
p.hotkey('Alt', 'F4')

# click on windows icon
p.click(37,748)

# search matrix.bat
p.write('matrix.bat')

# Sleep 2 seconds
sleep(2)

# press enter for run
p.press('Enter')
