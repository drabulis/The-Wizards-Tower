import PySimpleGUI as sg

intro_window = [
    [sg.Text("Enter player name:")]
    [sg.Input("Demogorgon", key='name_input')]
    [sg.Button("Create wizard"), sg.Button("Exit")]
]
