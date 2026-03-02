import sys
import os
from markdown_pdf import MarkdownPdf, Section
import fitz  # PyMuPDF is installed as a dependency of markdown-pdf

def convert_to_pdf(md_content, output_pdf):
    # Initialize the PDF object
    # toc_level=0 as resumes usually don't need a TOC
    pdf = MarkdownPdf(toc_level=0)
    
    # Define simple, ATS-friendly CSS
    css = """
    body { 
        font-family: Helvetica, Arial, sans-serif; 
        line-height: 1.4; 
        font-size: 11pt; 
        color: #333;
        margin: 40px;
    }
    h1 { 
        font-size: 22pt; 
        text-align: center; 
        color: #000; 
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    h2 { 
        font-size: 14pt; 
        border-bottom: 1px solid #ccc; 
        color: #000; 
        margin-top: 20px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    p { margin: 5px 0; }
    ul { margin: 5px 0 10px 20px; }
    li { margin-bottom: 3px; }
    hr { border: 0; border-top: 1px solid #eee; margin: 15px 0; }
    """
    
    # Add content as a Section
    pdf.add_section(Section(md_content), user_css=css)
    
    # Save the PDF
    pdf.save(output_pdf)
    print(f"Successfully created PDF: {output_pdf}")

def convert_pdf_to_png(pdf_path, output_png):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    # Get the first page (resumes are typically 1 page)
    page = doc.load_page(0)
    # Render page to a pixmap (image)
    # Increase zoom for higher quality
    zoom = 2  # 2x zoom
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    # Save the pixmap as a PNG file
    pix.save(output_png)
    doc.close()
    print(f"Successfully created PNG: {output_png}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_resume.py <input_md_file> <output_format> [output_file]")
        sys.exit(1)

    input_md_file = sys.argv[1]
    output_format = sys.argv[2].lower()
    
    if not os.path.exists(input_md_file):
        print(f"Error: File {input_md_file} not found.")
        sys.exit(1)

    with open(input_md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    base_name = os.path.splitext(input_md_file)[0]
    
    if output_format == "pdf":
        output_pdf = sys.argv[3] if len(sys.argv) > 3 else f"{base_name}.pdf"
        convert_to_pdf(md_content, output_pdf)
    elif output_format == "png":
        temp_pdf = f"{base_name}_temp.pdf"
        output_png = sys.argv[3] if len(sys.argv) > 3 else f"{base_name}.png"
        convert_to_pdf(md_content, temp_pdf)
        convert_pdf_to_png(temp_pdf, output_png)
        # Clean up temporary PDF
        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)
    else:
        print(f"Error: Unsupported format {output_format}. Use 'pdf' or 'png'.")
        sys.exit(1)
