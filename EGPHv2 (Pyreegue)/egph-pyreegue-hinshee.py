# -- coding: utf-8 --

msfs_mode = 1
icao = "egph"

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
def customOffset(aircraftData):
	table = {
		0: 0,
		757: 0,
		767: 0,
		777: 4.7,
		787: 4.7,
		319: 7.8,
		320: 0,
		321: 0,
		330: 1.3,
		350: 4.7,
		380: 4.7,
	}

	table787 = {
     	0: 0, #8.05
		8: 0,
		9: 0, #12.05
		10: 0,
	}

	if aircraftData.idMajor == 787:
		return Distance.fromMeters( table787.get(aircraftData.idMinor)  - 0.25 )
	else:
		try:
			return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
		except:
			return Distance()

@AlternativeStopPositions
def customOffset_Gate16(aircraftData):
	table = {
		0: 0,
		170: 0,
		175: 0,
		737: 8,
		320: 8,
		319: 8,
		321: 11.3,
		900: 11.3,
		767: 13.1,
		787: 13.1,
		777: 14.15,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffset_Gate18(aircraftData):
	table = {
		0: 0,
		170: 0,
		175: 0,
		737: 8,
		320: 8,
		319: 8,
		321: 11.3,
		900: 11.3,
		767: 13.1,
		787: 13.1,
		777: 14.15,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffset_Stand12(aircraftData):
	table = {
		0: 0,
		170: 0,
		175: 0,
		737: 7.2,
		320: 7.2,
		319: 7.2,
		321: 11.3,
		900: 11.3,
		767: 13.3,
		787: 13.3,
		777: 13.8,
	}

	return Distance.fromMeters( table.get(aircraftData.idMajor, 0) - 0.25 )

@AlternativeStopPositions
def customOffset_Gate4A(aircraftData):
	table = {
		0: 0,
		777: 4,
		787: 4,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def customOffset_Stand102(aircraftData):
	table = {
		0: 0,
		321: 11.9,
		757: 11.9,
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
SoutheastPierNames = StandNames("Southeast Pier", "", 1)
SoutheastApronNames = StandNames("Southeast Apron", "", 2)
TurnhouseApronNames = StandNames("Turnhouse Apron", "", 2)
NorthApronNames = StandNames("North Apron", "", 3)
EastApronNames = StandNames("East Apron", "", 4)
RemoteNames = StandNames("Remote Stands", "", 5)
GANames = StandNames("GA Apron", "", 6)

parkings = {
    GATE: {
        None: ( ),
			99 : (MainApronNames, customOffset_Stand),
			100 : (MainApronNames, customOffset_Stand),
			101 : (MainApronNames, customOffset_Stand),
			102 : (MainApronNames, customOffset_Stand102),
			103 : (MainApronNames, customOffset_Stand),
			104 : (MainApronNames, customOffset_Stand),
			105 : (MainApronNames, customOffset_Stand),
			106 : (MainApronNames, customOffset_Stand),
			"1B" : (MainApronNames, customOffset_Stand),
			"1A" : (MainApronNames, customOffset_Stand),
			1 : (MainApronNames, customOffset_Stand),
			2 : (MainApronNames, customOffset_Stand),
			3 : (MainApronNames, customOffset_Stand),
			4 : (MainApronNames, customOffset_Stand),
			"4A" : (MainApronNames, customOffset_Gate4A),
			5 : (MainApronNames, customOffset_Stand),
			6 : (MainApronNames, customOffset_Stand),
			7 : (MainApronNames, customOffset_Stand),
			8 : (MainApronNames, customOffset_Stand),
			9 : (MainApronNames, customOffset_Stand),
			10 : (MainApronNames, customOffset_Stand),
			11 : (MainApronNames, customOffset_Stand),
			12 : (MainApronNames, customOffset_Stand12),
			14 : (MainApronNames, customOffset_Stand),
			15 : (SoutheastPierNames, ),
			"15A" : (SoutheastPierNames, ),
			"15B" : (SoutheastPierNames, ),
			16 : (SoutheastPierNames, customOffset_Gate16),
			"16A" : (SoutheastPierNames, ),
			"16B" : (SoutheastPierNames, ),
			17 : (SoutheastPierNames, ),
			18 : (SoutheastPierNames, customOffset_Gate18),
			19 : (SoutheastPierNames, customOffset_Gate),
			20 : (SoutheastPierNames, customOffset_Gate),
			21 : (SoutheastPierNames, customOffset_Gate),
			22 : (SoutheastPierNames, customOffset_Gate),
			23 : (SoutheastPierNames, customOffset_Gate),
			24 : (SoutheastPierNames, customOffset_Gate),
			25 : (SoutheastPierNames, customOffset_Gate),
			26 : (SoutheastApronNames, customOffset_Stand),
			27 : (SoutheastApronNames, customOffset_Stand),
			28 : (SoutheastApronNames, customOffset_Stand),
			29 : (SoutheastApronNames, customOffset_Stand),
			30 : (SoutheastApronNames, customOffset_Stand),
			31 : (SoutheastApronNames, customOffset_Stand),
			32 : (SoutheastApronNames, customOffset_Stand),
			33 : (SoutheastApronNames, customOffset_Stand),
			34 : (SoutheastApronNames, customOffset_Stand),
    },
	SE_PARKING: {
		None: ( ),
			1 : (GANames, ),
			308 : (TurnhouseApronNames, customOffset_Stand),
			309 : (TurnhouseApronNames, customOffset_Stand),
			310 : (TurnhouseApronNames, customOffset_Stand),
			"310R" : (TurnhouseApronNames, customOffset_Stand),
			311 : (TurnhouseApronNames, customOffset_Stand),
			"311R" : (TurnhouseApronNames, customOffset_Stand),
			"311L" : (TurnhouseApronNames, customOffset_Stand),
			312 : (TurnhouseApronNames, customOffset_Stand),
			"312L" : (TurnhouseApronNames, customOffset_Stand),
			313 : (TurnhouseApronNames, customOffset_Stand),
			314 : (TurnhouseApronNames, customOffset_Stand),
			315 : (TurnhouseApronNames, customOffset_Stand),
			316 : (TurnhouseApronNames, customOffset_Stand),
			317 : (TurnhouseApronNames, customOffset_Stand),
			"317A" : (TurnhouseApronNames, customOffset_Stand),
	},
	E_PARKING: {
		None: ( ),
			210 : (EastApronNames, customOffset_Stand),
			211 : (EastApronNames, customOffset_Stand),
			212 : (EastApronNames, customOffset_Stand),
	},
	N_PARKING: {
		None: ( ),
			200 : (NorthApronNames, customOffset_Stand),
			201 : (NorthApronNames, customOffset_Stand),
			202 : (NorthApronNames, customOffset_Stand),
			203 : (NorthApronNames, customOffset_Stand),
			204 : (NorthApronNames, customOffset_Stand),
			205 : (NorthApronNames, customOffset_Stand),
			206 : (NorthApronNames, customOffset_Stand),
			207 : (NorthApronNames, customOffset_Stand),
			208 : (NorthApronNames, customOffset_Stand),
	},
}