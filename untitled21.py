# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Krx5AC0uDBQ2igv1jFpgd9rXNzEoq0K_
"""

# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_m011w9xnQLRsMrsuByDesfBp9ZEpUBu
"""

def kasallik_tashxisi(belgi):
   if belgi== "bosh ogrigi":
      return "bolnol iching"
   elif belgi=="qorin ogrigi":
      return "esmonizan iching"
   elif belgi=="tish ogrigi":
      return"qupen iching"
   else:
        return "shifokorga murojat qiling"
belgi=input("kasallik belgisini kiriting")
natija=kasallik_tashxisi(belgi)
print(natija)

def mevalar_narxi(nomi):
  if nomi=="olma":
    return "25000"
  elif nomi=="anor":
    return"30000"
  elif nomi=="banana":
    return"28000"
  elif nomi=="nok":
    return"20000"
  elif nomi=="kiwi":
    return"30000"
  elif nomi=="mandarin":
    return"40000"
  elif nomi=="avakado":
    return"15000"
  elif nomi=="uzum":
    return"26000"
  elif nomi=="kok olma":
    return"20000"
  elif nomi=="behi":
    return"48000"
  else:
    return"afsuski bu meva tugadi lekn uni 17000 sotgan edik"
nomi=input("meva nomini kiriting")
natija=mevalar_narxi(nomi)
print(natija)

