INPUT_FOLDER = "input_data"
OUTPUT_FOLDER = "output_data"
GIGACHAT_CREDENTIALS = "YourAuthorizationKey"

PROMPT = """You are a movie trailer comment analyst.

Analyze the following YouTube comment about a movie trailer and return ONLY valid JSON.

Movie trailer: {video_title}
Comment: {comment_text}

Return JSON in this exact format:
{{
    "sentiment": "positive/negative/neutral/mixed",
    "emotion": "joy/sadness/anger/surprise/fear/disgust/anticipation/trust/none",
    "intensity": 1-10,
    "aspects": ["acting", "plot", "visuals", "music", "direction", "characters", "pacing", "dialogue"],
    "recommendation": true/false
}}

Rules:
- sentiment: overall tone toward the trailer or upcoming movie
- emotion: main emotion (anticipation is very common for trailers)
- intensity: 1 (weak) to 10 (very strong)
- aspects: only include if clearly mentioned, otherwise []
- recommendation: true if the user expresses excitement or intent to watch

IMPORTANT:
- Return ONLY valid JSON
- No explanations
- No extra text
"""