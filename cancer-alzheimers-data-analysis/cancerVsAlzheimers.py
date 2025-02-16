import pandas as pd

state_map = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts',
    'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
    'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico',
    'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
    'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

def makeFipsData():
    df_fips = pd.read_csv("datasets/fips_codes.csv")
    df_fips = df_fips.dropna().reset_index()
    df_fips = df_fips.drop(columns="index")
    df_fips['state'] = df_fips['state'].map(state_map)
    df_fips["County"] = df_fips["name"] + ", " + df_fips['state']
    return df_fips

def cleanAlzData(fileName):
    df = pd.read_csv("datasets/" + fileName)
    df = df.drop(columns=["Unnamed: 0"])
    return df

def cleanCancerData(fileName):
    df = pd.read_csv("datasets/" + fileName, skiprows=8)
    df = df.dropna()
    df.index -= 1
    df = df[(df["Lower 95% Confidence Interval"] != "data not available") & (df["Average Annual Count"] != "3 or fewer")]
    #Must include when initializing dataframe:
    df = df.drop(columns=["Lower CI (CI*Rank)", "CI*Rank([rank note])", "Upper CI (CI*Rank)"])
    df["County"] = df["County"].str[:-3]
    return df