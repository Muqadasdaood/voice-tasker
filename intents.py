import re

def understand_command(text):
    if re.search(r"(close|band)\s+(app|application|window)", text):
        return "CLOSE_APP"
    elif re.search(r"(call|phone)\s+(ali|ahmed|amna)", text):
        return "CALL_PERSON"
    elif re.search(r"(receive|answer|utha)\s+(call|phone)", text):
        return "ANSWER_CALL"
    else:
        return "UNKNOWN"
def understand_command(text):
    text = text.strip().lower()

    # Urdu + Roman Urdu patterns
    if any(phrase in text for phrase in ["band karo", "بند کرو", "بند کر دو", "بند کر دیں"]):
        return "CLOSE_APP"
    elif any(phrase in text for phrase in ["call utha lo", "receive call", "کال اٹھاؤ", "کال ریسیو کرو"]):
        return "ANSWER_CALL"
    elif any(phrase in text for phrase in ["call lagao", "call karo", "کال کرو", "کال ملاؤ"]):
        return "CALL_PERSON"
    else:
        return "UNKNOWN"