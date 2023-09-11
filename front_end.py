import PySimpleGUI as sg
import random
from main import Player
from enemies import Goblin, Dragon
from magic import Firebolt, ManaRestore, Fireball
import os

sg.theme('DarkBrown4') 

def get_player_name():
    while True:
        layout = [
            [sg.Text("Enter your name:")],
            [sg.InputText(key='-PLAYER_NAME-')],
            [sg.Button('Start')]
        ]
        window = sg.Window('THE WIZARDS TOWER', layout, finalize=True)
        while True:
            event, values = window.read()
            player_name = values['-PLAYER_NAME-']
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Start':
                player_name = values['-PLAYER_NAME-']
                if len(player_name) > 0:
                    window.close()
                    return player_name
                else:
                    sg.popup_error("Please enter your name.")           

def second_stage(wizard):
    dragon = Dragon(name="Dragon", hp=100) 
    spells = [Firebolt(), ManaRestore(), Fireball()] 

    stage2_left_column = [
        [sg.Image(filename="img/wizardas.png")],
        [sg.Text(wizard.name, font=("Helvetica", 12), text_color='black')],
        [sg.Text(f"HP: {wizard.hp}", key='-PLAYER_HP-', text_color='red')],
        [sg.Text(f"Mana: {wizard.mana}", key='-PLAYER_MANA-', text_color='blue')],
    ]

    stage2_center_column = [
        [sg.Text("SECOND STAGE", size=(40, 1), justification='center', font=("Helvetica", 16))],
        [sg.Output(size=(55, 10), key='-FIGHT_INFO-', text_color='black', background_color='white', font=("Helvetica", 10))],
    ]

    stage2_right_column = [
        [sg.Image(filename="img/drakonas.png")],
        [sg.Text(dragon.name, font=("Helvetica", 12), text_color='black')],
        [sg.Text(f"HP: {dragon.hp}", key='-ENEMY_HP-', text_color='red')],
    ]

    spell_buttons = [sg.Button(spell.name, key=spell.name) for spell in spells]

    layout = [
        [sg.Column(stage2_left_column, element_justification='center'), sg.Column(stage2_center_column, element_justification='center'), sg.Column(stage2_right_column, element_justification='center')],
        [sg.HorizontalSeparator()],
        spell_buttons,
        [sg.Button("Exit")],
    ]

    window = sg.Window("THE WIZARDS TOWER", layout, finalize=True)

    game_over = False
    fight_log = []

    while not game_over:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        if event in [spell.name for spell in spells]:
            selected_spell = next((spell for spell in spells if spell.name == event), None)

            if selected_spell:
                if wizard.mana < selected_spell.mana_cost:
                    window['-FIGHT_INFO-'].update("Not enough mana to cast the spell.")
                else:
                    wizard.mana -= selected_spell.mana_cost

                    if isinstance(selected_spell, ManaRestore):
                        mana_restore_info = selected_spell.restore_mana()
                        fight_log.append(mana_restore_info)
                    else:
                        player_damage = selected_spell.get_damage()
                        dragon.receive_damage(player_damage)
                        player_info = f"\nPlayer casts {selected_spell.name} and deals {player_damage} damage to Dragon!"
                        fight_log.append(player_info)

                    if dragon.hp <= 0:
                        window['-ENEMY_HP-'].update("Defeated!")
                        fight_log.append(f"Player wins!")
                        sg.popup("   Victory!", title="Victory")
                        window.close()
                        game_over = True

                    else:
                        enemy_damage, selected_attack = dragon.attack()
                        wizard.take_damage(enemy_damage)
                        enemy_info = f"Dragon uses {selected_attack} and deals {enemy_damage} damage to Wizard!"
                        fight_log.append(enemy_info)

                        if wizard.hp <= 0:
                            window['-PLAYER_HP-'].update("Defeated!")
                            window['-PLAYER_MANA-'].update("")
                            fight_log.append("Dragon wins!")
                            sg.popup("You lost!", title="Defeat")
                            game_over = True

                    window['-FIGHT_INFO-'].update('\n'.join(fight_log))
                    window['-ENEMY_HP-'].update(f"HP: {dragon.hp}")
                    window['-PLAYER_HP-'].update(f"HP: {wizard.hp}")
                    window['-PLAYER_MANA-'].update(f"Mana: {wizard.mana}")

    window.close()

