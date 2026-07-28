# -- coding: utf-8 --

version = 1
msfs_mode = 1
icao = "katw"

# ==============================
# Default Offsets
# ==============================


@AlternativeStopPositions
def customOffset_Stand(aircraftData):
    table = {
        0: 0,
        318: 0,
        319: 0,
        320: 0,
        321: 0,
        737: 0,
    }

    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor) - 0.25)
    except:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate(aircraftData):
    table = {
        0: 0,
        318: 0,
        319: 0,
        320: 0,
        321: 0,
        737: 0,
    }

    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor) - 0.25)
    except:
        return Distance()


# ==============================
# Custom Offsets Per Stand/Gate
# ==============================


@AlternativeStopPositions
def customOffset_Gate1A(aircraftData):
    table = {0: 0, 717: 5.5, 321: 2.7}

    table737 = {8: 2.7, 9: 5.5}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate2(aircraftData):
    table = {
        0: 0,
        717: 2.3,
        321: 2.3,
        221: 2.3,
        223: 2.3,
        200: 2.3,
        700: 2.3,
        900: 2.3,
        140: 4.4,
        145: 4.4,
    }

    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate3(aircraftData):
    table = {0: 0, 140: 3.6, 145: 3.6, 200: 3.6, 700: 3.6, 900: 7}

    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate4(aircraftData):
    table = {
        0: 0,
        321: 1.9,
        200: 1.9,
        700: 1.9,
        900: 1.9,
        221: 1.9,
        223: 1.9,
        757: 1.9,
        140: 3,
        145: 3,
    }

    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate5(aircraftData):
    table = {0: 0, 717: 5.5, 321: 5.5, 221: 2.7, 223: 2.7}

    table737 = {7: 1.8, 8: 3.5, 9: 5.5}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate6(aircraftData):
    table = {
        0: 0,
        221: 1.8,
        223: 1.8,
        140: 3.7,
        145: 3.7,
        200: 3.7,
        700: 3.7,
        900: 3.7,
        717: 3.7,
        312: 3.7,
    }

    table737 = {7: 1.8, 8: 3.7, 9: 3.7}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate7(aircraftData):
    table = {
        0: 0,
        717: 3.6,
        321: 3.6,
        221: 2.3,
        223: 2.3,
        200: 2.3,
        700: 2.3,
        900: 2.3,
        140: 2.3,
        145: 2.3,
    }

    table737 = {7: 2.3, 8: 3.6, 9: 3.6}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate8(aircraftData):
    table = {
        0: 0,
        717: 3.6,
        321: 3.6,
        221: 2.3,
        223: 2.3,
        200: 2.3,
        700: 2.3,
        900: 2.3,
        140: 2.3,
        145: 2.3,
    }

    table737 = {7: 2.3, 8: 3.6, 9: 3.6}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate9A(aircraftData):
    table = {0: 0, 140: 5.8, 145: 5.8, 200: 5.8, 700: 5.8, 900: 5.8, 717: 5.8}

    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate9(aircraftData):
    table = {0: 0, 221: 2.9, 223: 2.9, 717: 4.8, 312: 4.8}

    table737 = {7: 2.9, 8: 4.8, 9: 4.8}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate10A(aircraftData):
    table = {0: 0, 717: 2.3, 321: 3.6, 200: 2.3, 700: 2.3, 900: 2.3, 140: 2.3, 145: 2.3}

    table737 = {7: 0, 8: 2.3, 9: 3.6}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate10(aircraftData):
    table = {
        0: 0,
        221: 2.3,
        223: 2.3,
        717: 3.6,
        321: 3.6,
        200: 2.3,
        700: 2.3,
        900: 2.3,
        140: 2.3,
        145: 2.3,
    }

    table737 = {7: 2.3, 8: 3.6, 9: 3.6}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate11(aircraftData):
    table = {0: 0, 717: 3.8, 321: 3.8, 200: 3.8, 700: 3.8, 900: 3.8, 140: 3.8, 145: 3.8}

    table737 = {7: 0, 8: 1.7, 9: 3.8}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


