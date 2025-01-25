from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus.paraparser import _addAttributeNames, _paraAttrMap
from reportlab.lib.colors import black

def getAttrs(A):
    _addAttributeNames(A)
    S = {}
    for k, v in A.items():
        a = v[0]
        if a not in S:
            S[a] = [k]
        else:
            S[a].append(k)

    K = list(sorted(S.keys()))
    D = [('Attribute', 'Synonyms')]
    for k in K:
        D.append((k, ", ".join(list(sorted(S[k])))))
    cols = 2 * [None]
    rows = len(D) * [None]
    return D, cols, rows

story = []

table_data, cols, rows = getAttrs(_paraAttrMap)
t = Table(table_data, colWidths=cols)
t.setStyle(TableStyle([
    ('FONT', (0, 0), (-1, 0), 'Times-Bold', 10),
    ('FONT', (0, 1), (-1, -1), 'Courier', 8),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
    ('BOX', (0, 0), (-1, -1), 0.25, black),
]))
story.append(t)

# Generate PDF
filename = "output.pdf"
doc = SimpleDocTemplate(filename)
doc.build(story)

print(f"PDF generated successfully and saved as '{filename}'.")