player_name = get_player_name()

if player_name:
    wizard = Player(name=player_name, hp=1000, mana=50)
    goblin = Goblin(name="Goblin", hp=50)
    spells = [Firebolt(), ManaRestore()]

left_column = [
    [sg.Image(filename="img/wizardas.png")],
    [sg.Text(wizard.name, font=("Helvetica", 12), text_color='white')],
    [sg.Text(f"HP: {wizard.hp}", key='-PLAYER_HP-', text_color='red')],
    [sg.Text(f"Mana: {wizard.mana}", key='-PLAYER_MANA-', text_color='blue')],
]

center_column = [
    [sg.Text("FIRST STAGE", size=(40, 1), justification='center', font=("Helvetica", 16))],
    [sg.Output(size=(55, 10), key='-FIGHT_INFO-', text_color='black', background_color='white', font=("Helvetica", 10))],
]

right_column = [
    [sg.Image(filename="img/goblinas.png")],
    [sg.Text(goblin.name, font=("Helvetica", 12), text_color='white')],
    [sg.Text(f"HP: {goblin.hp}", key='-ENEMY_HP-', text_color='red')],
]

spell_buttons = [sg.Button(spell.name, key=spell.name) for spell in spells]

layout = [
    [sg.Column(left_column, element_justification='center'), sg.Column(center_column, element_justification='center'), sg.Column(right_column, element_justification='center')],
    [sg.HorizontalSeparator()],
    spell_buttons,
    [sg.Button("Exit")]
]

window = sg.Window("THE WIZARDS TOWER", layout, finalize=True)

game_over = False
fight_log = [] 
while not game_over:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event in [spell.name for spell in spells]:
        selected_spell = next((spell for spell in spells if spell.name == event), None)

        if selected_spell:
            if wizard.mana < selected_spell.mana_cost:
                window['-FIGHT_INFO-'].update("Not enough mana to cast the spell.")
            else:
                wizard.mana -= selected_spell.mana_cost

                if isinstance(selected_spell, ManaRestore):
                    mana_restore_info = selected_spell.restore_mana()
                    fight_log.append(mana_restore_info)
                else:
                    player_damage = selected_spell.get_damage()
                    goblin.receive_damage(player_damage)
                    player_info = f"\nPlayer casts {selected_spell.name} and deals {player_damage} damage to Goblin!"
                    fight_log.append(player_info)

                if goblin.hp <= 0:
                    window['-ENEMY_HP-'].update("Defeated!")
                    fight_log.append(f"Player wins!")
                    sg.popup(f"{wizard.name} wins and got new powerful spell 'Fireball'!", title="Victory")
                    window.close()
                    second_stage(wizard)
                    game_over = True

                else:
                    enemy_damage, selected_attack = goblin.attack()
                    wizard.take_damage(enemy_damage)
                    enemy_info = f"Goblin uses {selected_attack} and deals {enemy_damage} damage to {wizard.name}!"
                    fight_log.append(enemy_info)

                    if wizard.hp <= 0:
                        window['-PLAYER_HP-'].update("Defeated!")
                        window['-PLAYER_MANA-'].update("")
                        fight_log.append("Goblin wins!")
                        sg.popup("Goblin wins!", title="Defeat")
                        game_over = True

                window['-FIGHT_INFO-'].update('\n'.join(fight_log))
                window['-ENEMY_HP-'].update(f"HP: {goblin.hp}")  
                window['-PLAYER_HP-'].update(f"HP: {wizard.hp}")  
                window['-PLAYER_MANA-'].update(f"Mana: {wizard.mana}") 

window.close()

