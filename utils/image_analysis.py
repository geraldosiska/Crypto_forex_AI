import random

def analyze_chart(image_path):
    fake_patterns = ["Double Top", "Head & Shoulders", "Bullish Engulfing"]
    pattern = random.choice(fake_patterns)
    probability = round(random.uniform(60, 90), 2)

    explanation = {
        "Double Top": "A bearish reversal pattern.",
        "Head & Shoulders": "Signals a potential trend reversal.",
        "Bullish Engulfing": "A bullish signal after a downtrend."
    }

    return {
        "pattern": pattern,
        "probability": f"{probability}%",
        "explanation": explanation.get(pattern, "No explanation found.")
    }