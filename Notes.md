# Notes

---

## allgemeine Videowiedergabe
- Aufteilung zwischen VLC (extern) und pygame (intern / mit einzelnen Frames)
- VLC für lange Videos
- pygame für kürzere Videos und alles mit Overlays / alles interaktive

---

## Videowiedergabe via VLC

### Befehle (Linux):
Starten des Videos:  
`cvlc -f --no-video-title-show  ./<path> &`

Enden des Videos / VLC beenden:  
`killall vlc`

### in Python:
`import os`  
`os.command(<command>)`  

´killall vlc´ muss zeitverzögert ausgeführt, werden um den vlc-Prozess zu
killen, wenn das fertig abgepielt wurde.
Benötigt:  
- `time`-Modul
- `time.time` zum Zeitmessen

---

