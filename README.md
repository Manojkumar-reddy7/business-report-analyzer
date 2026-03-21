# AI-Powered Business Report Analyzer

A GenAI-powered web application that analyzes business reports and annual reports using Large Language Models. Upload any PDF report and instantly extract financial insights, business risks, strategic priorities, and operational metrics.

## Live Demo
[https://business-report-analyzer.streamlit.app](https://business-report-analyzer.streamlit.app)

## Features
- Upload any business or annual report in PDF format
- Auto-generates 4 key insights instantly:
  - Financial Highlights
  - Key Business Risks
  - Strategic Priorities
  - Operational Metrics
- Ask custom questions about the report
- Powered by LLM via OpenRouter API
- Deployed live — accessible from any device

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **AI/LLM:** OpenRouter API (LLaMA / DeepSeek models)
- **PDF Processing:** PyPDF2
- **Text Chunking:** LangChain Text Splitters
- **Deployment:** Streamlit Cloud

## Project Structure
```
business-report-analyzer/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .env               # API keys (not pushed to GitHub)
└── .gitignore         # Git ignore rules
```

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Manojkumar-reddy7/business-report-analyzer.git
cd business-report-analyzer
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up API key
Create a `.env` file in the root directory:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Get your free API key from [https://openrouter.ai](https://openrouter.ai)

### 5. Run the app
```bash
streamlit run app.py
```

## Deployment
This app is deployed on **Streamlit Cloud**.

To deploy your own version:
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Add `OPENROUTER_API_KEY` in Secrets settings
5. Deploy

## Use Cases
- Analyze company annual reports instantly
- Extract financial metrics without reading 100+ pages
- Compare business risks across companies
- Resume screening and candidate analysis
- Research and competitive intelligence

## Example Questions to Ask
- "What are the key financial highlights?"
- "What are the major business risks?"
- "What is the company's growth strategy?"
- "How many employees does the company have?"
- "What are the operational performance metrics?"

## Future Improvements
- [ ] Multi-document comparison
- [ ] Export insights as PDF report
- [ ] Historical trend analysis
- [ ] Integration with financial data APIs

##  Author
**Reddypalli Manojkumar Reddy**
- GitHub: [@Manojkumar-reddy7](https://github.com/Manojkumar-reddy7)
- LinkedIn: [manojkumar-reddy7](https://linkedin.com/in/manojkumar-reddy7)
- Email: manojkumar1889238@gmail.com

## License
MIT License