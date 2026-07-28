msfs_mode = 1
version = 1.3

# ORBX EGPH Handler
AIRPORT_ICAO = "EGPH"
SCENERY = "Pyreegue Edinburgh"
VEHICLE_PREFERENCE = {
    "Staircase": {"search": ["CDS"], "boost": 50},
    "Pushback": {"search": ["Trepel"], "boost": 50},
    "PassengerBus": {"search": ["Cobus"], "boost": 50},
    "BaggageTractor": {"search": ["Endurance"], "boost": 50},
}

BAD_JETWAY_GATES = {
    "Main Apron (1-14, 99-106)": {
        "Gate 3A",
        "Gate 4"
    },
    }

AIRLINE_HANDLERS = {
    "AAL": "SWISSPORT",
    "ACA": "SWISSPORT",
    "AEE": "SWISSPORT",
    "AFR": "SWISSPORT",
    "AWC": "MENZ",
    "BEL": "AVIATIONSERVICES",
    "BGH": "SWISSPORT",
    "CHH": "SWISSPORT",
    "DAL": "SWISSPORT",
    "DLH": "MENZ",
    "EAG": "SWISSPORT",
    "EAI": "SWISSPORT",
    "EDW": "MENZ",
    "EJU": "AVIATIONSERVICES",
    "EWG": "SWISSPORT",
    "EXS": "EXS_WHITE",
    "EZS": "AVIATIONSERVICES",
    "EZY": "AVIATIONSERVICES",
    "FHY": "SWISSPORT",
    "FIN": "MENZ",
    "FLI": "SWISSPORT",
    "IBE": "MENZ",
    "JBU": "SWISSPORT",
    "KLM": "SWISSPORT",
    "LAV": "SWISSPORT",
    "LOG": "MENZ",
    "NSZ": "SWISSPORT",
    "NOZ": "SWISSPORT",
    "PGT": "MENZ",
    "QTR": "SWISSPORT",
    "RUK": "SWISSPORT",
    "RYR": "SWISSPORT",
    "SAS": "SWISSPORT",
    "SHT": "MENZ",
    "SXS": "MENZ",
    "THY": "SWISSPORT",
    "TOM": "SWISSPORT",
    "TRA": "SWISSPORT",
    "TUI": "SWISSPORT",
    "UAE": "MENZ",
    "UAL": "MENZ",
    "VIR": "SWISSPORT",
    "VLG": "MENZ",
    "WJA": "SWISSPORT",
}

FALLBACKS = "SWISSPORT,MENZ,WFS,AVIATIONSERVICES,EXS_WHITE"
FALLBACK_DEFAULT = "SWISSPORT"

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

def Bad_Jetway_Data_Check(self):
    if not _is_this_airport():
        return
    
    gateData = getGate()
    terminal = stripWhitespace(gateData.uiTerminalName)
    stand = stripWhitespace(gateData.uiGateName)
    print("DEBUG: Detected Terminal: '%s', Stand: '%s'" % (terminal, stand))
    BAD_GATES = BAD_JETWAY_GATES.get(terminal, [])
    if stand in BAD_GATES:
        print("DEBUG: Detected Bad Jetway Data for Terminal '%s', Stand '%s'" % (terminal, stand))
        choice = choiceBox(
            "Bad Jetway Data Detected\n"
            "Would you like to try toggling the jetway via SimConnect?\n\n"
            "Note: This is not guaranteed to work. Please don't report this as an issue to GSX or the Scenery Developer - this is an Asobo issue as a jetway can only be connected to one gate.",
            "%s - GSX Profile" % SCENERY,
            ["YES", "NO"],
            default=0,
        )
        if choice == 0:
            transmitKeyEvent("TOGGLE_JETWAY")

def onAirportBeforeVehicleSelect(self):
    apply_handler()

def onBoardingRequested(self):
    Bad_Jetway_Data_Check(self)

def onDeboardingRequested(self):
    Bad_Jetway_Data_Check(self)
    
def onJetwayRequested(self):
    Bad_Jetway_Data_Check(self)
    
def onDepartureRequested(self):
    Bad_Jetway_Data_Check(self)