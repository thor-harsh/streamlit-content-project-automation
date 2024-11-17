import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

def generate_summary(content, model_name="gemini-1.5-flash"):
    try:
        prompt = (
            f"Summarize the following content in 2-3 sentences, providing the key details:\n\n{content}"
        )

        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)

        summary = response.text.strip()

        if len(summary.split()) < 5:
            summary += " (Content too brief to summarize effectively.)"

        return summary
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Summary generation failed due to an error."


def summarize_dataframe(df):
    if len(df) > 0:
        summaries = []

        for index, row in df.iterrows():
            content = row.get("Description", "")

            content = clean_description(content)
            summary = generate_summary(content)
            summaries.append(summary)

        df["Summary"] = summaries
        return df
    else:
        return df


def clean_description(content):
    from bs4 import BeautifulSoup
    import re

    content = BeautifulSoup(content, "html.parser").get_text()
    content = re.sub(r"\s+", " ", content).strip()

    return content
