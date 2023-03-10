import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("*.xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")

    pdf =FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    filename=Path(filepath).stem
    invoice_nr,date= filename.split("-")


    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice Number:{invoice_nr}",ln=1)


    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date:{date}",ln=2)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    col= list(df.columns)
    col= [items.replace("_"," ") for items in col]
    pdf.set_font(family="Times", size=10,style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=col[0], border=1)
    pdf.cell(w=70, h=8, txt=col[1], border=1)
    pdf.cell(w=30, h=8, txt=col[2], border=1)
    pdf.cell(w=30, h=8, txt=col[3], border=1)
    pdf.cell(w=30, h=8, txt=col[4], border=1,ln=1)
    #print(df)

    for index,row in df.iterrows():

        pdf.set_font(family="Times",size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30,h=8,txt=str(row["product_id"]),border=1)
        pdf.cell(w=70,h=8,txt=str(row["product_name"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1,ln=1)


    total_sum = df["total_price"].sum()
    pdf.set_font(family ="Times", size = 10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font(family="Times",size=10)
    pdf.cell(w=30,h=8,txt=f"The total price is {total_sum}",ln=1)

    pdf.set_font(family="Times",size=10)
    pdf.cell(w=30,h=8,txt=f"PythonHow")












    pdf.output(f"PDFs/{filename}.pdf")
"""
    from fpdf import FPDF
 
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
 
content = "
Lorem ipsum dolor sit amet, consectetur adipiscing 
elit, sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco.
"
 
pdf.set_font(family="Times", size=12)
pdf.multi_cell(w=0, h=6, txt=content)
pdf.output("output.pdf")
    """





