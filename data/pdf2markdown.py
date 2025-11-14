import pdfplumber
import camelot
import pandas as pd
from pathlib import Path

def tables_to_markdown(pdf_path, temp_csv_dir):
    Path(temp_csv_dir).mkdir(exist_ok=True)
    md_sections = []
    tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")
    for i, table in enumerate(tables, start=1):
        df = table.df
        # clean up header row if needed
        df.columns = df.iloc[0]
        df = df[1:]
        md_sections.append(f"### Table {i}\n\n{df.to_markdown(index=False)}\n")
    return "\n".join(md_sections)

def text_to_markdown(pdf_path):
    md_sections = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            md_sections.append(f"## Page {page_num}\n\n{text}\n")
    return "\n".join(md_sections)

def pdf_to_markdown(pdf_path, output_md):
    tables_md = tables_to_markdown(pdf_path, "tmp_tables")
    text_md = text_to_markdown(pdf_path)
    Path(output_md).write_text("# PDF Export\n\n" + text_md + "\n" + tables_md, encoding="utf-8")

if __name__ == "__main__":
    pdf_to_markdown("EWR Cotton Client Interface Manual - Files Received From EWR.pdf", "output.md")