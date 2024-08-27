from data import dt
import pandas as pd
import streamlit as st

df = pd.DataFrame(dt[1:], columns=dt[0])

colnm = ['S.No.', 'Organization', 'Problem Statement Title', 'Category', 'PS Number', 'Submitted Idea(s) Count', 'Domain Bucket']

sr = {
    0: df["S.No."],
    1: df["Organization"],
    2: df["Problem Statement Title"],
    3: df["Category"],
    4: df["PS Number"],
    5: df["Submitted Idea(s) Count"],
    6: df["Domain Bucket"]
}

# List of categories
categories = list(df[colnm[3]].unique())

# List of organizations
organizations = list(df[colnm[1]].unique())

# List of domains
domains = list(df[colnm[6]].unique())






st.set_page_config(
    page_title="SIH 2023 Problem-Statement",
    page_icon="🪴",
    layout="wide",
)
st.write("Developed by [Jitendra-Kumar](https://www.jitendra.me)")

st.title("SIH 2023 Problem-Statement")

st.write("This Web app is designed to analyse the problem statement of SIH 2023 in a fast and efficient way.")






# filter by rows
row_filter = st.checkbox("activate filter by row")
row_filtered_data = df
if row_filter:
    multi = st.checkbox("activate multi select", value=False)
    if multi:
        category = st.multiselect("Select Category", categories, [])
        organization = st.multiselect("Select Organization", organizations, [])
        domain = st.multiselect("Select Domain", domains, [])
        row_filtered_data = df[
            (df[colnm[3]].isin(category)) & 
            (df[colnm[1]].isin(organization)) & 
            (df[colnm[6]].isin(domain))
        ]
    else:
        category = st.selectbox("Select Category", categories)
        organization = st.selectbox("Select Organization", organizations)
        domain = st.selectbox("Select Domain", domains)
        row_filtered_data = df[
            (df[colnm[3]] == category) & 
            (df[colnm[1]] == organization) & 
            (df[colnm[6]] == domain)
        ]







st.divider()
# filter by column option
options = st.multiselect(
    "select to columns to show",
    ['S.No.', 'Organization', 'Problem Statement Title', 'Category', 'PS Number', 'Submitted Idea(s) Count', 'Domain Bucket'],
    [
        'S.No.', 
        'Category',   
        'PS Number' , 
        'Domain Bucket',
        'Submitted Idea(s) Count',
        'Organization',   
        'Problem Statement Title'
    ],
)
filtered_df = row_filtered_data[options]







st.dataframe(filtered_df)

