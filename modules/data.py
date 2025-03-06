import fitz  
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)  # Open the PDF
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text()  # Extract text
    return text



def extract_text_from_resumes(base_folder_path):
    resume_texts = []
    
    # Iterate through each subfolder
    for career_field in os.listdir(base_folder_path):
        career_field_path = os.path.join(base_folder_path, career_field)
        
        # Check if it's a directory (career field folder)
        if os.path.isdir(career_field_path):
            # Iterate through each PDF file in the folder
            for filename in os.listdir(career_field_path):
                if filename.endswith(".pdf"):
                    pdf_path = os.path.join(career_field_path, filename)
                    text = extract_text_from_pdf(pdf_path)  
                    resume_texts.append(text)
    
    return resume_texts


base_folder_path = "./data/data"  
all_resume_texts = extract_text_from_resumes(base_folder_path)
print(all_resume_texts[:500])

