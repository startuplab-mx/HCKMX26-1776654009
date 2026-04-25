import re

def scan_for_criminal_slang(text: str):
    """
    Detecta modismos y simbología de facciones criminales (CJNG, CDS).
    Basado en el análisis de etnografía digital del Colmex.
    """
    # Diccionario de semiótica criminal [cite: 72, 74, 75, 421]
    patterns = {
        "CJNG": [r"🐓", r"NG", r"4letras", r"4 LTRS", r"mencho", r"señormencho"],
        "Sinaloa": [r"🍕", r"chapizza", r"mayiza", r"gentedelmz", r"zambada"],
        "General_Riesgo": [r"🥷", r"⛑️", r"maña", r"belicon", r"labor4r"]
    }
    
    findings = []
    for cartel, markers in patterns.items():
        for marker in markers:
            if re.search(marker, text, re.IGNORECASE):
                findings.append(f"Detección de {cartel}: {marker}")
    
    return findings if findings else "No se detectaron patrones explícitos."

def assess_exploitation_risk(text: str):
    """
    Evalúa el riesgo de reclutamiento basado en promesas de empleo falsas.
    Correlación Paga/Entrenamiento: 0.82[cite: 654].
    """
    # Marcadores de ofertas fraudulentas [cite: 121, 132, 178]
    triggers = [
        "12 mil", "15 mil", "semanal", "hospedaje", 
        "comida", "adiestramiento", "no pedimos dinero"
    ]
    
    risk_score = 0
    detected_triggers = [t for t in triggers if t.lower() in text.lower()]
    
    if len(detected_triggers) >= 2:
        risk_score = 85  # Riesgo alto por acumulación de promesas [cite: 655]
    
    return {
        "score": risk_score,
        "triggers": detected_triggers,
        "status": "ALERTA ROJA" if risk_score > 70 else "Monitoreo"
    }

def validate_content_safety(content_type: str):
    # Clasificación de las 6 categorías de riesgo [cite: 31-35, 338-342]
    safe_categories = ["Educación", "Deporte", "Tecnología"]
    return content_type in safe_categories