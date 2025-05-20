import os

try:
  from dotenv import load_dotenv
  load_dotenv()

  MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.0-flash")
except ImportError:
  print("Warning: python-dotenv not installed. Ensure API key is set")
  MODEL_NAME = "gemini-2.0-flash"

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

from learning_agent.instructions import (
  VERSE_INPUT_INSTRUCTION,
  TAFSIR_CONTEXT_INSTRUCTION,
  ARABIC_LINGUISTICS_INSTRUCTION,
  REFLECTION_INSTRUCTION,
  NOTES_INSTRUCTION,
  STUDY_FORMATTER_INSTRUCTION,
  QURAN_ORCHESTRATOR_INSTRUCTION
)

# --- Sub Agent 1: VerseFinder ---
verse_find_agent = LlmAgent(
  name="VerseFinder",
  model=MODEL_NAME,
  instruction=VERSE_INPUT_INSTRUCTION,
  tools=[google_search],
  output_key="verse_input"
)

# --- Sub Agent 2: TafsirContext ---
tafsir_context_agent = LlmAgent(
  name="TafsirContext",
  model=MODEL_NAME,  # Using environment variable
  instruction=TAFSIR_CONTEXT_INSTRUCTION,
  output_key="tafsir_context" # Save result to state
)

# --- Sub Agent 3: ArabicLinguistics ---
arabic_linguistics_agent = LlmAgent(
  name="LinguisticBreakdown",
  model=MODEL_NAME,  # Using environment variable
  instruction=ARABIC_LINGUISTICS_INSTRUCTION,
  output_key="linguistic_breakdown" # Save result to state
)

# --- Sub Agent 4: Reflection ---
reflection_agent = LlmAgent(
  name="ReflectionQuestions",
  model=MODEL_NAME,  # Using environment variable
  instruction=REFLECTION_INSTRUCTION,
  output_key="reflection_questions" # Save result to state
)

# --- Sub Agent 5: Notes ---
notes_agent = LlmAgent(
  name="Notes",
  model=MODEL_NAME,  # Using environment variable
  instruction=NOTES_INSTRUCTION,
  output_key="notes" # Save result to state
)

# --- Sub Agent 6: StudyFormatter ---
study_formatter_agent = LlmAgent(
  name="StudyFormatter",
  model=MODEL_NAME,  # Using environment variable
  instruction=STUDY_FORMATTER_INSTRUCTION,
  output_key="formatted_report" # Save result to state
)

# --- Main Agent: SequentialAgent ---
campaign_orchestrator_agent = SequentialAgent(
  name="CampaignOrchestrator",
  description=QURAN_ORCHESTRATOR_INSTRUCTION,
  sub_agents=[
    verse_find_agent,
    tafsir_context_agent,
    arabic_linguistics_agent,
    reflection_agent,
    notes_agent,
    study_formatter_agent
  ]
)

root_agent = campaign_orchestrator_agent