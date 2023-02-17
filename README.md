# Mousetrack

Version 1.0.0
    grundlegender Code erstellt:
        einfache GUI, mit Buttons ohne Funktionalität

Version 1.0.1            
        pynput eingefügt
            start button startet Anwendung
            stopp button stoppt Anwendung (kein Restart möglich(Threading))
Version 1.0.2
    Änderung der Code Reihenfolge

Version 1.0.3
    Bewegungs und Klick Daten werden in txt-File gespeichert
    Zeitpunkt, relativ zum Start des Listeners, an denen das Event stattfindet ist gespeichert

Version 1.0.4
    bei Beenden des Listeners (Stopp Button) werden 2 Heatmaps angezeigt
        1. Heatmap der movement data
        2. Heatmap der click data

Version 1.0.5
    Geschwindigkeit wird berechnet
    1. in direction x and y
    Geschwindigkeitsberechnung

Version 1.0.6
    die zuvor hinzugefügten Features werden in ein GUI eingefügt
        1. Seite 1 zur Informationsabfrage Seite 3
        
Version 1.0.7
    1. Quit Button hinzugefügt
    2. Heatmap mit Zufallszahlen wird in GUI Seite 5 eingebunden
        Button ermöglicht Anzeigen der Heatmap der Moves

Version 1.0.8
    1.Threading
        Listener kann mehrere Male gestartet werden
    2.Heatmap
        zwischen Heatmaps der Moves und Klicks kann über Button gewechselt 
        
Version 1.0.9
    1. Tracking nur auf einem Bildschirm
        Heatmap wird auf Screenshot des Bildschirms erstellt

Version 1.1.0
    1. Bewegunstrajektorie als Heatmap erkennbar
