# -- coding: utf-8 --

version = 1
msfs_mode = 1
icao = "lgsm"

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


def StandNames(name, letter, priority):
	return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
  
MainNames = StandNames("Main Apron", "", 1)
GANames = StandNames("GA Stands", "", 2)

parkings = {
    0: {
        None: ( ),
            1 : (MainNames, customOffset_Stand),
            2 : (MainNames, customOffset_Stand),
            3 : (MainNames, customOffset_Stand),
            4 : (MainNames, customOffset_Stand),
            5 : (MainNames, customOffset_Stand),
            6 : (MainNames, customOffset_Stand),
            7 : (MainNames, customOffset_Stand),
            8 : (MainNames, customOffset_Stand),
            "1S" : (GANames, customOffset_Stand),
            "2S" : (GANames, customOffset_Stand),
            "3S" : (GANames, customOffset_Stand),
	},
}