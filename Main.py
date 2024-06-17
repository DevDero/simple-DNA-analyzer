from tkinter import *
from tkinter import ttk
from DNA import *
from BioLibrary import *
from UI import *

def cmd_analyze():
    canvas.delete("all")
    dna_sequence = entry_field1.get().upper()
    dna_sequence2 = entry_field2.get().upper()
    
    pointM = CountPointMutation(str(dna_sequence), str(dna_sequence2))

    count_A = dna_sequence.count('A')
    count_T = dna_sequence.count('T')
    count_G = dna_sequence.count('G')
    count_C = dna_sequence.count('C')

    DrawStrand(canvas, dna_sequence)

    A_text.config(text="A: " + str(count_A))
    T_text.config(text="T: " + str(count_T))
    G_text.config(text="G: " + str(count_G))
    C_text.config(text="C: " + str(count_C))

    Pmutation_text.config(text="Point Mutation: " + str(pointM))
    canvas.configure(scrollregion=canvas.bbox("all"))

def cmd_convert():
    pass

def cmd_complement():
    pass

def testcommand():
   canvas.delete("all")
   Test_Gui(canvas)
   canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()

wrapper1 = LabelFrame(root, background='purple')
wrapper2 = LabelFrame(root, background='#FFD700')

canvas = Canvas(wrapper1)
scrollbar = Scrollbar(wrapper1, orient='horizontal', command=canvas.xview)
canvas.config(xscrollcommand=scrollbar.set)

wrapper1.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

notebook = ttk.Notebook(wrapper2)

tab1 = Frame(notebook)
label_entry = Label(tab1, text="Entry Field for DNA Analyze")
entry_field1 = Entry(tab1, width=20)
label_entry2 = Label(tab1, text="Entry Field for Point Mutations")
entry_field2 = Entry(tab1, width=20)
button_analyze = Button(tab1, text='Analyze', command=cmd_analyze)
CreateComplementingDNA = Button(tab1, text='Complementing DNA', command=cmd_complement)

A_text = Label(tab1, text="A: 0", width=10, anchor='w', relief="sunken", bd=1)
T_text = Label(tab1, text="T: 0", width=10, anchor='w', relief="sunken", bd=1)
G_text = Label(tab1, text="G: 0", width=10, anchor='w', relief="sunken", bd=1)
C_text = Label(tab1, text="C: 0", width=10, anchor='w', relief="sunken", bd=1)
Pmutation_text = Label(tab1, text="Point Mutation: ", width=40, anchor='w', relief="sunken", bd=1)

label_entry.pack(padx=1, pady=(5, 10), anchor='nw')
entry_field1.pack(padx=1, pady=5, anchor='nw', side='top')
label_entry2.pack(padx=1, pady=(5, 10), anchor='nw')
entry_field2.pack(padx=1, pady=5, anchor='nw', side='top')
button_analyze.pack(padx=1, pady=5, anchor='nw', side='left')
CreateComplementingDNA.pack(padx=1, pady=5, anchor='nw', side='left')

Pmutation_text.pack(padx=10, pady=5, anchor='w', side='bottom')
A_text.pack(side='left', padx=5, pady=5)
T_text.pack(side='left', padx=5, pady=5)
G_text.pack(side='left', padx=5, pady=5)
C_text.pack(side='left', padx=5, pady=5)

notebook.add(tab1, text='DNA Analyze')

tab2 = Frame(notebook)
label_entry2 = Label(tab2, text="Entry Field for DNA to RNA")
entry_field2_tab2 = Entry(tab2, width=20)
button_convert = Button(tab2, text='Convert', command=cmd_convert)

label_entry2.pack(padx=5, pady=(5, 10), anchor='nw')
entry_field2_tab2.pack(padx=5, pady=5, anchor='nw')
button_convert.pack(padx=5, pady=5, anchor='nw')

notebook.add(tab2, text='DNA to RNA')

tab3 = Frame(notebook)
label_test = Label(tab3, text="Test Tab Content")
button_test = Button(tab3, text='Run Test', command=testcommand)

label_test.pack(padx=5, pady=(5, 10), anchor='nw')
button_test.pack(padx=5, pady=5, anchor='nw')

notebook.add(tab3, text='Test')

notebook.pack(fill="both", expand=True, padx=10, pady=10)

wrapper1.pack(fill="both", expand="yes", padx=30, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
scrollbar.pack(side=BOTTOM, fill=X)
canvas.pack(fill="both", expand=True)

root.geometry("800x600")
root.title("DNA Analysis and Conversion")

root.mainloop()
