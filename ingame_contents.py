
#MAKE ANOTHER EVIDENCE MAP1

evidence_map1 =  {
    "Roasted Chicken": ["Poisoning", "Choking"],
    "Ice Cream": ["Allergic Reaction", "Intolerance"],
    "Soup": ["Poisoning"], #Poisoned
    "Steak": ["Choking"],
    "Salad": ["Poisoning"],
    "Condiments": ["Poisoning"]
}


evidence_map11 = [
"Soup: “Only item reheated before serving. Minor temperature fluctuation recorded during holding stage.”",

"Roasted Chicken: “Even seasoning confirmed across all portions. No anomalies detected in prep.”",

"Ice Cream: “Continuous freezer monitoring shows no interruptions.”",

"Steak: “Served immediately after cooking, no holding time.”",

"Salad: “All ingredients individually verified clean before mixing.”",

"Condiments: “Frequently used but properly sealed and replaced during service.”"
    
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
  


cause_of_death = [
  "Stab Wound", 
  "Allergic Reaction", 
  "Complication",
  "Choking",
  ]



evidence2 = [
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

 