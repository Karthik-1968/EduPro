from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors

doc = SimpleDocTemplate("registration_for_building_construction.pdf", pagesize=letter, rightMargin=50, leftMargin=36, topMargin=72, bottomMargin=18)

story = []

image_path = "https://crm-backend-media-static.s3.ap-south-1.amazonaws.com/alpha/media/tgbpass_logo.png"
title = "OFFICE OF THE GREATER HYDERABAD MUNICIPAL CORPORATION"
small_text = "TG-bPASS"

image_flowable = Image(image_path, width=1.5 * inch, height=1.5 * inch)
image_flowable.hAlign = 'LEFT'

title_flowable = Paragraph(title, ParagraphStyle(name='TitleStyle', fontSize=10, fontName='Helvetica-Bold'))
title_flowable.hAlign = 'CENTER'

small_text_flowable = Paragraph(small_text, ParagraphStyle(name='SmallTextStyle', fontSize=10, fontName='Helvetica-Bold', textColor=colors.green))
small_text_flowable.hAlign = 'RIGHT'

header_data = [
    [image_flowable, title_flowable, small_text_flowable]
]
header_table = Table(header_data, colWidths=[1.5 * inch, 3 * inch, 2 * inch])
header_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                    ('BOTTOMPADDING', (0, 0), (-1, -1), 12)]))
story.append(header_table)

story.append(Spacer(1, 12))
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

table = Table(data, colWidths=[50, 200, 200])

style = TableStyle([
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
story.append(Spacer(1, 12))

conditions = [
    "1. The certificate issued does not confer upon any ownership rights over the property. The applicant is solely responsible for legal litigations or disputes if any.",
    "2. The extent/area of this plot is not more than 70.0 Sq. Yards and the plot is not part of a bigger plot which has been split for this purpose.",
    "3. The applicant should not construct more than Ground Floor. Any further construction beyond will be liable for penalty / demolition.",
    "4. The applicant shall not violate the front set back of 1.5mts and no structure / balcony projection is allowed in the setback area.",
    "5. If the abutting road width is less than 30 feet (9.00 Mts.), 15 feet (4.5 Mts.) from the center of the existing road has to be left for road widening as per rule 4 (a) of G.O. Ms. No. 168 MA&UD dt:07-04-2012 or required area affected under Master Plan road and in case of plot abutting to MP / RDP / SRDP roads the extent of affected portion of land should be left in addition to the front setback.",
    "6. The proposed construction should be in conformity with the Master plan, Land use and Zoning Regulations.",
    "7. The proposed site should not be a part of Government land / Prohibited land / ULC Land / Disputed land / Municipal land / Layout Open space / Water bodies / NALA / Earmarked Parks and playgrounds not passing through High Tension/Electricity lines.",
    "8. No building activity shall be carried out in certain areas as per rule 3 of G.O. Ms. No. 168 MA&UD dt:07-04-2012.",
    "9. The applicant should commence the construction within 6 months and should complete within a period of 3 years from date of registration.",
    "10. The registration shall stand lapsed if the construction is not completed within stipulated period and a fresh application shall have to be submitted.",
    "11. Post verification will be carried out as per GHMC TG-bPASS Act and action will be initiated if any violation or misrepresentation of the facts is found.",
    "12. Applicant is liable for penal action as per GHMC TG-bPASS Act, in case of misrepresentation or false declaration during post verification. Further the Certificate of Registration will be revoked and construction there upon will be demolished as per the provisions of the GHMC TG-bPASS Act.",
    "13. In case if the building is constructed in deviation to the Building permission, the construction made in deviation to the Building Permission will be demolished as per the provisions of the GHMC TG-bPASS Act.",
    "14. The applicant shall commence the construction of the building as per the Building Rules in force only after the completion of and clearance from the Post Verification process.",
    "15. The issued proceedings are valid for any financial assistance / loan from financial institutions."
]

story.append(Paragraph("""The Certificate of Registration for building construction is issued subject to the
                following conditions:""", ParagraphStyle(name='Title', fontSize=12, textColor=colors.black, fontName='Helvetica-Bold')))
story.append(Spacer(1, 12))
for condition in conditions:
    story.append(Paragraph(condition, ParagraphStyle(name='Title', fontSize=10, textColor=colors.black, fontName='Helvetica')))
    story.append(Spacer(1, 2))
story.append(Spacer(1, 12))
story.append(Paragraph("""NOTE: This is computer generated letter, doesn't require any manual signature""", \
                      ParagraphStyle(name='Title', fontSize=12, textColor=colors.black, fontName='Helvetica', alignment=1)))
story.append(Spacer(1, 12))
def add_watermark(canvas, doc):

    image_path = "https://crm-backend-media-static.s3.ap-south-1.amazonaws.com/alpha/media/tgbpass_logo.png"

    img_width = 400
    img_height = 400

    page_width, page_height = letter
    x_position = (page_width - img_width) / 2
    y_position = (page_height - img_height) / 2

    canvas.setFillAlpha(0.3)

    canvas.drawImage(image_path, x_position, y_position, width=img_width, height=img_height, mask='auto')

doc.build(story, onFirstPage=add_watermark, onLaterPages=add_watermark)