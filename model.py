# model.py

"""
AI Extraction Model
Author: Kimberly Navarrete
Description:
    Core functions to extract structured data from raw prescription text.
"""

import re

def extract_prescription_data(text):
    """
    Extract patient details, medication, dosage, and instructions from text.

    Args:
        text (str): Raw text extracted from the prescription.

    Returns:
        dict: Structured prescription information.
    """
    data = {
        "Patient Name": None,
        "Medication": None,
        "Dosage": None,
        "Frequency": None,
        "Instructions": None
    }

    # Example basic pattern matching (this should be replaced with a more advanced model later)
    name_match = re.search(r'Patient[:\-]?\s*(.*)', text, re.IGNORECASE)
    med_match = re.search(r'Medication[:\-]?\s*(.*)', text, re.IGNORECASE)
    dosage_match = re.search(r'Dosage[:\-]?\s*(.*)', text, re.IGNORECASE)
    freq_match = re.search(r'Frequency[:\-]?\s*(.*)', text, re.IGNORECASE)
    instr_match = re.search(r'Instructions[:\-]?\s*(.*)', text, re.IGNORECASE)

    if name_match:
        data["Patient Name"] = name_match.group(1).strip()
    if med_match:
        data["Medication"] = med_match.group(1).strip()
    if dosage_match:
        data["Dosage"] = dosage_match.group(1).strip()
    if freq_match:
        data["Frequency"] = freq_match.group(1).strip()
    if instr_match:
        data["Instructions"] = instr_match.group(1).strip()

    return data
