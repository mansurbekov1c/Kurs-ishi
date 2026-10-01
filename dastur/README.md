# Dastur — Word (.docx) yig'uvchi

`yigish.py` talaba papkasidagi manba matn va chizmalardan tayyor `.docx` ni yig'adi.

```
python3 Kurs-ishi/dastur/yigish.py talabalar/N.Familiya_Ism          # to'liq: docx + PDF tekshiruvi
python3 Kurs-ishi/dastur/yigish.py talabalar/N.Familiya_Ism --tez    # faqat docx
```

Kerak: python-docx, lxml, pdfplumber, pandoc (formulalar uchun), LibreOffice (`soffice`, PDF tekshiruvi uchun).

Nima qiladi:
- `manba/malumot.md` dagi anketa jadvalidan muqovani to'ldiradi (yozilmagan maydonlar — standart qiymatlar);
- `manba/matn/*.md` fayllarini nom tartibida o'qiydi;
- formulalarni pandoc orqali Word formulasiga (OMML, Cambria Math, 14 pt) aylantiradi, keshni
  `manba/tekshiruv/formulalar_kesh.json` da saqlaydi;
- LibreOffice bilan PDF qilib, mundarija sahifa raqamlarini va muqova pastki bo'shlig'ini avtomatik
  moslaydi (`manba/tekshiruv/mundarija.json`), har bir bet oxiridagi bo'sh joyni chiqaradi
  (>30 pt — bet to'lmagan).

## Matn belgilash (`manba/matn/*.md`)

| Yozuv | Natija |
|---|---|
| `# I. Kirish` | bob sarlavhasi (yangi betdan, bosh harflarda, markazda) |
| `## 2.1. Nomi` | bo'lim sarlavhasi (qalin, markazda) |
| oddiy qator | xatboshi (1,25 sm chekinish bilan); bitta xatboshi = bitta qator |
| `\| matn` | chekinishsiz xatboshi (adabiyotlar ro'yxati uchun) |
| `$...$` | matn ichidagi formula (LaTeX) |
| `$$ ... $$ {#nom}` | alohida qatordagi formula: markazda, raqami o'ng chetda; `{#nom}` ixtiyoriy |
| `@eq:nom` | formula raqamiga havola, masalan `(@eq:nom) formuladan` |
| `!rasm nom \| fayl.png \| eni_sm \| Rasm nomi` | rasm (`manba/chizmalar/` dan) va ostida `N.M-rasm. Nomi` |
| `@rasm:nom` | rasm raqami, masalan `(@rasm:nom-rasm)` |
| `**qalin**`, `*kursiv*` | shrift |
| `% izoh` | e'tiborga olinmaydi |

Tutuq belgilari avtomatik bir xil qilinadi: `o'`, `g'` → `o‘`, `g‘`; qolgan `'` → `’`; `"..."` → `“...”`.

## Eslatma: LibreOffice va Word farqi

LibreOffice formulalarni 12 pt da chizadi, Word esa 14 pt (Cambria Math) da. Shuning uchun formulali
betlarda PDF hisobotidagi bo'sh joy Word'dagidan biroz farq qilishi mumkin (sinovda farq bob oxirida
~120 pt, rasmlar esa bir xil betlarga tushdi). Yakuniy tekshiruvni foydalanuvchi o'zi Word'da qiladi.
