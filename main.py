# AuraCare Health System Core
#Maryam Zafar(503495)

APP_VERSION = "1.0.0"
MODULES_ENABLED = []

def patient_triage(symptoms):
    if "chest pain" in symptoms or "difficulty breathing" in symptoms:
        return "Emergency"
    elif "fever" in symptoms or "headache" in symptoms:
        return "Urgent"
    else:
        return "Routine"