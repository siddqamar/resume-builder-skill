# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "markdown-pdf>=1.13.1,<2",
#   "pymupdf>=1.25.3,<2",
# ]
# ///

"""Convert a Markdown resume to PDF or a rendered PNG."""

from __future__ import annotations

import sys
from pathlib import Path

from markdown_pdf import MarkdownPdf, Section
import fitz


CSS = """
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


def convert_to_pdf(markdown: str, output_pdf: Path) -> None:
    pdf = MarkdownPdf(toc_level=0)
    pdf.add_section(Section(markdown), user_css=CSS)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(str(output_pdf))
    print(f"Successfully created PDF: {output_pdf}")


def convert_pdf_to_png(pdf_path: Path, output_png: Path) -> None:
    with fitz.open(pdf_path) as document:
        if document.page_count == 0:
            raise ValueError("The generated PDF has no pages.")
        page = document.load_page(0)
        pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
        output_png.parent.mkdir(parents=True, exist_ok=True)
        pixmap.save(str(output_png))
    print(f"Successfully created PNG: {output_png}")


def main() -> int:
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python convert_resume.py <input_md_file> <pdf|png> [output_file]")
        return 2

    input_path = Path(sys.argv[1]).expanduser()
    output_format = sys.argv[2].lower()

    if output_format not in {"pdf", "png"}:
        print(f"Error: unsupported format {output_format!r}; use 'pdf' or 'png'.")
        return 2
    if not input_path.is_file():
        print(f"Error: input Markdown file not found: {input_path}")
        return 2

    output_path = (
        Path(sys.argv[3]).expanduser()
        if len(sys.argv) == 4
        else input_path.with_suffix(f".{output_format}")
    )
    markdown = input_path.read_text(encoding="utf-8")

    if output_format == "pdf":
        convert_to_pdf(markdown, output_path)
        return 0

    temporary_pdf = output_path.with_name(f"{output_path.stem}_temp.pdf")
    try:
        convert_to_pdf(markdown, temporary_pdf)
        convert_pdf_to_png(temporary_pdf, output_path)
    finally:
        if temporary_pdf.exists():
            temporary_pdf.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
