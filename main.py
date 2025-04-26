# main.py

"""
AI Pharmacy Script Reader
Author: Kimberly Navarrete
Description:
    An AI agent designed to read and extract information from pharmacy prescriptions (scripts).
    It identifies patient details, prescribed medications, dosages, and instructions.
"""

import os
from model import extract_prescription_data

def load_prescription(file_path):
    """
    Load a pharmacy script from a file.
    
    Args:
        file_path (str): Path to the script image or text file.

    Returns:
        str: Content of the script (text or OCR extracted text).
    """
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf')):
        # If image or PDF, apply OCR (Optical Character Recognition)
        import pytesseract
        from PIL import Image

        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        return text
    elif file_path.lower().endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError("Unsupported file type. Please use image (.png, .jpg) or text (.txt) files.")

def main():
    """
    Main function to run the AI agent.
    """
    # Example usage
    file_path = input("Enter the path to the prescription file: ").strip()

    try:
        script_text = load_prescription(file_path)
        structured_data = extract_prescription_data(script_text)

        print("\nExtracted Prescription Details:")
        for key, value in structured_data.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


# Inside main()

    method = input("Choose extraction method (simple / huggingface): ").strip().lower()

    if method == 'simple':
        structured_data = extract_prescription_data(script_text)
    elif method == 'huggingface':
        from huggingface_model import extract_prescription_data_hf
        structured_data = extract_prescription_data_hf(script_text)
    else:
        print("Invalid extraction method selected.")
        return

