# -- coding: utf-8 --

msfs_mode = 1
icao = "bkpr"
version = 1.2

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

@AlternativeStopPositions
def customOffset_GateHeavy(aircraftData):
	table = {
		"Unknown": 0,
		"ARC-B": 0,
        "ARC-C": 0,
        "ARC-D": 4,
        "ARC-E": 6.8,
        "ARC-F": 8.8,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.aircraftGroup)  - 0.25 )
	except:
		return Distance()

def TerminalNames(name, letter, priority):
	return CustomizedName( "%s | Gate %s#§" % (name, letter), priority )

def StandNames(name, letter, priority):
	return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
  
ApronKNames = TerminalNames("Apron K (101-203)", "", 1)
ApronDNames = TerminalNames("Apron D (1-7)", "", 2)
ApronJNames = TerminalNames("Apron J (1-3)", "", 3)
ApronLNames = TerminalNames("Apron L (1-2)", "", 4)

parkings = {
    GATE: {
        None: ( ),
			101 : (ApronKNames, customOffset_GateHeavy),
    },
	GATE_A: {
		None: ( ),
			"101A" : (ApronKNames, customOffset_Gate),
			"201A" : (ApronKNames, customOffset_Gate),
			"202A" : (ApronKNames, customOffset_Gate),
            "203A" : (ApronKNames, customOffset_Gate),
	},
    GATE_B: {
		None: ( ),
			"101B" : (ApronKNames, customOffset_Gate),
			"201B" : (ApronKNames, customOffset_Gate),
			"202B" : (ApronKNames, customOffset_Gate),
            "203B" : (ApronKNames, customOffset_Gate),
	},
    GATE_D: {
		None: ( ),
			1 : (ApronDNames, customOffset_Gate),
			2 : (ApronDNames, customOffset_Gate),
			3 : (ApronDNames, customOffset_Gate),
            4 : (ApronDNames, customOffset_Gate),
            5 : (ApronDNames, customOffset_Gate),
			6 : (ApronDNames, customOffset_Gate),
            7 : (ApronDNames, customOffset_Gate),
	},
    GATE_J: {
		None: ( ),
			1 : (ApronJNames, customOffset_Gate),
			"1A" : (ApronJNames, customOffset_Gate),
			2 : (ApronJNames, customOffset_Gate),
            "3A" : (ApronJNames, customOffset_Gate),
	},
    GATE_L: {
		None: ( ),
			1 : (ApronLNames, customOffset_Gate),
			"1A" : (ApronLNames, customOffset_Gate),
			2 : (ApronLNames, customOffset_Gate),
	},
	PARKING: {
		None: ( ),
			201 : (ApronKNames, customOffset_GateHeavy),
	},
    0: {
		None: ( ),
            "1A" : (ApronDNames, customOffset_Gate),
			202 : (ApronKNames, customOffset_GateHeavy),
			203 : (ApronKNames, customOffset_GateHeavy),
	},
}