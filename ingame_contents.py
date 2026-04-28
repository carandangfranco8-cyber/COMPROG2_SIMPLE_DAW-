
#MAKE ANOTHER EVIDENCE MAP1

evidence_map1 =  {
    "Roasted Chicken": ["Poisoning", "Choking"],
    "Ice Cream": ["Allergic Reaction", "Intolerance"],
    "Soup": ["Poisoning"], #Poisoned
    "Steak": ["Choking"],
    "Salad": ["Poisoning"], 
    "Condiments": ["Poisoning"]
}

evidence_map2 = {
    "Weapon Malfunction": ["Wrong"],
    "Assassin Missed Shot": ["Wrong"],
    "Victim Misidentified": ["Failure caused by the victim being identified incorrectly at the scene"],
    "External Interference": ["Wrong"]
}

evidence_map3 = {
    "Tea": ["Poisoning"],  # poisoned drink (main clue)
    "Finger Sandwiches": ["Poisoning"],
    "Fruit Platter": ["Allergic Reaction"],
    "Wine": ["Complication"],
    "Condiments Tray": ["Poisoning"]
}



evidence_map11 = [
"Soup: “Only item reheated before serving. Minor temperature fluctuation recorded during holding stage.”",

"Roasted Chicken: “Even seasoning confirmed across all portions. No anomalies detected in prep.”",

"Ice Cream: “Continuous freezer monitoring shows no interruptions.”",

"Steak: “Served immediately after cooking, no holding time.”",

"Salad: “All ingredients individually verified clean before mixing.”",

"Condiments: “Frequently used but properly sealed and replaced during service.”"
    
]

evidence_map22 = [

"Bullet Shell: “Recovered from the rooftop line of fire. Caliber matches standard hired-hit equipment.”",

"Old Man: “Victim confirmed collateral damage after bodyguard intervention redirected the shot.”",

"Phone: “Last outgoing call shows sudden interruption followed by background struggle sounds.”",

"Notebook: “Contains fragmented entries about payment delay and employer identity hints.”",

"Angel’s Staff: “A known location tied to past staff movements and internal personnel access.”",

"Kitchen Tools: “Shows prior handling consistent with food preparation and controlled access environment.”"

]

evidence_map44 = [
"Tea: “Only drink served personally by a GUEST before the gathering began. Cup shows trace contamination before service time.”",

"Finger Sandwiches: “Prepared in batches and left on table during the event. No immediate tampering observed.”",

"Fruit Platter: “Freshly sliced fruits, but traces of allergens detected in mixed serving area.”",

"Wine: “Opened during the gathering, shared among multiple guests. No early contamination found.”",

"Condiments Tray: “Prepared before guests arrived. Frequently handled but no mid-event contamination detected.”"

]


cases = [
    {
        "name": "Case 1",
        "victim": {
            "name": "Robert",
            "age": "32",
            "career": "Guard",
            "cause_of_death": "Poisoning"
            
        },
        "location": "Angel's Share"
    }
]

cases3 = [
    {
        "name": "Case 3 - Diplomat Murder Case",
        "victim": {
            "name": "Unnamed Diplomat",
            "age": "45",
            "career": "Diplomat",
            "cause_of_death": "Poisoning"
        },
            "location": "Diplomat Residence"
    }
    ]

cases2 = [
     {
        "name": "Case 2 - Failed Assassination Incident",
        "victim": {
        "name": "Unnamed Old Man",
        "age": "68",
        "career": "Civilian",
        "cause_of_death": "Failure caused by the victim being identified incorrectly at the scene",
        },
        "location": "COUNTRYSNACK"
        
    },
]

cause_of_death = [
  "Stab Wound", 
  "Allergic Reaction", 
  "Complication",
  "Choking",
  ]


cause_of_death_2 = [
    "Failure caused by weapon malfunction during execution",

    "Failure caused by the assassin missing the target during the shot",

    "Failure caused by external interference after the assassination attempt"
]


cause_of_death_3 = [
    "Stab Wound", 
    "Allergic Reaction", 
    "Complication",
    "Choking",
]


evidence_1 = [
    {
        "HINT": "CASE 1",
        "HINTS": {
            "Bloody knife": "--Seems like the blood come from the food not a human being.",
            "Footprints": "--Lead to the kitchen area. Someone was present during food prep.",
            "Vial of iocaine": "--A rare odorless poison used in food contamination cases.",
            "Medical report": "--Victim died from anaphylaxis reaction, not direct injury."
        }
    }
]

evidence_2 = {
        "HINT": "CASE 2 - Failed Assassination Incident",
        "HINTS": {
        "Bullet Shell": "--Confirms the shot was accurate. The weapon worked as intended.",

        "Phone Call": "--Final call shows panic and sudden interruption. Suggests communication broke during the mission.",

        "Notebook": "--Contains wrong or unclear instructions from the start. Indicates the plan itself was flawed.",

        "Angel’s Staff": "--Only shows where people were moving. Not related to why the mission failed.",

        "Old Man Scene": "--Victim was not the intended target. This is the RESULT of the failure, not the cause."
    }
    }
 
evidence_3 = [
    {
        "HINT": "CASE 3",
        "HINTS": {
            "Tea Cup": "--A faint trace lingers in the drink, something that shouldn’t be there.",
            
            "Guest Statements": "--They agree on when it was served, but not on its condition.",
            
            "Serving Tray": "--One cup seems to have been set apart before the others.",
            
            "Kitchen Log": "--Preparation was completed earlier than the gathering suggests.",
            
            "Medical Report": "--The reaction began quietly, long before anyone noticed."
        }
    }
]