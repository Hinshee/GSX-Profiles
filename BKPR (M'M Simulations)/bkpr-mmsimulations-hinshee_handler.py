msfs_mode = 1
version = 1.2

# Pyreegue EGPHv2 Handler
AIRPORT_ICAO = "BKPR"
SCENERY = "M'M Simulations Prishtina"
VEHICLE_PREFERENCE = {
    "Staircase": {"search": ["CDS"], "boost": 50},
    "Pushback": {"search": ["Trepel"], "boost": 50},
    "PassengerBus": {"search": ["Cobus"], "boost": 50},
    "BaggageTractor": {"search": ["JET_16"], "boost": 50},
}

AIRLINE_HANDLERS = {
}

FALLBACKS = ""
FALLBACK_DEFAULT = "LIMAK"

def _is_this_airport():
    a = getAirport()
    return bool(a and getattr(a, "icao", None) == AIRPORT_ICAO)

def stripWhitespace(s):
    return s.strip() if s else s

def get_simbrief_icao():
    sb = getSimbrief()

    if not sb:
        return None
    
    if getattr(sb, "last_error", None):
        return None
    
    code = getattr(sb, "icao_airline", None)

    if not code:
        return None
    
    return str(code).strip().upper()

def resolve_icao():
    icao = get_simbrief_icao()

    if not icao:
        icao = getattr(aircraft, "icaoAirline", None)
        if icao:
            icao = str(icao).strip().upper()
    
    return icao

def get_handler():
    icao = resolve_icao()
    
    if icao and icao in AIRLINE_HANDLERS:
        return AIRLINE_HANDLERS[icao]
    if icao and FALLBACK_DEFAULT:
        return FALLBACK_DEFAULT
    return FALLBACKS

def apply_handler():
    gate = getGate()
    
    if not gate:
        return
    
    handler = get_handler()

    gate.handlingTexture = handler

def onAirportVehicleCandidatesScored(self, vehicleType, candidates):
    if not _is_this_airport():
        return

    pref = VEHICLE_PREFERENCE.get(vehicleType)
    if not pref:
        return

    title_needles = [n.lower() for n in pref.get("search", [])]
    boost = pref.get("boost", 0)

    # Get handler value from current airline for texture matching
    handler_value = get_handler()
    texture_needles = [handler_value.lower()] if handler_value else []

    if not boost or (not title_needles and not texture_needles):
        return

    # Candidate Scoring
    for c in candidates:
        try:
            title = str(getattr(c, "title", "") or "")
        except Exception:
            title = ""

        try:
            texture = str(getattr(c, "texture", "") or "")
        except Exception:
            texture = ""

        # Check if title matches
        title_matched = False
        for needle in title_needles:
            if needle and needle in title.lower():
                title_matched = True
                break

        # Check if texture matches
        texture_matched = False
        for needle in texture_needles:
            if needle and needle in texture.lower():
                texture_matched = True
                break

        # Only boost if both title AND texture match
        if title_matched and texture_matched:
            c.boostScore(boost)

def onAirportBeforeVehicleSelect(self):
    apply_handler()