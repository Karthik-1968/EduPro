from reportlab.platypus import SimpleDocTemplate, ListFlowable, ListItem, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib.units import inch

doc = SimpleDocTemplate("ordered_lists.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

def get_paragraph_style(font_size=None, text_color=None, font_name=None):
    style = ParagraphStyle(name='Custom')
    if font_size:
        style.fontSize = font_size
    if text_color:
        style.textColor = text_color
    if font_name:
        style.fontName = font_name
    return style
story = []

story.append(Paragraph("Document with Lists and Images", get_paragraph_style(font_size=25, text_color='blue', font_name=\
                                                                             'Helvetica-Bold')))
story.append(Spacer(0, 0.5 * inch))

line = Drawing(500, 1)
line_shape = Line(0, 0, 450, 0)
line_shape.strokeColor = colors.blue
line.add(line_shape)
story.append(line)
story.append(Spacer(0, 0.2 * inch))

story.append(Paragraph("Ordered List Example", get_paragraph_style(font_size=20, text_color='black', font_name='Helvetica-Bold')))
story.append(Spacer(0, 0.5 * inch))

ordered_list = ListFlowable([   
                                ListItem(Paragraph("Project Planning", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                bulletColor='blue', value=1),
                                ListFlowable(
                                    [
                                        ListItem(Paragraph("Define project scope", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=1),
                                        ListItem(Paragraph("Set timeline", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=2),
                                        ListItem(Paragraph("Allocate resources", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=3)
                                    ]
                                ),
                                ListItem(Paragraph("Implementation Phase", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                bulletColor='blue', value=2),
                                ListFlowable(
                                    [
                                        ListItem(Paragraph("Development", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=1),
                                        ListItem(Paragraph("Testing", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=2),
                                        ListItem(Paragraph("Deployment", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=3),
                                    ]
                                ),
                                ListItem(Paragraph("Project Review", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                bulletColor='blue', value=3),
                                ListFlowable(
                                    [
                                        ListItem(Paragraph("Performance analysis", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=1),
                                        ListItem(Paragraph("Documentation", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=2),
                                        ListItem(Paragraph("Feedback collection", get_paragraph_style(font_size=12, text_color='black', font_name='Helvetica')),\
                                                                                                        bulletColor='blue', value=3),
                                    ]
                                )
                            ])
story.append(ordered_list)
doc.build(story)
print("PDF created successfully!")