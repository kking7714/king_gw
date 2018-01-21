from bb_Data import fetch_data
import json
import pandas as pd 
from flask import Flask, jsonify, render_template
app = Flask(__name__)

bb_ids, otu_desc, metadata_, wash_freq, samples = fetch_data()

@app.route("/")
def index():
    """Return plotly dashboard."""
    return render_template("index.html")

@app.route("/names")
def sample_names():
    return jsonify(bb_ids)


@app.route("/otu")
def otu_descriptions():
    return jsonify(otu_desc)

@app.route("/metadata/<sample>")
def metadata_return(sample="BB_940"):
    search = int(sample[3:])
    m = metadata_.loc[metadata_["SAMPLEID"]== search]
    metadata = {
    "AGE": m["AGE"].tolist()[0],
    "BBTYPE": m["BBTYPE"].tolist()[0],
    "ETHNICITY": m["ETHNICITY"].tolist()[0],
    "GENDER": m["GENDER"].tolist()[0],
    "LOCATION": m["LOCATION"].tolist()[0],
    "SAMPLEID": m["SAMPLEID"].tolist()[0]}
    return jsonify(metadata)

@app.route("/wfreq/<sample>")
def washing_freq(sample="BB_940"):
    w = wash_freq.loc[wash_freq["SAMPLEID"]== sample]
    wash = {
        "SAMPLEID": w["SAMPLEID"].tolist()[0],
        "WFREQ": w["WFREQ"].tolist()[0]
    }
    return jsonify(wash)

@app.route("/samples/<sample>")
def sample_fetch(sample="BB_940"):
    filtered = samples[['otu_id', sample]]
    filtered.rename(columns={sample:'BB'},inplace=True)
    clean_filtered = filtered[filtered.BB != 0]
    clean_filtered.rename(columns={'BB':'sample_values'},inplace=True)
    clean_filtered.sort_values(by='sample_values', ascending=False, inplace=True)
    clean_filtered.dropna(inplace=True)  
    sample_output = [{"otu_ids": clean_filtered['otu_id'].tolist()},
                    {"sample_values": clean_filtered['sample_values'].tolist()}]
    return jsonify(sample_output)  



if __name__ == "__main__":
    app.run(debug=True)