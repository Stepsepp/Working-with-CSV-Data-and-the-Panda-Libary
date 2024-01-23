## Kasutusjuhend

# 1. Käivitage programm.
# 2. Sisestage osariigi nimi, kui programm küsib.
# 3. Korrake kuni olete arvanud kõik 50 osariiki või sisetage "Exit" lõpetamiseks
# 4. Programm näitab puuduvad osariigid ja salvestab need " states_to_learn.csv" faili.

# Koodi selgitus

# Programm kasutab Turtle graafilise liidese loomiseks
# Laeb osariikide andmed CSV-failist "50_states.csv".
# Kasutajalt küsitakse osariigi nime, ja kui vastus on õige, kuvatakse see kaardil.
#  Programm jätkab, kuni kasutaja arvab kõik osariigid või sisestab "Exit".
# Puuduvad osariigid salvestatakse "states_to_learn.csv" faili.

# Sõltuvused ja nõuded

# turtle
# pandas


import turtle
import pandas
# Loome Turtle'i ekraani
screen = turtle.Screen()
screen.title("U.S. States Game")
# Laeme kaardi pildi ja seome selle Turtle'iga
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# Laeme osariikide andmed CSV-failist
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
quessed_states = []

# Kuni kõik osariigid on ära arvatud või kasutaja sisestab "Exit"
while len(quessed_states) < 50:
    # Küsime kasutajalt osariigi nime
    answer_state = screen.textinput(title=f"{len(quessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # Kui kasutaja sisestab "Exit", näitame puuduvaid osariike ja salvestame need faili
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in quessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # Kui kasutaja sisestatud osariik on õige, kuvame selle kaardil
    if answer_state in all_states:
        quessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





