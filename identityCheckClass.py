# MODUULI HENKILÖTUNNUKSEN TARKISTUKSEEN
# ======================================
# Module that makes sanity checks for Finnish Social Security Number.

# KIRJASTOT JA MODUULIT
# ---------------------
import datetime

# TODO: Modulo 31 checksum

# LUOKAT
# --------
class NationalSSN:
    """Class with methods for social security numbers
    """
    def __init__(self, ssn: str):
        """

        Args:
            ssn (str): Social security number to use
        """
        self.ssn = ssn
        self.dateOfBirth: str = self.getDateOfBirthFin() # taken from ssn
        self.age: int = self.calculateAge() # age as whole number (full years)
        self.gender: str = self.getGender() # Male or Female, calculated from the last 3 numbers in ssn
        self.checksum: str # modulo 31 checksum

    def getDateOfBirthFin(self) -> str: # get date of birth from ssn
        # TODO: Pull date of birth from ssn
        dayPart = self.ssn[0:2]
        monthPart = self.ssn[2:4]
        birthYear = self.getBirthYear()

        dateOfBirth = f"{dayPart}.{monthPart}.{birthYear}"
        return dateOfBirth
    
    def getDateOfBirthIso(self) -> str:
        dayPart = self.ssn[0:2]
        monthPart = self.ssn[2:4]
        birthYear = self.getBirthYear()
        dateOfBirth = f"{birthYear}-{monthPart}-{dayPart}"
        return dateOfBirth

    def getBirthYear(self):
        yearPart = self.ssn[4:6]
        centuryPart = self.ssn[6:7]
        if centuryPart == "+":
            yearPart = "18" + yearPart
        elif centuryPart == "-":
            yearPart = "19" + yearPart
        elif centuryPart == "A":
            yearPart = "20" + yearPart
        return int(yearPart)

    def calculateAge(self) -> int: # calculate age, full years from ssn
        birthDate = datetime.date.fromisoformat(self.getDateOfBirthIso())
        currentDate = datetime.date.today()
        self.age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))
        return self.age
    
    def getGender(self) -> str:
        numberPart = self.ssn[7:10]
        numberPart = int(numberPart)
        print(numberPart)
        if numberPart % 2 == 0:
            gender = "Female"
        else:
            gender = "Male"
        self.gender = gender
        return gender

    def checkSsnLengthOk(self) -> bool:
        ssnLength = len(self.ssn)
        if ssnLength != 11:
            return False
        else: 
            return True
        
    # Pilkotaan hetu osiin ja palautetaan osat dictionaryna
    def splitSsn(self):
        if not self.checkSsnLengthOk():
            return {'status': 'error'}
        
        splitSsn = {
            "days": self.ssn[0:2], 
            "months": self.ssn[2:4], 
            "years": self.ssn[4:6],
            "century": self.ssn[6:7],
            "number": self.ssn[7:10],
            "checkSum": self.ssn[10]
        }

        return splitSsn



    def checkSsn(self, ssn):
        # Henkilötunnus esimerkki 130728-478N testataan
        # 1. Pituus
        # 2. Syntymäaikaosan oikeellisuus
        # 3. Vuosisatakoodit +, - ja A
        # 4. Modulo 31 tarkistus

        # Lopullisena tavoitteena on funktio, joka tarkistaa henkilötunnuksen oikeellisuuden ja palauttaa virhekoodin ja virheilmoituksen
        # joka kertoo mikä vika HeTu:ssa on. Esim 0, OK tai 1, tunnus liian lyhyt tai 3, tunnus liian pitkä jne.

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
        # Jos pituus väärä, poistutaan returnilla
        if self.checkSsnLengthOk() == False:
            return

        splitSsn = self.splitSsn()

        # Tarkistetaan päiväosan oikeellisuus, pitää olla pelkkiä numeroita
        if splitSsn["days"].isdigit():
            day = int(splitSsn["days"])

            # Päivän pitää olla väliltä 1 - 31
            if day < 1:
                result = (3, 'Päivä virheellinen')
            if day > 31:
                result = (3, 'Päivä virheellinen')

        # Jos muuta kuin pelkkiä numeroita
        else:
            result = (3, 'Päivä virheellinen')

        # Tarkistetaan kuukausiosan oikeellisuus, pitää olla pelkkiä numeroita
        if splitSsn["months"].isdigit():
            month = int(splitSsn["months"])

            # Kuukausi pitää olla väliltä 1 - 12
            if month < 1:
                result = (4, 'Kuukausi virheellinen')
            if month > 12:
                result = (4, 'Kuukausi virheellinen')

        # Jos muuta kuin pelkkiä numeroita
        else:
            result = (4, 'Kuukausi virheellinen')

        # Tarkistetaan kuukausiosan oikeellisuus, pitää olla pelkkiä numeroita
        if splitSsn["years"].isdigit():
            year = int(splitSsn["years"])
        else:
            result = (5, "Vuosi virheellinen")

        # Tarkistetaan vuosisatakoodi
        try:
            position = list(validCenturyCodes).index(splitSsn["century"])
        except :
            result = (6, 'Vuosisatakoodi virheellinen')

        # Lasketaan modulo 31 tarkiste ja verrataan sitä syötetyn HeTu:n tarkisteeseet
        partsCombined = splitSsn["days"] + splitSsn["months"] + splitSsn["years"] + splitSsn["number"]
        
        if partsCombined.isdigit() and result == (0, 'OK') :
            checkSumCalculated = int(partsCombined)%31
            if splitSsn["checkSum"] != modulusSymbols[checkSumCalculated]:
                result = (7, 'Varmistussumma ei täsmää')

        # if length < 11:
        #     result = (1, 'Henkiötunnus liian lyhyt')

        # if length > 11:
        #     result = (2, 'Henkilötunnus liian pitkä')

        return result

    def isValid(self) -> bool: # check if ssn is correct
        if self.checkSsn(self.ssn) == (0, "OK"):
            return True
        else:
            return False 

# KOKEILLAAN ERILAISIA VAIHTOEHTOJA
# ---------------------------------
if __name__ == "__main__":
    sepe = NationalSSN("130728-478N")
    # sepe_syntymaaika = sepe.getDateOfBirth()
    
    print(sepe.getDateOfBirthFin())
    print(datetime.date.today())
    print(sepe.getDateOfBirthIso())
    print(sepe.calculateAge())
    print(sepe.getGender())
