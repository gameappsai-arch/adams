#!/usr/bin/env python3
"""
Convert markdown architecture document to PDF with professional styling
"""

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import sys

def markdown_to_html(md_file):
    """Convert markdown to HTML with extensions"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Use markdown extensions for better formatting
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'extra',
            'codehilite',
            'tables',
            'toc',
            'nl2br',
            'sane_lists'
        ]
    )

    # Wrap in a complete HTML document with styling
    full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NyotaPay Architecture Document</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm 1.5cm;
            @top-center {{
                content: "NyotaPay Architecture v2.0";
                font-size: 9pt;
                color: #666;
            }}
            @bottom-right {{
                content: "Page " counter(page) " of " counter(pages);
                font-size: 9pt;
                color: #666;
            }}
        }}

        @page :first {{
            @top-center {{
                content: none;
            }}
        }}

        body {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            font-size: 10pt;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }}

        h1 {{
            font-size: 28pt;
            font-weight: bold;
            color: #2c3e50;
            margin-top: 0;
            margin-bottom: 8pt;
            page-break-after: avoid;
        }}

        h2 {{
            font-size: 20pt;
            font-weight: bold;
            color: #34495e;
            margin-top: 24pt;
            margin-bottom: 12pt;
            border-bottom: 2px solid #3498db;
            padding-bottom: 6pt;
            page-break-after: avoid;
        }}

        h3 {{
            font-size: 14pt;
            font-weight: bold;
            color: #2c3e50;
            margin-top: 18pt;
            margin-bottom: 10pt;
            page-break-after: avoid;
        }}

        h4 {{
            font-size: 12pt;
            font-weight: bold;
            color: #34495e;
            margin-top: 14pt;
            margin-bottom: 8pt;
            page-break-after: avoid;
        }}

        p {{
            margin: 8pt 0;
            text-align: justify;
        }}

        ul, ol {{
            margin: 8pt 0;
            padding-left: 20pt;
        }}

        li {{
            margin: 4pt 0;
        }}

        code {{
            background-color: #f4f4f4;
            padding: 2pt 4pt;
            border-radius: 3pt;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
            color: #c7254e;
        }}

        pre {{
            background-color: #f8f8f8;
            border: 1pt solid #ddd;
            border-radius: 4pt;
            padding: 10pt;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 8pt;
            line-height: 1.4;
            margin: 12pt 0;
            page-break-inside: avoid;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
            color: #333;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 12pt 0;
            font-size: 9pt;
            page-break-inside: avoid;
        }}

        th {{
            background-color: #3498db;
            color: white;
            font-weight: bold;
            padding: 8pt;
            text-align: left;
            border: 1pt solid #2980b9;
        }}

        td {{
            padding: 8pt;
            border: 1pt solid #ddd;
        }}

        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        blockquote {{
            border-left: 4pt solid #3498db;
            padding-left: 12pt;
            margin: 12pt 0;
            color: #555;
            font-style: italic;
            background-color: #f9f9f9;
            padding: 10pt 12pt;
        }}

        hr {{
            border: none;
            border-top: 2pt solid #3498db;
            margin: 24pt 0;
        }}

        a {{
            color: #3498db;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        .page-break {{
            page-break-after: always;
        }}

        /* Cover page styling */
        .cover {{
            text-align: center;
            margin-top: 100pt;
        }}

        .cover h1 {{
            font-size: 36pt;
            color: #2c3e50;
            margin-bottom: 20pt;
        }}

        .cover h2 {{
            font-size: 18pt;
            color: #7f8c8d;
            border: none;
            font-weight: normal;
        }}

        .cover p {{
            font-size: 12pt;
            color: #95a5a6;
            margin: 10pt 0;
        }}

        /* Table of contents styling */
        .toc {{
            page-break-after: always;
        }}

        .toc h2 {{
            font-size: 24pt;
            margin-bottom: 20pt;
        }}

        .toc ul {{
            list-style-type: none;
            padding-left: 0;
        }}

        .toc li {{
            margin: 8pt 0;
            font-size: 11pt;
        }}

        /* Warning/Note boxes */
        .note {{
            background-color: #e8f4f8;
            border-left: 4pt solid #3498db;
            padding: 12pt;
            margin: 12pt 0;
            page-break-inside: avoid;
        }}

        .warning {{
            background-color: #fef5e7;
            border-left: 4pt solid #f39c12;
            padding: 12pt;
            margin: 12pt 0;
            page-break-inside: avoid;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""
    return full_html

def html_to_pdf(html_content, output_file):
    """Convert HTML to PDF using WeasyPrint"""
    font_config = FontConfiguration()

    # Create PDF
    HTML(string=html_content).write_pdf(
        output_file,
        font_config=font_config
    )

def main():
    input_md = '/home/user/adams/NyotaPay_Architecture_Improved.md'
    output_pdf = '/home/user/adams/NyotaPay_Architecture_Improved.pdf'

    print("Converting markdown to HTML...")
    html_content = markdown_to_html(input_md)

    print("Generating PDF...")
    html_to_pdf(html_content, output_pdf)

    print(f"PDF successfully generated: {output_pdf}")

if __name__ == '__main__':
    main()
