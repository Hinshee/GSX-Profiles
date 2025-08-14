# -- coding: utf-8 --

msfs_mode = 1
icao = "bggh"

@AlternativeStopPositions
def customOffset(aircraftData):
	table = {
		0: 0,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def customOffset_Gate1(aircraftData):

    table = {
        0: 0,
        42: -53.5,
        72: -53.5,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

@AlternativeStopPositions
def customOffset_Gate2C(aircraftData):

    table = {
        0: 0,
        320: 8.5,
        330: 8.5,
        340: 8.5,
        350: 8.5,
        747: 8.5,
        757: 8.5,
        767: 8.5,
        777: 8.5,
        787: 8.5,
        82: 8.5,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )

def TerminalNames(name, letter, priority):
	return CustomizedName( "%s | Gate %s#§" % (name, letter), priority )
    
def StandNames(name, letter, priority):
	return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
    
  
ApronAStandNames = TerminalNames("Apron A", "", 1)
ApronBStandNames = StandNames("Apron B", "", 2)
ApronCStandNames = StandNames("Apron C", "", 3)

parkings = {
    GATE: {
        None: ( ),
			1 : (ApronAStandNames, customOffset_Gate1),
            "1B" : (ApronBStandNames, customOffset),
            "1C" : (ApronCStandNames, customOffset),
            2 : (ApronAStandNames, customOffset),
            "2B" : (ApronBStandNames, customOffset),
            "2C" : (ApronCStandNames, customOffset_Gate2C),
            3 : (ApronAStandNames, customOffset),
            "3B" : (ApronBStandNames, customOffset),
            "3C" : (ApronCStandNames, customOffset),
            "4A" : (ApronAStandNames, customOffset),
            "4B" : (ApronAStandNames, customOffset),
            "5A" : (ApronAStandNames, customOffset),
            "5B" : (ApronAStandNames, customOffset),
            6 : (ApronAStandNames, customOffset)
	},
    PARKING: {
        None: ( ),
            "4B" : (ApronBStandNames, customOffset)
    }
}