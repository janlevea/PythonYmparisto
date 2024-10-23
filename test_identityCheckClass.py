# Testataan modulin identityCheckClass toimivuus
import identityCheckClass

testitunnusOk = identityCheckClass.NationalSSN("130728-478N")
#testitunnusLyhyt = identityCheckClass.NationalSSN("130728478N")
#testitunnusPitka = identityCheckClass.NationalSSN("130728-4781N")


def test_getDateOfBirthFin():
    assert testitunnusOk.getDateOfBirthFin() == "13.07.1928"

def test_getDateOfBirthIso():
    assert testitunnusOk.getDateOfBirthIso() == "1928-07-13"

def test_getBirthYear():
    assert testitunnusOk.getBirthYear() == 1928

def test_calculateAge():
    assert testitunnusOk.calculateAge() == 96

def test_getGender():
    assert testitunnusOk.getGender() == "Female"

def test_checkSsnLengthOk():
    assert testitunnusOk.checkSsnLengthOk() == True

def test_splitSsn():
    assert testitunnusOk.splitSsn() == {
        "days": "13",
        "months": "07",
        "years": "28",
        "century": "-",
        "number": "478",
        "checkSum": "N"
    }

def test_checkSsn():
    assert testitunnusOk.checkSsn("130728-478N") == (0, "OK")

def test_isValid():
    assert testitunnusOk.isValid() == True