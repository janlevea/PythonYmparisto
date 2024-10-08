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


# Henkilötunnus esimerkki 130728-478N testataan
# 1. Pituus
# 2. Syntymäaikaosan oikeellisuus
# 3. Vuosisatakoodit +, - ja A
# 4. Modulo 31 tarkistus

# Lopullisena tavoitteena on funktio, joka tarkistaa henkilötunnuksen oikeellisuuden ja palauttaa virhekoodin ja virheilmoituksen, joka kertoo mikä vika HeTu:ssa on. Esim 0, OK tai 1, tunnus liian lyhyt tai 3, tunnus liian pitkä jne.

def checkHeTu(hetu):

    # Oletustulos 0 OK jos kaikki on kunnossa
    result = (0, 'OK')

    # Vuosisatakoodien sanakirja
    centuryCodes = {
        '+': 1800,
        '-': 1900,
        'A': 2000
    }

    validCenturyCodes = centuryCodes.keys()

    # Sanakirja, jossa on jakojäännösten kirjaintunnukset
    modulusSymbols = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
        16: 'H',
        17: 'J',
        18: 'K',
        19: 'L',
        20: 'M',
        21: 'N',
        22: 'P',
        23: 'R',
        24: 'S',
        25: 'T',
        26: 'U',
        27: 'V',
        28: 'W',
        29: 'X',
        30: 'Y'
    }
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

        # Jos muuta kuin pelkkiä numeroita
        else:
            result = (3, 'Päivä virheellinen')

        # Tarkistetaan kuukausiosan oikeellisuus, pitää olla pelkkiä numeroita
        if monthPart.isdigit():
            month = int(monthPart)

            # Kuukausi pitää olla väliltä 1 - 12
            if month < 1:
                result = (4, 'Kuukausi virheellinen')
            if month > 12:
                result = (4, 'Kuukausi virheellinen')

        # Jos muuta kuin pelkkiä numeroita
        else:
            result = (4, 'Kuukausi virheellinen')

        # Tarkistetaan kuukausiosan oikeellisuus, pitää olla pelkkiä numeroita
        if yearPart.isdigit():
            year = int(yearPart)
        else:
            result = (5, "Vuosi virheellinen")

        # Tarkistetaan vuosisatakoodi
        try:
            position = list(validCenturyCodes).index(centuryPart)
        except :
            result = (6, 'Vuosisatakoodi virheellinen')

        # Lasketaan modulo 31 tarkiste ja verrataan sitä syötetyn HeTu:n tarkisteeseet
        partsCombined = dayPart + monthPart + yearPart + numberPart
        
        if partsCombined.isdigit() and result == (0, 'OK') :
            checkSumCalculated = int(partsCombined)%31
            if checkSum != modulusSymbols[checkSumCalculated]:
                result = (7, 'Varmistussumma ei täsmää')

    if length < 11:
        result = (1, 'Henkiötunnus liian lyhyt')

    if length > 11:
        result = (2, 'Henkilötunnus liian pitkä')

    return result

# TODO: Poista loput rivit, kun valmista!
# KOKEILLAAN ERILAISIA VAIHTOEHTOJA
# ---------------------------------

if __name__ == "__main__":
    pass