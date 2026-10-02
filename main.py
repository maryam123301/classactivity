# AuraCare Health System Core
#SHAZIL (532263)

APP_VERSION = "2.0.0-Beta"
MODULES_ENABLED = []

def patient_triage(symptoms):
    if "chest pain" in symptoms or "difficulty breathing" in symptoms:
        return "Emergency"
    elif "fever" in symptoms or "headache" in symptoms:
        return "Urgent"
    else:
        return "Routine"


def doctor_schedule(doctor_name):
    schedules = {
        "Dr. Ahmed": "Monday to Friday, 9 AM - 1 PM",
        "Dr. Sara": "Monday, Wednesday, Friday, 2 PM - 6 PM"
    }

    return schedules.get(doctor_name, "Schedule not available")