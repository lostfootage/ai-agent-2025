# huggingface_model.py

"""
Advanced Extraction using Hugging Face Transformers
Author: Kimberly Navarrete
Description:
    Uses a pre-trained NER model to extract structured data from pharmacy scripts.
"""

from transformers import pipeline

# Load Named Entity Recognition (NER) model
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def extract_prescription_data_hf(text):
    """
    Extract prescription information using a Hugging Face NER model.
    
    Args:
        text (str): Raw text extracted from the prescription.

    Returns:
        dict: Structured prescription information.
    """
    entities = ner_pipeline(text)
    
    data = {
        "Patient Name": None,
        "Medication": [],
        "Dosage": [],
        "Frequency": [],
        "Instructions": None
    }

    for entity in entities:
        if entity['entity_group'] == "PER":  # Person names (sometimes picked up)
            if not data["Patient Name"]:
                data["Patient Name"] = entity['word']
        elif entity['entity_group'] == "MISC" or entity['entity_group'] == "ORG":
            data["Medication"].append(entity['word'])
        # Dosage, Frequency, and Instructions are tricky
        # You might later fine-tune a custom model for these
        # For now, we gather general medication-related info

    return data
