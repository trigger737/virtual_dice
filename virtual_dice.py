import random
import time

import PySimpleGUI as sg


class Dice:
    def __init__(self):
        sg.theme('DarkTeal2')  # Add a touch of color
        self.window = sg.Window('Window Title', self.layout(), no_titlebar=True, grab_anywhere=True,
                                element_padding=(0, 0), margins=(0, 0))

    @staticmethod
    def layout():
        layout = [[sg.Column([[sg.Button('x', key='quit', size=(3, 1))]], expand_x=True, element_justification='right',
                             pad=0)],
                  [sg.Column([[sg.Image(filename='res\\1.png', key='img')],
                              [sg.Button('Hodit kostkou', key='generate', size=(20, 3), pad=(0, (10, 0)))]],
                             element_justification='center', vertical_alignment='bottom', expand_x=True, pad=20)]
                  ]
        return layout

    def generate(self):
        self.window['generate'].update(disabled=True)
        for i in range(10):
            number = random.randint(1, 6)
            self.window['img'].update(filename='res\\{}.png'.format(number))
            self.window.finalize()
            time.sleep(0.2)
        self.window['generate'].update(disabled=False)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'quit':  # if user closes window or clicks cancel
                break
            if event == 'generate':  # if user closes window or clicks cancel
                self.generate()
        self.window.close()


if __name__ == '__main__':
    app = Dice()
    app.run()
