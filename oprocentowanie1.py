infl1 = float(1.592824484)
infl2 = float(-0.453509101)
infl3 = float(2.324671717)
infl4 = float(1.261254407)
infl5 = float(1.782526286)
infl6 = float(2.329384541)
infl7 = float(1.502229842)
infl8 = float(1.782526286)
infl9 = float(2.328848994)
infl10 = float(0.616921348)
infl11 = float(2.352295886)
infl12 = float(0.337779545)
infl13 = float(1.577035247)
infl14 = float(-0.292781443)
infl15 = float(2.48619659)
infl16 = float(0.267110318)
infl17 = float(1.417952672)
infl18 = float(1.054243267)
infl19 = float(1.480520104)
infl20 = float(1.577035247)
infl21 = float(-0.07742069)
infl22 = float(1.165733399)
infl23 = float(-0.404186718)
infl24 = float(1.499708521)

print("Podaj kwotę swojego kredytu:")
kwotapocz = float(input())
print("Podaj oprocentowanie kredytu w %:")
oproc = float(input())
print("Podaj stałą ratę miesięczną:")
rata = float(input())

zostanie1 = float((1 + ((infl1+oproc)/1200)) * kwotapocz-rata)
mniej = kwotapocz - zostanie1
print("Styczeń")
print(f"Twoja pozostała kwota kredytu to {round(zostanie1, 2)}, to {round(mniej, 2)} mniej niż w poprzednim miesiącu.")

zostanie2 = float((1 + ((infl2 + oproc) / 1200)) * zostanie1 - rata)
mniej2 = zostanie1 - zostanie2
print("Luty")
print(f"Twoja pozostała kwota kredytu to {round(zostanie2, 2)}, to  {round(mniej2, 2)} mniej niż w poprzednim miesiącu.")

zostanie3 = float((1 + ((infl3 + oproc) / 1200)) * zostanie2 - rata)
mniej3 = zostanie2 - zostanie3
print("Marzec")
print(f"Twoja pozostała kwota kredytu to {round(zostanie3, 2)}, to  {round(mniej3, 2)} mniej niż w poprzednim miesiącu.")

zostanie4 = float((1 + ((infl4 + oproc) / 1200)) * zostanie3 - rata)
mniej4 = zostanie3 - zostanie4
print("Kwiecień")
print(f"Twoja pozostała kwota kredytu to {round(zostanie4, 2)}, to  {round(mniej4, 2)} mniej niż w poprzednim miesiącu.")

zostanie5 = float((1 + ((infl5 + oproc) / 1200)) * zostanie4 - rata)
mniej5 = zostanie4 - zostanie5
print("Maj")
print(f"Twoja pozostała kwota kredytu to {round(zostanie5, 2)}, to  {round(mniej5, 2)} mniej niż w poprzednim miesiącu.")

zostanie6 = float((1 + ((infl6 + oproc) / 1200)) * zostanie5 - rata)
mniej6 = zostanie5 - zostanie6
print("Czerwiec")
print(f"Twoja pozostała kwota kredytu to {round(zostanie6, 2)}, to  {round(mniej6, 2)} mniej niż w poprzednim miesiącu.")

zostanie7 = float((1 + ((infl7 + oproc) / 1200)) * zostanie6 - rata)
mniej7 = zostanie6 - zostanie7
print("Lipiec")
print(f"Twoja pozostała kwota kredytu to {round(zostanie7, 2)}, to  {round(mniej7, 2)} mniej niż w poprzednim miesiącu.")

zostanie8 = float((1 + ((infl8 + oproc) / 1200)) * zostanie7 - rata)
mniej8 = zostanie7 - zostanie8
print("Sierpień")
print(f"Twoja pozostała kwota kredytu to {round(zostanie8, 2)}, to  {round(mniej8, 2)} mniej niż w poprzednim miesiącu.")

zostanie9 = float((1 + ((infl9 + oproc) / 1200)) * zostanie8 - rata)
mniej9 = zostanie8 - zostanie9
print("Wrzesień")
print(f"Twoja pozostała kwota kredytu to {round(zostanie9, 2)}, to  {round(mniej9, 2)} mniej niż w poprzednim miesiącu.")

zostanie10 = float((1 + ((infl10 + oproc) / 1200)) * zostanie9 - rata)
mniej10 = zostanie9 - zostanie10
print("Październik")
print(f"Twoja pozostała kwota kredytu to {round(zostanie10, 2)}, to  {round(mniej10, 2)} mniej niż w poprzednim miesiącu.")

