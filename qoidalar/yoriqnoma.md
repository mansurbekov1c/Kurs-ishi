# Kurs ishi yozish bo'yicha yo'riqnoma

## 0. Kirish ma'lumotlari

Har bir talaba beradi: **Familiya Ism, guruh, fan, mavzu, rahbar.**

Standart qiymatlar (talaba boshqacha bermasa shular ishlatiladi):

| Maydon | Standart qiymat |
|---|---|
| Fakultet | Fizika-matematika |
| Kafedra | Fizika |
| Yo'nalish | Mexanika va matematik modellashtirish |
| Yil | joriy yil |

Fakultet, kafedra, yo'nalish, guruh va yil muqovada yoziladi (4-bo'lim).

Kurs ishi Urganch davlat universiteti talabasi nomidan, o'zbek tilida (lotin yozuvi), ilmiy
uslubda yoziladi. Matn avvalo `materiallar/adabiyotlar/` dagi manbalarga tayanadi.

## 1. Fayl va hajm

- Format: `.docx` (Word)
- Hajm: muqova bilan **25–28 bet**
- Rasmlar (chizma, diagramma, sxema, grafik, shakl): har bir kurs ishida **3–5 ta**

## 2. Sahifa va shrift

- Qog'oz: A4
- Hoshiyalar: chap 2,5 sm, o'ng 1,5 sm, yuqori 2 sm, past 2 sm
- Shrift: Times New Roman, 14 pt (butun matn)
- Qator oralig'i: 1,5
- Tekislash: ikki tomonlama (eni bo'yicha)
- Xat boshi: 1,25 sm
- Header yo'q
- Sahifa raqami: har bir betda, pastda, markazda; muqovada ko'rinmaydi, lekin sanaladi

## 3. Betlarni to'ldirish (MUHIM)

- Har bir bet oxirigacha matn bilan to'ldiriladi, bet oxirida bo'sh joy qolmaydi.
- Har bir bob (I, II, III, IV) yangi betdan boshlanadi, lekin undan oldingi bet ham
  oxirigacha to'ldirilgan bo'lishi kerak: bobning oxirgi beti to'lguncha matn hajmi moslanadi.
- Rasm sig'may keyingi betga o'tib ketsa va oldingi betda bo'sh joy qolsa, rasm yoki matn
  o'rni almashtiriladi (rasmdan oldin/keyin matn qo'shiladi yoki ko'chiriladi).
- Istisno: muqova, mundarija va oxirgi bet (adabiyotlar ro'yxati).

## 4. Muqova (yuqoridan pastga, hammasi markazda)

1. Sarlavha — bosh harflarda, 14 pt, qalin:
   `O'ZBEKISTON RESPUBLIKASI OLIY TA'LIM, FAN VA INNOVATSIYALAR VAZIRLIGI`
   `ABU RAYHON BERUNIY NOMIDAGI URGANCH DAVLAT UNIVERSITETI [FAKULTET] FAKULTETI [KAFEDRA] KAFEDRASI`
2. Universitet logosi (`shablon/logo.png`)
3. `[Guruh]-guruh [yo'nalish] guruhi talabasi [Familiya Ism]ning "[Mavzu]" mavzusida yozgan`
4. `KURS ISHI` — katta shrift (72 pt), qalin
5. Imzo qatorlari (chapdan, chiziq bilan):
   - `Bajardi:     ____________     [Familiya Ism]`
   - `Tekshirdi:   ____________     [Rahbar]`
   - `Baholash:    ____________`
6. `Urganch-[Yil].` — betning eng pastida

## 5. Tuzilma

```
REJA
I. Kirish
II. Asosiy qism
   2.1. [Birinchi bo'lim nomi]
   2.2. [Ikkinchi bo'lim nomi]
   2.3. [Uchinchi bo'lim nomi]
III. Xulosa
IV. Foydalanilgan adabiyotlar
```

- Sarlavha **REJA** (MUNDARIJA emas); bandlar qarshisida **bet raqamlari va nuqtalar yo'q**.
  _Vaqtinchalik: kurs ishi rahbari tasdiqlagach aniqlashtiriladi. Bet raqamli mundarijaga qaytish
  kerak bo'lsa — `dastur/yigish.py` da `REJA_BET_RAQAMI = True`._
- Bob sarlavhalari (`I. KIRISH` ...): qalin, bosh harflarda, markazda.
- Bo'lim sarlavhalari (`2.1. ...`): qalin, markazda.

## 6. Kirish

Mavzuning dolzarbligi, tarixiy rivojlanishi, amaliy ahamiyati, kurs ishining maqsadi va
vazifalari, qo'llanilgan usullar, ishning tuzilishi.

## 7. Har bir asosiy bo'lim (2.1, 2.2, 2.3)

- Nazariy qism: aniq ta'riflar, tushunchalar va ularning izohi
- 3–5 ta formula
- Kamida 2 ta yechilgan masala:

```
Masala: [shart]
Berilgan: ...
Topish kerak: ...
Yechish: [bosqichma-bosqich, formulalar bilan]
Javob: ...
```

## 8. Formulalar

- Hamma formulalar Word'ning haqiqiy formulasi (OMML), Cambria Math shriftida,
  **Professional** ko'rinishda — daftarga qo'lda qanday yozilsa, shunday ko'rinadi:
  - daraja yuqorida o'ngda: x², v₀² (haqiqiy yuqori indeks)
  - indeks pastda o'ngda: p₅, qⱼ (haqiqiy pastki indeks)
  - kasr — kasr chizig'i bilan (surat ustida, maxraj ostida)
  - ildiz — ildiz belgisi ostida
  - yig'indi, integral — chegaralari bilan; hosila ustidagi nuqta — harf ustida
- Formulani oddiy matn qilib terish (`n = 3N - k`, `x^2`, `a/b`, Unicode `p₅`) taqiqlanadi.
- Alohida qatordagi formula **betning o'rtasida**, raqami **o'ng chetda**: (1), (2), (3) ...
  — butun ish bo'yicha oddiy ketma-ket raqamlanadi.
- Raqam probel bilan emas, tabulyatsiya bilan suriladi (markaziy va o'ng tab).
- Matn ichidagi belgilar ham formula sifatida yoziladi (masalan, "bu yerda m — massa").
- Bir xil formula ikki marta raqamlanmaydi; matnda formulaga havola: "(3) formuladan".

## 9. Rasmlar

- Rasm deganda chizma, diagramma, sxema, grafik, shakl tushuniladi.
- Rasm markazda; nomi rasmning **pastida**, markazda, Times New Roman 12 pt.
- Nom tuzilishi: `[bob raqami].[bob ichidagi tartib raqami]-rasm. [Rasm nomi]`
  (masalan, II bobdagi birinchi rasm: `2.1-rasm. ...`, ikkinchisi: `2.2-rasm. ...`).
  `2.1-rasm.` qismi qalin, nomi oddiy shriftda, oxirida nuqta qo'yilmaydi.
- Rasm ichiga sarlavha yozilmaydi — nomi faqat ostida.
- Rasm va uning nomi bir betda turadi (bo'linmaydi).
- Matnda har bir rasmga havola bo'ladi: "(2.1-rasm)".

## 10. Xulosa

Har bir bo'lim natijasi raqamlangan bandlarda (1, 2, 3, ...), kamida 7 band.

## 11. Foydalanilgan adabiyotlar

- 8–10 ta manba (darslik, monografiya, qo'llanma, maqola).
- Avval foydalanuvchi bergan manbalar (`materiallar/adabiyotlar/`), yetmasa internetdan.
- Faqat haqiqatan mavjud manbalar: internetdan olinganining muallifi, nomi, nashriyoti va yili
  tekshiriladi. To'qib chiqarilgan manba yozilmaydi.
- Ko'rinishi:
  `1. Targ S.M. Nazariy mexanikadan qisqa qo'llanma. — Moskva: Vysshaya shkola, 1986. — 416 b.`

## 12. Til

- O'zbek tilida, lotin yozuvida; o', g' harflari va tutuq belgisi butun ishda bir xil.
- Atamalar butun ishda bir xil (masalan, "golonomik/holonomik" aralashmaydi).
- Ruscha so'zlar (rulevoy, ravnoraspredelenie) o'zbekcha atamaga almashtiriladi.
