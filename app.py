# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

import sound # Äänimerkit ja äänitiedostot
import video # Videomoduuli

# ASETUKSET
# ---------
kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0

# Käynnistetään videokuva ja ilmoitetaan sen käynnistymisestä äänimerkillä
sound.parametricBeep(400,330)
sound.playWav('Alkaa.WAV')

# TESTIT KOODAUKSEN AIKANA
# ========================

if __name__ == "__main__":
    pass