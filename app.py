# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT JA MODUULIT
# ---------------------

# OpenCV-kirjasto videokameraa varten
# import cv2

# Winsound-kirjasto äänikorttia varten
import winsound

# ASETUKSET
# ---------

kameraIndeksi = 1 # Ensimmäinen kamera on aina 0

# Funktiot

def piippaa():
    """Tuottaa puolen sekunnin 1 kHz äänimerkin
    """
    taajuus = 1000 # Hz
    kesto = 500 # ms
    winsound.Beep(taajuus, kesto)

piippaa()