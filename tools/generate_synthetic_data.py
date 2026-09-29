"""Generate the #AI4Elections synthetic starter data pack.
All data is FICTIONAL. Party names, IDs, people and events do not correspond to any
real party, polling unit, voter or incident. Seeded for reproducibility.
Usage: python tools/generate_synthetic_data.py
"""
import csv, json, random, os
from datetime import datetime, timedelta
random.seed(2026)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "synthetic")
os.makedirs(OUT, exist_ok=True)

ZONES = {
 "North Central": ["Benue", "Kwara", "Plateau", "Niger"],
 "North East": ["Bauchi", "Borno", "Adamawa"],
 "North West": ["Kano", "Kaduna", "Sokoto"],
 "South East": ["Enugu", "Anambra", "Imo"],
 "South South": ["Rivers", "Delta", "Cross River"],
 "South West": ["Lagos", "Oyo", "Ogun", "Osun"],
}
PARTIES = ["A", "B", "C", "D", "E"]

def w(name, rows, fields):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=fields); wr.writeheader(); wr.writerows(rows)

# 1. polling units
pus = []; n = 0
for zone, states in ZONES.items():
    for st in states:
        for lga_i in range(1, 4):
            for ward_i in range(1, 4):
                for pu_i in range(1, 6):
                    n += 1
                    urban = random.random() < 0.45
                    pus.append({
                        "pu_id": f"SIM-{n:05d}", "zone": zone, "state": st,
                        "lga": f"{st} LGA-{lga_i}", "ward": f"{st} L{lga_i}-W{ward_i}",
                        "settlement": "urban" if urban else "rural",
                        "registered_voters": random.randint(250, 1500),
                        "accessible_venue": random.random() < (0.55 if urban else 0.3),
                        "has_grid_power": random.random() < (0.8 if urban else 0.35),
                        "network_coverage": random.choices(["4G","3G","2G","none"], [0.5,0.25,0.15,0.1] if urban else [0.15,0.3,0.3,0.25])[0],
                        "distance_to_lga_hq_km": round(random.uniform(1,25) if urban else random.uniform(8,90),1),
                    })
w("polling_units_synthetic.csv", pus, list(pus[0].keys()))

# 2. results + held-out anomaly labels
res, labels = [], []
for p in pus:
    reg = p["registered_voters"]
    turnout = min(0.95, max(0.2, random.gauss(0.55, 0.12)))
    acc = int(reg * turnout); rejected = int(acc * random.uniform(0.005, 0.04)); valid = acc - rejected
    shares = [random.random() ** 1.5 for _ in PARTIES]; s = sum(shares)
    votes = [int(valid * x / s) for x in shares]; votes[0] += valid - sum(votes)
    row = {"pu_id": p["pu_id"], "registered_voters": reg, "accredited_voters": acc,
           **{f"votes_{k}": v for k, v in zip(PARTIES, votes)}, "rejected_votes": rejected}
    anomaly = "none"; r = random.random()
    if r < 0.012:
        row["accredited_voters"] = reg + random.randint(20, 300); anomaly = "accredited_exceeds_registered"
    elif r < 0.024:
        row["votes_A"] += random.randint(80, 400); anomaly = "sum_mismatch"
    elif r < 0.034 and len(str(row["votes_B"])) > 2:
        row["votes_B"] = int(str(row["votes_B"])[::-1]); anomaly = "digit_transposition"
    elif r < 0.044:
        for k in PARTIES: row[f"votes_{k}"] = 100
        anomaly = "suspicious_round_numbers"
    elif r < 0.052 and res:
        for k in PARTIES: row[f"votes_{k}"] = res[-1][f"votes_{k}"]
        anomaly = "duplicated_from_previous_unit"
    res.append(row); labels.append({"pu_id": p["pu_id"], "anomaly_type": anomaly})
w("results_synthetic.csv", res, list(res[0].keys()))
w("anomaly_labels_HELD_OUT.csv", labels, ["pu_id", "anomaly_type"])

# 3. multilingual FAQ
faq = [
 ("registration","How do I check if I am registered to vote?","How I fit check say I don register to vote?"),
 ("registration","What documents do I need to register?","Wetin I go carry to register?"),
 ("pvc","How do I collect my Permanent Voter Card (PVC)?","How I go take my PVC?"),
 ("pvc","What if my PVC is lost or damaged?","Wetin I go do if my PVC loss or spoil?"),
 ("voting_day","Can I vote without a PVC?","I fit vote if I no get PVC?"),
 ("voting_day","What time do polling units open and close?","Wetin be the time wey polling unit dey open and close?"),
 ("voting_day","How do I find my polling unit?","How I go find my polling unit?"),
 ("voting_day","Can I take a photo of my ballot?","I fit take photo of my ballot paper?"),
 ("accessibility","What support exists for voters with disabilities?","Wetin dey for people wey get disability to vote?"),
 ("accessibility","Can someone assist me to vote if I cannot see or read?","Person fit help me vote if I no fit see or read?"),
 ("results","How are results announced?","How dem dey announce results?"),
 ("results","Who can declare the official election result?","Who fit declare the official result?"),
 ("security","How do I report vote buying or intimidation?","How I go report say dem dey buy vote or dey threaten people?"),
 ("security","Is my vote secret?","Na secret my vote be?"),
 ("misinformation","How can I tell if a viral election message is fake?","How I fit know say viral election message na fake?"),
 ("misinformation","Where can I find official election information?","Where I fit see correct election information?"),
 ("observers","Who is allowed to observe an election?","Who fit observe election?"),
 ("voting_day","What happens if I am in the queue when polls close?","Wetin go happen if I dey queue when polling close?"),
 ("registration","Can I transfer my registration to a new location?","I fit move my registration go new place?"),
 ("voting_day","Can I vote if I am outside my state?","I fit vote if I no dey my state?"),
]
rows = [{"faq_id": f"FAQ-{i+1:03d}", "topic": t, "en": e, "pcm_draft": p, "ha": "", "yo": "", "ig": "",
         "translation_status": "ha/yo/ig NEEDED (community contribution); pcm DRAFT needs native-speaker review",
         "answer_en": "PLACEHOLDER: replace with text from an official public source and cite it."}
        for i,(t,e,p) in enumerate(faq)]
