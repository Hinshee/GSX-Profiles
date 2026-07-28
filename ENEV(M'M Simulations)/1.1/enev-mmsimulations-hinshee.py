# -- coding: utf-8 --

version = 1.1
msfs_mode = 1
icao = "enev"

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
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
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
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

def TerminalNames(name, letter, priority):
	return CustomizedName( "%s | Gate %s#§" % (name, letter), priority )
  
def StandNames(name, letter, priority):
    return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
    
def NC_StandNames(name, letter, priority):
    return CustomizedName( "%s | Stand %s#§ - Not Customised" % (name, letter), priority )
    
def DIS_StandNames(name, letter, priority):
    return CustomizedName( "%s | [Disabled] Stand %s#§" % (name, letter), priority )
    
TASN = StandNames("Terminal Apron (21-30)", "", 1)
TASN_DIS = DIS_StandNames("Terminal Apron (21-30)", "", 1)
MAWSN = NC_StandNames("Mil Apron West", "", 2)
MAESN = NC_StandNames("Mil Apron East", "", 3)
LSASA = NC_StandNames("Line South Apron", "", 4)

parkings = {
    GATE_P: {
        None: ( ),
        1 : (MAWSN, customOffset_Gate),
        2 : (MAWSN, customOffset_Gate),
        3 : (MAWSN, customOffset_Gate),
        4 : (MAWSN, customOffset_Gate),
        5 : (MAWSN, customOffset_Gate),
    },
    PARKING: {
        None: ( ),
        1 : (MAESN, customOffset_Stand),
        2 : (MAESN, customOffset_Stand),
        3 : (MAESN, customOffset_Stand),
        30 : (TASN, customOffset_Gate),
        29 : (TASN, customOffset_Gate),
        28 : (TASN, customOffset_Gate),
        27 : (TASN, customOffset_Gate),
        26 : (TASN, customOffset_Gate),
        "26B" : (TASN, customOffset_Gate),
        "26C" : (TASN, customOffset_Gate),
        25 : (TASN, customOffset_Stand),
        24 : (TASN, customOffset_Stand),
        23 : (TASN, customOffset_Stand),
        22 : (TASN, customOffset_Stand),
        21 : (TASN, customOffset_Stand),
        101 : (TASN_DIS, customOffset_Stand),
    },
    NE_PARKING: {
        None: ( ),
        2 : (LSASA, customOffset_Stand),
        3 : (LSASA, customOffset_Stand),
        4 : (LSASA, customOffset_Stand),
    },
}