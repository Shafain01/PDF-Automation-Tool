import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to merge PDFs
def merge_pdfs(pdf_list, output_name):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_name)
    merger.close()

# Function to split PDF
def split_pdf(pdf_path, start_page, end_page, output_name):
    reader = PyPDF2.PdfReader(pdf_path)
    writer = PyPDF2.PdfWriter()

    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])

    with open(output_name, 'wb') as output_pdf:
        writer.write(output_pdf)

# GUI Application
def open_pdf():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file:
        pdf_listbox.insert(tk.END, file)

def merge_selected_pdfs():
    pdfs = list(pdf_listbox.get(0, tk.END))
    if pdfs:
        merge_pdfs(pdfs, "merged_output.pdf")
        messagebox.showinfo("Success", "PDFs Merged Successfully!")

app = tk.Tk()
app.title("PDF Automation Tool")
app.geometry("400x300")

pdf_listbox = tk.Listbox(app)
pdf_listbox.pack(fill=tk.BOTH, expand=True)

open_button = tk.Button(app, text="Add PDF", command=open_pdf)
open_button.pack()

merge_button = tk.Button(app, text="Merge PDFs", command=merge_selected_pdfs)
merge_button.pack()

app.mainloop()
