from tkinter import *
import http.client

win=Tk()
win.title("covid info")
win.geometry("600x450")

#загальна функція
def refresh():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "72ccabb70amsh27b43378ab274c0p119443jsnc7cb3f194139",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"}
    conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
    res = conn.getresponse()
    data = res.read()
    js=(data.decode("utf-8"))

#функія для пошуку та виведення інформацї
    def datap(country,xx,yy):
        
        Label(win, text=country,font=("Calibri",10)).place(x=xx,y=yy)
        
        d1 = js.find('TotalCases',js.find(country))
        d11 = js.find('NewCases',js.find(country))
        tc=js[d1+12:d11-2]
        Label(win, text=tc,font=("Calibri",10)).place(x=xx,y=yy+30)
            
        d2 = js.find('NewCases',js.find(country))
        d22 = js.find('TotalDeaths',js.find(country))
        nc=js[d2+10:d22-2]
        Label(win, text=nc,font=("Calibri",10)).place(x=xx,y=yy+60)

        d3 = js.find('TotalDeaths',js.find(country))
        d33 = js.find('NewDeaths',js.find(country))
        td=js[d3+13:d33-2]
        Label(win, text=td,font=("Calibri",10)).place(x=xx,y=yy+90)
            
        d4 = js.find('NewDeaths',js.find(country))
        d44 = js.find('TotalRecovered',js.find(country))
        nd=js[d4+11:d44-2]
        Label(win, text=nd,font=("Calibri",10)).place(x=xx,y=yy+120)

        d5 = js.find('Population',js.find(country))
        d55 = js.find('one_Caseevery_X_ppl',js.find(country))
        p=js[d5+13:d55-3]
        Label(win, text=p,font=("Calibri",10)).place(x=xx,y=yy+150)

    countries=['Japan','China','Maldives','Sri Lanka','Singapore']

    Label(win, text="Country:", font=("Calibri", 10)).place(x=10,y=10)
    Label(win, text="Total Cases:", font=("Calibri", 10)).place(x=10,y=40)
    Label(win, text="New Cases:", font=("Calibri", 10)).place(x=10,y=70)
    Label(win, text="Total Deaths:", font=("Calibri", 10)).place(x=10,y=100)
    Label(win, text="New Deaths:", font=("Calibri", 10)).place(x=10,y=130)
    Label(win, text="Population:", font=("Calibri", 10)).place(x=10,y=160)

    xq=90
    yq=10

    #вивід інформації по зазначеним країнам
    for i in range(len(countries)):
        datap(countries[i],xq+80*i,yq)

    #функція по пошуку за введеною країною
    def search():
        key=str(searchw.get())
        #вивід помилки якщо такої країни немає у переліку
        if key not in js:
            Label(win, text="no information"+" "*20, font=("Calibri", 10)).place(x=10,y=270)
        #вивід інформації про введену країну
        else:
            Label(win, text="only asian countries"+" "*20, font=("Calibri", 10)).place(x=10,y=270)
            datap(key,120+75*len(countries),10)
        
    Label(win, text="only asian counrties"+" "*20, font=("Calibri", 10)).place(x=10,y=270)
    
    searchw=Entry(win, width=15,font=("Calibri", 10))
    searchw.place(x=10,y=240)

    #кнопка для пошуку
    schb=Button(win, text="search!",command=search).place(x=120,y=234.5)

#кнопка для оновлення програми
rf=Button(win, text="refresh!",command=refresh).place(x=10,y=190)

refresh()    
win.mainloop()
