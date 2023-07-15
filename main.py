# This is a sample Python script.
import random
import pprint
import pickle


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    frequency = {}
    tests = 0
    while sum(frequency.values()) < 240:
        print(tests)
        lista_cadouri = [
            "Ceva de squash / sala / sport",
            "O carte",
            "Ceva cu Facultatea / Universitatea / ASMI",
            "Un tricou",
            "Ciorapi / Chiloți",
            "Ochelari de soare",
            "Ceva de pus pe cap (șapcă, etc.)",
            "Ceva Bucureștean (sau anti-provincial)",
            "Ceva la caterincă (eventual inutil)",
            "Un boardgame",
            "Ceva de îmbrăcat (nu șapcă, tricou, chiloți sau ciorapi)",
            "Vinil",
            "Joc (PC / PS4 / Xbox)",
            "Bijuterie (lanț, inel, etc.)",
            "Un cadou pe care îl mai are deja odată",
        ]
        lista_events = [
            "Cuiva i se face rau",
            "Cineva greșește numele altcuiva din greșeală",
            "Se urează la mulți ani Marinei",
            "Cineva dă cu vin / vin spumant pe sine",
            "Cineva dă cu vin / vin spumant pe altcineva",
            "Se sparge un pahar",
            "A existat un grup de cadou (min. 3 persoane)",
            "Cineva nu știe câți ani împlinește Rareș",
            "Cineva își amintește unul dintre bancurile lui Rareș din anul I de facultate",
            "Se scapă un telefon pe jos (cel putin de la inaltimea mesei)",
            "Am văzut un story de la această zi de naștere",
            "Rareș scapă pe jos un cadou sau îl strică",
            "Se postează un TikTok filmat la această zi de naștere",
            "Cineva comandă cafea",
            "Cineva își ia de mâncare și nu termină tot din farfurie",
        ]
        tests = tests + 1
        lista_full = lista_events + lista_cadouri
        frequency = {}
        for i in lista_full:
            frequency[i] = 0
        carduri = {}

        for card_index in range(20):
            selectie_cadouri = []
            selectie_eventuri = []
            # Fa extragerea si verifica daca sunt extrageri valide
            while True:
                if len(lista_cadouri) >= 8:
                    selectie_cadouri = random.sample(lista_cadouri, k=6)
                else:
                    for element in sorted(frequency.items(), key=lambda x:x[1]):
                        if element[0] in lista_cadouri:
                            selectie_cadouri.append(element[0])
                        if len(selectie_cadouri) == 6:
                            break
                        else:
                            Exception("adasdaindfai")
                esec = False
                for item in selectie_cadouri:
                    if item in frequency and frequency[item] >= 8:
                        esec = True
                if esec is False:
                    break
            # Confirma extragerea:
            for item in selectie_cadouri:
                frequency[item] += 1
                if frequency[item] == 8:
                    lista_cadouri.remove(item)

            # EVENTS
            # Fa extragerea si verifica daca sunt extrageri valide
            while True:
                # selectie_eventuri = random.sample(lista_events, k=6)
                if len(lista_events) >= 8:
                    selectie_eventuri = random.sample(lista_events, k=6)
                else:
                    for element in sorted(frequency.items(), key=lambda x:x[1]):
                        if element[0] in lista_events:
                            selectie_eventuri.append(element[0])
                        if len(selectie_eventuri) == 6:
                            break
                        else:
                            Exception("adasdaindfai")
                esec = False
                for item in selectie_eventuri:
                    if item in frequency and frequency[item] >= 8:
                        esec = True
                if esec is False:
                    break
            # Confirma extragerea:
            for item in selectie_eventuri:
                frequency[item] += 1
                if frequency[item] == 8:
                    lista_events.remove(item)


            carduri[card_index] = selectie_cadouri + selectie_eventuri

            for key, value in carduri.items():
                if(len([x for n, x in enumerate(value) if x in value[:n]])) > 0:
                    frequency = {}

    with open('extragere.pkl', 'wb') as fp:
        pickle.dump(carduri, fp)
        print('dictionary saved successfully to file')

    pprint.pprint(carduri)
    pprint.pprint(frequency)
    print(sum(frequency.values()))

    