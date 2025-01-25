from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch

styles = ParagraphStyle(name='Normal')

def get_paragraph_style(font_size=None, text_color=None, font_name=None):
    if font_size:
        styles.fontSize = font_size
    if text_color:
        styles.textColor = text_color
    if font_name:
        styles.fontName = font_name
    return styles

story = []
story.append(Paragraph('Data Analysis Project Assignment', get_paragraph_style(font_size=15, text_color='blue', font_name='Helvetica-Bold')))
story.append(Spacer(0, 0.5*inch))
story.append(Paragraph('Project Description', get_paragraph_style(font_size=12, text_color='blue', font_name='Helvetica')))
story.append(Spacer(0, 12))
story.append(Paragraph("""You will analyze our e-commerce platform's customer behavior data. This analysis aims to
                            identify key purchasing patterns and customer segments driving business growth. The project
                            involves working with real transaction data from the past 12 months.
                            """, get_paragraph_style(font_size=10, text_color='black', font_name='Helvetica')))
story.append(Spacer(0, 12))
story.append(Paragraph('Technical Requirements', get_paragraph_style(font_size=12, text_color='blue', font_name='Helvetica')))
story.append(Spacer(0, 12))
story.append(Paragraph("""The analysis requires proficiency in Python, particularly with pandas and scikit-learn libraries.
                                You will need to perform data cleaning, exploratory data analysis, and create meaningful
                            visualizations of key insights. The project emphasizes efficient handling of large datasets while
                            maintaining data integrity throughout the analysis process.""", get_paragraph_style(font_size=10, text_color='black', font_name='Helvetica')))
c  = Canvas('data_analysis_project_assignment.pdf')
f = Frame(inch, inch, 6*inch, 9*inch)
f.addFromList(story,c)
c.save()
