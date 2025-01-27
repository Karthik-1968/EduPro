from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors

styles = {
    "title":ParagraphStyle(name='TitleStyle', fontSize=10, fontName='Helvetica-Bold'),
    "small_text": ParagraphStyle(name='SmallTextStyle', fontSize=10, fontName='Helvetica-Bold', textColor=colors.green),
    "text_block": ParagraphStyle(name='Normal',fontSize=10,leading=12,fontName='Helvetica'),
    "permit": ParagraphStyle(name='TitleStyle', fontSize=10, fontName='Helvetica-Bold', alignment=1),
     "To": ParagraphStyle(name='TitleStyle', fontSize=10, fontName='Helvetica-Bold'),
     "Sir/Madam": ParagraphStyle(name='Title', fontSize=12),
     "Sub": ParagraphStyle(name='Title', fontSize=12, fontName='Helvetica-Bold', textColor=colors.black),
     "Ref": ParagraphStyle(name='Title', fontSize=12, textColor=colors.black, fontName='Helvetica-Bold'),
     "para": ParagraphStyle(name='Title', fontSize=10, textColor=colors.black, fontName='Helvetica')

}

doc = SimpleDocTemplate("building_permit_order.pdf", pagesize=letter, rightMargin=50, leftMargin=36, topMargin=72, \
                                                                                                        bottomMargin=18)

story = []

image_path = 'https://crm-backend-media-static.s3.ap-south-1.amazonaws.com/alpha/media/tgbpass_logo.png'
image_flowable = Image(image_path, width=1* inch, height=1 * inch)

title_flowable = Paragraph("""OFFICE OF THE GREATER HYDERABAD MUNICIPAL <br/>
                           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
                           CORPORATION""", styles["title"])
small_text_flowable = Paragraph("TG-bPASS", styles["small_text"])

header_data = [
    [image_flowable, title_flowable, small_text_flowable]
]
header_table = Table(header_data, colWidths=[100,340,70])
header_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                    ('BOTTOMPADDING', (0, 0), (-1, -1), 12)]))
story.append(header_table)

story.append(Paragraph("TG-bPASS - BUILDING PERMIT ORDER", styles["permit"]))
story.append(Spacer(1,12))
story.append(Paragraph("To,", styles["To"]))
story.append(Spacer(1,12))
text_block  = Paragraph("""Sri. Test<br/>
                        S/o test1<br/>
                        test""", styles["text_block"])

table_data = [
    ['Application No/ Permit No', '128909/GHMC/0130/2024'],
    ['Permit No', '128909/GHMC/0130/2024' ],
    ['Date', '13-11-2024'],
]

table = Table(table_data)
table.setStyle(TableStyle([
    ('TEXTCOLOR', (0, 0), (1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (0, 2), 'Helvetica-Bold'),
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

story.append(Paragraph("Sir/Madam,", styles["Sir/Madam"]))
story.append(Spacer(1, 12))
story.append(Paragraph("""Sub: Greater Hyderabad Municipal Corporation - Construction of Individual<br/>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Residential Building consisting of Ground Floor to an extent of 267.56<br/>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sq.Meters (320.0 Sq.Yds)situated at Plot No: 23, Locality: 23, Survey No:<br/>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;233, Amberpet(V), Musheerabad Circle 15, Secunderabad Zone,<br/>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amberpet(M), GHMC, Hyderabad(Dist) - Building Permission-Instant Approval<br/>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;issued - Reg""", styles["Sub"]))
story.append(Spacer(1, 2))
story.append(Paragraph("""Ref:""", styles["Ref"]))
story.append(Spacer(1, 2))
story.append(Paragraph("""&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Your Application dated: 13-11-2024""", styles["Ref"]))
story.append(Spacer(1, 2))
story.append(Paragraph("""&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. G.O.Ms.No.168, MA&UD, dt.07-04-2012 and its time to time
amendments.""", styles["Ref"]))
story.append(Spacer(1, 12))
story.append(Paragraph("""Your application for individual Residential building permission submitted in the reference cited
                            has been sanctioned based on the Self Certification given by you as detailed below and subject to
                            conditions mentioned therein:
                            """, styles["para"]))
story.append(Spacer(1, 12))
data = [
    ['A','APPLICANT DETAILS', '', '', '', '', '', '', ''],
    ['1','Name', 'Sri Test', '', '', '', '', '', ''],
    ['B','SITE DETAILS', '', '', '', '', '', '', ''],
    ['1',' Survey No', '233','','Plot No','23','','',''],
    ['2','Approved Building Plan', '342', '', '', '', '', '', ''],
    ['3','Street/Road', 'N/A','','Locality','23', '', '', ''],
    ['4','Village Name', 'Amberpet', '', '', '', '', '', ''],
    ['5','Circle Name', 'Musheerabad Circle 15', '', '', '', '', '', ''],
    ['6','Mandal Name', 'Amberpet', '', '', '', '', '', ''],
    ['7','Zone Name', 'Secunderabad Zone', '', '', '', '', '',''],
    ['8','District Name', 'Hyderabad', '', '', '', '', '', ''],
    ['C','DETAILS OF PERMISSION SANCTIONED', '', '', '', '', '', '', ''],
    ['1','Extent of Plot', '267.56 Sq.Mtrs (320.0 Sq.Yds)', '', '', '', '', '', ''],
    ['2','Road Affected Area', '0.0 Sq. Yards', '', '', '', '', '', ''],
    ['3','Net Plot Area', '320.0 Sq. Yards', '', '', '', '', '', ''],
    ['4','Floors', '', 'Ground Floor', 'Upper Floor/s', '', 'Parking Floor/s', '', ''],
    ['a','Use', 'Sub-use', 'Area (Sq.Yards)', 'No', 'Area (Sq.Yards)', 'Level', 'No', 'Area (Sq.Yards)'],
    ['b','Residentail', 'Individula Residentail Building', '320.0', '0', '','Stilt', '0', '0.0'],
    ['5','No of floors', 'Ground Floor', '','','','','',''],
    ['6','Height', '3 Mts', '','','','','',''],
    ['7', 'Setbacks (Mts)', 'Front', 'Rear','','Side-I','','Side-II',''],
    ['','','2','1.0','','1.0','','1.0',''],
    ['8','No. of Rain Water Harvesting Pits', '1','No. of Tress', '','','10','',''],
    ['D','MORTGAGE DETAILS','','','','','','',''],
    ['1','Mortgage Area', '32.0Sq. Yards', '', 'SRO','','SECUNDRABAD','',''],
    ['2','Floors Handed Over', 'GROUND', '', 'Date','','2024-11-12','',''],
    ['3','Mortgage No', '12', '', 'Market Value','','1000.0','','']

doc.build(story)
