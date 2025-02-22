import Mahlzeit_planer  # Importiert den Mahlzeitenplan aus separater Datei

def eingaben():
    """Funktion zur Erfassung der Benutzereingaben mit Fehlerbehandlung"""
    try:    
        # Benutzereingaben mit Typkonvertierung
        gewicht = float(input("Gewicht in kg: "))
        groesse = float(input("Größe in cm: "))
        alter = int(input("Alter in Jahren: "))
        geschlecht = input("Geschlecht (m/w): ").lower()  # Konvertiert zu Kleinbuchstaben

        # Validierung der Eingaben
        if geschlecht not in ["m", "w"]:
            raise ValueError("Bitte geben Sie m oder w ein.")
        
        if gewicht <= 0 or groesse <= 0 or alter <= 0:
            raise ValueError("Bitte geben Sie gültige Werte ein.")

        # Rückgabe als Tuple
        return gewicht, groesse, alter, geschlecht
    
    except (ValueError, TypeError) as e:
        print(f"Fehler bei der Eingabe: {e}")
        print("Bitte geben Sie gültige Werte ein.")

def bmi(gewicht, groesse):
    """Berechnet den Body Mass Index"""
    bmi = gewicht/(groesse**2)  # BMI Formel: Gewicht / (Größe²)
    return bmi

def bmi_diagramm(bmi_wert):
    """Erstellt eine visuelle Darstellung der BMI-Kategorien"""
    # Definition der BMI-Grenzen und Kategorien
    skala = [18.5, 25, 30]
    kategorien = ["Unter", "Normal", "Über"]

    # Breiten für konsistente Ausrichtung im ASCII-Diagramm
    breite1 = 10  # Für "Unter" und "18.50"
    breite2 = 11  # Für "Normal" und "25.00"
    breite3 = 11  # Für "Über" und "30.00"

    # Erstellung des ASCII-Diagramms
    bmi_diagramm = f"BMI: {bmi_wert:.2f} {kategorisierung_bmi(bmi_wert)}\n"
    bmi_diagramm += "|" + "-"*breite1 + "|" + "-"*breite2 + "| \n "
    bmi_diagramm += f"{skala[0]:<{breite1}}{skala[1]:<{breite2}}{skala[2]:<{breite3}}\n"
    bmi_diagramm += f"{kategorien[0]:<{breite1}}{kategorien[1]:<{breite2}}{kategorien[2]:<{breite3}}"

    return bmi_diagramm

def kategorisierung_bmi(bmi_wert):    
    """Ordnet den BMI-Wert einer Kategorie zu"""
    if bmi_wert < 18.5:
        return "Untergewicht"
    elif bmi_wert < 24.9:
        return "Normalgewicht"
    else:
        return "ThickBOI"

def grundumsatzformel(gewicht, groesse, alter, geschlecht):
    """Berechnet den Grundumsatz nach Harris-Benedict-Formel"""
    if geschlecht == "m":
        # Formel für Männer
        grundumsatzformel = float(66.5 + (13.75 * gewicht) + (5.003 * groesse) - (6.75 * alter))
    else:
        # Formel für Frauen
        grundumsatzformel = float(655.1 + (9.6 * gewicht) + (1.8 * groesse) - (4.7 * alter))
    return f"{grundumsatzformel:.2f}"

def Kalorienbedarf(grundumsatzformel):
    """Berechnet den Gesamtkalorienbedarf basierend auf Aktivitätslevel"""
    try:
        # Benutzerabfrage für Aktivitätslevel
        PAL = int(input("Wie aktiv sind Sie? \n 1.sitzend(wenig Bewegung) \n 2.Leicht aktiv(1-3x/Woche Sport) \n 3. Moderat aktiv(3-5x/Woche Sport) \n 4. Sehr aktiv(6-7x/Woche Sport) \n 5. Extrem aktiv(2x/Tag Sport)"))
        
        # Validierung der Eingabe
        if PAL not in [1,2,3,4,5]:
            raise ValueError("Bitte geben Sie eine gültige Auswahl ein.")
        
        # PAL-Faktoren für verschiedene Aktivitätslevel
        pal_faktoren = {1:1.2, 2:1.375, 3:1.55, 4:1.725, 5:1.9}
        kalorienbedarf = float(grundumsatzformel) * pal_faktoren[PAL]
        return f"{kalorienbedarf:.2f}"
          
    except ValueError as e:
        print(f"Fehler: {e}")

def vorschlag_mahlzeitenplaners(bmi_wert):
    """Erstellt einen personalisierten Ernährungsplan basierend auf dem BMI"""
    try:
        # Dictionary mit Empfehlungen für jede BMI-Kategorie
        empfehlung = {
            "Untergewicht": "Empfehlung: Erhöhen Sie die Portionsgrößen und ergänzen Sie kalorienreiche, gesunde Snacks.",
            "Normalgewicht": "Empfehlung: Behalten Sie Ihre ausgewogene Ernährung bei.",
            "ThickBOI": "Empfehlung: Reduzieren Sie die Portionsgrößen und wählen Sie kalorienärmere Alternativen."
        }

        # BMI-Kategorisierung
        if bmi_wert < 18.5:
            kategorie = "Untergewicht"
        elif bmi_wert < 24.9:
            kategorie = "Normalgewicht"
        else:
            kategorie = "ThickBOI"
        
        # Formatierung der Ausgabe
        output = "\n Ihr persönlicher Ernährungsplan: \n"
        output += "=" * 40 + "\n"

        # Holt den passenden Mahlzeitenplan
        tagesplan = Mahlzeit_planer.meal_plan[kategorie]

        # Formatiert den Mahlzeitenplan
        for mahlzeit, gerichte in tagesplan.items():
            output += f"{mahlzeit}:\n"
            for gericht in gerichte:
                output += f"- {gericht}\n"
            output += "\n"
        
        output += "=" * 40 + "\n"
        output += f"\nEmpfehlung:{empfehlung[kategorie]}\n"

        return output

    except Exception as e:
        return f"Fehler bei der Erstellung des Mahlzeitenplans: {e}"

def bmi_rechner():
    """Hauptfunktion des Programms"""
    while True:
        # Benutzerinformationen einlesen
        gewicht, groesse, alter, geschlecht = eingaben()

        # Menüauswahl
        print("\nWas möchten Sie tun?")
        print("1. Zusammenfassung anzeigen (1)")
        print("2. Programm beenden (2)")

        try:
            auswahl = int(input("Geben sie ihre ausgewählte Zahl aus: "))
            
            if auswahl == 2:
                print("Programm wird beendet.")
                break
            elif auswahl == 1:
                # Berechnung und Ausgabe aller Werte
                bmi_wert = bmi(gewicht, groesse)
                print(bmi_diagramm(bmi_wert))
                print(f"Ihr Grundumsatz ist {grundumsatzformel(gewicht, groesse, alter, geschlecht)}")
                print(f"Ihr Kalorienbedarf ist {Kalorienbedarf(grundumsatzformel(gewicht, groesse, alter, geschlecht))}")
                print(f"Hier ist Vorschlag für ein ihren Kalorienbedarf {vorschlag_mahlzeitenplaners(bmi_wert)}")
                break
            else:
                raise ValueError("Bitte geben Sie eine gültige Auswahl ein.")
        except (ValueError, KeyboardInterrupt) as e:
            print(f"Fehler: {e}")

# Programmstart
bmi_rechner()