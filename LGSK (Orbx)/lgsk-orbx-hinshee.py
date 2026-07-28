# -- coding: utf-8 --

version = 1.1
msfs_mode = 1
icao = "lgsk"

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
def customOffset_StandARC(aircraftData):
    table = {
        0: 0,
        "ARC-D" : 4.9,
        "ARC-E" : 4.9,
        "ARC-F" : 4.9,
    }

    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor) - 0.25)
    except:
        return Distance()


def TerminalNames(name, letter, priority):
    return CustomizedName("%s | Gate %s#§" % (name, letter), priority)


def StandNames(name, letter, priority):
    return CustomizedName("%s | Stand %s#§" % (name, letter), priority)


MASN = StandNames("Main Apron (1A-5)", "", 1)
GASN = StandNames("S Apron (S1-S5)", "S", 2)

parkings = {
    GATE_A: {
        None: (),
        1: (CustomizedName("Main Apron (1A-5) | Stand 1A", 1), customOffset_StandARC),
        3: (MASN, customOffset_StandARC),
        4: (MASN, customOffset_StandARC),
        5: (MASN, customOffset_StandARC),
        "MARS_1": (MASN, customOffset_Stand),
    },
    GATE_B: {
        None: (),
        1: (CustomizedName("Main Apron (1A-5) | Stand 1B", 1), customOffset_StandARC),
    },
    0: {
        None: (),
        2: (MASN, customOffset_Stand),
        "MARS_2A": (MASN, customOffset_Stand),
    },
    S_PARKING: {
        None: (),
        1: (GASN, customOffset_Stand),
        2: (GASN, customOffset_Stand),
        3: (GASN, customOffset_Stand),
        4: (GASN, customOffset_Stand),
        5: (GASN, customOffset_Stand),
    },
}
