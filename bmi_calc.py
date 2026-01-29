weight = float(input("Gewicht in Kilogramm [kg]: "))
height = float(input("Höhe in Metern [m]: "))

bmi = weight/(height**2)

comment =""

if bmi <= 18.5:
    comment = "Spargeltazan"
elif bmi <= 24.9:
    comment = "Normi"
elif bmi <= 29.9:
    comment = "Fett Sack"
elif bmi <= 34.9:
    comment = "Sack Kartoffeln"
elif bmi <= 39.9:
    comment = "Benjamin Blümchen"
elif bmi > 40:
    comment = "fetter Godzilla"

print(f'Dein BMI ist {bmi}. Du {comment}.')