zostanie11 = float((1 + ((infl11 + oproc) / 1200)) * zostanie10 - rata)
mniej11 = zostanie10 - zostanie11
print("Listopad")
print(f"Twoja pozostała kwota kredytu to {round(zostanie11, 2)}, to  {round(mniej11, 2)} mniej niż w poprzednim miesiącu.")

zostanie12 = float((1 + ((infl12 + oproc) / 1200)) * zostanie11 - rata)
mniej12 = zostanie11 - zostanie12
print("Grudzień")
print(f"Twoja pozostała kwota kredytu to {round(zostanie12, 2)}, to  {round(mniej12, 2)} mniej niż w poprzednim miesiącu.")

zostanie13 = float((1 + ((infl13 + oproc) / 1200)) * zostanie12 - rata)
mniej13 = zostanie12 - zostanie13
print("Styczeń")
print(f"Twoja pozostała kwota kredytu to {round(zostanie13, 2)}, to  {round(mniej13, 2)} mniej niż w poprzednim miesiącu.")

zostanie14 = float((1 + ((infl14 + oproc) / 1200)) * zostanie13 - rata)
mniej14 = zostanie13 - zostanie14
print("Luty")
print(f"Twoja pozostała kwota kredytu to {round(zostanie14, 2)}, to  {round(mniej14, 2)} mniej niż w poprzednim miesiącu.")

zostanie15 = float((1 + ((infl15 + oproc) / 1200)) * zostanie14 - rata)
mniej15 = zostanie14 - zostanie15
print("Marzec")
print(f"Twoja pozostała kwota kredytu to {round(zostanie15, 2)}, to  {round(mniej15, 2)} mniej niż w poprzednim miesiącu.")

zostanie16 = float((1 + ((infl16 + oproc) / 1200)) * zostanie15 - rata)
mniej16 = zostanie15 - zostanie16
print("Kwiecień")
print(f"Twoja pozostała kwota kredytu to {round(zostanie16, 2)}, to  {round(mniej16, 2)} mniej niż w poprzednim miesiącu.")

zostanie17 = float((1 + ((infl17 + oproc) / 1200)) * zostanie16 - rata)
mniej17 = zostanie16 - zostanie17
print("Maj")
print(f"Twoja pozostała kwota kredytu to {round(zostanie17, 2)}, to  {round(mniej17, 2)} mniej niż w poprzednim miesiącu.")

zostanie18 = float((1 + ((infl18 + oproc) / 1200)) * zostanie17 - rata)
mniej18 = zostanie17 - zostanie18
print("Czerwiec")
print(f"Twoja pozostała kwota kredytu to {round(zostanie18, 2)}, to  {round(mniej18, 2)} mniej niż w poprzednim miesiącu.")

zostanie19 = float((1 + ((infl19 + oproc) / 1200)) * zostanie18 - rata)
mniej19 = zostanie18 - zostanie19
print("Lipiec")
print(f"Twoja pozostała kwota kredytu to {round(zostanie19, 2)}, to  {round(mniej19, 2)} mniej niż w poprzednim miesiącu.")

zostanie20 = float((1 + ((infl20 + oproc) / 1200)) * zostanie19 - rata)
mniej20 = zostanie19 - zostanie20
print("Sierpień")
print(f"Twoja pozostała kwota kredytu to {round(zostanie19, 2)}, to  {round(mniej19, 2)} mniej niż w poprzednim miesiącu.")

zostanie21 = float((1 + ((infl21 + oproc) / 1200)) * zostanie20 - rata)
mniej21 = zostanie20 - zostanie21
print("Wrzesień")
print(f"Twoja pozostała kwota kredytu to {round(zostanie21, 2)}, to  {round(mniej21, 2)} mniej niż w poprzednim miesiącu.")

zostanie22 = float((1 + ((infl22 + oproc) / 1200)) * zostanie21 - rata)
mniej22 = zostanie21 - zostanie22
print("Październik")
print(f"Twoja pozostała kwota kredytu to {round(zostanie22, 2)}, to  {round(mniej22, 2)} mniej niż w poprzednim miesiącu.")

zostanie23 = float((1 + ((infl23 + oproc) / 1200)) * zostanie22 - rata)
mniej23 = zostanie22 - zostanie23
print("Listopad")
print(f"Twoja pozostała kwota kredytu to {round(zostanie23, 2)}, to  {round(mniej23, 2)} mniej niż w poprzednim miesiącu.")

zostanie24 = float((1 + ((infl24 + oproc) / 1200)) * zostanie23 - rata)
mniej24 = zostanie23 - zostanie24
print("Grudzień")
print(f"Twoja pozostała kwota kredytu to {round(zostanie24, 2)}, to  {round(mniej24, 2)} mniej niż w poprzednim miesiącu.")
