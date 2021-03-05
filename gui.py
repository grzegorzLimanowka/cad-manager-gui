import PySimpleGUI as sg
import os


class Graphic:
    def __init__(self):

        # menu z lewej
        left_menu = [ [sg.Text('')],
            [sg.B('Zarządzanie gotówką',key='menu1')],
            [sg.B('Włącz / wyłącz akceptory',key='menu2')],
            [sg.B('Włącz / wyłącz\n przyjmowanie gotówki',size=(20,2),key='menu3')],
            [sg.B('Resetuj urządzenia',key='menu4')],
                  [sg.Text('')]
        ]
        left_menu=sg.Frame('',left_menu)


        #góra
        static_top = [
            [sg.Text('Port       '), sg.Input(size=(10,1)),sg.Button("PL"),sg.Button("ENG")],
            [sg.Text('Baudrate'), sg.Listbox(values=('115200', '9600')), sg.Button("Wykonaj")]]


        #środek

        button_input=  [[sg.B("Money Return", key='2')],[sg.Input(size=(10,1),key='-Input-')]]
        inside = [
            [sg.B('Money Get', key='1'), sg.Column(button_input)],
            [sg.B('Coins Get', key='3'), sg.Button('Notes Get', key='4'), sg.Button('LOL')]]
        # inside2 = [
        #     [sg.B('Device Enable Coins'), sg.B('Device Enable notes')],
        #     [sg.B('Device Disable Coins'), sg.Button('Device Disable notes')]]        #template
        # prawo + góra
        right = [
            [sg.Frame(layout=[[sg.Column(static_top, vertical_alignment='c')]], vertical_alignment='c', title='')],
            [sg.Frame(layout=[[sg.Column(inside, vertical_alignment='c')]], vertical_alignment='c', title='')]]

        self.layout = [[left_menu, sg.Column(right)]]




        self.window = sg.Window('Cash Manager', self.layout,# default_element_size=(12, 1),
                                size=(500, 500))

    def left_menu(self):

        flag_menu = 1 #first menu

        message = ""

        while True:

            event, values = self.window.read()

            if event is None or event == 'Exit':
                break


            #left menu
            if event == 'menu1':
                flag_menu = 1
                self.window['1'].update('Money Get')
                self.window['2'].update('Money Return')
                self.window['3'].update('Coins Get')
                self.window['4'].update('Notes Get')
            if event == 'menu2':
                flag_menu = 2
                self.window['1'].update('Device On Coins')
                self.window['2'].update('Device On Notes')
                self.window['3'].update('Device Off Coins')
                self.window['4'].update('Device Off Notes')
            if event == 'menu3':
                flag_menu = 3
                self.window['1'].update('Device Enable Coins')
                self.window['2'].update('Device Enable notes')
                self.window['3'].update('Device Disable Coins')
                self.window['4'].update('Device Disable Notes')
            if event == 'menu4':
                flag_menu = 2
                self.window['1'].update('Adapter reboot')
                self.window['2'].update('Device Reset All')
                self.window['3'].update('Device Reset Coins')
                self.window['4'].update('Device Reset Notes')
            if event in '1234':
                    message = self.options(event,message,flag_menu, values)

            if event == 'Wykonaj':
                self.send(message)
        self.window.close()

    def options(self, event, message,flag_menu, values):
            #menu1
            if event == '1' and flag_menu == 1:
                message = "python adapter.py -money-get amount" # + amount
            if  event == '2' and flag_menu == 1:
                message = "python adapter.py -money-return "  + str(values['-Input-'])
            if  event == '3' and flag_menu == 1:
                message = "python adapter.py -coins-get" + "'tube-type', 'tube-status', 'tube-money'" # need fix
            if  event == '4' and flag_menu == 1:
                message = "python adapter.py -notes-get" + "'map', 'enable', 'recycler-note', 'recycler-amount'" #.
            #menu2
            if event == '1' and flag_menu == 2:
                message = "python adapter.py -device-on coins"
            if  event == '2' and flag_menu == 2:
                message = "python adapter.py -device-on notes"
            if  event == '3' and flag_menu == 2:
                message = "python adapter.py -device-off coins"
            if  event == '4' and flag_menu == 2:
                message = "python adapter.py -device-off amount"
            #menu3
            if event == '1' and flag_menu == 3:
                message = "python adapter.py -device-enable coins"
            if  event == '2' and flag_menu == 3:
                message = "python adapter.py -device-enable notes"
            if  event == '3' and flag_menu == 3:
                message = "python adapter.py -device-disable coins"
            if  event == '4' and flag_menu == 3:
                message = "python adapter.py -device-disable coins"
            #menu4
            if event == '1' and flag_menu == 4:
                message = "python adapter.py -adapter reboot"
            if  event == '2' and flag_menu == 4:
                message = "python adapter.py -device_rst All"
            if  event == '3' and flag_menu == 4:
                message = "python adapter.py -device_rst Coins"
            if  event == '4' and flag_menu == 4:
                message = "python adapter.py -device_rst Notes"

            return message

    def send(self, message):

        os.system(message)
        sg.popup(message,'MESSAGE')



gui = Graphic()
gui.left_menu()
