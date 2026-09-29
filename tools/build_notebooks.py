import os, json
def _cell(t, src): 
    c={"cell_type":t,"metadata":{},"source":src.splitlines(True)}
    if t=="code": c.update({"execution_count":None,"outputs":[]})
    return c
def md(s): return _cell("markdown", s)
def code(s): return _cell("code", s)
def new_notebook(cells): return {"cells":cells,"metadata":{},"nbformat":4,"nbformat_minor":5}
class nbf:
    @staticmethod
    def write(nb, path): json.dump(nb, open(path,"w",encoding="utf-8"), indent=1)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "notebooks")

SETUP = """import sys; sys.path.append('../src')
import pandas as pd, numpy as np
from ai4elections import load_csv, load_jsonl
pd.set_option('display.max_columns', 30)"""

def save(name, cells):
    nb = new_notebook(cells=cells); nb["metadata"]["kernelspec"] = {"name":"python3","display_name":"Python 3","language":"python"}
    nbf.write(nb, os.path.join(OUT, name))

save("01_track1_claim_classifier.ipynb", [
 md("# Track 1 starter: Claim classification baseline\nTF-IDF + logistic regression on synthetic claims. **Goal:** show the workflow (split, baseline, error analysis). Real solutions need real, ethically sourced data, multilingual coverage and human fact-checkers in the loop.\n\n> Synthetic templates are easy to memorise, so high scores here are NOT evidence of real-world performance."),
 code(SETUP),
 code("claims = load_jsonl('misinformation_claims_synthetic.jsonl')\nclaims['label'].value_counts()"),
 code("from sklearn.model_selection import train_test_split\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.metrics import classification_report\n\n# Split by language-stratified sample; consider group splits to avoid template leakage.\nX_tr, X_te, y_tr, y_te = train_test_split(claims['text'], claims['label'], test_size=0.25, stratify=claims['label'], random_state=0)\nclf = make_pipeline(TfidfVectorizer(ngram_range=(1,2), min_df=2), LogisticRegression(max_iter=1000))\nclf.fit(X_tr, y_tr)\nprint(classification_report(y_te, clf.predict(X_te)))"),
 md("## Your turn\n1. Break the model: write 10 claims in different phrasing and see what fails.\n2. Evaluate per language (`en` vs `pcm`).\n3. Add an **abstain** option: return 'needs human review' when confidence < threshold.\n4. Document limits in `docs/05_templates/MODEL_CARD.md`.\n\n**Important design rule:** flag content for human fact-checkers. Do not auto-censor or auto-label real citizens' speech as false."),
 code("# Example: confidence-based abstention\nproba = clf.predict_proba(X_te); conf = proba.max(axis=1)\nthreshold = 0.6\nabstained = (conf < threshold).mean()\nprint(f'Abstains on {abstained:.0%} of items at threshold {threshold}')"),
])

save("02_track2_results_anomaly_detection.ipynb", [
 md("# Track 2 starter: Data-quality flags on synthetic results\nRule-based checks + an unsupervised model. Outputs are **flags for human review**, never declarations of fraud or results."),
 code(SETUP + "\nfrom ai4elections.checks import integrity_flags"),
 code("res = load_csv('results_synthetic.csv')\nflagged = integrity_flags(res)\nflag_cols = [c for c in flagged.columns if c.startswith('flag_')]\nflagged[flag_cols].sum()"),
 code("# Evaluate against held-out labels (available only for practice; real data has no answer key)\nlab = load_csv('anomaly_labels_HELD_OUT.csv')\nm = flagged.merge(lab, on='pu_id')\nm['any_flag'] = m[flag_cols].any(axis=1)\nm['is_anom'] = m['anomaly_type'] != 'none'\nprint(pd.crosstab(m['is_anom'], m['any_flag']))\nprint(m[m.is_anom].groupby('anomaly_type')['any_flag'].mean())"),
 code("# Unsupervised: Isolation Forest on turnout & vote shares\nfrom sklearn.ensemble import IsolationForest\nP = ['votes_A','votes_B','votes_C','votes_D','votes_E']\nX = pd.DataFrame({'turnout': res.accredited_voters/res.registered_voters})\nvalid = res[P].sum(axis=1).replace(0,np.nan)\nfor p in P: X['share_'+p[-1]] = res[p]/valid\nX = X.fillna(0)\niso = IsolationForest(contamination=0.05, random_state=0).fit(X)\nm['iso_flag'] = iso.predict(X) == -1\nprint(pd.crosstab(m['is_anom'], m['iso_flag']))"),
 md("## Your turn\n- Which anomaly types do rules catch vs the model? Combine them.\n- Report precision/recall AND the cost of false alarms on reviewers' time.\n- Never train or test on live or unauthorised data. See `docs/01_technical_briefs/track2_electoral_data_intelligence.md`."),
])

