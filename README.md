# Mousetrack

Version 1.0.0
    grundlegender Code erstellt:
        simples GUI

Version 1.0.1
    basic code finished
    
    Overview:
        basic GUI existing:
            Start and Stop Button with function
        
        pynput included
            start pressed Tracking starts
            stop pressed tracking stops completely (cannot be restarted cause "threads can only be started once")

Version 1.0.2
    sequence changed (functions before "main" code)

Version 1.0.3
    movement and click data are saved in txt-File
    Zeitpunkt, relativ zum Start des Listeners, an denen das Event stattfindet ist gespeichert

Version 1.0.4
    bei Beenden des Listeners (Stopp Button) werden 2 Heatmaps angezeigt
        1. Heatmap der movement data
        2. Heatmap der click data

Version 1.0.5
    Velocity is calculated
    1. in direction x and y

Version 1.0.6
    die zuvor hinzugefügten Features werden in ein GUI eingefügt
        1. Seite 1 zur Informationsabfrage
        2. Seite 2 zum Vornehmen von Einstellungen und Starten der Anwendung
        3. Seite 3
        4. Seite 4

Version 1.0.7
    1. Quit Button hinzugefügt
    2. Heatmap mit Zufallszahlen wird in GUI Seite 5 eingebunden
        Button ermöglicht Anzeigen der Heatmap der Moves

Version 1.0.8
    1.Threading
        Listener kann multiple Times gestartet werden
    2.Heatmap
        zwischen Heatmaps der Moves und Klicks kann über Button gewechselt werden

                # Zukunft: 
                3. Seite 3 nach Ende des Trackings, die die Möglichkeit bietet die getrackten Parameter darzustellen (Heatmap,...) 
                Es gibt nun die Möglickeit genau auszuwählen, was mit den Daten im Nachhinein geschieht
                # 3. Live Seite während des Trackings mit Timer und Stop
