import tkinter as tk
from tkinter import ttk
from tkinter import *

HEIGHT = 700
WIDTH = 800
root = tk.Tk()
root.title('Interchaange - Coded by Ryan')
root.iconbitmap('ryan.ico')

my_entries = []


def something(*args):
    entry_list = ''

    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'

        my_label.config(text=entry_list)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

###### YEAR #########
label = tk.Label(frame, text='Enter Year', font=('Calibri', '12'))
label.place(relx=0.04, rely=0.06, relwidth=0.15, relheight=0.05)

n = tk.StringVar()
year = ttk.Combobox(frame, width=27, textvariable=n, font=('Calibri', '12'))
year['values'] = (
    '--Select Year--',
    '2021',
    '2020',
    '2019',
    '2018',
    '2017',
    '2016',
    '2015',
    '2014',
    '2013',
    '2012',
    '2011',
    '2010',
    '2009',
    '2008',
    '2007',
    '2006',
    '2005',
    '2004',
    '2003',
    '2002',
    '2001',
    '2000',
    '1999',
    '1998',
    '1997',
    '1996',
    '1995',
    '1994',
    '1993',
    '1992',
    '1991',
    '1990',
    '1989',
    '1988',
    '1987',
    '1986',
    '1985',
    '1984',
    '1983',
    '1982',
    '1981',
    '1980',
    '1979',
    '1978',
    '1977',
    '1976',
    '1975',
    '1974',
    '1973',
    '1972',
    '1971',
    '1970',
    '1969',
    '1968',
    '1967',
    '1966',
    '1965',
    '1964',
    '1963',
    '1962',
    '1961',
    '1960',
    '1959',
    '1958',
    '1957',
    '1956',
    '1955',
    '1954',
    '1953',
    '1952',
    '1951',
    '1950',
    '1949',
    '1948',
    '1947',
    '1946',
    '1945',
    '1944',
    '1943',
    '1942',
    '1941',
    '1940',
    '1939',
    '1938',
    '1937',
    '1936',
    '1935',
    '1934',
    '1933',
    '1932',
    '1931',
    '1930',
    '1929',
    '1928',
    '1927',
    '1926',
    '1925',
    '1924',
    '1923',
    '1922',
    '1921',
    '1920',
    '1919',
    '1918',
    '1917',
    '1916',
    '1915',
    '1914',
    '1913',
    '1912',
    '1911',
    '1910',
    '1909',
    '1908',
    '1907',
    '1906',
    '1905',
    '1904',
    '1903',
    '1902',
    '1901',
    '1900',)

year.place(relx=0.2, rely=0.06, relwidth=0.17, relheight=0.05)
year.bind("<<ComboboxSelected>>", something)
year.current(0)
my_entries.append(year)

###### MAKE ########
makelabel = tk.Label(frame, text='Enter Make', font=('Calibri', '12'))
makelabel.place(relx=0.04, rely=0.15, relwidth=0.15, relheight=0.05)

m = tk.StringVar()
make = ttk.Combobox(frame, width=27, textvariable=m, font=('Calibri', '12'))
make['values'] = [
    '--Select Make--',
    'acura',
    'alfa-romeo',
    'american-motors',
    'aston-martin',
    'audi',
    'bentley',
    'bmw',
    'buick',
    'cadillac',
    'chevrolet',
    'chrysler',
    'citroen',
    'daihatsu',
    'dodge',
    'ferrari',
    'fiat',
    'ford',
    'gmc',
    'honda',
    'hyundai',
    'infiniti',
    'isuzu',
    'jaguar',
    'jeep',
    'kia',
    'lamborghini',
    'lexus',
    'lincoln',
    'lotus',
    'mahindra',
    'maserati',
    'maybach',
    'mazda',
    'mercedes-benz',
    'merkur',
    'mg/austin',
    'mini-cooper',
    'mitsubishi',
    'nissan',
    'opel',
    'peugeot',
    'porsche',
    'renault',
    'rolls-royce',
    'rover',
    'scion',
    'subaru',
    'suzuki',
    'tesla',
    'toyota',
    'volkswagen',
    'volvo',
    'smart',
    'panoz',
    'fisker',
    'saab',
    'mercury',
    'pontiac',
    'saturn',
    'freightliner',
    'studebaker',
    'oldsmobile',
    'daewoo',
    'international-harvester',
    'miscellaneous--motorcycles',
    'plymouth',
    'eagle',
    'checker',
    'miscellaneous--trailers',
    'skoda',
    'tvr',
    'yugo/zastava',
    'de-tomaso',
    'delorean',
    'triumph',
    'jensen',
    'bricklin',
    'simca',
    'rootes']

