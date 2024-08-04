# -- coding: utf-8 --

msfs_mode = 1
icao = "kjac"

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

def TerminalNames(name, letter, priority):
	return CustomizedName( "%s | Gate %s#§" % (name, letter), priority )

def StandNames(name, letter, priority):
	return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
  
MainApronNames = TerminalNames("Commercial Apron", "", 1)

parkings = {
    0: {
        None: ( ),
			1 : (MainApronNames, customOffset_Stand),
			2 : (MainApronNames, customOffset_Stand),
			3 : (MainApronNames, customOffset_Stand),
			4 : (MainApronNames, customOffset_Stand),
			5 : (MainApronNames, customOffset_Stand),
			6 : (MainApronNames, customOffset_Stand),
			8 : (MainApronNames, customOffset_Stand),
			9 : (MainApronNames, customOffset_Stand),
    },
	PARKING: {
		None: ( ),
			7 : (MainApronNames, customOffset_Stand),
	},
}