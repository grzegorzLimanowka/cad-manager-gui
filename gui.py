import PySimpleGUI as sg


class Graphic:
    def __init__(self):

        # menu z lewej
        left_menu = [ [sg.Text('')],
            [sg.B('Zarządzanie gotówką')],
            [sg.B('Włącz / wyłącz akceptory')],
            [sg.B('Włącz / wyłącz\n przyjmowanie gotówki',size=(20,2))],
            [sg.B('Resetuj urządzenia')],
                  [sg.Text('')]
        ]
        left_menu=sg.Frame('',left_menu)


        #góra
        static_top = [
            [sg.Text('Port       '), sg.Input(size=(10,1)),sg.Button("PL"),sg.Button("ENG")],
            [sg.Text('Baudrate'), sg.Listbox(values=('Opcja 1', 'Opcja 2')), sg.Button("Wykonaj")]]


        #środek

        button_input=  [[sg.B("Money Return")],[sg.Input(size=(10,1))]]
        inside = [
            [sg.B('Money Get'), sg.Column(button_input)],
            [sg.B('Coins Get'), sg.Button("Notes Get")]]

        # prawo + góra
        right = [
            [sg.Frame(layout=[[sg.Column(static_top, vertical_alignment='c')]], vertical_alignment='c', title='')],
            [sg.Frame(layout=[[sg.Column(inside, vertical_alignment='c')]], vertical_alignment='c', title='')]]

        layout = [[left_menu, sg.Column(right)]]




        self.window = sg.Window('Cash Manager', layout,# default_element_size=(12, 1),
                                size=(1000, 1000))

    def work(self):

        while True:

            event, values = self.window.read()

            if event is None or event == 'Exit':
                break

        self.window.close()


gui = Graphic()
gui.work()
