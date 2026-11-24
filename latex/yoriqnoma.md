# LaTeX ishi — yo'riqnoma (MUSTAQIL ISH)

LaTeX bo'limi Word kurs ishlaridan alohida: o'z adabiyotlari, namunasi va talabalari bor
(`kurs_ishi/latex/`). Natija — **PDF** (XeLaTeX) va Overleaf'ga yuklasa bo'ladigan `.tex` manba.
Bu qoidalar namuna (`latex/materiallar/namuna/Shirin Latex.pdf`, 2026-11-24 o'lchangan) asosida yozilgan.
Bu yerda yozilmagan mazmun qoidalari (til, ilmiy uslub, adabiyotlar haqiqiyligi) — umumiy
`qoidalar/yoriqnoma.md` (11, 12-bo'limlar) dan olinadi. Muqova, format va tuzilma — FAQAT shu fayldan.

## 0. Ish turi

- **Mustaqil ish** (kurs ishi emas). Fan: "Suyuqlik va gazlar mexanikasi" (boshqa fan kelsa — shu shakl saqlanadi).
- Mazmun yadrosi: kafedraning amaliy to'plamidagi (`3_mex (1).pdf`) bitta mavzu — uning nazariyasi
  va **o'sha mavzudagi 15 ta "mustaqil ishlash uchun masala"ning hammasi** yechiladi.
- Hajm: **16–20 bet** (namuna 18 bet).

## 1. Sahifa va shrift (namunadan o'lchangan)

| Parametr | Qiymat |
|---|---|
| Qog'oz | A4 |
| Hoshiyalar | chap 3 sm, o'ng 1,5 sm, yuqori 2 sm, past 2 sm |
| Shrift | CMU Serif (`fontspec`), asosiy matn **12 pt**; formulalar Computer Modern |
| Qator oralig'i | 1,5 (`setspace`, `\onehalfspacing`; 12 pt da qatorlar orasi ~18 pt) |
| Xatboshi | 1,25 sm, birinchi xatboshi ham chekinadi (`indentfirst`) |
| Tekislash | ikki tomonlama |
| Sahifa raqami | pastda, markazda; muqovada ko'rinmaydi, lekin sanaladi (MUNDARIJA = 2-bet) |
| Header | yo'q |
| Tutuq belgisi | butun ishda bitta: ’ (U+2019), namunadagidek — `O’zbekiston`, `ko’rinishda` |

## 2. Muqova (1-bet, raqamsiz)

Yuqoridan pastga:
1. Markazda, qalin, bosh harflarda (har biri alohida qatorda, orasida bo'sh joy):
   `O’ZBEKISTON RESPUBLIKASI TA’LIM VA ILM FAN VAZIRLIGI`
   `ABU RAYXON BERUNIY NOMIDAGI URGANCH DAVLAT UNIVERSITETI`
   `FIZIKA-MATEMATIKA FAKULTETI`
   `“MEXANIKA VA MATEMATIK INJINIRING” KAFEDRASI`
2. Markazda, kursiv: `[Fan nomi] fanidan` (masalan, "Suyuqlik va gazlar mexanikasi fanidan").
3. Markazda, katta (~20 pt): `MUSTAQIL ISH`.
4. Chapda: `Mavzu:` (qalin) + mavzu nomi (tagiga chizilgan).
5. O'ng yarmida (blok o'ng tomonda, matn chapga tekis):
   `Bajardi: [guruh]-[yo'nalish] – guruh talabasi` / `[Familiya Ism]`,
   pastroqda `Tekshirdi: [Rahbar]`.
6. Betning pastida, markazda: `Urganch – [Yil]`.
Logo YO'Q (namunada yo'q).

Standart qiymatlar (anketada boshqacha bo'lmasa): fakultet — Fizika-matematika; kafedra —
"Mexanika va matematik injiniring"; yo'nalish — "mexanika va matematik modellashtirish"; yil — joriy.

## 3. Tuzilma

```
MUNDARIJA                                   ← bet raqamli, nuqtali (\tableofcontents)
KIRISH                                      ← ~1 bet
I BOB. [MAVZU] NAZARIYASI                   ← 3–4 bet
   1.1. ...   1.2. ...   1.3. ...
II BOB. MASALALAR YECHIMI
   2.1. Masalalar yechimlari                ← 15 masala, ~9–11 bet
   2.2. Natijalar jamlanmasi                ← javoblar jadvali
XULOSA                                      ← ~1 bet
FOYDALANILGAN ADABIYOTLAR
```

- Har bir bob (KIRISH, I BOB, II BOB, XULOSA, ADABIYOTLAR) yangi betdan; sarlavha qalin, bosh harflarda
  (`\large`, ~14 pt). Bo'lim sarlavhasi `1.1. Nomi` — qalin, 12–14 pt, chapda.
- **KIRISH:** mavzuning ahamiyati (2–3 xatboshi, manbaga havolalar bilan), `Mustaqil ishning maqsadi — ...`,
  `Mustaqil ishning vazifalari:` raqamlangan ro'yxat (oxirgisi: "o’quv qo’llanmadagi [N] mustaqil ishlash
  uchun berilgan 15 ta masalani yechish").
- **I BOB:** 3 ta bo'lim; ta'riflar, keltirib chiqarishlar, raqamlangan formulalar, kerak bo'lsa jadval
  va rasm (masalan, asosiy oqimlar jadvali, superpozitsiya rasmi). Darslik va boshqa manbalarga `[1, 3]` havolalar.
- **2.1:** kichik kirish (1–2 jumla: rasmlarda nima ko'rsatilgan), keyin har bir masala:
  - `**N-masala.**` + shart (qo'llanmadagi shartni o'z so'zi bilan, ma'nosini o'zgartirmay);
  - `*Yechish.*` — bosqichma-bosqich, I bobdagi formulalarga `(2) dan` kabi havola bilan;
  - `**Javob:**` — yakuniy natija, birliklari bilan;
  - **har bir masalaga bitta rasm** (grafik/sxema), nomi rasm ostida.
  - Qo'llanma javobi bilan farq chiqsa — `*Izoh.*` bilan sababi (namunadagi 9-masala kabi).
- **2.2:** jadval `№ | Javob | Qo’llanma bilan` — 15 qator, oxirgi ustunda "mos" yoki farq izohi.
  Qo'llanmada javoblar jadvali bo'lsa (to'plam oxirida), solishtirish shu bilan qilinadi.
- **XULOSA:** 1 xatboshi + raqamlangan 5–7 band (nazariy natijalar + masalalar bo'yicha natija).

## 4. Formulalar, rasmlar, jadvallar

- Alohida formulalar `equation` (raqam o'ng chetda), **butun ish bo'yicha ketma-ket (1), (2), ...**;
  havola `(\ref{...})` — matnda "(2) dan", "(3) ga ko’ra". Masala yechimidagi oraliq formulalar raqamsiz
  (`\[ ... \]` yoki matn ichida). Hisoblashlar matn ichida `$...$`.
- Rasm nomi rasm **ostida**, markazda: `Rasm N. Nomi` — butun ish bo'yicha ketma-ket
  (`\figurename{Rasm}`, ajratuvchi nuqta). Masala rasmlarida: `Rasm 7. 6-masala: erkin uyurma`.
- Jadval nomi jadval **ustida**: `Jadval N. Nomi`.
- Rasmlar: matplotlib, 300 dpi, oq fon, rasm ichida sarlavha yo'q; yozuvlar o'zbekcha; eni matn enining
  ~60–75%. Potensial oqim mavzularida: oqim chiziqlari (ψ = const) ko'k, ekvipotensiallar (φ = const)
  qizil uzuq chiziq, legenda pastda; maxsus nuqtalar (turg'unlik nuqtasi va h.k.) belgilanadi.
- Rasm sig'masa keyingi betga o'tadi (`[htbp]`), lekin bet o'rtasida katta bo'sh joy qolmasin.

## 5. Adabiyotlar

- Ro'yxat `[1] Muallif. Nomi. — Shahar: Nashriyot, yil.` ko'rinishida (`thebibliography`), matnda `[1, 2]`.
- 5–8 ta manba. Albatta: amaliy to'plam (`3_mex`) va Xudoynazarov darsligi. Qo'shimcha klassik
  darsliklar (rus/ingliz) — faqat haqiqiyligi tekshirilganlari (umumiy yoriqnoma, 11-bo'lim).
  Xudoynazarov kitobining adabiyotlar ro'yxati (300-bet) qo'shimcha manba tanlash uchun yaxshi boshlanish.
- Har bir manba matnda kamida bir marta havola qilingan bo'lsin.

## 6. Texnik qoidalar

- Kompilyator: **XeLaTeX** (MiKTeX, foydalanuvchi kompyuterida); har kompilyatsiya 2 marta.
- Shrift: `\setmainfont{CMU Serif}`. Kirill harflar ham CMU Serif'da bor.
- Agar `unicode-math` kerak bo'lsa: `\setmathfont{latinmodern-math.otf}` (nomi bilan topilmaydi);
  lekin namunadagidek klassik CM formulalar uchun `unicode-math` shart emas.
- `latexmk` ishlatilmaydi (Perl yo'q).
- Codex sandbox'ida tarmoq yo'q — MiKTeX yangi paketni yuklay olmaydi. Faqat shablondagi paketlar
  ishlatiladi; shablon oldindan (sandbox'dan tashqarida) kompilyatsiya qilinib paketlar o'rnatilgan.
- Overleaf'da ham kompilyatsiya bo'lishi kerak: standart paketlar, nisbiy yo'llar, bo'limlar `\input` bilan.
  (Overleaf'da CMU Serif `cm-unicode` paketi bilan mavjud.)

## 7. Sifat tekshiruvi (har bir tayyor PDF uchun)

1. Kompilyatsiya logida xato (`!`) yo'q; `undefined references`, `Missing character`, `Overfull \hbox`
   (> 5pt) yo'q yoki hisobotda izohlangan.
2. Har bir bet rasm qilib ko'rib chiqiladi: matn chetdan chiqmagan, bo'sh/yarim bo'sh bet yo'q
   (bob oxiridan tashqari), sarlavha bet oxirida yolg'iz qolmagan, rasm nomi ostida, formulalar to'g'ri.
3. Bet soni 16–20; 15 masalaning hammasi yechilgan, har birida rasm va javob; 2.2-jadvalda 15 qator.
4. Har bir masala javobi Python bilan tekshirilgan va qo'llanma javobi (bo'lsa) bilan solishtirilgan.
5. Muqova ma'lumotlari `malumot.md` bilan bir xil; MUNDARIJA bet raqamlari to'g'ri.
6. Adabiyotlar haqiqiy va har biri matnda ishlatilgan.
7. `manba/tex/` alohida papkada mustaqil kompilyatsiya bo'ladi (Overleaf zip uchun).
