import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scan_for_criminal_slang(text: str) -> Dict[str, Any]:
    """
    Scans the provided text for coded language, slang, or regional jargon 
    commonly associated with narcocultura and cartel recruitment.

    Args:
        text: The user input text to analyze.

    Returns:
        A dictionary containing identified terms and a risk indicator.
    """
    # Curated internal list of suspicious terms/emojis (simplified for this example)
    suspicious_patterns = {
        "delivery": "Often used for transporting illicit goods.",
        "quick money": "Red flag for illegal activities.",
        "encrypted": "Request to move to unmonitored channels.",
        "🍕": "Sometimes used as code in regional recruitment.",
        "💎": "Can symbolize high-value illicit rewards.",
    }
    
    found_terms = []
    text_lower = text.lower()
    for term, reason in suspicious_patterns.items():
        if term in text_lower:
            found_terms.append({"term": term, "reason": reason})
            
    risk_level = "High" if len(found_terms) > 2 else "Medium" if len(found_terms) > 0 else "Low"
    
    return {
        "found_terms": found_terms,
        "risk_level": risk_level,
        "summary": f"Detected {len(found_terms)} suspicious patterns."
    }

def assess_exploitation_risk(conversation_context: str) -> str:
    """
    Analyzes the conversation context for red flags of grooming or exploitation tactics.

    Args:
        conversation_context: A summary or transcript of the recent interaction.

    Returns:
        A string indicating the risk level: 'Low', 'Medium', or 'High'.
    """
    red_flags = [
        "asking for age",
        "promising rewards",
        "requesting secret",
        "isolation",
        "job offer",
    ]
    
    count = sum(1 for flag in red_flags if flag in conversation_context.lower())
    
    if count >= 3:
        return "High"
    elif count >= 1:
        return "Medium"
    else:
        return "Low"

def validate_content_safety(content_description: str) -> bool:
    """
    Validates if a described scene, image, or content aligns with safety policies 
    regarding extreme violence and narcocultura glorification.

    Args:
        content_description: A description of the content to be validated.

    Returns:
        True if the content is deemed safe, False if it violates safety policies.
    """
    restricted_keywords = [
        "beheading",
        "torture",
        "execution",
        "cartel leader glorification",
        "massacre",
    ]
    
    is_unsafe = any(keyword in content_description.lower() for keyword in restricted_keywords)
    return not is_unsafe
