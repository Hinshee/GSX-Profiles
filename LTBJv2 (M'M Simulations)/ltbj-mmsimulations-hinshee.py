# -- coding: utf-8 --

version = 1
msfs_mode = 1
icao = "ltbj"

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

@AlternativeStopPositions
def customOffset_Gates37(aircraftData):
	table = {
		"Unknown": 0,
		"ARC-B": 0,
        "ARC-C": 3.2,
        "ARC-D": 7.2,
        "ARC-E": 10.7,
        "ARC-F": 14.5,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.aircraftGroup)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def customOffset_Gates35(aircraftData):
	table = {
		"Unknown": 0,
		"ARC-B": 0,
        "ARC-C": 3.2,
        "ARC-D": 5.6,
        "ARC-E": 8.6,
        "ARC-F": 12.4,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.aircraftGroup)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def customOffset_Gates29(aircraftData):
	table = {
		"Unknown": 0,
		"ARC-B": 0,
        "ARC-C": 3.2,
        "ARC-D": 5.6,
        "ARC-E": 8.6,
        "ARC-F": 11,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.aircraftGroup)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def customOffset_Gates26(aircraftData):
	table = {
		"Unknown": 0,
		"ARC-B": 0,
        "ARC-C": 3.2,
        "ARC-D": 5.6,
        "ARC-E": 16.6,
        "ARC-F": 19.2,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.aircraftGroup)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def customOffset_Gates25(aircraftData):
	table = {
		"Unknown": 0,
		"ARC-B": 0,
        "ARC-C": 3.2,
        "ARC-D": 13.6,
        "ARC-E": 20.2,
        "ARC-F": 25.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.aircraftGroup)  - 0.25 )
	except:
		return Distance()

def TerminalNames(name, letter, priority):
	return CustomizedName( "%s | Gate %s#§" % (name, letter), priority )

def StandNames(name, letter, priority):
	return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
  
Apron1GateNames = TerminalNames("Apron 1 / Domestic (36-42, 8-13)", "", 1)
Apron1StandNames = StandNames("Apron 1 / Domestic (36-42, 8-13)", "", 1)
Apron2GateNames = TerminalNames("Apron 2 / International (24-35, 14-23)", "", 2)
Apron2StandNames = StandNames("Apron 2 / International (24-35, 14-23)", "", 2)
CargoApronStandNames = StandNames("Cargo (43-60)", "", 3)
Apron3StandNames = StandNames("Apron 3 (61-68)", "(NC)", 4)
MilApronNames = StandNames("Military Apron", "", 5)

parkings = {
    GATE: {
        None: ( ),
            24 : (Apron2GateNames, customOffset_Gates25),
            25 : (Apron2GateNames, customOffset_Gates25),
            26 : (Apron2GateNames, customOffset_Gates26),
            27 : (Apron2GateNames, customOffset_Gates29),
            28 : (Apron2GateNames, customOffset_Gates29),
            29 : (Apron2GateNames, customOffset_Gates29),
            30 : (Apron2GateNames, customOffset_Gates35),
            31 : (Apron2GateNames, customOffset_Gates35),
            32 : (Apron2GateNames, customOffset_Gates35),
            33 : (Apron2GateNames, customOffset_Gates35),
            34 : (Apron2GateNames, customOffset_Gates35),
            35 : (Apron2GateNames, customOffset_Gates35),
			36 : (Apron1GateNames, customOffset_Gates37),
            37 : (Apron1GateNames, customOffset_Gates37),
            38 : (Apron1GateNames, customOffset_CDGap),
            39 : (Apron1GateNames, customOffset_CDGap),
            40 : (Apron1GateNames, customOffset_CDGap),
            41 : (Apron1GateNames, customOffset_CDGap),
            42 : (Apron1GateNames, customOffset_CDGap),
	},
    PARKING: {
        None: ( ),
            43 : (CargoApronStandNames, customOffset_Stand),
            44 : (CargoApronStandNames, customOffset_Stand),
            "45A" : (CargoApronStandNames, customOffset_Stand),
            "45B" : (CargoApronStandNames, customOffset_Stand),
            45 : (CargoApronStandNames, customOffset_Stand),
            46 : (CargoApronStandNames, customOffset_Stand),
            51 : (CargoApronStandNames, customOffset_Stand),
            52 : (CargoApronStandNames, customOffset_Stand),
            53 : (CargoApronStandNames, customOffset_Stand),
            54 : (CargoApronStandNames, customOffset_Stand),
			"54A" : (CargoApronStandNames, customOffset_Stand),
            "54B" : (CargoApronStandNames, customOffset_Stand),
            54 : (CargoApronStandNames, customOffset_Stand),
            55 : (CargoApronStandNames, customOffset_Stand),
            "56B" : (CargoApronStandNames, customOffset_Stand),
            "56A" : (CargoApronStandNames, customOffset_Stand),
            56 : (CargoApronStandNames, customOffset_Stand),
            57 : (CargoApronStandNames, customOffset_Stand),
            58 : (CargoApronStandNames, customOffset_Stand),
            59 : (CargoApronStandNames, customOffset_Stand),
            60 : (CargoApronStandNames, customOffset_Stand),
            61 : (Apron3StandNames, customOffset_Stand),
            62 : (Apron3StandNames, customOffset_Stand),
            63 : (Apron3StandNames, customOffset_Stand),
            64 : (Apron3StandNames, customOffset_Stand),
            65 : (Apron3StandNames, customOffset_Stand),
            66 : (Apron3StandNames, customOffset_Stand),
            67 : (Apron3StandNames, customOffset_Stand),
            68 : (Apron3StandNames, customOffset_Stand),
            23 : (Apron2StandNames, customOffset_Stand),
            22 : (Apron2StandNames, customOffset_Stand),
            21 : (Apron2StandNames, customOffset_Stand),
            20 : (Apron2StandNames, customOffset_Stand),
            19 : (Apron2StandNames, customOffset_Stand),
            18 : (Apron2StandNames, customOffset_Stand),
            17 : (Apron2StandNames, customOffset_Stand),
            16 : (Apron2StandNames, customOffset_Stand),
            15 : (Apron2StandNames, customOffset_Stand),
            14 : (Apron2StandNames, customOffset_Stand),
			13 : (Apron1StandNames, customOffset_Stand),
            12 : (Apron1StandNames, customOffset_Stand),
            11 : (Apron1StandNames, customOffset_Stand),
            10 : (Apron1StandNames, customOffset_Stand),
            9 : (Apron1StandNames, customOffset_Stand),
            8 : (Apron1StandNames, customOffset_Stand),
            "1M" : (MilApronNames, ),
	},
    DOCK: {
        None: ( ),
            47 : (CargoApronStandNames, customOffset_Stand),
            "48B" : (CargoApronStandNames, customOffset_Stand),
            "48A" : (CargoApronStandNames, customOffset_Stand),
            48 : (CargoApronStandNames, customOffset_Stand),
            49 : (CargoApronStandNames, customOffset_Stand),
            "50B" : (CargoApronStandNames, customOffset_Stand),
            "50A" : (CargoApronStandNames, customOffset_Stand),
            50 : (CargoApronStandNames, customOffset_Stand),
	},
}