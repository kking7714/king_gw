import pandas as pd 
from matplotlib import pyplot as plt 

# Define file paths to data
file = ('data/belly_button_biodiversity_otu_id.csv')
file1 = ('data/Belly_Button_Biodiversity_Metadata.csv')
file2 = ('data/belly_button_biodiversity_samples.csv')
file3 = ('data/metadata_columns.csv')

# Read files as dataframes
otu = pd.read_csv(file)
metadata = pd.read_csv(file1)
samples = pd.read_csv(file2)
metadataColumns = pd.read_csv(file3)

def fetch_data():
    # Pull list of sample names
    bb_ids = list(samples)[1:]

    # Pull list of descriptions
    otu_desc = list(otu['lowest_taxonomic_unit_found'])

    # Create dictionary for relevant metadata samples
    metadata_dict = {
    "AGE": metadata['AGE'].tolist(),
    "BBTYPE": metadata["BBTYPE"].tolist(),
    "ETHNICITY": metadata["ETHNICITY"].tolist(),
    "GENDER": metadata["GENDER"].tolist(),
    "LOCATION": metadata["LOCATION"].tolist(),
    "SAMPLEID": metadata["SAMPLEID"].tolist()}
    metadata_ = pd.DataFrame(metadata_dict)


    # Create dictionary for washing frequency
    wash_freq_dict = {
    "SAMPLEID": metadata["SAMPLEID"],
    "WFREQ": metadata["WFREQ"]}
    # Add 'BB_' to the beginning of each sampleid
    wash_freq_dict['SAMPLEID'] = 'BB_' + wash_freq_dict['SAMPLEID'].astype(str)
    wash_freq = pd.DataFrame(wash_freq_dict)

    # Create dataframe with otu_id and sample_values 
    

    return bb_ids, otu_desc, metadata_, wash_freq, samples

if __name__ == "__main__":
    bb_ids, otu_desc, metadata_, wash_freq, samples = fetch_data()
    print(bb_ids, otu_desc, meatadata_, wash_freq, samples)




