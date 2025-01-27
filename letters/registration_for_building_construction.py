from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors

doc = SimpleDocTemplate("registration_for_building_construction.pdf", pagesize=letter, rightMargin=50, leftMargin=36, topMargin=72, bottomMargin=18)

story = []

text_style = ParagraphStyle(
    name='Normal',
    fontSize=10,
    leading=12,
    fontName='Helvetica'
)

text_block = Paragraph(
    """Sri. Akhil<br/>
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
    ('BACKGROUND', (0, 0), (-1, -1), colors.white),
    ('TEXTCOLOR', (0, 0), (1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (0, 1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

combined_content = Table([[text_block, table]], colWidths=[250, 250])
combined_content.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ('BOX', (0, 0), (0, 1), 1, colors.black),
]))

story.append(combined_content)
story.append(Spacer(1, 12))

story.append(Paragraph("Sir/Madam", ParagraphStyle(name='Title', fontSize=12)))
story.append(Spacer(1, 12))
story.append(Paragraph("""Sub: Greater Hyderabad Municipal Corporation - Construction of Individual<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Residential Building consisting of Ground Floor to an extent of 58.53<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sq.Meters (70.0 Sq.Yds) situated at Plot No: 12, Locality: 123, Survey No: 12,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amberpet(V), Musheerabad Circle 15, Secunderabad Zone, Amberpet(M),<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GHMC, Hyderabad(Dist) - Certificate of Registration - issued.""", \
                                ParagraphStyle(name='Title', fontSize=12, fontName='Helvetica-Bold', textColor=colors.black)))
story.append(Spacer(1, 2))
story.append(Paragraph("""Ref:""", ParagraphStyle(name='Title', fontSize=12, textColor=colors.black, fontName='Helvetica-Bold')))
story.append(Spacer(1, 2))
story.append(Paragraph("""&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Your Application dated: 13-11-2024""", ParagraphStyle(name='Title', fontSize=12, \
                                                                                                                    textColor=colors.black, fontName='Helvetica-Bold')))
story.append(Spacer(1, 2))
story.append(Paragraph("""&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. G.O.Ms.No.168, MA&UD, dt.07-04-2012 and its time to time
amendments.""", ParagraphStyle(name='Title', fontSize=12, textColor=colors.black, fontName='Helvetica-Bold')))
story.append(Spacer(1, 12))
story.append(Paragraph("""With reference to your application 1st cited, the Certificate of Registration for construction of Individual Residential Building is hereby \
                       issued based on Self-Certification given by you as detailed below and subject to conditions mentioned there in """,\
                          ParagraphStyle(name='Title', fontSize=10, textColor=colors.black, fontName='Helvetica')))
story.append(Spacer(1, 12))

data = [
    ['A.','APPLICANT DETAILS',''],
    ['1', 'Name', 'Sri Akhil'],
    ['2', 'S/o', 'Test'],
    ['3', 'Address', 'k'],
    ['B.',' PLOT DETAILS', ''],
    ['1', 'Extent of the Plot', '58.53 Sq.Mtrs (70.0 Sq.Yds)'],
    ['2', 'Net Plot Area', '60.0 Sq.Yards'],
    ['3', 'Plot No', '12'],
    ['4', 'Survey No', '12'],
    ['5', 'Locality', '123'],
    ['6', 'Village Name', 'Amberpet'],
    ['7', 'Circle Name', 'Musheerabad Circle 15'],
    ['8', 'Mandal Name', 'Amberpet'],
    ['9', 'Zone Name', 'Secunderabad Zone'],
    ['10', 'District Name', 'Hyderabad'],
    ['C.',' DETAILS OF REGISTRATION', ''],
    ['1', 'No. of Floors', 'Ground Floor'],
    ['2', 'Construction to be Commenced', 'Before 13-05-2025'],
    ['3', 'Construction to be Completed', 'Before 13-11-2027'],
]

table = Table(data, colWidths=[50, 200, 100])

style = TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('BACKGROUND', (0, 0), (-1, -1), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 4), (-1, 4), 'Helvetica-Bold'),
    ('FONTNAME', (0, 15), (-1, 15), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('SPAN', (1, 0), (2, 0)),
    ('SPAN', (1, 4), (2, 4)),
    ('SPAN', (1, 15), (2, 15)),
])

table.setStyle(style)
story.append(table)

doc.build(story)
