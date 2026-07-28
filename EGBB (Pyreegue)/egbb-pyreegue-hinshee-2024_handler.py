msfs_mode = 1
version = 1.4.0

# Pyreegue EGBB Handler
# With Thanks to Krake for the support <3

HANDLERS = {
    "EIN": "SWISSPORT",
    "EAI": "SWISSPORT",
    "EAG": "SWISSPORT",
    "DLA": "SWISSPORT",
    "AFR": "SWISSPORT",
    "AIC": "SWISSPORT",
    "AUR": "SWISSPORT",
    "CAI": "SWISSPORT",
    "EZY": "SWISSPORT",
    "EJU": "SWISSPORT",
    "EZS": "SWISSPORT",
    "UAE": "SWISSPORT",
    "EWG": "SWISSPORT",
    "LOG": "SWISSPORT",
    "DLH": "SWISSPORT",
    "LHX": "SWISSPORT",
    "PGT": "SWISSPORT",
    "QTR": "SWISSPORT",
    "RYR": "SWISSPORT",
    "RUK": "SWISSPORT",
    "MAY": "SWISSPORT",
    "RYS": "SWISSPORT",
    "LDA": "SWISSPORT",
    "SVA": "SWISSPORT",
    "SAS": "SWISSPORT",
    "SXS": "SWISSPORT",
    "SWR": "SWISSPORT",
    "THY": "SWISSPORT",
    "WZZ": "SWISSPORT",
    "WUK": "SWISSPORT",
    "WMT": "SWISSPORT",
    "GEC": "SWISSPORT",
    "SRR": "SWISSPORT",
    "EXS": "EXS_WHITE",
    "TOM": "TUI",
    "KLM": "SKYTANKING",
    "KLC": "SKYTANKING",
}

HANDLING_FALLBACKS = "EXS,EXS_WHITE,SWISSPORT,SKYTANKING,TUI"

CATERING = {
    "EIN": "DNATA",
    "EAI": "DNATA",
    "EAG": "DNATA",
    "DLA": "DNATA",
    "AFR": "DNATA",
    "AIC": "DNATA",
    "AUR": "DNATA",
    "CAI": "DNATA",
    "EZY": "DNATA",
    "EJU": "DNATA",
    "EZS": "DNATA",
    "UAE": "DNATA",
    "EWG": "DNATA",
    "LOG": "DNATA",
    "DLH": "DNATA",
    "LHX": "DNATA",
    "PGT": "DNATA",
    "QTR": "DNATA",
    "RYR": "DNATA",
    "RUK": "DNATA",
    "MAY": "DNATA",
    "RYS": "DNATA",
    "LDA": "DNATA",
    "SVA": "DNATA",
    "SAS": "DNATA",
    "SXS": "DNATA",
    "SWR": "DNATA",
    "THY": "DNATA",
    "WZZ": "DNATA",
    "WUK": "DNATA",
    "WMT": "DNATA",
    "GEC": "DNATA",
    "SRR": "DNATA",
    "EXS": "DNATA",
    "TOM": "DNATA",
    "KLM": "DNATA",
    "KLC": "DNATA",
}

CATERING_FALLBACKS = "DNATA"

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

def get_handler():
    icao = get_simbrief_icao()

    if not icao:
        icao = getattr(aircraft, "icaoAirline", None)
        if icao:
            icao = str(icao).strip().upper()
    
    if icao and icao in HANDLERS:
        return HANDLERS[icao], icao
    
    return HANDLER_FALLBACKS, icao

def get_catering():
    icao = get_simbrief_icao()

    if not icao:
        icao = getattr(aircraft, "icaoAirline", None)
        if icao:
            icao = str(icao).strip().upper()
    
    if icao and icao in CATERING:
        return CATERING[icao], icao
    
    return CATERING_FALLBACKS, icao

def apply_handler():
    gate = getGate()
    
    if not gate:
        return
    
    handler, icao = get_handler()
    catering, icao = get_catering()

    gate.handlingTexture = handler
    gate.cateringTexture = catering
    print(f"Handler: {handler} set for airline: {icao}")

def onAirportBeforeVehicleSelect(self):
    apply_handler()
    VDGSMessages(self)

def onAircraftEngaged(self):
    VDGSMessages(self)

def onVehicleCandidatesScored(self, vehicleType, candidates):
    CDS_ACFT = [737, 320, 319, 318, 321, 757]
    idMajor = aircraft.idMajor

    if vehicleType == "Staircase":
        for c in candidates:
            if 'CDS' in c.title and '2445' in c.title and idMajor in CDS_ACFT:
                c.boostScore(10)

            elif 'CDS' in c.title and '2445' in c.title:
                c.boostScore(-10)

            if 'FW' in c.title:
                c.boostScore(-10)

    if vehicleType == "BaggageTractor":
        for c in candidates:
            if 'JET_16' in c.title:
                c.boostScore(10)

def VDGSMessages(self):
    # Replace the stock flight info page with custom content
    addVdgsMessage({
        "id": "flight_information",
        "display": {
            "small": {
                "pages": [{"lines": ["WAIT"], "duration": 500000}]
            }
        }
    })
    
    addVdgsMessage({
        "id": "chock_and_gate_display",
        "display": {
            "small": {
                "pages": [
                    {"lines": [
                        ''
                    ], "duration": 0}
                ]
            }
        }
    })

    addVdgsMessage({
        "id": "connections_display",
        "display": {
            "small": {
                "pages": [
                    {"lines": [
                        ''
                    ], "duration": 0}
                ]
            }
        }
    })
    
    addVdgsMessage({
        "id": "passenger_cargo_info",
        "display": {
            "small": {
                "pages": [
                    {"lines": [
                        ''
                    ], "duration": 0}
                ]
            }
        }
    })