# -- coding: utf-8 --

msfs_mode = 1
icao = "efou"

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
    
def CustomTerminalNames(gate, name, letter, priority):
	return CustomizedName("%s | Gate %s%s" % (name, letter, gate), priority )

def StandNames(name, letter, priority):
	return CustomizedName( "%s | Stand %s#§" % (name, letter), priority )
  
Apron1GateNames = TerminalNames("Apron 1", "", 1)
Apron1StandNames = StandNames("Apron 1", "", 1)
Apron2Names = StandNames("Apron 2", "", 2)
Apron3Names = StandNames("Apron 3 (GA)", "", 3)
MilApronNames = StandNames("Military Apron", "", 4)

parkings = {
    GATE: {
        None: ( ),
			13 : (Apron1GateNames, customOffset_Gate),
            14 : (Apron1GateNames, customOffset_Gate),
            "15B" : (CustomTerminalNames(15 ,"Apron 1", "", 1), customOffset_Gate),
            16 : (Apron1GateNames, customOffset_Gate),
	},
    PARKING: {
        None: ( ),
            1 : (Apron3Names, customOffset_Stand),
            2 : (Apron3Names, customOffset_Stand),
            3 : (Apron3Names, customOffset_Stand),
            4 : (Apron3Names, customOffset_Stand),
            5 : (Apron2Names, customOffset_Stand),
            6 : (Apron2Names, customOffset_Stand),
            "7A" : (Apron2Names, customOffset_Stand),
            "7B" : (Apron2Names, customOffset_Stand),
            "8B" : (Apron2Names, customOffset_Stand),
            9 : (Apron1StandNames, customOffset_Stand),
            10 : (Apron1StandNames, customOffset_Stand),
            11 : (Apron1StandNames, customOffset_Stand),
            12 : (Apron1StandNames, customOffset_Stand),
            "13B" : (Apron1GateNames, customOffset_Gate),
            "15B" : (Apron1GateNames, customOffset_Gate),
    },
    0: {
        None: ( ),
            1 : (MilApronNames, customOffset_Stand),
            2 : (MilApronNames, customOffset_Stand),
            3 : (MilApronNames, customOffset_Stand),
            4 : (MilApronNames, customOffset_Stand),
            5 : (MilApronNames, customOffset_Stand),
            6 : (MilApronNames, customOffset_Stand),
            7 : (MilApronNames, customOffset_Stand),
            8 : (MilApronNames, customOffset_Stand),
            9 : (MilApronNames, customOffset_Stand),
            10 : (MilApronNames, customOffset_Stand),
    },
}