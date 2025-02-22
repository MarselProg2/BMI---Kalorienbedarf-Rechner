# Projektaufgabe: Persönlicher Fitness-Tracker

## Beschreibung
Entwickle einen BMI & Kalorienbedarf Rechner in Python, der Benutzern hilft, ihre Fitnessziele zu verfolgen. Der Rechner soll auf Basis der eingegebenen Körperdaten den BMI, Grundumsatz und Gesamtkalorienbedarf berechnen sowie personalisierte Empfehlungen geben.

## Implementierungsschritte

### Woche 1: Grundgerüst
- Erstelle eine Funktion zur Datenerfassung
- Implementiere die BMI-Berechnung mit If-Statements zur Kategorisierung
- Teste die Funktionalität mit verschiedenen Eingabewerten

### Woche 2: Erweiterung
- Implementiere die Grundumsatz-Berechnung
- Füge die Gesamtkalorienbedarf-Berechnung hinzu
- Erstelle ein Benutzermenü für verschiedene Optionen
- Implementiere Fehlerbehandlung für ungültige Eingaben

## Bonusaufgaben
- Grafische Darstellung der Ergebnisse mit einfachen ASCII-Diagrammen
- Implementierung eines einfachen Mahlzeitenplaners basierend auf dem Kalorienbedarf


def Vorschlag_Mahlzeitenplaners(bmi_wert):
    try:
        empfehlung = ""
        if bmi_wert < 18.5:
            empfehlung = "\nEmpfehlung: Erhöhen Sie die Portionsgrößen und ergänzen Sie "
            empfehlung += "kalorienreiche, gesunde Snacks.\n"
            return Mahlzeit_planer.meal_plan["Untergewicht"] + empfehlung
        elif bmi_wert < 24.9:
            empfehlung = "\nEmpfehlung: Behalten Sie Ihre ausgewogene Ernährung bei.\n"
            return Mahlzeit_planer.meal_plan["Normalgewicht"] + empfehlung
        else:
            empfehlung = "\nEmpfehlung: Reduzieren Sie die Portionsgrößen und "
            empfehlung += "wählen Sie kalorienärmere Alternativen.\n"
            return Mahlzeit_planer.meal_plan["Übergewicht"]+ empfehlung

    except Exception as e:
        return f"Fehler bei der Erstellung des Mahlzeitenplans: {e}"
    #except Exception as e: fängt alle Fehler ab, die nicht durch die anderen except-Blöcke abgefangen wurden