import PySimpleGUI as sg

""" 
Kazkokie front endo griauciai arba bent jau pradzia , aisku viska galima keisti.
Savo nuoziura pabandziau paradyt intro screen, bet nzn kaip inputas turi persinest i main().
Visi mygtukai yra tik placeholder pagal poreiki
"""

intro_layout = [
    [sg.Text("WELCOME TO THE WIZARDS TOWER!", text_color="#37FD12")],
    [sg.Text("Enter name", text_color="black"), sg.InputText(key="-INPUT-", text_color="black", size=(20, 1))],
    [sg.Button("ACCEPT"), sg.Button("EXIT")]
]

intro_window = sg.Window("WIZARDS TOWER", intro_layout)

while True:
    intro_event, intro_values = intro_window.read()

    if intro_event == sg.WINDOW_CLOSED or intro_event == "EXIT":
        break
    if intro_event == "ACCEPT":
        intro_window.close()

    def main():    
        layout = [
            [sg.Button("VEIKSMAS1"),
            sg.Button("VEIKSMAS2"), 
            sg.Button("VEIKSMAS3"), 
            sg.Button("VEIKSMAS4"),
            sg.Button("EXIT GAME"),
            sg.Text(size=(40, 1), key="-OUTPUT-")]
        ]

        window = sg.Window("WIZARDS TOWER", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "EXIT GAME":
                window.close()
                break
            elif event == "VEIKSMAS1":
                pass
            elif event == "VEIKSMAS2":
                pass
            elif event == "VEIKSMAS3":
                pass
            elif event == "VEIKSMAS4":
                pass

        window['-OUTPUT-'].update(
            f"GAME OVER",
            text_color='#ffeecc')

intro_window.close()

if __name__ == "__main__":
        main()