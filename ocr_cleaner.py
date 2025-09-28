import re
import string
from collections import Counter
import unicodedata

def get_cleaned_ocr_text(ocr_text, min_header_footer_length=3, min_repetition_count=2):


    def normalize_text(text):
        text = unicodedata.normalize('NFKC', text)
        text = re.sub(r'\s+', ' ', text)
        replacements = {
            r'[|]': 'I',
            r'[`\']': "'",
            r'[“”]': '"',
            r'[–]': '-',
        }
        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text)
        return text

    def fix_line_breaks(text):
        text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
        text = re.sub(r'([a-z])\s*\n\s*([a-z])', r'\1 \2', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)
        return text

    def remove_repeated_headers_footers(text, min_length, min_count):
        lines = text.split('\n')
        line_counts = Counter(lines)
        repeated_patterns = [
            line for line, count in line_counts.items()
            if count >= min_count and len(line.strip()) >= min_length
        ]
        cleaned_lines = [line for line in lines if line not in repeated_patterns or len(line.strip()) < min_length]
        return '\n'.join(cleaned_lines)

    def clean_text_structure(text):
        lines = [line.strip() for line in text.split('\n')]
        lines = [line for line in lines if line]
        text = '. '.join([sentence.strip().capitalize() for sentence in text.split('.')])
        return '\n'.join(lines)

    cleaned_text = normalize_text(ocr_text)
    cleaned_text = fix_line_breaks(cleaned_text)
    cleaned_text = remove_repeated_headers_footers(cleaned_text, min_header_footer_length, min_repetition_count)
    cleaned_text = clean_text_structure(cleaned_text)
    return cleaned_text

