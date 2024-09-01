from data2 import dt2 as dt
from data import dt as dt2
import pandas as pd
import streamlit as st





# labling and branding of page
st.set_page_config(
    page_title=f"SIH Problem-Statement",
    page_icon="🪴",
    layout="wide",
)

st.write("Developed by [Jitendra-Kumar](https://www.jitendra.me)")

st.title("SIH Problem-Statement")

st.write("This Web app is designed to analyse the problem statement of SIH in a fast and efficient way.😇😍")






# switch year filter
selected_year = st.selectbox("Select Year", ["2024", "2023"])

if selected_year == "2023":
    dt = dt2
else:
    dt = dt





# create dataframe
df = pd.DataFrame(dt[1:], columns=dt[0])
df["Problem Statement Title"] = df["Problem Statement Title"].str.replace("\n\n", "")
df["Problem Statement Title"] = df["Problem Statement Title"].str.replace("\n", "◾")


colnm = ['S.No.', 'Organization', 'Problem Statement Title', 'Category', 'PS Number', 'Submitted Idea(s) Count', 'Theme']

sr = {
    0: df["S.No."],
    1: df["Organization"],
    2: df["Problem Statement Title"],
    3: df["Category"],
    4: df["PS Number"],
    5: df["Submitted Idea(s) Count"],
    6: df["Theme"]
}

# List of categories
categories = list(df[colnm[3]].unique())

# List of organizations
organizations = list(df[colnm[1]].unique())

# List of domains
domains = list(df[colnm[6]].unique())





# filter by rows
row_filter = st.checkbox("activate filter by row", help="by selecting this you can apply filter on rows")
row_filtered_data = df
if row_filter:
    multi = st.checkbox("activate multi select", value=False, help="by selecting this you can apply multiple filter on same row. like show me all the rows which have column vlaue xyz and abc")
    if multi:
        category = st.multiselect("Select Category", ["ALL"]+categories, ["ALL"])
        organization = st.multiselect("Select Organization", ["ALL"]+organizations, ["ALL"])
        domain = st.multiselect("Select Domain", ["ALL"]+domains, ["ALL"])
        if "ALL" not in category:
            row_filtered_data = row_filtered_data[row_filtered_data[colnm[3]].isin(category)]
        if "ALL" not in organization:
            row_filtered_data = row_filtered_data[row_filtered_data[colnm[1]].isin(organization)]
        if "ALL" not in domain:
            row_filtered_data = row_filtered_data[row_filtered_data[colnm[6]].isin(domain)]
    else:
        category = st.selectbox("Select Category", ["ALL"]+categories)
        organization = st.selectbox("Select Organization", ["ALL"]+organizations)
        domain = st.selectbox("Select Domain", ["ALL"]+domains)
        if category  != "ALL":
            row_filtered_data = row_filtered_data[row_filtered_data[colnm[3]] == category]
        if organization != "ALL":
            row_filtered_data = row_filtered_data[row_filtered_data[colnm[1]] == organization]
        if domain != "ALL":
            row_filtered_data = row_filtered_data[row_filtered_data[colnm[6]] == domain]







st.divider()
# filter by column option
options = st.multiselect(
    "select to columns to show",
    colnm,
    [
        'S.No.', 
        'Category',   
        'PS Number' , 
        'Theme',
        'Organization',   
        'Problem Statement Title'
    ],
)
filtered_df = row_filtered_data[options]






st.write("Total Problem Statement: ", len(filtered_df))
st.dataframe(filtered_df)

