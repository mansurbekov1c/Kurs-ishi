# LaTeX ishi — Codex uchun ko'rsatma

Sen `kurs_ishi/latex/` papkasida talaba uchun ishni **LaTeX'da** yozasan va tayyor **PDF** yasaysan.
Vazifa `talabalar/N.Familiya_Ism/topshiriq.md` da beriladi (papka, anketa, adabiyotlar tanlovi va
topshiriqni Claude tayyorlaydi; matn, chizmalar, `.tex` va PDF'ni SEN tayyorlaysan).
Ish davomida foydalanuvchidan savol so'rama: eng oqilona qarorni o'zing qabul qil va `manba/hisobot.md` ga yoz.
Yo'llar `kurs_ishi/latex/` ga nisbatan; repo `../Kurs-ishi/`.

## 1. Boshlashdan oldin o'qi (to'liq)

1. `../Kurs-ishi/latex/yoriqnoma.md` — LaTeX ishi qoidalari va Word'dan farqlar.
2. `../Kurs-ishi/qoidalar/yoriqnoma.md` — umumiy mazmun qoidalari (LaTeX yoriqnomasi unga tayanadi).
3. `../Kurs-ishi/latex/shablon/` — `asosiy.tex` bo'lsa, ish SHU shablondan boshlanadi.
4. `materiallar/adabiyotlar-royxati.md` va `materiallar/namuna/` — kitoblar va namuna ish (shakl uchun).
5. `talabalar/N.Familiya_Ism/topshiriq.md` va `manba/malumot.md`.

Ustunlik: `topshiriq.md` > `latex/yoriqnoma.md` > umumiy `yoriqnoma.md`.

## 2. Muhit

Kerak: `xelatex` (MiKTeX), Python + pdfplumber, matplotlib. `xelatex` PATH'da topilmasa:
`%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64\xelatex.exe`.
`major issue: So far, you have not checked for MiKTeX updates` xabari — zararsiz, e'tibor berma.
Hech narsani o'zing o'rnatma (MiKTeX paketlari ham — sandbox'da tarmoq yo'q). Kompilyatsiya
"File `...sty' not found" bilan to'xtasa: ishni to'xtat, `manba/hisobot.md` ga qaysi paket yetishmasligini yoz.

## 3. Fayllar qayerga (qat'iy)

Faqat `talabalar/N.Familiya_Ism/` ichiga yoz:
```
N.Familiya_Ism/
├── Familiya_Ism.pdf          ← tayyor ish
├── Familiya_Ism_overleaf.zip ← manba/tex/ ning zip'i (Overleaf'ga yuklash uchun; yordamchi fayllarsiz)
├── topshiriq.md              ← (Claude yozgan, o'zgartirma)
└── manba/
    ├── malumot.md            ← anketa + o'zgarishlar tarixi
    ├── manbalar.md           ← qaysi ta'rif/formula/masala qaysi kitobdan (kitob, §, bet) / havola
    ├── hisobot.md            ← oxirgi hisobot
    ├── tex/                  ← main.tex, bolimlar/*.tex, rasmlar/*.png — mustaqil kompilyatsiya bo'ladi
    ├── chizmalar/            ← rasmlarni chizadigan .py kod (natija .png → tex/rasmlar/)
    ├── hisob/                ← raqamli hisob kodi va natijalari (bo'lsa)
    └── tekshiruv/            ← vaqtinchalik: .log, .aux, bet rasmlari; ish oxirida tozalanadi
```
Boshqa joyga yozma. `../Kurs-ishi/` va `materiallar/` — FAQAT O'QISH. Boshqa talabalar papkasiga tegma.

## 4. Ish tartibi

1. **Adabiyot.** Topshiriqdagi kitoblarning kerakli boblarini o'qi (pdfplumber). Kirill OCR formulalari buzilgan
   bo'lishi mumkin — formulani mantiqan va Python bilan tekshir. O'z so'zing bilan, ilmiy uslubda yoz.
2. **Internet** (tarmoq bo'lsa): umumiy yoriqnoma 11-bo'lim. Manba, muallif, yil, sahifani hech qachon TO'QIMA.
3. **Matn.** `manba/tex/bolimlar/` da bo'limlarga bo'lib yoz (`01_kirish.tex`, `02_1_....tex`, ..., `04_adabiyotlar.tex`),
   `main.tex` ularni `\input` bilan ulaydi. Hajm va tuzilma — yoriqnoma va namuna bo'yicha.
   Masalalardagi barcha raqamli natijalarni Python bilan hisoblab tekshir.
4. **Chizmalar.** Yoriqnomadagi soni; matplotlib (300 dpi, oq fon, rasm ichida sarlavha yo'q, yozuvlar o'zbekcha) yoki TikZ.
   Har biri matnda `\ref` bilan havola qilinib izohlanadi.
5. **Kompilyatsiya.** `manba/tex/` ichida:
   `xelatex -interaction=nonstopmode -halt-on-error -output-directory=../tekshiruv main.tex` — 2 marta
   (havolalar uchun; adabiyotlar BibTeX bo'lsa orasida `bibtex`). Natija `../tekshiruv/main.pdf` →
   `Familiya_Ism.pdf` qilib talaba papkasi tepasiga nusxala.
6. **Tekshir.** `../Kurs-ishi/latex/yoriqnoma.md`, 3-bo'lim bo'yicha: logni o'qi, har bir betni rasm qilib ko'r,
   topilgan xatoni tuzatib qayta kompilyatsiya qil (5 martagacha).
7. **Zip.** `manba/tex/` ni (faqat .tex, .bib, rasmlar) `Familiya_Ism_overleaf.zip` qilib joyla.
8. **Tozalash.** `manba/tekshiruv/` ni o'chir (yoki faqat oxirgi .log qoldir).
9. **Hisobot** `manba/hisobot.md`: nima tayyorlandi; bet, so'z, rasm, formula soni; tekshiruvlar o'tdi/o'tmadi;
   internet manbalari havolasi; muammolar — ochiq, yashirmasdan.

## 5. Tuzatish (`tuzatish.md` berilsa)

Avval `manba/malumot.md` va `manba/tex/` ni o'qi, faqat so'ralgan joyni o'zgartir, qayta kompilyatsiya qil,
PDF va zip'ni yangila, o'zgarishni `malumot.md` dagi tarixga sana bilan yoz.
