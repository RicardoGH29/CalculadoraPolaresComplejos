import cmath

import PySimpleGUI as sg

from Operations import convertToPolar, polarToComplex
sg.theme('DarkAmber')   # Add a touch of color
layoutPolarToComplex = [[sg.Text('Module'), sg.InputText(key='module')],
                        [sg.Text('Angle'), sg.InputText(key='angle')],
                        [sg.Button('Convert'), sg.Button('Exit')]]
layoutPrincipal = [[sg.Button('Polar to Complex'), sg.Button('Complex to Polar')],
                   [sg.Button('Exit')]]
layoutComplexToPolar = [[sg.Text('Complex Number'), sg.InputText(key='complexNumber')],
                        [sg.Button('Convert')]]


def main():

    window = sg.Window('Complex Numbers', layoutPrincipal)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Polar to Complex':
            window.close()
            window = sg.Window('Polar to Complex', layoutPolarToComplex)
            event, values = window.read()
            if event == 'Convert':
                module = float(values['module'])
                angle = float(values['angle'])
                complexNumber = polarToComplex(module, angle)
                sg.popup('Complex Number: ', complexNumber)
            if event == sg.WIN_CLOSED or event == 'Exit':
                window.close()
                break
        if event == 'Complex to Polar':
            window.close()
            window = sg.Window('Complex to Polar', layoutComplexToPolar)
            event, values = window.read()
            if event == 'Convert':
                complexNumber = complex(values['complexNumber'])
                module, angle = convertToPolar(complexNumber)
                sg.popup('Module: ', module, 'Angle: ', angle)
            if event == sg.WIN_CLOSED or event == 'Exit':
                window.close()
                break
    window.close()


if __name__ == '__main__':
    main()
