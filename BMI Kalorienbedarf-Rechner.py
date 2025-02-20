import Mahlzeit_planer
def eingaben():
    try:    
        gewicht = float(input("Gewicht in kg: "))
        groesse = float(input("Größe in cm: "))
        alter = int(input("Alter in Jahren: "))
        geschlecht = input("Geschlecht (m/w): ").lower()

        if geschlecht not in ["m", "w"]:
            raise ValueError("Bitte geben Sie m oder w ein.")
        
        if gewicht <= 0 or groesse <= 0 or alter <= 0:
            raise ValueError("Bitte geben Sie gültige Werte ein.")
           

        return gewicht, groesse, alter, geschlecht
    
    except (ValueError,TypeError) as e:
        print(f"Fehler bei der Eingab: {e}")
        print("Bitte geben Sie gültige Werte ein.")
        #man muss keinen TypeError extra raisen da python das automatisch macht
        

def bmi(gewicht, groesse):
    bmi= gewicht/groesse**2
    return bmi

def bmi_diagramm(bmi_wert):

    skala=[18.5,25,30]
    kategorien=["Unter","Normal","Über"]

    # Breiten für konsistente Ausrichtung
    breite1 = 10  # Für "Unter" und "18.50"
    breite2 = 11  # Für "Normal" und "25.00"
    breite3 = 11  # Für "Über" und "30.00"

    # Diagramm erstellen
    bmi_diagramm = f"BMI: {bmi_wert:.2f} {kategorisierung_bmi(bmi_wert)}\n"
    bmi_diagramm += "|" + "-"*breite1 + "|" + "-"*breite2 + "| \n "
    # Zahlen mit gleicher Breite wie Kategorien
    bmi_diagramm += f"{skala[0]:<{breite1}}{skala[1]:<{breite2}}{skala[2]:<{breite3}}\n"
    # Kategorien
    bmi_diagramm += f"{kategorien[0]:<{breite1}}{kategorien[1]:<{breite2}}{kategorien[2]:<{breite3}}"

    return bmi_diagramm

def kategorisierung_bmi(bmi_wert):    
        if bmi_wert < 18.5:
            return"Untergewicht"
        elif bmi_wert < 24.9:
            return"Normalgewicht"
        else:
            return"ThickBOI"

def Vorschlag_Mahlzeitenplaners(bmi_wert,Kalorienbedarf):
    """Erstellt einen personalisierten Mahlzeitenplan basierend auf BMI und Kalorienbedarf."""
    plan = "\nIhr persönlicher Mahlzeitenplan\n"
    plan += "=" * 50 + "\n"
    
    mahlzeiten = {
        "Frühstück": {
            "Gericht": "Erdnussbutter-Toast mit Banane",
            "Kalorien": 500
        },
        "Snack 1": {
            "Gericht": "Handvoll Nüsse & dunkle Schokolade",
            "Kalorien": 300
        },
        "Mittagessen": {
            "Gericht": "Rindersteak mit Kartoffeln & Gemüse",
            "Kalorien": 700
        },
        "Snack 2": {
            "Gericht": "Proteinshake mit Milch & Haferflocken",
            "Kalorien": 400
        },
        "Abendessen": {
            "Gericht": "Vollkornnudeln mit Pesto & Parmesan",
            "Kalorien": 450
        }
    }
    
    gesamt_kalorien = 0
    for mahlzeit, details in Mahlzeit_planer.mahlzeiten.items():
        gesamt_kalorien += details["Kalorien"]
        plan += f"{mahlzeit:<12} ({details['Kalorien']:>4} kcal): {details['Gericht']}\n"
    
    plan += "=" * 50 + "\n"
    plan += f"Gesamtkalorien: {gesamt_kalorien} kcal\n"
    
    if kategorisierung_bmi(bmi_wert) == "Untergewicht":
        plan += "\nEmpfehlung: Erhöhen Sie die Portionsgrößen und fügen Sie\n"
        plan += "kalorienreiche, gesunde Snacks zwischen den Mahlzeiten hinzu."
    
    return plan

def Grundumsatzformel(gewicht, groesse, alter, geschlecht ):
    """Der Grundumsatz gibt den täglichen Kalorienverbrauch in Kilokalorien (kcal) an."""
    if geschlecht == "m":
        grundumsatzformel= float(88.36+(13.4 * gewicht)+(4.8*groesse)-(5.7*alter))
        return f"{grundumsatzformel:.2f}"   
    else:
        grundumsatzformel= float(447.6 + (9.2*gewicht)+(3.1*groesse)-(4.3*alter))
        return f"{grundumsatzformel:.2f}"   

def bmi_rechner():
    while True:
        gewicht, groesse, alter, geschlecht = eingaben()

        print("\nWas möchten Sie tun?")
        print("1. Zusammenfassung anzeigen (1)")
        print("2. Programm beenden (2)")

        try:
            auswahl = int(input("Geben sie ihre ausgewählte Zahl aus: "))
            
            if auswahl == 2:
                print("Programm wird beendet.")
                break
            elif auswahl == 1:
                bmi_wert = bmi(gewicht, groesse)
                # print(f"Ihr BMI beträgt:{bmi_wert:.2f} sie sind in der \n Kategorie {kategorisierung_bmi(bmi_wert)}")
                
                print(bmi_diagramm(bmi_wert))
            
                print(f"Ihr Kalorienbedarf ist {Grundumsatzformel(gewicht, groesse, alter, geschlecht)}")
                break
            else:
                raise ValueError("Bitte geben Sie eine gültige Auswahl ein.")
        except ValueError as e:
            print(f"Fehler: {e}")

bmi_rechner()