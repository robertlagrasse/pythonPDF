from fpdf import FPDF
import pandas

pdf = FPDF(orientation="p", unit="mm", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv('data/pdf-topics.csv')
pageCount = 0
for index, row in df.iterrows():
    Topic = row['Topic']
    pages = int(row['Pages'])

    for i in range(pages):
        pageCount += 1
        pdf.add_page()
        pdf.set_font(family="Times", size=24)
        pdf.set_text_color(25,25,25)
        pdf.cell(w=0, h=24, txt=f"Topic: {Topic}",
                 align="L", ln=1, border=0)
        pdf.line(10, 30, 200, 30)
        pdf.ln(220)
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(2, 2, 2)
        pdf.cell(w=0, h=24, txt=f"Page: {pageCount}",
                 align="R", ln=1, border=0)
        pdf.line(10, 260, 200, 260)


pdf.output("output.pdf")