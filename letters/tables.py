from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics.shapes import Drawing, Line

doc = SimpleDocTemplate("tables.pdf", pagesize=letter, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)
def get_paragraph_style(font_size=None, text_color=None, font_name=None, line_spacing=None):
    style = ParagraphStyle(name='Custom')
    if font_size:
        style.fontSize = font_size
    if text_color:
        style.textColor = text_color
    if font_name:
        style.fontName = font_name
    if line_spacing:
        style.leading = line_spacing
    return style

default_styles = [('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
          ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
          ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
          ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
          ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
          ('GRID', (0, 0), (-1, -1), 1, colors.black),]

monthly_revenue_data = [
    ['Month', 'Revenue ($)', 'Expenses ($)', 'Profit ($)', 'Margin (%)'],
    ['January', '150,000', '95,000', '55,000', '36.7'],
    ['February', '165,000', '98,000', '67,000', '40.6']
]

product_performance_data = [
    ['Product Category', '', 'Q1 Sales','', 'Q2 Sales', ''],
    ['', '', 'Units', 'Revenue', 'Units', 'Revenue'],
    ['Electronics', '', '500', '$75,000', '650', '$97,500'],
    ['Furniture', '', '300', '$45,000', '400', '$60,000']
]

customer_segmentation_data = [
    ['Segment', 'Customer Count', 'Avg. Purchase', 'Total Revenue'],
    ['Premium', '250', '$2,500', '$625,000'],
    ['Standard', '1,000', '$500', '$500,000']
]

regional_performance_data = [
    ['Region', 'Performance Metrics', '', ''],
    ['', 'Sales ($)', 'Growth (%)', 'Market Share (%)'],
    ['North', '1,200,000', '15.5', '35'],
    ['South', '950,000', '12.3', '28']
]

elements = []

elements.append(Paragraph("""Sample Table Layouts for Data Analysis Report""", get_paragraph_style(font_size=25, text_color='darkblue', \
                                font_name='Helvetica-Bold', line_spacing=30)))
elements.append(Spacer(0, 0.2 * inch))

line = Drawing(500, 1)
line_shape = Line(0, 0, 450, 0)
line_shape.strokeColor = colors.blue
line.add(line_shape)
elements.append(line)
elements.append(Spacer(0, 0.2 * inch))

elements.append(Paragraph('1. Monthly Revenue Analysis', get_paragraph_style(font_size=15, text_color='blue', font_name='Helvetica')))
t = Table(monthly_revenue_data, spaceBefore=20, spaceAfter=20, colWidths=[1.2*inch]*5)
additional_styles_for_table = [('BACKGROUND', (0, 1), (-1, -1), colors.beige), ('BACKGROUND', (0, 0), (-1, 0), colors.grey)]
styles_for_table = default_styles + additional_styles_for_table
t.setStyle(TableStyle(styles_for_table))
elements.append(t)

elements.append(Paragraph('2. Product Performance Matrix', get_paragraph_style(font_size=15, text_color='blue', font_name='Helvetica')))
t = Table(product_performance_data, spaceBefore=20, spaceAfter=20, colWidths=[inch]*6)
additional_styles_for_table = [
    ('BACKGROUND', (0, 0), (-1, 1), colors.grey),
    ('BACKGROUND', (0, 2), (-1, -1), colors.beige),
    ('SPAN', (0, 0), (1, 1)),
    ('SPAN', (2, 0), (3, 0)),
    ('SPAN', (4, 0), (5, 0)),
    ('SPAN', (0, 2), (1, 2)),
    ('SPAN', (0, 3), (1, 3)),
]
styles_for_table = default_styles + additional_styles_for_table
t.setStyle(TableStyle(styles_for_table))
elements.append(t)

elements.append(Paragraph('3. Customer Segmentation Analysis', get_paragraph_style(font_size=15, text_color='blue', font_name='Helvetica')))
t = Table(customer_segmentation_data, spaceBefore=20, spaceAfter=20, colWidths=[1.5*inch]*4)
additional_styles_for_table = [('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('BACKGROUND', (0, 1), (-1, -1), colors.beige)]
styles_for_table = default_styles + additional_styles_for_table
t.setStyle(TableStyle(styles_for_table))
elements.append(t)

elements.append(Paragraph('4. Regional Performance Summary', get_paragraph_style(font_size=15, text_color='blue', font_name='Helvetica')))
t = Table(regional_performance_data, spaceBefore=20, spaceAfter=20, colWidths=[1.5*inch]*4)
additional_styles_for_table = [
    ('BACKGROUND', (0, 0), (-1, 1), colors.grey),
    ('BACKGROUND', (0, 2), (-1, -1), colors.beige),
    ('SPAN', (1, 0), (3, 0)),
    ('SPAN', (0, 0), (0, 1)),
]
styles_for_table = default_styles + additional_styles_for_table
t.setStyle(TableStyle(styles_for_table))
elements.append(t)

print("PDF created successfully!")