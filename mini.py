//MINI-PROJ

import streamlit as st
from typing import List

# Knowledge base of treatments
knowledge_base = {
    "cold": [
        "1: Tylenol",
        "2: Panadol",
        "3: Nasal spray",
        "4: Please wear warm clothes!",
        "5: Antibiotics usually not needed, but consult if bacterial infection is suspected."
    ],
    "influenza": [
        "1: Tamiflu",
        "2: Panadol",
        "3: Zanamivir",
        "4: Please take a warm bath and do salt gargling!",
        "5: Antibiotics like Azithromycin may be prescribed if secondary bacterial infection occurs."
    ],
    "typhoid": [
        "1: Chloramphenicol",
        "2: Amoxicillin",
        "3: Ciprofloxacin",
        "4: Azithromycin",
        "5: Please do complete bed rest and take soft diet!",
        "6: Antibiotics used: Ciprofloxacin, Azithromycin, Cefixime"
    ],
    "chicken pox": [
        "1: Varicella vaccine",
        "2: Immunoglobulin",
        "3: Acetaminophen",
        "4: Acyclovir",
        "5: Please have oatmeal baths and stay home!",
        "6: Antibiotics not typically required unless there is a bacterial skin infection."
    ],
    "measles": [
        "1: Tylenol",
        "2: Aleve",
        "3: Advil",
        "4: Vitamin A",
        "5: Please rest and increase liquid intake!",
        "6: Antibiotics like Amoxicillin or Erythromycin may be given if bacterial complications occur."
    ],
    "malaria": [
        "1: Aralen",
        "2: Qualaquin",
        "3: Plaquenil",
        "4: Mefloquine",
        "5: Avoid sleeping outdoors and cover skin!",
        "6: Antibiotics like Doxycycline may be used in combination therapies."
    ],
    "dengue": [
        "1: Acetaminophen",
        "2: Hydration salts",
        "3: Papaya leaf extract",
        "4: Complete rest and fluids!",
        "5: Antibiotics are not effective and not used for viral dengue."
    ],
    "covid-19": [
        "1: Paracetamol",
        "2: Vitamin C",
        "3: Zinc supplements",
        "4: Isolation, hydration, rest!",
        "5: Azithromycin may be prescribed in case of bacterial coinfection."
    ]
}


# Mapping symptoms to disease
symptom_disease_map = {
    frozenset(["headache", "runny nose", "sneezing", "sore throat"]): "cold",
    frozenset(["sore throat", "fever", "headache", "chills", "body ache"]): "influenza",
    frozenset(["rash", "body ache", "fever"]): "chicken pox",
    frozenset(["headache", "abdominal pain", "poor appetite", "fever"]): "typhoid",
    frozenset(["fever", "runny nose", "rash", "conjunctivitis"]): "measles",
    frozenset(["fever", "sweating", "headache", "nausea", "vomiting", "diahrrea"]): "malaria",
    frozenset(["fever", "rash", "joint pain", "headache", "muscle pain"]): "dengue",
    frozenset(["fever", "dry cough", "fatigue", "loss of smell", "shortness of breath"]): "covid-19"
}

st.header("🩺 Medical Diagnosis Expert System")

def respond(symptoms: List[str]):
    input_symptoms = set(symptoms)
    best_match = None
    best_overlap = 0

    # Find the disease with the highest symptom match
    for symptom_set, disease in symptom_disease_map.items():
        match_count = len(input_symptoms.intersection(symptom_set))
        if match_count > best_overlap:
            best_overlap = match_count
            best_match = disease

    if best_match and best_overlap >= 2:  # Change threshold here if needed
        st.success(f"You may have **{best_match.title()}** based on partial symptom match!")
        st.write("Recommended treatment and precautions:")
        for treatment in knowledge_base[best_match]:
            st.write(treatment)
    else:
        st.warning("No close match found in the knowledge base.")
        answer = st.text_area("Please suggest a treatment or precaution (optional):")
        add = st.button("Add to knowledge base")
        if add and answer:
            new_disease = st.text_input("Name of the condition/disease:")
            if new_disease:
                knowledge_base[new_disease.lower()] = [answer]
                symptom_disease_map[frozenset(input_symptoms)] = new_disease.lower()
                st.success("New condition added to the knowledge base.")

if __name__ == "__main__":
    options = st.multiselect(
        'What symptoms are you experiencing?',
        ["headache", "runny nose", "sneezing", "sore throat", "fever", "chills", "body ache",
         "abdominal pain", "poor appetite", "rash", "conjunctivitis", "sweating", "nausea",
         "vomiting", "diahrrea", "joint pain", "muscle pain", "dry cough", "fatigue", "loss of smell", "shortness of breath"],
        [])

    col1, col2 = st.columns([1, 0.3])
    with col1:
        ask = st.button("Diagnose")
    with col2:
        quit = st.button("Quit")

    if ask:
        respond(options)
    if quit:
        st.info("Thank you for using the Expert System! Stay healthy! 😊")
        