w("voter_info_faq_multilingual.csv", rows, list(rows[0].keys()))

# 4. claims
subjects = ["the polling unit in {x}", "the voter register in {x}", "ballot papers in {x}", "results collation in {x}", "the new voting app"]
templates = {
 "false": ["BREAKING: {s} has been cancelled, stay at home.", "Voting has been moved to next week in {x}, share to warn others.", "Anyone who posts a photo of their ballot gets a cash reward."],
 "misleading": ["Turnout was low in {x}, this proves the whole process is rigged.", "One delayed delivery in {x} means the entire election is compromised."],
 "true": ["Materials for {x} arrived two hours late according to the observer group.", "Polling unit in {x} opened on schedule, per the observer checklist."],
 "unverifiable": ["My cousin says {s} has a problem, nobody knows what.", "I heard something is wrong with {s}."],
}
claims = []
for i in range(300):
    label = random.choices(list(templates), [0.3,0.25,0.25,0.2])[0]
    x = random.choice(pus)["lga"]; s = random.choice(subjects).format(x=x)
    claims.append({"claim_id": f"CLM-{i+1:04d}", "text": random.choice(templates[label]).format(s=s, x=x),
      "label": label, "language": random.choices(["en","pcm"],[0.6,0.4])[0],
      "channel": random.choice(["whatsapp","x_post","facebook","tiktok_caption","sms"]),
      "synthetic_media_attached": random.random() < 0.15, "spread_score": random.randint(1,100),
      "note": "Fully synthetic; not a real claim."})
with open(os.path.join(OUT,"misinformation_claims_synthetic.jsonl"),"w",encoding="utf-8") as f:
    for c in claims: f.write(json.dumps(c, ensure_ascii=False)+"\n")

# 5. incidents
cats = {"logistics_delay":"Materials arrived late at {x}.", "accessibility_barrier":"Polling unit in {x} has steps and no ramp for wheelchair users.",
        "queue_management":"Very long queue and no shade at {x}.", "equipment_failure":"Card reader not working at {x}.",
        "intimidation":"Voters report being intimidated near {x}.", "information_gap":"Voters at {x} did not know which unit to go to.",
        "positive_practice":"Officials at {x} assisted elderly voters promptly."}
sev = {"logistics_delay":2,"accessibility_barrier":3,"queue_management":1,"equipment_failure":3,"intimidation":4,"information_gap":2,"positive_practice":0}
base = datetime(2030,1,15,6,0); inc = []
for i in range(400):
    c = random.choice(list(cats)); p = random.choice(pus)
    inc.append({"incident_id": f"INC-{i+1:04d}", "timestamp": (base+timedelta(minutes=random.randint(0,780))).isoformat(),
        "state": p["state"], "lga": p["lga"], "pu_id": p["pu_id"], "category": c,
        "description": cats[c].format(x=p["ward"]), "severity_0_4": max(0,min(4,sev[c]+random.choice([-1,0,0,1]))),
        "reporter_type": random.choice(["observer","citizen","simulated_agent"]), "verified": random.random()<0.6,
        "has_photo_evidence": random.random()<0.3})
w("incident_reports_synthetic.csv", inc, list(inc[0].keys()))

# 6. logistics
lg = []
for p in random.sample(pus, 300):
    d = p["distance_to_lga_hq_km"]; speed = random.uniform(15,45)
    hours = d/speed + random.expovariate(1/0.8) + (1.5 if p["settlement"]=="rural" else 0)
    lg.append({"pu_id": p["pu_id"], "lga": p["lga"], "distance_km": d, "settlement": p["settlement"],
      "vehicle": random.choice(["bus","truck","motorcycle","boat"]), "dispatch_hour": random.randint(4,9),
      "transit_hours": round(hours,2), "materials_complete": random.random()<0.9})
w("logistics_deliveries_synthetic.csv", lg, list(lg[0].keys()))

# 7. accessibility survey
barriers = ["physical_access","no_braille_or_large_print","language","distance","no_id_documents","information_gap","safety_concerns","none"]
sv = []
for i in range(500):
    p = random.choice(pus)
    sv.append({"resp_id": f"SRV-{i+1:04d}", "state": p["state"], "settlement": p["settlement"],
      "age_band": random.choice(["18-24","25-34","35-49","50-64","65+"]), "gender": random.choice(["female","male","undisclosed"]),
      "disability_type": random.choices(["none","mobility","visual","hearing","cognitive","multiple"],[0.6,0.12,0.1,0.08,0.05,0.05])[0],
      "preferred_language": random.choices(["en","ha","yo","ig","pcm","other"],[0.25,0.2,0.2,0.15,0.15,0.05])[0],
      "main_barrier": random.choice(barriers), "voted_last_cycle_simulated": random.random()<0.55,
      "confidence_finding_info_1_5": random.randint(1,5)})
w("accessibility_barriers_survey_synthetic.csv", sv, list(sv[0].keys()))
print("Generated:", sorted(os.listdir(OUT)))
