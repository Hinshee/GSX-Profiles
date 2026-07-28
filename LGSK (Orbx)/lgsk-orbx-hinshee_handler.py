msfs_mode = 1

# ORBX LGSK Handler
AIRPORT_ICAO = "LGSK"
VEHICLE_PREFERENCE = {
    "Staircase": {"search": ["CDS"], "boost": 50},
    "Pushback": {"search": ["Trepel"], "boost": 50},
    "PassengerBus": {"search": ["Neoplan"], "boost": 50},
    "BaggageTractor": {"search": ["Endurance"], "boost": 50},
}


def _is_this_airport():
    a = getAirport()
    return bool(a and getattr(a, "icao", None) == AIRPORT_ICAO)


def onAirportVehicleCandidatesScored(self, vehicleType, candidates):
    if not _is_this_airport():
        return

    pref = VEHICLE_PREFERENCE.get(vehicleType)
    if not pref:
        return

    title_needles = [n.lower() for n in pref.get("search", [])]
    boost = pref.get("boost", 0)

    if not boost or not title_needles:
        return

    # Candidate Scoring
    for c in candidates:
        title = str(getattr(c, "title", "") or "").lower()
        if any(needle in title for needle in title_needles):
            c.boostScore(boost)
