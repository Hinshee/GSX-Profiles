# -- coding: utf-8 --

icao = "lgkv"
version = 1
msfs_mode = 1

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
def customOffset_CDGap(aircraftData):
	table = {
		"Unknown": 0,
		"ARC-B": 0,
        "ARC-C": 3.2,
        "ARC-D": 9,
        "ARC-E": 11.5,
        "ARC-F": 15.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.aircraftGroup)  - 0.25 )
	except:
		return Distance()

def StandNames(name, letter, priority):
	return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
  
MASN = StandNames("Main Apron", "", 1)
GASN = StandNames("GA Apron", "", 2)
MILSN = StandNames("Military Apron", "", 3)

parkings = {
    0: {
        None: ( ),
            1 : (MASN, customOffset_Stand),
            2 : (MASN, customOffset_Stand),
            "2A" : (MASN, customOffset_Stand),
            "2B" : (MASN, customOffset_Stand),
            3 : (MASN, customOffset_Stand),
            4 : (MASN, customOffset_Stand),
            5 : (MASN, customOffset_Stand),
            6 : (MASN, customOffset_Stand),
            "1E" : (GASN, customOffset_Stand),
            "2E" : (GASN, customOffset_Stand),
            "3E" : (GASN, customOffset_Stand),
            "4E" : (GASN, customOffset_Stand),
            "5E" : (GASN, customOffset_Stand),
            "6E" : (GASN, customOffset_Stand),
            "7E" : (GASN, customOffset_Stand),
            "8E" : (GASN, customOffset_Stand),
            "9E" : (GASN, customOffset_Stand),
            "10E" : (GASN, customOffset_Stand),
            "11E" : (GASN, customOffset_Stand),
            "12E" : (GASN, customOffset_Stand),
            "13E" : (GASN, customOffset_Stand),
            "14E" : (GASN, customOffset_Stand),
            "15E" : (GASN, customOffset_Stand),
            "16E" : (GASN, customOffset_Stand),
            "17E" : (GASN, customOffset_Stand),
            "18E" : (GASN, customOffset_Stand),
            "19E" : (GASN, customOffset_Stand),
            "20E" : (GASN, customOffset_Stand),
            "21E" : (GASN, customOffset_Stand),
            "22E" : (GASN, customOffset_Stand),
            "23E" : (GASN, customOffset_Stand),
            "24E" : (GASN, customOffset_Stand),
            "25E" : (GASN, customOffset_Stand),
    },
    GATE_M: {
        None: ( ),
            1 : (MILSN, customOffset_Stand),
            2 : (MILSN, customOffset_Stand),
            3 : (MILSN, customOffset_Stand),
            4 : (MILSN, customOffset_Stand),
            5 : (MILSN, customOffset_Stand),
            6 : (MILSN, customOffset_Stand),
            7 : (MILSN, customOffset_Stand),
            8 : (MILSN, customOffset_Stand),
            9 : (MILSN, customOffset_Stand),
            10 : (MILSN, customOffset_Stand),
            11 : (MILSN, customOffset_Stand),
            12 : (MILSN, customOffset_Stand),
            13 : (MILSN, customOffset_Stand),
            14 : (MILSN, customOffset_Stand),
    },
}