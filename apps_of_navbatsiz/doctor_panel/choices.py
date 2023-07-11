from djchoices import DjangoChoices, ChoiceItem


class Activate_choices(DjangoChoices):
    yes = ChoiceItem()
    no = ChoiceItem()


Doctor_specialties = [
    ("Allergist/Immunologist", "Allergist/Immunologist"),
    ("Anesthesiologist", "Anesthesiologist"),
    ("Cardiologist", "Cardiologist"),
    ("Dermatologist", "Dermatologist"),
    ("Emergency Medicine Specialist", "Emergency Medicine Specialist"),
    ("Endocrinologist", "Endocrinologist"),
    ("Gastroenterologist", "Gastroenterologist"),
    ("Geriatrician", "Geriatrician"),
    ("Hematologist/Oncologist", "Hematologist/Oncologist"),
    ("Infectious Disease Specialist", "Infectious Disease Specialist"),
    ("Internal Medicine Physician", "Internal Medicine Physician"),
    ("Nephrologist", "Nephrologist"),
    ("Neurologist", "Neurologist"),
    ("Obstetrician/Gynecologist (OB/GYN)", "Obstetrician/Gynecologist (OB/GYN)"),
    ("Ophthalmologist", "Ophthalmologist"),
    ("Orthopedic Surgeon/Specialist", "Orthopedic Surgeon/Specialist"),
    ("Otolaryngologist (ENT Specialist)", "Otolaryngologist (ENT Specialist)"),
    ("Pediatrician", "Pediatrician"),
    (
        "Physical Medicine and Rehabilitation Specialist",
        "Physical Medicine and Rehabilitation Specialist",
    ),
    ("Psychiatrist", "Psychiatrist"),
    ("Pulmonologist (lung specialist)", "Pulmonologist (lung specialist)"),
    ("Radiologist", "Radiologist"),
    ("Rheumatologist", "Rheumatologist"),
]