@AlternativeStopPositions
def customOffset_Gate12(aircraftData):
    table = {0: 0, 717: 3.7, 321: 3.7, 200: 3.7, 700: 3.7, 900: 3.7, 140: 3.7, 145: 3.7}

    table737 = {7: 0, 8: 1.6, 9: 3.7}

    try:
        if aircraftData.idMajor == 737:
            return Distance.fromMeters(table737.get(aircraftData.idMinor, 0) - 0.25)
        else:
            return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
    except Exception:
        return Distance()


def TerminalNames(name, letter, priority):
    return CustomizedName("%s | Gate %s#§" % (name, letter), priority)


def StandNames(name, letter, priority):
    return CustomizedName("%s | Stand %s#§" % (name, letter), priority)


def NC_StandNames(name, letter, priority):
    return CustomizedName("%s | [NC] Stand %s#§" % (name, letter), priority)


def DIS_StandNames(name, letter, priority):
    return CustomizedName("%s | [Disabled] Stand %s#§" % (name, letter), priority)


TATN = TerminalNames("Main Terminal (1-12)", "", 1)
FASN = StandNames("FedEx Apron (Taxiway H)", "", 2)
GNEASN = StandNames("Gulfstream NE Apron", "", 3)
FBO_S = NC_StandNames("Appleton Flight Center (FBO)", "South ", 4)
FBO_W = NC_StandNames("Appleton Flight Center (FBO)", "West ", 4)
DIS = DIS_StandNames("Main Terminal (1-12)", "", 1)

parkings = {
    0: {
        None: (),
        1: (TATN, customOffset_Gate),
        "1A": (TATN, customOffset_Gate1A),
        "1D": (DIS, customOffset_Gate),
        "1G": (GNEASN, customOffset_Stand),
        "2G": (GNEASN, customOffset_Stand),
        "2D": (DIS, customOffset_Gate),
        "3G": (GNEASN, customOffset_Stand),
        "3D": (DIS, customOffset_Gate),
        "4G": (GNEASN, customOffset_Stand),
        "5G": (GNEASN, customOffset_Stand),
        2: (TATN, customOffset_Gate2),
        3: (TATN, customOffset_Gate3),
        4: (TATN, customOffset_Gate4),
        5: (TATN, customOffset_Gate5),
        6: (TATN, customOffset_Gate6),
        7: (TATN, customOffset_Gate7),
        8: (TATN, customOffset_Gate8),
        9: (TATN, customOffset_Gate9),
        "9A": (TATN, customOffset_Gate9A),
        10: (TATN, customOffset_Gate10),
        "10A": (TATN, customOffset_Gate10A),
        11: (TATN, customOffset_Gate11),
        12: (TATN, customOffset_Gate12),
    },
    GATE_A: {
        None: (),
        "1A": (FASN, customOffset_Stand),
        "1B": (FASN, customOffset_Stand),
        1: (FASN, customOffset_Stand),
    },
    S_PARKING: {
        None: (),
        "1G": (FBO_S, customOffset_Stand),
        "2G": (FBO_S, customOffset_Stand),
        "3G": (FBO_S, customOffset_Stand),
        "4G": (FBO_S, customOffset_Stand),
        "5G": (FBO_S, customOffset_Stand),
        "6G": (FBO_S, customOffset_Stand),
        "7G": (FBO_S, customOffset_Stand),
        "8G": (FBO_S, customOffset_Stand),
        "9G": (FBO_S, customOffset_Stand),
        "10G": (FBO_S, customOffset_Stand),
        "11G": (FBO_S, customOffset_Stand),
        "12G": (FBO_S, customOffset_Stand),
        "13G": (FBO_S, customOffset_Stand),
        "14G": (FBO_S, customOffset_Stand),
    },
    W_PARKING: {
        None: (),
        "1G": (FBO_W, customOffset_Stand),
        "2G": (FBO_W, customOffset_Stand),
        "3G": (FBO_W, customOffset_Stand),
        "4G": (FBO_W, customOffset_Stand),
        "5G": (FBO_W, customOffset_Stand),
        "6G": (FBO_W, customOffset_Stand),
        "7G": (FBO_W, customOffset_Stand),
    },
}
