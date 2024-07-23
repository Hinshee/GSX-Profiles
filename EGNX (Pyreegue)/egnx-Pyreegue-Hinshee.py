# -- coding: utf-8 --

msfs_mode = 1
icao = "egnx"

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
MainAreaNorthNames = StandName("GA Aprons | Maint. North (NC)", "", 3)
MainAreaSouthNames = StandName("GA Aprons | Maint. South (NC)", "", 3)
RVLApronNames = StandName("GA Aprons | RVL Apron (NC)", "", 3)

parkings = {
	PARKING : {
		None : ( ),
		4 : (CentralApronNames, ),
		5 : (CentralApronNames, ),
		6 : (CentralApronNames, ),
		7 : (CentralApronNames, ),
		8 : (CentralApronNames, ),
		9 : (CentralApronNames, ),
		10 : (CentralApronNames, ),
		11 : (CentralApronNames, ),
		12 : (CentralApronNames, ),
		13 : (CentralApronNames, ),
		14 : (CentralApronNames, ),
		15 : (CentralApronNames, ),
		16 : (CentralApronNames, ),
		17 : (CentralApronNames, ),
		20 : (CentralApronRemoteNames, ),
		21 : (CentralApronRemoteNames, ),
		22 : (CentralApronRemoteNames, ),
		23 : (CentralApronRemoteNames, ),
		24 : (CentralApronRemoteNames, ),
		30 : (CentralApronRemoteNames, ),
		31 : (CentralApronRemoteNames, ),
		32 : (CentralApronRemoteNames, ),
		33 : (CentralApronRemoteNames, ),
		40 : (CentralWestApronNames, ),
		41 : (CentralWestApronNames, ),
		42 : (CentralWestApronNames, ),
		43 : (CentralWestApronNames, ),
		44 : (CentralWestApronNames, ),
		45 : (CentralWestApronNames, ),
		"70R" : (EasternApron, ),
		70 : (EasternApron, ),
		"70L" : (EasternApron, ),
		71 : (EasternApron, ),
		72 : (EasternApron, ),
		73 : (EasternApron, ),
		"73L" : (EasternApron, ),
		74 : (EasternApron, ),
		"74L" : (EasternApron, ),
		75 : (EasternApron, ),
		"75R" : (EasternApron, ),
		"76R" : (EasternApron, ),
		76 : (EasternApron, ),
		"76L" : (EasternApron, ),
		"77R" : (EasternApron, ),
		77 : (EasternApron, ),
		"78R" : (EasternApron, ),
		78 : (EasternApron, ),
		"78L" : (EasternApron, ),
		79 : (EasternApron, ),
		80 : (EasternApron, ),
		81 : (EasternApron, ),
		82 : (EasternApron, ),
		83 : (EasternApron, ),
		84 : (EasternApron, ),
		85 : (EasternApron, ),
		86 : (EasternApron, ),
	},
	0 : {
		None : ( ),
		98 : (WesternApron, ),
		99 : (WesternApron, ),
		100 : (WesternApron, ),
		101 : (WesternApron, ),
		102 : (WesternApron, ),
		103 : (WesternApron, ),
		104 : (WesternApron, ),
		105 : (WesternApron, ),
		106 : (WesternApron, ),
		107 : (WesternApron, ),
		108 : (WesternApron, ),
		109 : (WesternApron, ),
		110 : (WesternApron, ),
		111 : (WesternApron, ),
		112 : (WesternApron, ),
		114 : (WesternApron, ),
		120 : (WesternApron, ),
		121 : (WesternApron, ),
		122 : (WesternApron, ),
		123 : (WesternApron, ),
		124 : (WesternApron, ),
		125 : (WesternApron, ),
		"125R" : (WesternApron, ),
		"125L" : (WesternApron, ),
		200 : (WesternApronRemote, ),
		201 : (WesternApronRemote, ),
		"201L" : (WesternApronRemote, ),
		"201R" : (WesternApronRemote, ),
		202 : (WesternApronRemote, ),
		"202L" : (WesternApronRemote, ),
		"202R" : (WesternApronRemote, ),
		203 : (WesternApronRemote, ),
		"203R" : (WesternApronRemote, ),
	},
	SW_PARKING : {
		None : (MainAreaNorthNames, ),
	},
	S_PARKING : {
		None : (MainAreaSouthNames, ),
		1 : (MainAreaSouthNames, ),
		2 : (MainAreaSouthNames, ),
	},
	W_PARKING : {
		None : (RVLApronNames, ),
	},
}