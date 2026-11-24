# LaTeX ishi — yo'riqnoma

LaTeX bo'limi Word kurs ishlaridan alohida: o'z adabiyotlari, namunasi va talabalari bor
(`kurs_ishi/latex/`). Natija — **PDF** (XeLaTeX bilan) va Overleaf'ga yuklasa bo'ladigan `.tex` manba.

## 0. Holat (2026-11-24)

Namuna ish va o'qituvchi talablari hali berilmagan. Ular kelguncha **umumiy
`qoidalar/yoriqnoma.md` amal qiladi** (kirish ma'lumotlari, muqova, tuzilma, kirish, bo'limlar,
formulalar mazmuni, rasmlar, xulosa, adabiyotlar, til), quyidagi LaTeX farqlari bilan.
Namuna kelgach: undan farq qiladigan har bir qoida shu faylga yoziladi va `shablon/asosiy.tex` yasaladi.

Namunadan aniqlanadigan ochiq savollar:
- Muqova shakli va universitet/kafedra (umumiy yoriqnomadagidek bo'lmasligi mumkin).
- Hajm (bet soni), shrift (Times New Roman yoki LaTeX'ning o'z shrifti), hoshiyalar, interval.
- REJA yoki MUNDARIJA (bet raqamli `\tableofcontents`).
- Formula raqamlash: ketma-ket (1), (2) yoki bob bo'yicha (2.1).
- Adabiyotlar: qo'lda `thebibliography` yoki BibTeX.
- Topshirish shakli: faqat PDF, `.tex` manba yoki Overleaf havolasi.

## 1. Word'dan farqlar (hozirdan amal qiladi)

- Formulalar LaTeX'ning o'zida (`equation`, `align`), raqami va havolasi `\label`/`\eqref` bilan —
  qo'lda raqam yozilmaydi. MathType/OMML yo'q.
- Rasm, jadval, formula raqamlari va havolalari avtomatik (`\label`/`\ref`).
- "Har bir bet oxirigacha to'ldiriladi" (umumiy yoriqnoma, 3-bo'lim) LaTeX'da qo'lda moslanmaydi:
  matn betga avtomatik teriladi. Faqat quyidagilar tekshiriladi: bo'sh yoki yarim bo'sh bet yo'q
  (bob oxiridan tashqari), sarlavha bet oxirida yolg'iz qolmagan, rasm/jadval yolg'iz betga tushmagan.
- Rasm/jadval nomlari o'zbekcha: `N.M-rasm.` / `N.M-jadval.` (inglizcha "Figure", "Table" chiqmasin).
- Chizmalar: matplotlib (.png, 300 dpi) yoki TikZ/pgfplots — ikkalasi ham mumkin.

## 2. Texnik qoidalar

- Kompilyator: **XeLaTeX** (MiKTeX, foydalanuvchi kompyuterida). Har kompilyatsiya 2 marta (havolalar uchun).
- O'zbek harflari: `fontspec` + Unicode matn. Tutuq belgisi butun ishda bir xil (ʻ U+02BB yoki ' — namunaga qarab).
- Matematik shrift fayl nomi bilan: `\setmathfont{latinmodern-math.otf}` (nomi bilan topilmaydi).
- `latexmk` ishlatilmaydi (Perl o'rnatilmagan).
- Yangi paket kerak bo'lsa: MiKTeX uni birinchi kompilyatsiyada o'zi yuklaydi (AutoInstall=1), lekin Codex
  sandbox'ida tarmoq yo'q — shuning uchun shablondagi paketlar oldindan bir marta (sandbox'dan tashqarida)
  kompilyatsiya qilib o'rnatiladi. Shablonda yo'q paket qo'shishdan saqlan.
- Manba Overleaf'da ham kompilyatsiya bo'lishi kerak: faqat standart paketlar, nisbiy yo'llar,
  bo'limlar `\input` bilan ulanadi, shrift fayl/tizim nomi Overleaf'da ham bor bo'lsin
  (Times New Roman Overleaf'da `TeX Gyre Termes` bilan almashadi — namuna talab qilsa hal qilinadi).

## 3. Sifat tekshiruvi (har bir tayyor PDF uchun)

1. Kompilyatsiya logida xato (`!`) yo'q; `undefined references`, `Missing character`, `Overfull \hbox`
   (> 5pt) ogohlantirishlari yo'q yoki hisobotda izohlangan.
2. Har bir bet rasm qilib ko'rib chiqiladi (pdfplumber `to_image`): matn chetdan chiqmagan, bo'sh bet yo'q,
   rasm/jadval nomi ostida, formulalar va raqamlari to'g'ri.
3. Bet soni, rasmlar soni, formulalar raqamlanishi — `yoriqnoma.md` (va namuna) ga mos.
4. Muqova ma'lumotlari `malumot.md` bilan bir xil.
5. Adabiyotlar haqiqiy va har biri matnda ishlatilgan (umumiy yoriqnoma, 11-bo'lim).
6. `.tex` manba alohida papkada mustaqil kompilyatsiya bo'ladi (Overleaf zip uchun).
