# Notes

## allgemein: Videowiedergabe
- Aufteilung zwischen VLC (extern) und pygame (intern / mit einzelnen Frames)
- VLC für lange Videos
- pygame für kürzere Videos und alles mit Overlays / alles interaktive

## Videowiedergabe via VLC

### Befehle (Linux):

Starten des Videos:  
`cvlc -f --no-video-title-show --play-and-exit ./<path> &`

Enden des Videos / VLC beenden:  
`killall vlc`

### Befehle (Windows):

Starten des Videos:  
`C:"\Program Files\VideoLAN\VLC\vlc.exe" --no-video-title-show --play-and-exit ./<path>`

Enden des videos / VLC beenden:

`TASKKILL /IM VLC.EXE`  (nicht notwendig, vlc beendet von selbst)

### Umsetzung in Python:
`import os`  
`os.system(<command>)`  

`killall vlc` muss zeitverzögert ausgeführt, werden um den vlc-Prozess zu
killen, wenn das Video fertig abgepielt wurde.
Benötigt:  

- `time`-Modul
- `time.time` zum Zeitmessen

---

## Opencv Notizen

### Packages installieren mit:

`pip install opencv-python`
`pip install numpy==1.19.3`

### misc.

