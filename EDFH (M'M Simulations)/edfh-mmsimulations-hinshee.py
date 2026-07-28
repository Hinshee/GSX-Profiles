# -- coding: utf-8 --

version = 1.1
msfs_mode = 1
icao = "edfh"

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


def StandNames(name, letter, priority):
    return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
    
Apron3 = StandNames("Apron 3 (311-351)", "", 1)
Apron4 = StandNames("Apron 4 (411-451)", "", 2)
Apron5 = StandNames("Apron 5", "", 3)

parkings = {
    0: {
        None: ( ),
            311: (Apron3, customOffset_Stand),
            312: (Apron3, customOffset_Stand),
            313: (Apron3, customOffset_Stand),
            314: (Apron3, customOffset_Stand),
            315: (Apron3, customOffset_Stand),
            316: (Apron3, customOffset_Stand),
            322: (Apron3, customOffset_Stand),
            323: (Apron3, customOffset_Stand),
            324: (Apron3, customOffset_Stand),
            325: (Apron3, customOffset_Stand),
            331: (Apron3, customOffset_Stand),
            332: (Apron3, customOffset_Stand),
            333: (Apron3, customOffset_Stand),
            341: (Apron3, customOffset_Stand),
            351: (Apron3, customOffset_Stand),
            411: (Apron4, customOffset_Stand),
            421: (Apron4, customOffset_Stand),
            431: (Apron4, customOffset_Stand),
            441: (Apron4, customOffset_Stand),
            521: (Apron5, customOffset_Stand),
            522: (Apron5, customOffset_Stand),
    },
}