# -- coding: utf-8 --

msfs_mode = 1
icao = "entc"

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
  
MainApronNames = TerminalNames("Main Apron", "", 1)
MainApronStandNames = StandNames("Main Apron", "", 1)
NorthApronNames = StandNames("North (De-ice) Apron", "", 2)

parkings = {
    GATE: {
        None: ( ),
			23 : (MainApronNames, customOffset_Gate),
	},
    0: {
        None: ( ),
            16 : (MainApronStandNames, customOffset_Stand),
            17 : (MainApronStandNames, customOffset_Stand),
            18 : (MainApronNames, customOffset_Gate),
            19 : (MainApronNames, customOffset_Gate),
            20 : (MainApronNames, customOffset_Gate),
            21 : (MainApronNames, customOffset_Gate),
            22 : (MainApronNames, customOffset_Gate),
            24 : (MainApronStandNames, customOffset_Stand),
            25 : (MainApronStandNames, customOffset_Stand),
    },
    W_PARKING: {
        None: ( ),
            2 : (NorthApronNames, customOffset_Stand),
    },
}