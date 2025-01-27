from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle

# Create a PDF document
doc = SimpleDocTemplate("block_and_table_side_by_side.pdf", pagesize=letter)

# Define the block of text (formatted using Paragraph)
text_style = ParagraphStyle(
    name='Normal',
    fontSize=10,
    leading=12,
    fontName='Helvetica'
)

text_block = Paragraph(
    """<b>Sri. Akhil</b><br/>
    S/o Test<br/>
    k<br/>""",
    text_style
)

table_data = [
    ['File Number', '128909/GHMC/0130/2024'],
    ['Date', '13-11-2024']
]

table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (0, 1), 'Helvetica-Bold'),
    ('FONTNAME', (1, 0), (1, 1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

combined_content = Table([[text_block, table]], colWidths=[270, 270])
combined_content.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ('BOX', (0, 0), (0, 1), 1, colors.black),
]))
# Build the PDF
doc.build([combined_content])