save("03_track3_multilingual_faq_retrieval.ipynb", [
 md("# Track 3 starter: Multilingual FAQ retrieval\nA tiny retrieval baseline over the FAQ file (English + draft Nigerian Pidgin). Hausa, Yoruba and Igbo columns are intentionally empty: **finding and validating good translations with native speakers is part of the challenge.**"),
 code(SETUP),
 code("faq = load_csv('voter_info_faq_multilingual.csv')\nfaq[['faq_id','topic','en','pcm_draft']].head()"),
 code("from sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.metrics.pairwise import cosine_similarity\n\ncorpus = pd.concat([faq['en'], faq['pcm_draft']], ignore_index=True)\nids = list(faq['faq_id'])*2\nvec = TfidfVectorizer(analyzer='char_wb', ngram_range=(2,4)).fit(corpus)\nM = vec.transform(corpus)\n\ndef ask(q, k=3):\n    sims = cosine_similarity(vec.transform([q]), M).ravel()\n    top = sims.argsort()[::-1][:k]\n    return [(ids[i], corpus[i], round(float(sims[i]),2)) for i in top]\n\nask('I no get PVC, I fit vote?')"),
 md("## Your turn\n1. Replace TF-IDF with multilingual embeddings and compare.\n2. Never let the system invent answers: return **only** approved, cited text, or hand over to a human/official source.\n3. Test with low-literacy phrasing, code-switching, typos and voice-to-text noise.\n4. Add accessibility: screen-reader friendly output, SMS/USSD-length answers."),
])

save("04_track5_incident_triage_and_logistics.ipynb", [
 md("# Track 5 starter: Incident triage and logistics analysis (synthetic)\nSummaries to support **observers and civic organisations**. Protect reporters: no real names, minimal location detail, no public exposure of unverified accusations."),
 code(SETUP),
 code("inc = load_csv('incident_reports_synthetic.csv')\ninc.groupby('category')['severity_0_4'].agg(['count','mean']).round(2).sort_values('mean', ascending=False)"),
 code("# Baseline text classifier for incident category\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.pipeline import make_pipeline\nfrom sklearn.model_selection import cross_val_score\ncl = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=500))\nprint(cross_val_score(cl, inc['description'], inc['category'], cv=5).mean().round(3))"),
 code("# Logistics: what drives late delivery?\nlg = load_csv('logistics_deliveries_synthetic.csv')\nprint(lg.groupby('settlement')['transit_hours'].describe().round(2))\nfrom sklearn.ensemble import GradientBoostingRegressor\nX = pd.get_dummies(lg[['distance_km','settlement','vehicle','dispatch_hour']], drop_first=True)\nmodel = GradientBoostingRegressor(random_state=0).fit(X, lg['transit_hours'])\npd.Series(model.feature_importances_, X.columns).sort_values(ascending=False).round(3)"),
 md("## Your turn\n- Build a severity-ranked triage queue with a human review step.\n- Join incidents to `polling_units_synthetic.csv` to find accessibility gaps by state.\n- Add data-minimisation and consent-by-design to your reporting flow."),
])

save("05_track4_security_privacy_basics.ipynb", [
 md("# Track 4 starter: Privacy-preserving analytics & defensive monitoring (offline)\nAll exercises are **local and on synthetic data**. Do not scan, probe or test any live or third-party system."),
 code(SETUP),
 code("sv = load_csv('accessibility_barriers_survey_synthetic.csv')\n# k-anonymity check on quasi-identifiers\nqi = ['state','age_band','gender','disability_type']\nk = sv.groupby(qi).size()\nprint('Groups with k<3:', (k<3).sum(), 'of', len(k))"),
 code("# Suppress small cells before publishing aggregates\ndef suppress(df, cols, min_k=5):\n    g = df.groupby(cols).size().reset_index(name='n')\n    g.loc[g['n']<min_k,'n'] = np.nan\n    return g\nsuppress(sv, ['state','disability_type']).head()"),
 code("# Toy log-anomaly monitor: bursts of incident reports per hour\ninc = load_csv('incident_reports_synthetic.csv'); inc['hour'] = pd.to_datetime(inc['timestamp']).dt.floor('h')\ncounts = inc.groupby('hour').size(); z = (counts-counts.mean())/counts.std()\nz[z>2]"),
 md("## Your turn\nDesign an audit-log format, a role-based access model, and a threat model (STRIDE) for your solution. Use the templates in `docs/05_templates/`."),
])
print(sorted(os.listdir(OUT)))
