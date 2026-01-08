import streamlit as st

st.title(":material/vpn_key: Day 1: Connect to Snowflake")

# Connect to Snowflake
try:
    #Works in Streamlit in Snowflake
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
except:
    #Works locally and on Streamlit Community Cloud
    from snowflake.snowpark import Session
    session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()
    
version = session.sql("SELECT CURRENT_VERSION()").collect()[0][0]

st.success(f"Connected to Snowflake version {version} :tada:")