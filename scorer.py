#import GUI module
import PySimpleGUI as sg

#create dictionaries for raw scores
readingDict = {
		"0" : 10,
		"1" : 10,
		"2" : 10,
        "3" : 11,
		"4" : 12,
		"5" : 13,
		"6" : 14,
        "7" : 15,
        "8" : 15,
        "9" : 16,
        "10" : 17,
		"11" : 17,
		"12" : 18,
        "13" : 19,
		"14" : 19,
		"15" : 20,
		"16" : 20,
        "17" : 21,
        "18" : 21,
        "19" : 22,
        "20" : 22,
		"21" : 23,
		"22" : 23,
        "23" : 24,
		"24" : 24,
		"25" : 25,
		"26" : 25,
        "27" : 26,
        "28" : 26,
        "29" : 27,
        "30" : 28,
		"31" : 28,
		"32" : 29,
        "33" : 29,
		"34" : 30,
		"35" : 30,
		"36" : 31,
        "37" : 31,
        "38" : 32,
        "39" : 32,
        "40" : 33,
		"41" : 33,
		"42" : 34,
        "43" : 35,
		"44" : 35,
		"45" : 36,
		"46" : 37,
        "47" : 37,
        "48" : 38,
        "49" : 38,
        "50" : 39,
        "51" : 40,
        "52" : 40
	}

writingDict = {
		"0" : 10,
		"1" : 10,
		"2" : 10,
        "3" : 10,
		"4" : 11,
		"5" : 12,
		"6" : 13,
        "7" : 13,
        "8" : 14,
        "9" : 15,
        "10" : 16,
		"11" : 16,
		"12" : 17,
        "13" : 18,
		"14" : 19,
		"15" : 19,
		"16" : 20,
        "17" : 21,
        "18" : 21,
        "19" : 22,
        "20" : 23,
		"21" : 23,
		"22" : 24,
        "23" : 25,
		"24" : 25,
		"25" : 26,
		"26" : 26,
        "27" : 27,
        "28" : 28,
        "29" : 28,
        "30" : 29,
		"31" : 30,
		"32" : 30,
        "33" : 31,
		"34" : 32,
		"35" : 32,
		"36" : 33,
        "37" : 34,
        "38" : 34,
        "39" : 35,
        "40" : 36,
		"41" : 37,
		"42" : 38,
        "43" : 39,
		"44" : 40
	}

mathDict = {
		"0" : 200,
		"1" : 200,
		"2" : 210,
        "3" : 230,
		"4" : 240,
		"5" : 260,
		"6" : 280,
        "7" : 290,
        "8" : 310,
        "9" : 320,
        "10" : 330,
		"11" : 340,
		"12" : 360,
        "13" : 370,
		"14" : 380,
		"15" : 390,
		"16" : 410,
        "17" : 420,
        "18" : 430,
        "19" : 440,
        "20" : 450,
		"21" : 460,
		"22" : 470,
        "23" : 480,
		"24" : 480,
		"25" : 490,
		"26" : 500,
        "27" : 510,
        "28" : 520,
        "29" : 520,
        "30" : 530,
		"31" : 540,
		"32" : 550,
        "33" : 560,
		"34" : 560,
		"35" : 570,
		"36" : 580,
        "37" : 590,
        "38" : 600,
        "39" : 600,
        "40" : 610,
		"41" : 620,
		"42" : 630,
        "43" : 640,
		"44" : 650,
		"45" : 660,
		"46" : 670,
        "47" : 670,
        "48" : 680,
        "49" : 690,
        "50" : 700,
        "51" : 710,
        "52" : 730,
        "53" : 740,
        "54" : 750,
        "55" : 760,
        "56" : 780,
        "57" : 790,
        "58" : 800
	}

#implelement GUI
layout = [
    [sg.Text('Enter your raw scores below: ')],
    [sg.Text('Reading', size=(15, 1)), sg.InputText()],
    [sg.Text('Writing', size=(15, 1)), sg.InputText()],
    [sg.Text('Math', size=(15, 1)), sg.InputText()],
    [sg.Text('Your score:'), sg.Text('', size=(15,1), key='_OUTPUT_')],
    [sg.Submit()]
]

window = sg.Window('SAT Scorer', layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Submit':
        window.Element('_OUTPUT_').Update(readingDict[values[0]]*10+writingDict[values[1]]*10+mathDict[values[2]])

window.Close()
'''
layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', size=(15,1), key='_OUTPUT_')],
          [sg.Input(key='_IN_')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

'''

"""
print("SAT SCORER")
readingRaw = input("Enter your raw score for reading: ")
writingRaw = input("Enter your raw score for writing: ")
mathRaw = input("Enter your raw score for math: ")

print("\nYou got a", readingDict[readingRaw]*10+writingDict[writingRaw]*10+mathDict[mathRaw])
"""
