# 📖 Quran Study Companion — Agent System using Google ADK

A structured Quranic study tool powered by Google’s Agent Development Kit (ADK). This system guides users through verse selection, tafsir, linguistic analysis, reflection, and note-taking — all managed through a cooperative team of specialized agents.

---

## ✨ Features

- 🔍 **Verse Selector Agent**  
  Helps users choose Quranic verse(s) to study.

- 📖 **Tafsir & Context Agent**  
  Provides historical context and classical tafsir.

- 🧠 **Linguistic Analysis Agent**  
  Breaks down Arabic grammar, morphology, and root meanings.

- 💭 **Reflection Questions Agent**  
  Encourages deep thinking with guided reflection prompts.

- 📝 **Personal Notes Agent**  
  Lets users jot down their insights and reflections.

- 📚 **Study Report Generator Agent**  
  Compiles all outputs into a formatted, readable report.

---

## 🧠 Agent System Overview

| Agent Name              | Purpose                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| `VerseFinder`           | Guides the user in selecting verse(s)                                   |
| `TafsirContextAgent`    | Supplies tafsir and historical background                               |
| `LinguisticAgent`       | Provides Arabic linguistic breakdowns                                   |
| `ReflectionAgent`       | Asks thoughtful reflection questions                                    |
| `NoteTakingAgent`       | Captures personal notes from the user                                   |
| `StudyFormatterAgent`   | Formats and combines all agent responses into a cohesive study guide    |

---

## 📁 Folder Structure

```

quran-with-google-adk/
├── learning_agent/
│   ├── __init__.py
│   ├── .env                  # API keys and environment configs
│   ├── instructions.py       # Prompt templates for each agent
│   └── agent.py              # Agent implementations
├── requirements.txt          # Packages need to be install
└── README.md                 # You're reading it

````

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/seAfnan/quran-with-google-adk.git
cd quran-with-google-adk
````

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API keys to `.env`

Create a `.env` file in the root directory with the following contents:

```env
GOOGLE_API_KEY=your-google-api-key
GOOGLE_GENAI_MODEL=gemini-1.5-pro  # or gemini-1.5-flash
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

---

## 🚀 Running the App

To start the agent orchestration:

```bash
adk web
```

You’ll be prompted to:

1. Select a verse or range of verses.
2. Receive tafsir and linguistic insights.
3. Reflect through guided prompts.
4. Take personal notes.
5. Receive a formatted study summary.

---

## 📋 Sample Output

```
📖 Surah Al-Kahf: Ayah 10

🧕 Tafsir & Context:
This verse was revealed when...

🧬 Linguistic Breakdown:
- Word: "فتية" (young men) — Root: ف ت و
- Grammar: Plural masculine, nominative...

💡 Reflection Questions:
- What are the sacrifices I make for faith?
- What would it mean to "seek mercy" in my daily life?

📝 My Notes:
I sometimes feel unsure about my beliefs, but this verse...

📄 Study Summary Ready!
```

---

Furthermore, you can also visit [ADK Official Docs](https://google.github.io/adk-docs/get-started/quickstart/)

---

## 🧰 Built With

* [Google ADK](https://github.com/google/adk-python)
* [Python 3.10+](https://www.python.org/)
* [Gemini API (Generative AI)](https://ai.google.dev/)
* dotenv (for managing API keys)

---

## 🪪 License

MIT License © 2025
