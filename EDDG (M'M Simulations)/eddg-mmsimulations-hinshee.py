# -- coding: utf-8 --

msfs_mode = 1
icao = "eddg"

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
	return CustomizedName( "%s | Gate #§%s" % (name, letter), priority )

def StandNamesNC(name, letter, priority):
	return CustomizedName( "%s | Stand #§ %s" % (name, letter), priority )

def StandNames(name, letter, priority):
	return CustomizedName( "%s | Stand #§%s" % (name, letter), priority )
	
def Stand21ANames(name, letter, priority):
	return CustomizedName( "%s | Stand 21%s" % (name, letter), priority )

MainTerminalNames = TerminalNames("Terminal", "", 1)
EastApronNames = StandNames("East Apron", "", 2)
EastApronNamesStand21A = Stand21ANames("East Apron", "A", 2)
CentralApronNames = StandNames("Central Apron", "", 3)
CentralApronNamesA = StandNames("Central Apron", "A", 3)
CentralApronNamesB = StandNames("Central Apron", "B", 3)
CentralApronNamesC = StandNames("Central Apron", "C", 3)
CentralApronNamesD = StandNames("Central Apron", "D", 3)
CentralApronNamesE = StandNames("Central Apron", "E", 3)
CentralApronNCNames = StandNamesNC("Central Apron", "(NC)", 3)
WestApronNames = StandNamesNC("West Apron", "(NC)", 4)

parkings = {
	GATE_A : {
		None : ( ),
			"9A" : (MainTerminalNames, ),
			18 : (CentralApronNamesA, customOffset_Stand, ),
            19 : (CentralApronNamesA, customOffset_Stand, ),
            "21B" : (EastApronNamesStand21A, customOffset_Stand, ),
			"24A" : (EastApronNames, customOffset_Stand, ),
	},
	GATE_B : {
		None : ( ),
			"9B" : (MainTerminalNames, customOffset_Stand, ),
            18 : (CentralApronNamesB, customOffset_Stand, ),
			19 : (CentralApronNamesB, customOffset_Stand, ),
            "21B" : (EastApronNames, customOffset_Stand, ),
            "24B" : (EastApronNames, customOffset_Stand, ),
	},
	GATE_C : {
		None : ( ),
            18 : (CentralApronNamesC, customOffset_Stand, ),
            19 : (CentralApronNamesC, customOffset_Stand, ),
	},
	GATE_D : {
		None : ( ),
            18 : (CentralApronNamesD, customOffset_Stand, ),
            19 : (CentralApronNamesD, customOffset_Stand, ),
	},
	GATE_E : {
		None : ( ),
			18 : (CentralApronNamesE, customOffset_Stand, ),
            19 : (CentralApronNamesE, customOffset_Stand, ),
            20 : (EastApronNames, customOffset_Stand, ),
            21 : (EastApronNames, customOffset_Stand, ),
	},
    0: {
        None: ( ),
            7: (MainTerminalNames, customOffset_Stand, ),
            8: (MainTerminalNames, customOffset_Stand, ),
            9: (MainTerminalNames, customOffset_Stand, ),
			10: (MainTerminalNames, customOffset_Stand, ),
			11: (MainTerminalNames, customOffset_Stand, ),
			12: (MainTerminalNames, customOffset_Stand, ),
			13: (MainTerminalNames, customOffset_Stand, ),
			14: (MainTerminalNames, customOffset_Stand, ),
			22: (EastApronNames, customOffset_Stand, ),
            24: (EastApronNames, customOffset_Stand, ),
            25: (EastApronNames, customOffset_Stand, ),
			301: (CentralApronNCNames, customOffset_Stand, ),
			302: (CentralApronNCNames, customOffset_Stand, ),
			303: (CentralApronNCNames, customOffset_Stand, ),
			401: (CentralApronNCNames, customOffset_Stand, ),
			402: (CentralApronNCNames, customOffset_Stand, ),
			403: (CentralApronNCNames, customOffset_Stand, ),
			404: (CentralApronNCNames, customOffset_Stand, ),
			405: (CentralApronNCNames, customOffset_Stand, ),
			406: (CentralApronNCNames, customOffset_Stand, ),
			101: (WestApronNames, customOffset_Stand, ),
			102: (WestApronNames, customOffset_Stand, ),
			103: (WestApronNames, customOffset_Stand, ),
			104: (WestApronNames, customOffset_Stand, ),
			201: (WestApronNames, customOffset_Stand, ),
			202: (WestApronNames, customOffset_Stand, ),
			203: (WestApronNames, customOffset_Stand, ),
    }
}