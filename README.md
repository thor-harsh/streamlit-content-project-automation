# Project--Automated Content Platform

<table>

**This repository contains an automated content platform built using Python and Streamlit. The application allows users to scrape articles, summarize key insights, and share content via Telegram effortlessly.** <br></br>

**Before jumping to the code, let’s understand the tools and features of this project, as well as its various components.** <br></br>

---

**What is this project about?** <br></br>

This project is a Streamlit-based web application designed to streamline content creation workflows. Users can scrape data, generate summaries using AI, and distribute them through Telegram bots. It's especially useful for professionals managing large-scale content.

---

**Features:** <br>

1. **Scrape Articles**: Collect content from various sources. <br>
2. **Generate Summaries**: Automatically summarize scraped content using AI models. <br>
3. **Upload CSV**: Add custom data files for analysis or summary generation. <br>
4. **Telegram Integration**: Share generated summaries directly via a Telegram bot. <br>
5. **Workflow Automation**: Ensures that each step is sequential and organized. <br></br>

---

**Modules in the Project:** <br>

1. **Scraper** (`scraper.py`): <br>
   Handles web scraping tasks to extract data from online sources. <br></br>

2. **Summarizer** (`summarizer.py`): <br>
   Leverages AI (e.g., OpenAI APIs or Gemini) to create concise summaries of the extracted data. <br></br>

3. **Telegram Bot** (`telegram_bot.py`): <br>
   Integrates a Telegram bot for automated sharing of content summaries. <br></br>

4. **Main Application** (`app.py`): <br>
   A Streamlit app that ties all the components together into a user-friendly interface. <br></br>

5. **Environment Configuration** (`.env`): <br>
   Stores sensitive information like API keys for security purposes. <br></br>

---

**How to Use the Application:** <br>

1. **Scrape Articles**: <br>
   Select the "Scrape Articles" option in the app's navigation panel and provide the URL or target source. <br></br>

2. **Upload CSV**: <br>
   If you already have a dataset, navigate to the "Upload CSV" section to upload your data for processing. <br></br>

3. **Generate Summaries**: <br>
   Once the data is uploaded, select "Generate Summaries" to create concise insights from your data. <br></br>

4. **Send to Telegram**: <br>
   After generating summaries, use the "Send to Telegram" option to share them with your target audience through a Telegram bot. <br></br>

---

**Workflow Sequence and Automation:** <br>

This application enforces a sequential workflow to ensure clarity and avoid confusion. Here’s how it works: <br>

1. **Upload Data (CSV or Scrape Articles):** Ensure that you’ve uploaded or scraped data first. <br>
2. **Generate Summaries:** Summaries can only be generated after data is uploaded. <br>
3. **Send to Telegram:** Once summaries are generated, they can be shared through Telegram. <br>
4. **Freeze Navigation:** After initiating the Telegram sharing process, the app freezes all steps to avoid interruption. Only after all messages are sent does the navigation unlock. <br></br>

---

**Environment Configuration:** <br>

To run this app securely, ensure you add the required environment variables to a `.env` file or Streamlit secrets. For example: <br>

```plaintext
TELEGRAM_API_KEY=your_telegram_api_key
OPENAI_API_KEY=your_openai_api_key
```

**So what are you waiting for...? Jump to the code to get started. As usual for any doubt or query see you in pull request section 😁😂. Thanks**
