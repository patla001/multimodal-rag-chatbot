def generate_prompt(symptoms: str) -> str:
    return f"""
You are a medical assistant helping to analyze visible skin symptoms.

The user has uploaded an image showing a skin condition, along with the following symptoms:

Symptom description:
\"\"\"
{symptoms}
\"\"\"

Please analyze the image in conjunction with the symptoms and return the following:

1. **Possible Diagnoses** (Ranked by likelihood)
2. **Severity Level** (Mild, Moderate, Severe)
3. **Suggested Actions**:
   - Home treatments if applicable
   - When to see a doctor
4. **Confidence Level** of your assessment (Low / Medium / High)
5. **Brief Explanation** of your reasoning (1–2 sentences)

Only return medically relevant interpretations — do not provide a diagnosis if the data is insufficient.
"""

