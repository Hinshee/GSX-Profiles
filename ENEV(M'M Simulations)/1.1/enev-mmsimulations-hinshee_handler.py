msfs_mode = 1
version = 1.1

AIRPORT_ICAO = "ENEV"

def _set_aviramp_exits(handler):
	handler.avirampExits = [0]

def _is_this_airport():
	a = getAirport()
	return bool(a and getattr(a, "icao", None) == AIRPORT_ICAO)

def onEnterAirport(self):
	if not _is_this_airport():
		return

def onAirportBeforeVehicleSelect(self):
	if not _is_this_airport():
		return
	_set_aviramp_exits(self)