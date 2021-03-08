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
            [sg.Text('Port       '), sg.Listbox(values=('/dev/ttyUSB0', '/dev/ttyUSB1'),key='-Port-'),sg.Button("PL"),sg.Button("ENG")],
            [sg.Text('Baudrate'), sg.Listbox(values=('115200', '9600'),key='-Bdrate-'), sg.Button("Wykonaj")]]


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
        #flag_port = 0
        #flag_bdrate = 0
        message = {}

        while True:

            event, values = self.window.read()
            #message = str(values['-Port-'])
            print(values['-Port-'])
            print(values['-Bdrate-'])
            if event is None or event == 'Exit':
                break
            # if event == values['-Port-'] and flag_port == 0:
            #     print("działá")
            # #message += str(values['-Port-'])
            # #    print(values['-Port-'])
            # #    flag_port = 1
            # if event == values['-Bdrate-'] and flag_bdrate == 0:
            #     #message += str(values['-Bdrate-'])
            #     print(values['-Bdrate-'])
            #     flag_bdrate = 1
            #left menu
            if event == 'menu1':
                flag_menu = 1
                self.window['1'].update('Money Get')
                self.window['1'].update(button_color='red')

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
                message["Port"] = values['-Port-']
                message["Baudrate"] = values['-Bdrate-']

                self.send(message)
                message = {}
        self.window.close()

    def options(self, event, msg,flag_menu, values):
            #menu1
            if event == '1' and flag_menu == 1:
                msg["money-get"] = "amount" # + amount}
            if event == '2' and flag_menu == 1:
                msg["money-return"] =  "adapter.py -money-return " #+ str(values['-Input-'])}
            if event == '3' and flag_menu == 1:
                msg["coins-get"] = "'tube-type', 'tube-status', 'tube-money'" # need fix
            if event == '4' and flag_menu == 1:
                msg["notes-get"] = "'map', 'enable', 'recycler-note', 'recycler-amount'" #.
            #menu2
            if event == '1' and flag_menu == 2:
                msg["device-on"] = "coins"
            if event == '2' and flag_menu == 2:
                msg["device-on"]= "notes"
            if event == '3' and flag_menu == 2:
                msg["device-off"] =  "coins"
            if event == '4' and flag_menu == 2:
                msg["device-off"] =  "notes"
            #menu3
            if event == '1' and flag_menu == 3:
                msg["device-enable"] =  "coins"
            if event == '2' and flag_menu == 3:
                msg["device-enable"] =  "notes"
            if event == '3' and flag_menu == 3:
                msg["device-disable"] =  "coins"
            if event == '4' and flag_menu == 3:
                msg["device-disable"] =  "notes"
            #menu4
            if event == '1' and flag_menu == 4:
                msg["adapter" ]= "reboot"
            if event == '2' and flag_menu == 4:
                msg["device_rst"] =  "All"
            if event == '3' and flag_menu == 4:
                msg["device_rst"] =  "Coins"
            if event == '4' and flag_menu == 4:
                msg["device_rst"] =  "Notes"

            return msg

    def send(self, mess):
        #mess = str(str(mess).replace("\'", "\""))
        mess = str(mess)
        mess+=  '\r\n'
        #os.system(mess)
        sg.popup(mess,'')



gui = Graphic()
gui.left_menu()
