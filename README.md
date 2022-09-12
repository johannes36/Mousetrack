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
