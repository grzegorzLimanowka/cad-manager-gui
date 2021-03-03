import PySimpleGUI as sg


class Graphic:
    def __init__(self):

        # menu z lewej
        left_menu = [ [sg.Text('')],
            [sg.B('Zarządzanie gotówką',key='o1')],
            [sg.B('Włącz / wyłącz akceptory',key='o2')],
            [sg.B('Włącz / wyłącz\n przyjmowanie gotówki',size=(20,2),key='o3')],
            [sg.B('Resetuj urządzenia',key='o4')],
                  [sg.Text('')]
        ]
        left_menu=sg.Frame('',left_menu)


        #góra
        static_top = [
            [sg.Text('Port       '), sg.Input(size=(10,1)),sg.Button("PL"),sg.Button("ENG")],
            [sg.Text('Baudrate'), sg.Listbox(values=('Opcja 1', 'Opcja 2')), sg.Button("Wykonaj")]]


        #środek

        button_input=  [[sg.B("Money Return",key='2')],[sg.Input(size=(10,1))]]
        inside = [
            [sg.B('Money Get', key='1'), sg.Column(button_input, key='2')],
            [sg.B('Coins Get', key='3'), sg.Button('Notes Get', key='4')]]
        # inside2 = [
        #     [sg.B('Device Enable Coins'), sg.B('Device Enable notes')],
        #     [sg.B('Device Disable Coins'), sg.Button('Device Disable notes')]]
        # prawo + góra
        right = [
            [sg.Frame(layout=[[sg.Column(static_top, vertical_alignment='c')]], vertical_alignment='c', title='')],
            [sg.Frame(layout=[[sg.Column(inside, vertical_alignment='c')]], vertical_alignment='c', title='')]]

        self.layout = [[left_menu, sg.Column(right)]]




        self.window = sg.Window('Cash Manager', self.layout,# default_element_size=(12, 1),
                                size=(1000, 1000))

    def work(self):

        while True:

            event, values = self.window.read()

            if event is None or event == 'Exit':
                break

            if event == 'o1':
                self.window['1'].update('Money Get')
                self.window['2'].update('Money Return')
                self.window['3'].update('Coins Get')
                self.window['4'].update('Notes Get')
            if event == 'o2':
                self.window['1'].update('Device On Coins')
                self.window['2'].update('Device On Notes')
                self.window['3'].update('Device Off Coins')
                self.window['4'].update('Device Off Notes')
            if event == 'o3':
                self.window['1'].update('Device Enable Coins')
                self.window['2'].update('Device Enable notes')
                self.window['3'].update('Device Disable Coins')
                self.window['4'].update('Device Disable Notes')
            if event == 'o4':
                self.window['1'].update('Adapter reboot')
                self.window['2'].update('Device Reset All')
                self.window['3'].update('Device Reset Coins')
                self.window['4'].update('Device Reset Notes')


        self.window.close()


gui = Graphic()
gui.work()
