import pyautogui
import webbrowser
import time
import OS
import clipboard
from datetime import date

SpecCrudAddress = "https://melscience.com/internal/sets/med-surgery-part1/production-spec-v2.html" #to do auto input from sheets
SetName = "Surgery 1"                                                                               #to do auto input from CRUD
now = date.today()
nowStrToPrint = now.strftime("%Y-%m-%d-")

webbrowser.open_new_tab("https://melscience.com/internal/sets/med-surgery-part1/production-spec-v2.html")

pyautogui.confirm('spec has appeared?')
pyautogui.keyDown('ctrl')
pyautogui.press('p')
pyautogui.keyUp('ctrl')
time.sleep(3)
pyautogui.press('enter')
pyautogui.confirm('Save file window has appeared?')
pyautogui.write(nowStrToPrint)
pyautogui.write("MED-" + "Surgery 1")
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')


NewFileName = nowStrToPrint + "MED-" + "Surgery 1" + ".pdf"
webbrowser.open_new_tab("https://www.ilovepdf.com/compress_pdf")
pyautogui.confirm('ILPdf window has appeared?')

