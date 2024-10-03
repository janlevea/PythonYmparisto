# MODUULI OPISKELIJANUMERON JA HENKILÖTUNNUKSEN TARKISTUKSEEN
# ===========================================================

"""Module makes sanity checks for Raseko student id and the Finnish Social Security Number
    """

# KIRJASTOT JA MODUULIT
# ---------------------

# FUNKTIOT
# --------

# Opiskelijatunnuksen oikea muoto
def opiskelijanumeroOk(opiskelijanumero: str) -> bool:
    """Checks if student number is 5 or 6 digits and does not contain any characters other than numerics

    Args:
        opiskelijanumero (str): Raseko's student id

    Returns:
        bool: True if correct otherwise False
    """
    result: bool = False
    pituus = len(opiskelijanumero)
    if pituus == 5 or pituus == 6:
        if opiskelijanumero.isdigit():
            result = True
    return result

# TODO: Tee testit HeTu:a varten ja vasta sitten kirjoita koodi

# Henkilötunnus esimerkki 130728-478N testataan
# 1. Pituus
# 2. Syntymäaikaosan oikeellisuus
# 3. Vuosisatakoodit +, - ja A
# 4. Modulo 31 tarkistus

# Lopullisena tavoitteena on funktio, joka tarkistaa henkilötunnuksen oikeellisuuden ja palauttaa virhekoodin ja virheilmoituksen, joka kertoo mikä vika HeTu:ssa on. Esim 0, OK tai 1, tunnus liian lyhyt tai 3, tunnus liian pitkä jne.

def checkHeTu(hetu):

    # Oletustulos 0 OK jos kaikki on kunnossa
    result = (0, 'OK')

    # Lasketaan HeTu-parametrin pituus
    length = len(hetu)

    # Jos pituus oikea tehdään eri osat
    if length == 11:
        dayPart = hetu[0:2]
        monthPart = hetu[2:4]
        yearPart = hetu[4:6]
        centuryPart = hetu[6:7]
        numberPart = hetu[7:10]
        checkSum = hetu[10]

        # Tarkistetaan päiväosan oikeellisuus, pitää olla pelkkiä numeroita
        if dayPart.isdigit():
            day = int(dayPart)
            
            # Päivän pitää olla väliltä 1 - 31 
            if day < 1:
                result = (3, 'Päivä virheellinen')
            if day > 31:
                result = (3, 'Päivä virheellinen')
        else:
            # Jos muuta kuin pelkkiä numeroita
            result = (3, 'Päivä virheellinen')


    if length < 11:
        result = (1, 'Henkiötunnus liian lyhyt')

    if length > 11:
        result = (2, 'Henkilötunnus liian pitkä')

    
    return result

if __name__ == "__main__":
    hetu = '130728-478N'
    paivat = hetu[0:2]
    kuukaudet = hetu[2:4]
    print(paivat)
    print(kuukaudet)