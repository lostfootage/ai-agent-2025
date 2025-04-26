# ai-agent-2025

# AI Pharmacy Script Reader

This project uses basic AI techniques (OCR + Pattern Recognition) to extract structured information from pharmacy prescriptions.

## Features
- Supports text and image inputs (.txt, .jpg, .png)
- Extracts:
  - Patient Name
  - Medication
  - Dosage
  - Frequency
  - Instructions

## Setup
```bash
pip install -r requirements.txt


## Advanced Usage

To use the Hugging Face model (more powerful AI extraction):

```bash
python main.py


---

### 🌟 Extra 

 **future plan** :


## Future Development Roadmap
- Fine-tune a medical NER model (e.g., BioClinicalBERT) on pharmacy scripts.
- Add support for handwritten OCR via Google Vision or Azure OCR.
- Deploy the model as an API using FastAPI.
- Add a simple Streamlit front-end for uploading prescriptions online.

