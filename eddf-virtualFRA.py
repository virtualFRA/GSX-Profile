# -- coding: utf-8 --

msfs_mode = 1
icao = "eddf"

def HandleAircraftOffsets(aircraftData, specificTables, genericTable):
    major_id = aircraftData.idMajor
    minor_id = aircraftData.idMinor

    if major_id in specificTables:
        specific_table, fallback_key = specificTables[major_id]
        result = specific_table.get(minor_id)
        if result is None:
            result = specific_table.get(fallback_key)
    else:
        result = genericTable.get(major_id, 0)

    return result

@AlternativeStopPositions
def customOffsetequal(aircraftData):

    table = {
        0: 0,
    }

    return Distance.fromMeters( table.get(aircraftData.idMajor, 0) )


Terminal1ASE = CustomizedName("Terminal 1 - A Gates (A1-A40 (V143+V144)) | Gate A#§",1)
Terminal1AN = CustomizedName("Terminal 1 - A Gates (A50-A69) | Gate A#§",2)

Terminal1BW = CustomizedName("Terminal 1 - B Gates (B10-B27) | Gate B#§",3)
Terminal1BE = CustomizedName("Terminal 1 - B Gates (B41-B48) | Gate B#§",4)

Terminal1CW = CustomizedName("Terminal 1 - C Gates (C2-C11) | Gate C#§",5)
Terminal2CE = CustomizedName("Terminal 2 - C Gates (C13-C16) | Gate C#§",6)

Terminal2DW = CustomizedName("Terminal 2 - D Gates (D1-D8) | Gate D#§",7)
Terminal2EE = CustomizedName("Terminal 2 - E Gates (E2-E9) | Gate E#§",8)

LHCargo = CustomizedName("LH Cargo Ramp (F211-F225) | Stand F#§",9)
NECargoF = CustomizedName("Cargo Ramp (F231-V270) | Stand F#§",10)
NECargoV = CustomizedName("Cargo Ramp (F231-V270) | Stand V#§",10)

VRampE = CustomizedName("Victor Ramp (V94-V118) | Stand V#§",11)
VRampCE = CustomizedName("Victor Ramp (V119-V130) | Stand V#§",12)
VRampCW = CustomizedName("Victor Ramp (V134-V163) | Stand V#§",13)
VRampW = CustomizedName("Victor Ramp V164-V178) | Stand V#§",14)

GAArea = CustomizedName("GA Area (S401-S420) | Stand S#",15)

SRamp = CustomizedName("Sierra Ramp [S] (S501-S604) | Stand S#",16)

Terminal3WG = CustomizedName("Terminal 3 - G Gates [W] (G1-G16) | Gate G#§",17)
Terminal3CH = CustomizedName("Terminal 3 - H Gates [C] (H2-H14) | Gate H#§",18)

Terminal3EJ = CustomizedName("Terminal 3 - J+K Gates (J2-J11+K2-K10) | Gate J#§",19)
Terminal3EK = CustomizedName("Terminal 3 - J+K Gates (J2-J11+K2-K10) | Gate K#§",19)

VRampSW = CustomizedName("Victor Ramp (V322-V328) | Stand V#§",20)
VRampSE = CustomizedName("Victor Ramp+GAT(V701-V721) | Stand V#§",21)


