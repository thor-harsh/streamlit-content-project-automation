import streamlit as st
import pandas as pd
from scraper import scrape_articles
from summarizer import summarize_dataframe
from telegram_bot import send_summaries_in_batches


if "scraped_df" not in st.session_state:
    st.session_state["scraped_df"] = None
if "uploaded_df" not in st.session_state:
    st.session_state["uploaded_df"] = None
if "summarized_df" not in st.session_state:
    st.session_state["summarized_df"] = None
if "telegram_sent" not in st.session_state:
    st.session_state["telegram_sent"] = False
if "step_completed" not in st.session_state:
    st.session_state["step_completed"] = {"scraping": False, "upload": False, "summarizing": False}

st.set_page_config(page_title="Content Automation", page_icon="📜", layout="wide")

st.title("📜 Automated Content Platform- By Harsh Prakash")

steps = ["🔍 Scrape Articles", "📤 Upload CSV", "📝 Generate Summaries", "📲 Send to Telegram"]
current_step = st.sidebar.radio("Choose a step:", steps)

def enforce_workflow(step):
    messages = {
        "upload": "⚠️ Please scrape articles first.",
        "summarizing": "⚠️ Please upload a CSV file first.",
        "sending": "⚠️ Please generate summaries first.",
    }
    if step == "upload" and not st.session_state["step_completed"]["scraping"]:
        st.error(messages["upload"])
        st.stop()
    elif step == "summarizing" and not st.session_state["step_completed"]["upload"]:
        st.error(messages["summarizing"])
        st.stop()
    elif step == "sending" and not st.session_state["step_completed"]["summarizing"]:
        st.error(messages["sending"])
        st.stop()

if st.session_state["telegram_sent"]:
    st.sidebar.warning("✅ Summaries sent to Telegram. All actions are now frozen.")
    st.stop()


if current_step == "🔍 Scrape Articles":
    st.header("🔍 Scrape Articles")
    if st.button("🚀 Start Scraping"):
        with st.spinner("Scraping articles..."):
            scraped_data = scrape_articles(max_articles=30)
            st.session_state["scraped_df"] = scraped_data
            st.session_state["step_completed"]["scraping"] = True
            st.success("✅ Scraping completed!")
    if st.session_state["scraped_df"] is not None:
        st.write("### Scraped Data")
        st.dataframe(st.session_state["scraped_df"])

elif current_step == "📤 Upload CSV":
    enforce_workflow("upload")
    st.header("📤 Upload CSV")
    uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])
    if uploaded_file:
        uploaded_df = pd.read_csv(uploaded_file)
        required_columns = ["Link", "Category Name", "Description"]
        if all(col in uploaded_df.columns for col in required_columns):
            st.session_state["uploaded_df"] = uploaded_df
            st.session_state["step_completed"]["upload"] = True
            st.success("✅ CSV uploaded successfully!")
        else:
            st.error("❌ Invalid CSV format. Please include 'Link', 'Category Name', and 'Description' columns.")
    if st.session_state["uploaded_df"] is not None:
        st.write("### Uploaded Data")
        st.dataframe(st.session_state["uploaded_df"])


elif current_step == "📝 Generate Summaries":
    enforce_workflow("summarizing")
    st.header("📝 Generate Summaries")
    if st.button("Generate Summaries"):
        with st.spinner("Generating summaries..."):
            summarized_data = summarize_dataframe(st.session_state["uploaded_df"])
            st.session_state["summarized_df"] = summarized_data
            st.session_state["step_completed"]["summarizing"] = True
            st.success("✅ Summaries generated successfully!")
    if st.session_state["summarized_df"] is not None:
        st.write("### Summaries")
        st.dataframe(st.session_state["summarized_df"])

elif current_step == "📲 Send to Telegram":
    enforce_workflow("sending")
    st.header("📲 Send Summaries to Telegram")
    if st.button("Send Summaries"):
        st.session_state["telegram_sent"] = True
        with st.spinner("Sending summaries to Telegram..."):
            send_summaries_in_batches(st.session_state["summarized_df"])
        st.success("🎉 All summaries have been sent to Telegram!")
        st.balloons()
        st.write("### Sent Summaries")
        st.dataframe(st.session_state["summarized_df"])
