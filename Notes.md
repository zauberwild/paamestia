# Notes

---

## allgemeine Videowiedergabe
- Aufteilung zwischen VLC (exetern) und pygame (intern / mit einzelnen Frames)
- VLC für lange Videos
- pygame für kürzere Videos und alles mit Overlays / alles interaktive

---

## Videowiedergabe via VLC

### Befehle
Starten des Videos:  
`cvlc -f --no-video-title-show  ./<path>`

Enden des Videos / VLC beenden:  
`kill vlc`

### Konsolen-Log:  
`pi@raspberrypi:/media/pi/LEGOUSB/test $ cvlc -f --no-video-title-show  ./color.mov`  
`VLC media player 3.0.11 Vetinari (revision 3.0.11-0-gdc0c5ced72)`  
`[008a4018] dummy interface: using the dummy interface module...`  
`[swscaler @ 0x92c49820] No accelerated colorspace conversion found from yuv420p to rgb24.`  
`pi@raspberrypi:/media/pi/LEGOUSB/test $ `  

---