parkings = {

    GATE : {
        None : ( ),
        16 : (Terminal2CE, ),
    },

    GATE_A : {
        None : ( ),
        1 : (Terminal1ASE, ),
        11 : (Terminal1ASE, ),
        13 : (Terminal1ASE, ),
        14 : (Terminal1ASE, ),
        15 : (Terminal1ASE, ),
        16 : (Terminal1ASE, ),
        17 : (Terminal1ASE, ),
        18 : (Terminal1ASE, ),
        19 : (Terminal1ASE, ),
        20 : (Terminal1ASE, ),
        21 : (Terminal1ASE, ),
        22 : (Terminal1ASE, ),
        23 : (Terminal1ASE, ),
        24 : (Terminal1ASE, ),
        25 : (Terminal1ASE, ),
        26 : (Terminal1ASE, ),
        28 : (Terminal1ASE, ),
        30 : (Terminal1ASE, ),
        34 : (Terminal1ASE, ),
        36 : (Terminal1ASE, ),
        38 : (Terminal1ASE, ),
        40 : (Terminal1ASE, ),
        
        50 : (Terminal1AN, ),
        52 : (Terminal1AN, ),
        54 : (Terminal1AN, ),
        "54A" : (Terminal1AN, ),
        "54B" : (Terminal1AN, ),
        58 : (Terminal1AN, ),
        "58A" : (Terminal1AN, ),
        "58B" : (Terminal1AN, ),
        62 : (Terminal1AN, ),
        "62A" : (Terminal1AN, ),
        "62B" : (Terminal1AN, ),
        66 : (Terminal1AN, ),
        "66A" : (Terminal1AN, ),
        "66B" : (Terminal1AN, ),
        69 : (Terminal1AN, ),
    },

    GATE_B : {
        None : ( ),
        10 : (Terminal1BW, ),
        20 : (Terminal1BW, ),
        22 : (Terminal1BW, ),
        23 : (Terminal1BW, ),
        24 : (Terminal1BW, ),
        25 : (Terminal1BW, ),
        26 : (Terminal1BW, ),
        27 : (Terminal1BW, ),
        28 : (Terminal1BW, ),
        
        41 : (Terminal1BE, ),
        42 : (Terminal1BE, ),
        43 : (Terminal1BE, ),
        44 : (Terminal1BE, ),
        45 : (Terminal1BE, ),
        46 : (Terminal1BE, ),
        47 : (Terminal1BE, ),
        48 : (Terminal1BE, ),
    },

    GATE_C : {
        None : ( ),
        2 : (Terminal1CW, ),
        4 : (Terminal1CW, ),
        5 : (Terminal1CW, ),
        6 : (Terminal1CW, ),
        8 : (Terminal1CW, ),
        11 : (Terminal1CW, ),
        13 : (Terminal2CE, ),
        14 : (Terminal2CE, ),
        15 : (Terminal2CE, ),
        "15B" : (Terminal2CE, ),
        "15A" : (Terminal2CE, ),
        16 : (Terminal2CE, ),
        "16A" : (Terminal2CE, ),
    },

    GATE_D : {
        None : ( ),
        1 : (Terminal2DW, ),
        "1A" : (Terminal2DW, ),
        4 : (Terminal2DW, ),
        "4A" : (Terminal2DW, ),
        "4B" : (Terminal2DW, ),
        5 : (Terminal2DW, ),
        "5A" : (Terminal2DW, ),
        8 : (Terminal2DW, ),
        "8A" : (Terminal2DW, ),
    },

    GATE_E : {
        None : ( ),
        2 : (Terminal2EE, ),
        "2A" : (Terminal2EE, ),
        "2B" : (Terminal2EE, ),
        5 : (Terminal2EE, ),
        "5A" : (Terminal2EE, ),
        6 : (Terminal2EE, ),
        "6A" : (Terminal2EE, ),
        9 : (Terminal2EE, ),
        "9A" : (Terminal2EE, ),
    },

    GATE_F : {
        None : ( ),
        211 : (LHCargo, ),
        212 : (LHCargo, ),
        213 : (LHCargo, ),
        214 : (LHCargo, ),
        215 : (LHCargo, ),
        216 : (LHCargo, ),
        221 : (LHCargo, ),
        222 : (LHCargo, ),
        223 : (LHCargo, ),
        224 : (LHCargo, ),
        225 : (LHCargo, ),
        
        231 : (NECargoF, ),
        232 : (NECargoF, ),
        233 : (NECargoF, ),
        234 : (NECargoF, ),
        235 : (NECargoF, ),
        237 : (NECargoF, ),
        238 : (NECargoF, ),
    },

    GATE_V : {
        None : ( ),
        94 : (VRampE, ),
        95 : (VRampE, ),
        96 : (VRampE, ),
        97 : (VRampE, ),
        106 : (VRampE, ),
        107 : (VRampE, ),
        108 : (VRampE, ),
        109 : (VRampE, ),
        110 : (VRampE, ),
        111 : (VRampE, ),
        112 : (VRampE, ),
        113 : (VRampE, ),
        114 : (VRampE, ),
        115 : (VRampE, ),
        116 : (VRampE, ),
        117 : (VRampE, ),
        118 : (VRampE, ),
        
        119 : (VRampCE, ),
        120 : (VRampCE, ),
        121 : (VRampCE, ),
        122 : (VRampCE, ),
        123 : (VRampCE, ),
        124 : (VRampCE, ),
        125 : (VRampCE, ),
        126 : (VRampCE, ),
        127 : (VRampCE, ),
        128 : (VRampCE, ),
        129 : (VRampCE, ),
        130 : (VRampCE, ),
        134 : (VRampCW, ),
        135 : (VRampCW, ),
        136 : (VRampCW, ),
        
        143 : (Terminal1ASE, ),
        144 : (Terminal1ASE, ),
        
        151 : (VRampCW, ),
        152 : (VRampCW, ),
        153 : (VRampCW, ),
        157 : (VRampCW, ),
        158 : (VRampCW, ),
        159 : (VRampCW, ),
        160 : (VRampCW, ),
        161 : (VRampCW, ),
        162 : (VRampCW, ),
        163 : (VRampCW, ),
        
        164 : (VRampW, ),
        165 : (VRampW, ),
        166 : (VRampW, ),
        167 : (VRampW, ),
        168 : (VRampW, ),
        169 : (VRampW, ),
        170 : (VRampW, ),
        171 : (VRampW, ),
        "171A" : (VRampW, ),
        "171B" : (VRampW, ),
        172 : (VRampW, ),
        "172A" : (VRampW, ),
        "172B" : (VRampW, ),
        173 : (VRampW, ),
        "173A" : (VRampW, ),
        "173B" : (VRampW, ),
        174 : (VRampW, ),
        175 : (VRampW, ),
        176 : (VRampW, ),
        177 : (VRampW, ),
        178 : (VRampW, ),
        
        266 : (NECargoV, ),
        267 : (NECargoV, ),
        268 : (NECargoV, ),
        269 : (NECargoV, ),
        270 : (NECargoV, ),
        
        322 : (VRampSW, ),
        324 : (VRampSW, ),
        326 : (VRampSW, ),
        328 : (VRampSW, ),
        
        701 : (VRampSE, ),
        702 : (VRampSE, ),
        704 : (VRampSE, ),
        706 : (VRampSE, ),
        708 : (VRampSE, ),
        711 : (VRampSE, ),
        712 : (VRampSE, ),
        713 : (VRampSE, ),
        714 : (VRampSE, ),
        715 : (VRampSE, ),
        716 : (VRampSE, ),
        717 : (VRampSE, ),
        718 : (VRampSE, ),
        719 : (VRampSE, ),
        721 : (VRampSE, ),
    },

    GATE_G : {
        None : ( ),
        1 : (Terminal3WG, ),
        2 : (Terminal3WG, ),
        3 : (Terminal3WG, ),
        4 : (Terminal3WG, ),
        5 : (Terminal3WG, ),
        6 : (Terminal3WG, ),
        7 : (Terminal3WG, ),
        8 : (Terminal3WG, ),
        9 : (Terminal3WG, ),
        10 : (Terminal3WG, ),
        11 : (Terminal3WG, ),
        12 : (Terminal3WG, ),
        13 : (Terminal3WG, ),
        14 : (Terminal3WG, ),
        15 : (Terminal3WG, ),
        16 : (Terminal3WG, ),
    },

    GATE_H : {
        None : ( ),
        2 : (Terminal3CH, ),
        4 : (Terminal3CH, ),
        6 : (Terminal3CH, ),
        8 : (Terminal3CH, ),
        10 : (Terminal3CH, ),
        12 : (Terminal3CH, ),
        14 : (Terminal3CH, ),
    },

    GATE_K : {
        None : ( ),
        2 : (Terminal3EK, ),
        4 : (Terminal3EK, ),
        6 : (Terminal3EK, ),
        8 : (Terminal3EK, ),
        10 : (Terminal3EK, ),
    },

    GATE_J : {
        None : ( ),
        2 : (Terminal3EJ, ),
        "2A" : (Terminal3EJ, ),
        "2B" : (Terminal3EJ, ),
        4 : (Terminal3EJ, ),
        5 : (Terminal3EJ, ),
        6 : (Terminal3EJ, ),
        "6A" : (Terminal3EJ, ),
        "6B" : (Terminal3EJ, ),
        7 : (Terminal3EJ, ),
        8 : (Terminal3EJ, ),
        9 : (Terminal3EJ, ),
        11 : (Terminal3EJ, ),
    },

}