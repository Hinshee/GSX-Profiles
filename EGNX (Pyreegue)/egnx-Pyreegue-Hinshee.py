# -- coding: utf-8 --

version = 1.7
msfs_mode = 1
icao = "egnx"

@AlternativeStopPositions
def Offset_Standard(aircraftData):
	table = {
		0: 0,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand4(aircraftData):
	table = {
		0: 0,
        42: 0,
        72: 0,
        175: -7,
        146: -7,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand8(aircraftData):
	table = {
		0: 0,
        319: -1.45,
        72: -1.45,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand9(aircraftData):
	table = {
		0: 0,
        321: -1.3,
        320: -1.3,
        319: -1.3,
        195: -1.3,
        175: -1.3,
        319: -1.3,
        72: -1.3,
        42: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand11(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()
        
@AlternativeStopPositions
def Offset_Stand12(aircraftData):
	table = {
		0: 0,
        737: -2.6,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()
        
@AlternativeStopPositions
def Offset_Stand14L(aircraftData):
	table = {
		0: 0,
        767: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()
        
@AlternativeStopPositions
def Offset_Stand14R(aircraftData):
	table = {
		0: 0,
        757: -2.8,
        321: -1.8,
        737: -0.7,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()
        
@AlternativeStopPositions
def Offset_Stand15(aircraftData):
	table = {
		0: 0,
        757: -1.8,
        321: -0.9,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand16(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand17(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand21(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand22(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand23(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand24(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand41(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand42(aircraftData):
	table = {
		0: 0,
        757: 2.2,
        787: 3.7,
        737: -10.5,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand43(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand44(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand45(aircraftData):
	table = {
		0: 0,
        321: -1.3,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand114(aircraftData):
	table = {
		0: 0,
        330: 7.7,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand112(aircraftData):
	table = {
		0: 0,
        330: 7.8,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand111(aircraftData):
	table = {
		0: 0,
        777: 3.6,
        747: 9.9,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand110(aircraftData):
	table = {
		0: 0,
        330: 7.25,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand109(aircraftData):
	table = {
		0: 0,
		777: 8.3,
		767: 8.3,
		330: 8.3,
	}
	
	table747 = {
		4: 11.5,
		8: 17.9,
	}

	try:
		if aircraftData.idMajor == 747:
			return Distance.fromMeters(table747.get(aircraftData.idMinor, 0) - 0.25)
		else:
			return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def Offset_Stand107(aircraftData):
	table = {
		0: 0,
	}
	
	table747 = {
		4: 3.5,
		8: 9.9,
	}

	try:
		if aircraftData.idMajor == 747:
			return Distance.fromMeters(table747.get(aircraftData.idMinor, 0) - 0.25)
		else:
			return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def Offset_Stand106(aircraftData):
	table = {
		0: 0,
        330: 6.9,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand103(aircraftData):
	table = {
		0: 0,
        757: 2.2,
        767: 5.5,
        330: 10.8,
        777: 12.4,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand102(aircraftData):
	table = {
		0: 0,
        757: 2.2,
        767: 5.5,
        330: 10.8,
        777: 12.4,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand101(aircraftData):
	table = {
		0: 0,
        330: 10.6,
        777: 17.7,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()


@AlternativeStopPositions
def Offset_Stand120(aircraftData):
	table = {
		0: 0,
        767: 9.4,
        757: 15.5,
        330: 18.4,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()
        
@AlternativeStopPositions
def Offset_Stand98(aircraftData):
	table = {
		0: 0,
        320: 11.7,
        777: 2.3,
	}
	
	table747 = {
		4: 5.7,
		8: 11.7,
	}

	try:
		if aircraftData.idMajor == 747:
			return Distance.fromMeters(table747.get(aircraftData.idMinor, 0) - 0.25)
		else:
			return Distance.fromMeters(table.get(aircraftData.idMajor, 0) - 0.25)
	except Exception:
		return Distance()

@AlternativeStopPositions
def Offset_Stand121(aircraftData):
	table = {
		0: 0,
        767: 9.4,
        757: 15.5,
        330: 18.4,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand125(aircraftData):
	table = {
		0: 0,
        737: 1.9,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand75(aircraftData):
	table = {
		0: 0,
        767: 10.2,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

@AlternativeStopPositions
def Offset_Stand77(aircraftData):
	table = {
		0: 0,
        320: 10.2,
        767: 10.2,
	}

	try:
		return Distance.fromMeters( table.get(aircraftData.idMajor)  - 0.25 )
	except:
		return Distance()

def TerminalName(name, letter, priority):
	return CustomizedName( "%s | Stand #§%s" % (name, letter), priority )

def StandName(name, letter, priority):
	return CustomizedName( "%s | Stand #§%s" % (name, letter), priority )
	
def RemoteStandName(name, letter, priority):
    return CustomizedName( "%s | Stand #§%s (Remote)" % (name, letter), priority )
    
def RemoteStandNameNC(name, letter, priority):
    return CustomizedName( "%s | Stand #§%s (Remote|NC)" % (name, letter), priority )
    
CentralApronNames = TerminalName("Central Aprons", "", 1)
CentralWestApronNames = TerminalName("Central Aprons", "", 1)
CentralApronRemoteNames = RemoteStandName("Central Aprons", "", 1)
EasternApron = StandName("Eastern Apron", "", 2)
WesternApron = StandName("Western Apron", "", 2)
WesternApronRemote = RemoteStandNameNC("Western Apron", "", 2)
MainAreaNorthNames = StandName("North Maintenance | Maint. (NC)", "", 4)
MainAreaSouthNames = StandName("South Maintenance | Maint. (NC)", "", 4)
RVLApronNames = StandName("GA Aprons | RVL Apron (NC)", "", 3)
RollsRoyceApron = StandName("GA Aprons | Rolls Royce Apron (NC)", "", 3)

parkings = {
	GATE : {
		None : ( ),
		4 : (CentralApronNames, Offset_Stand4),
		5 : (CentralApronNames, Offset_Standard),
		6 : (CentralApronNames, Offset_Standard),
		7 : (CentralApronNames, Offset_Standard),
		8 : (CentralApronNames, Offset_Stand8),
		9 : (CentralApronNames, Offset_Stand9),
		10 : (CentralApronNames, Offset_Standard),
		11 : (CentralApronNames, Offset_Stand11),
		12 : (CentralApronNames, Offset_Standard),
		"12L" : (CentralApronNames, Offset_Stand12),
		"12R" : (CentralApronNames, Offset_Standard),
		14 : (CentralApronNames, Offset_Standard),
		"14L" : (CentralApronNames, Offset_Stand14L),
		"14R" : (CentralApronNames, Offset_Stand14R),
		15 : (CentralApronNames, Offset_Stand15),
		16 : (CentralApronNames, Offset_Stand16),
		17 : (CentralApronNames, Offset_Stand17),
		20 : (CentralApronRemoteNames, Offset_Standard),
		21 : (CentralApronRemoteNames, Offset_Stand21),
		22 : (CentralApronRemoteNames, Offset_Stand22),
		23 : (CentralApronRemoteNames, Offset_Stand23),
		24 : (CentralApronRemoteNames, Offset_Stand24),
		30 : (CentralApronRemoteNames, Offset_Standard),
		31 : (CentralApronRemoteNames, Offset_Standard),
		32 : (CentralApronRemoteNames, Offset_Standard),
		33 : (CentralApronRemoteNames, Offset_Standard),
		40 : (CentralWestApronNames, Offset_Standard),
		41 : (CentralWestApronNames, Offset_Stand41),
		42 : (CentralWestApronNames, Offset_Stand42),
		43 : (CentralWestApronNames, Offset_Stand43),
		44 : (CentralWestApronNames, Offset_Stand44),
		45 : (CentralWestApronNames, Offset_Stand45),
	},
	W_PARKING : {
		None : ( ),
		1 : (RollsRoyceApron, ),
		2 : (RVLApronNames, ),
		98 : (WesternApron, Offset_Stand98),
		99 : (WesternApron, Offset_Standard),
		100 : (WesternApron, Offset_Standard),
		101 : (WesternApron, Offset_Stand101),
		102 : (WesternApron, Offset_Stand102),
		103 : (WesternApron, Offset_Stand103),
		104 : (WesternApron, Offset_Standard),
		105 : (WesternApron, Offset_Standard),
		106 : (WesternApron, Offset_Stand106),
		107 : (WesternApron, Offset_Stand107),
		108 : (WesternApron, Offset_Standard),
		109 : (WesternApron, Offset_Stand109),
		110 : (WesternApron, Offset_Stand110),
		111 : (WesternApron, Offset_Stand111),
		112 : (WesternApron, Offset_Stand112),
		114 : (WesternApron, Offset_Stand114),
		120 : (WesternApron, Offset_Stand120),
		121 : (WesternApron, Offset_Stand121),
		122 : (WesternApron, Offset_Standard),
		123 : (WesternApron, Offset_Standard),
		124 : (WesternApron, Offset_Standard),
		125 : (WesternApron, Offset_Stand125),
		"125R" : (WesternApron, Offset_Standard),
		"125L" : (WesternApron, Offset_Standard),
		200 : (WesternApronRemote, Offset_Standard),
		201 : (WesternApronRemote, Offset_Standard),
		"201L" : (WesternApronRemote, Offset_Standard),
		"201R" : (WesternApronRemote, Offset_Standard),
		202 : (WesternApronRemote, Offset_Standard),
		"202L" : (WesternApronRemote, Offset_Standard),
		"202R" : (WesternApronRemote, Offset_Standard),
		203 : (WesternApronRemote, Offset_Standard),
		"203R" : (WesternApronRemote, Offset_Standard),
	},
	E_PARKING : {
		None : (MainAreaNorthNames, ),
		"70R" : (EasternApron, Offset_Standard),
		70 : (EasternApron, Offset_Standard),
		"70L" : (EasternApron, Offset_Standard),
		71 : (EasternApron, Offset_Standard),
		72 : (EasternApron, Offset_Standard),
		73 : (EasternApron, Offset_Standard),
		"73L" : (EasternApron, Offset_Standard),
		74 : (EasternApron, Offset_Standard),
		"74L" : (EasternApron, Offset_Standard),
		75 : (EasternApron, Offset_Stand75),
		"75R" : (EasternApron, Offset_Standard),
		"76R" : (EasternApron, Offset_Standard),
		76 : (EasternApron, Offset_Standard),
		"76L" : (EasternApron, Offset_Standard),
		"77R" : (EasternApron, Offset_Standard),
		77 : (EasternApron, Offset_Stand77),
		"78R" : (EasternApron, Offset_Standard),
		78 : (EasternApron, Offset_Standard),
		"78L" : (EasternApron, Offset_Standard),
		79 : (EasternApron, Offset_Standard),
		80 : (EasternApron, Offset_Standard),
		81 : (EasternApron, Offset_Standard),
		82 : (EasternApron, Offset_Standard),
		83 : (EasternApron, Offset_Standard),
		84 : (EasternApron, Offset_Standard),
		85 : (EasternApron, Offset_Standard),
		86 : (EasternApron, Offset_Standard),
	},
	SW_PARKING : {
		None : (MainAreaNorthNames, ),
		1 : (MainAreaNorthNames, ),
		2 : (MainAreaNorthNames, ),
		3 : (MainAreaNorthNames, ),
	},
	S_PARKING : {
		None : (MainAreaSouthNames, ),
		1 : (MainAreaSouthNames, ),
		2 : (MainAreaSouthNames, ),
	},
}
