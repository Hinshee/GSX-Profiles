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
MainApronNamesNC = TerminalNames("Commercial Apron | (NC)", "", 1)
FBOApronNames = StandNames("FBO Apron | (NC)", "", 2)

parkings = {
    PARKING: {
        None: ( ),
		1 : (MainApronNames, customOffset_Stand),
		"1A" : (MainApronNames, customOffset_Stand),
		"1B" : (MainApronNamesNC, customOffset_Stand),
		2 : (MainApronNames, customOffset_Stand),
		3 : (MainApronNames, customOffset_Stand),
		4 : (MainApronNames, customOffset_Stand),
		5 : (MainApronNames, customOffset_Stand),
		6 : (MainApronNames, customOffset_Stand),
		7 : (MainApronNames, customOffset_Stand),
		8 : (MainApronNames, customOffset_Stand),
		9 : (MainApronNames, customOffset_Stand),
		10 : (FBOApronNames, customOffset_Stand),
		11 : (FBOApronNames, customOffset_Stand),
		12 : (FBOApronNames, customOffset_Stand),
		13 : (FBOApronNames, customOffset_Stand),
		14 : (FBOApronNames, customOffset_Stand),
		15 : (FBOApronNames, customOffset_Stand),
    },
	0: {
		None: ( FBOApronNames, customOffset_Stand ),
	},
}