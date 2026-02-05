import os
clear = lambda: os.system('cls')

settings ={
    "weight_input" :("kg","Kilogramm",1),
    "weight_options" : [("kg","Kilogramm",1),("g","Gramm",0.001),("t","Tonnen",1000)],
    "height_input": ("m","Meter",1),
    "height_options": [("m","Meter",1),("cm","Zentimeter",0.01),("km","Kilometer",1000)],
    "seperator" : (",","Kommata"),
    "seperator_options": [(".","Punkte"),(",","Kommata")]
}

def open_settings():
    first_options = ["gewicht eingabe","körpergröße", "trennzeichen","zurück"]
    second_options = {
        "weight" : ["Kilogramm","Gramm","Tonnen"],
        "height" : ["Meter","Zentimeter","Kilometer"],
        "seperator" : ["Punkt","Komma"]
    }

    answer = input(promt(first_options))

    if answer.lower() in answer_options(first_options[0]):
        answer = input(promt(second_options["weight"]))
        for o in second_options["weight"]:
            if answer.lower() in answer_options(o):
                if o == "Kilogramm":
                    settings["weight_input"] = settings["weight_options"][0]
                elif o == "Gramm":
                    settings["weight_input"] = settings["weight_options"][1]
                elif o== "Tonnen":
                    settings["weight_input"] = settings["weight_options"][2]
    elif answer.lower() in answer_options(first_options[1]):
        answer = input(promt(second_options["height"]))
        for o in second_options["height"]:
            if answer.lower() in answer_options(o):
                if o == "Meter":
                    settings["height_input"] = settings["height_options"][0]
                elif o == "Zentimeter":
                    settings["height_input"] = settings["height_options"][1]
                elif o== "Kilometer":
                    settings["height_input"] = settings["height_options"][2]
    elif answer.lower() in answer_options(first_options[2]):
        answer = input(promt(second_options["seperator"]))
        for o in second_options["seperator"]:
            if answer.lower() in answer_options(o):
                if o == "Punkt":
                    settings["seperator"] = settings["seperator_options"][0]
                elif o == "Komma":
                    settings["seperator"] = settings["seperator_options"][1]
    elif answer.lower() in answer_options(first_options[3]):
        return
    open_settings()



def promt(options):
    string = ""
    for o in options:
        string += f'[{o[0].upper()}]{o[1:]}; '
    string = string[:-2]
    string += ": "
    return string

def answer_options(options):
    if type(options) != list:
        options = [options]
    array = []
    for o in options:
        array.append(o[0].lower())
        array.append(o.lower())
        array.append(o.split()[0].lower())
    return array



def ask_input():
    weight_question = f'Geben Sie ihr Gewicht in {settings["weight_input"][1]} ({settings["weight_input"][0]}) an: '
    height_question = f'Geben Sie ihre Körpergröße in {settings["height_input"][1]} ({settings["height_input"][0]}) an: '

    clear()
    print("Für Einstellungen geben Sie \"s\" ein.\n")
    print(f"Als Trennzeichen verwenden Sie {settings['seperator'][1]} ({settings["seperator"][0]}).\n")

    
    input_weight = input(weight_question)
    if "s" == input_weight:
        open_settings()
        return ask_input()
    



    input_height = input(height_question)
    if "s" == input_height:
        open_settings()
        return ask_input()
    
    if settings["seperator"][1] == "Kommata":
        input_weight = input_weight.replace(",",".")
        input_height = input_height.replace(",",".")
    

    try:
        input_height = float(input_height)
        input_weight = float(input_weight)
    except ValueError:
        return ask_input()


    weight = input_weight * settings["weight_input"][2]
    height = input_height * settings["height_input"][2]

    return weight, height

def calc_bmi():
    weight,height = ask_input()


    bmi = weight/(height**2)

    comment =""
    if bmi < 16:
        comment = "Espenlaub"
    elif bmi <= 18.5:
        comment = "Spargeltarzan"
    elif bmi <= 24.9:
        comment = "Normi"
    elif bmi <= 29.9:
        comment = "Fetter Sack"
    elif bmi <= 34.9:
        comment = "Sack Kartoffeln"
    elif bmi <= 39.9:
        comment = "Benjamin Blümchen"
    elif bmi > 39.9:
        comment = "fetter Godzilla"

    output_bmi = str(round(bmi,2))
    if settings["seperator"][1] == "Kommata":
        output_bmi = str(round(bmi,2)).replace(".",",")

    print(f'Dein BMI ist {output_bmi}. Du {comment}.')

if __name__ == "__main__":
    while True:
        calc_bmi()
        
        answer = input("Zum Verlassen geben Sie e ein.\nFür neue Berechnungen drücken Sie Eingabe\n")
        if answer == "e":
            break