make.place(relx=0.2, rely=0.15, relwidth=0.20, relheight=0.05)
make.current(0)
my_entries.append(make)
make.bind("<<ComboboxSelected>>", something)

##### MODEL #######
modellabel = tk.Label(frame, text='Enter Model', font=('Calibri', '12'))
modellabel.place(relx=0.040, rely=0.25, relwidth=0.15, relheight=0.05)

md = tk.StringVar()
model = ttk.Combobox(frame, width=27, textvariable=md, font=('Calibri', '12'))
model["values"] = ['--Select Model--',
                   'a', 'b', 'c', 'd']

model.place(relx=0.2, rely=0.25, relwidth=0.20, relheight=0.05)
model.current(0)
my_entries.append(model)
model.bind("<<ComboboxSelected>>", something)

##### CAT ###########
catlabel = tk.Label(frame, text='Category', font=('Calibri', '12'))
catlabel.place(relx=0.040, rely=0.35, relwidth=0.15, relheight=0.05)

ct = tk.StringVar()
cat = ttk.Combobox(frame, width=27, textvariable=ct, font=('Calibri', '12'))
a = [
    ["name", ['ryan', 'deepak', 'rakshith']],
    ["name1", ['cyril', 'kumar', 'benjamin']],
    ["name2", ['adfcdfc']]
]

b = ["--select--", ]
for i in a:
    d = i[0]
    b.append(d)

print(b)
cat['values'] = b
cat.place(relx=0.2, rely=0.35, relwidth=0.20, relheight=0.05)
# cat.current(0)
my_entries.append(cat)
cat.bind("<<ComboboxSelected>>", something)

# ================ PART ===================#
prtlabel = tk.Label(frame, text='Part', font=('Calibri', '12'))
prtlabel.place(relx=0.040, rely=0.45, relwidth=0.15, relheight=0.05)

pt = tk.StringVar()
part = ttk.Combobox(frame, width=27, textvariable=pt, font=('Calibri', '12'))

part.place(relx=0.2, rely=0.45, relwidth=0.20, relheight=0.05)

y = []
for x in range(len(a)):
    for c in a[x]:
        if c == b:
            for x in a[x][1]:
                print(x)
                y.append(x)

print(y)
part['values'] = y
# part.current(0)
my_entries.append(part)
part.bind("<<ComboboxSelected>>", something)

# ===========Display Label===============#
my_label = Label(frame, text='', justify="left", bg='#80c1ff', fg='black', font=('Calibri', '15'))
my_label.place(relx=0.5, rely=0.05, relwidth=0.30, relheight=0.35)


# my_label.pack(pady=20, ipady=10, ipadx=10)


##########PRINT########

def test():
    yr1 = year.get()
    global yr
    yr = str(yr1)

    mk1 = make.get()
    global mk
    mk = str(mk1).lower()

    mdl1 = model.get()
    global mdl
    mdl = str(mdl1).lower()

    prt1 = cat.get()
    global prt
    prt = str(prt1).lower()

    print('%s/%s/%s/%s' % (yr, mk, mdl, prt))


def Clear():
    year.delete(0, END)
    make.delete(0, END)
    model.delete(0, END)
    cat.delete(0, END)
    my_label.config(text='')
    year.current(0)
    make.current(0)
    model.current(0)
    cat.current(0)


################### BUTTONS ########
button = tk.Button(frame, text="Submit", command=test)
button.place(relx=0.05, rely=0.85, relwidth=0.3, relheight=0.1)

clear = tk.Button(frame, text="Clear", command=Clear)
clear.place(relx=0.4, rely=0.85, relwidth=0.3, relheight=0.1)

root.mainloop()
