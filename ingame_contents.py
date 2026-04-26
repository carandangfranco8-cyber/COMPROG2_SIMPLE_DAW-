
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
    "Bullet Shell": ["Assassination Attempt"],
    "Old Man": ["Murder"],
    "Phone": ["Communication Breakdown"],
    "Notebook": ["Confession Evidence"],
    "Angel’s Staff": ["Location Link"],
    "Kitchen Tools": ["Poisoning", "Murder Planning"]
}

evidence_map3=  {
    "Tea": ["Poisoning"],  # poisoned drink (main clue)
    "Finger Sandwiches": ["Poisoning"],
    "Fruit Platter": ["Allergic Reaction"],
    "Wine": ["Complication"],
    "Pastries": ["Choking"],
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

evidence_map33 = [
"Tea: “Only drink served personally by a guest before the gathering began. Cup shows trace contamination before service time.”",

"Finger Sandwiches: “Prepared in batches and left on table during the event. No immediate tampering observed.”",

"Fruit Platter: “Freshly sliced fruits, but traces of allergens detected in mixed serving area.”",

"Wine: “Opened during the gathering, shared among multiple guests. No early contamination found.”",

"Pastries: “Stored in open display tray. Risk of accidental choking due to dry texture.”",

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
        "cause_of_death": "Gunshot"
        },
        "location": "Angel’s Staff"
    },
]

cause_of_death = [
  "Stab Wound", 
  "Allergic Reaction", 
  "Complication",
  "Choking",
  ]

cause_of_death_2 = [
    "Poisoning",
    "Stab Wound",
    "Allergic Reaction",
    "Choking",
    "Complication"
]

cause_of_death_3 = [
    "Stab Wound", 
    "Allergic Reaction", 
    "Complication",
    "Choking",
    "Poisoning"
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
            "Bullet Shell": "--Trajectory suggests the shot was not fired from a random position, but from a controlled line of sight.",
            
            "Phone Call": "--Final transmission contains signs of urgency followed by an abrupt disruption in communication flow.",
            
            "Notebook": "--Entries show inconsistencies between payment expectations and operational instructions.",
            
            "Angel’s Staff": "--Location repeatedly referenced in connection with personnel movement and internal coordination.",
            
            "Old Man Scene": "--Victim appears to be unintended target, indicating misdirection during execution."
        }
    }
 
evidence_3 = [
    {
        "HINT": "CASE 3",
        "HINTS": {
            "Tea Cup": "--Thermal residue analysis suggests the drink's condition does not fully align with the reported serving timeline.",
            
            "Guest Statements": "--Several accounts disagree on the sequence of beverage distribution, particularly regarding initial service.",
            
            "Serving Tray": "--Only one item shows handling patterns inconsistent with collective serving activity.",
            
            "Kitchen Log": "--Preparation records contain a timing gap that does not match recorded guest arrival flow.",
            
            "Observation Note": "--Toxic effect onset suggests exposure occurred outside the assumed interaction window."
        }
    }
]