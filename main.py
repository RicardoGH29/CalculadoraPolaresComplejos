import cmath

import PySimpleGUI as sg

from Operations import convertToPolar, polarToComplex

sg.theme('DarkAmber')  # Add a touch of color
layoutPolarToComplex = [[sg.Text('Module'), sg.InputText(key='module')],
                        [sg.Text('Angle'), sg.InputText(key='angle')],
                        [sg.Button('Convert'), sg.Button('Exit')]]
layoutPrincipal = [[sg.Button('Polar to Complex'), sg.Button('Complex to Polar')],
                   [sg.Button('Complex Suma'), sg.Button('Complex Resta')],
                   [sg.Button('Complex Multiplication'), sg.Button('Complex Division')],
                   [sg.Button('Exit')]]
layoutComplexToPolar = [[sg.Text('Complex Number'), sg.InputText(key='complexNumber')],
                        [sg.Button('Convert')], [sg.Button('Exit')]]
layoutComplexSuma = [[sg.Text('Complex Number 1'), sg.InputText(key='complexNumber1')],
                     [sg.Text('Complex Number 2'), sg.InputText(key='complexNumber2')],
                     [sg.Button('Add')], [sg.Button('Exit')]]
layoutComplexResta = [[sg.Text('Complex Number 1'), sg.InputText(key='complexNumber1')],
                      [sg.Text('Complex Number 2'), sg.InputText(key='complexNumber2')],
                      [sg.Button('Subtract')], [sg.Button('Exit')]]
layoutComplexMultiplicacion = [[sg.Text('Complex Number 1'), sg.InputText(key='complexNumber1')],
                               [sg.Text('Complex Number 2'), sg.InputText(key='complexNumber2')],
                               [sg.Button('Multiplicative')], [sg.Button('Exit')]]
layoutComplexDivision = [[sg.Text('Complex Number 1'), sg.InputText(key='complexNumber1')],
                         [sg.Text('Complex Number 2'), sg.InputText(key='complexNumber2')],
                         [sg.Button('Divide')], [sg.Button('Exit')]]


def main():
    windowPrincipal = sg.Window('Principal', layoutPrincipal)
    while True:
        event, values = windowPrincipal.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            windowPrincipal.close()
            break
        if event == 'Polar to Complex':
            windowPrincipal.close()
            windowPolarToComplex = sg.Window('Polar to Complex', layoutPolarToComplex)
            while True:
                event, values = windowPolarToComplex.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    windowPolarToComplex.close()
                    break
                if event == 'Convert':
                    module = float(values['module'])
                    angle = float(values['angle'])
                    complexNumber = polarToComplex(module, angle)
                    sg.popup('The complex number is: ', complexNumber)
        if event == 'Complex to Polar':
            windowPrincipal.close()
            windowComplexToPolar = sg.Window('Complex to Polar', layoutComplexToPolar)
            while True:
                event, values = windowComplexToPolar.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    windowComplexToPolar.close()
                    break
                if event == 'Convert':
                    complexNumber = complex(values['complexNumber'])
                    module, angle = convertToPolar(complexNumber)
                    sg.popup('The module is: ', module, 'The angle is: ', angle)
        if event == 'Complex Suma':
            windowPrincipal.close()
            windowComplexSuma = sg.Window('Complex Suma', layoutComplexSuma)
            while True:
                event, values = windowComplexSuma.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    windowComplexSuma.close()
                    break
                if event == 'Add':
                    complexNumber1 = complex(values['complexNumber1'])
                    complexNumber2 = complex(values['complexNumber2'])
                    complexNumber = complexNumber1 + complexNumber2
                    sg.popup('The complex number is: ', complexNumber)
        if event == 'Complex Resta':
            windowPrincipal.close()
            windowComplexResta = sg.Window('Complex Resta', layoutComplexResta)
            while True:
                event, values = windowComplexResta.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    windowComplexResta.close()
                    break
                if event == 'Subtract':
                    complexNumber1 = complex(values['complexNumber1'])
                    complexNumber2 = complex(values['complexNumber2'])
                    complexNumber = complexNumber1 - complexNumber2
                    sg.popup('The complex number is: ', complexNumber)
        if event == 'Complex Multiplication':
            windowPrincipal.close()
            windowComplexMultiplicacion = sg.Window('Complex Multiplication', layoutComplexMultiplicacion)
            while True:
                event, values = windowComplexMultiplicacion.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    windowComplexMultiplicacion.close()
                    break
                if event == 'Multiplicative':
                    complexNumber1 = complex(values['complexNumber1'])
                    complexNumber2 = complex(values['complexNumber2'])
                    complexNumber = complexNumber1 * complexNumber2
                    sg.popup('The complex number is: ', complexNumber)
        if event == 'Complex Division':
            windowPrincipal.close()
            windowComplexDivision = sg.Window('Complex Division', layoutComplexDivision)
            while True:
                event, values = windowComplexDivision.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    windowComplexDivision.close()
                    break
                if event == 'Divide':
                    complexNumber1 = complex(values['complexNumber1'])
                    complexNumber2 = complex(values['complexNumber2'])
                    complexNumber = complexNumber1 / complexNumber2
                    sg.popup('The complex number is: ', complexNumber)


if __name__ == '__main__':
    main()
