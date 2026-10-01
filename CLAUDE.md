# Kurs ishi — to'liq qoidalar ("katta xotira")

Bu repo talabalar uchun kurs ishi tayyorlashning umumiy qoidalari, shabloni va Word yig'uvchi
dasturini saqlaydi. Ish papkasi — bitta yuqoridagi `kurs_ishi/` (u yerdagi kichik `CLAUDE.md` ga qara).

**Muhim:** bu repoga talaba ismlari, matnlari, tayyor fayllar va adabiyotlar yozilmaydi.

## Umumiy talablar

- Hajmi: har bir kurs ishi o'rtacha **25 bet**.
- Har bir kurs ishida **3–5 ta chizma**.
- Mavzuga doir **formulalar** bo'ladi.
- Tafsilotlar quyidagi fayllarda:

| Fayl | Mazmuni | Holati |
|---|---|---|
| `qoidalar/formatlash.md` | hoshiya, shrift, interval, sahifa raqami, sarlavhalar | yo'riqnoma kelgach to'ldiriladi |
| `qoidalar/tuzilma.md` | titul, mundarija, kirish, boblar, xulosa, adabiyotlar, ilovalar | yo'riqnoma kelgach to'ldiriladi |
| `qoidalar/chizmalar.md` | chizma turi, raqamlash, nomlash | yo'riqnoma kelgach to'ldiriladi |
| `qoidalar/formulalar.md` | formula yozish va raqamlash | yo'riqnoma kelgach to'ldiriladi |
| `qoidalar/adabiyotlar.md` | adabiyotlar ro'yxatini rasmiylashtirish | yo'riqnoma kelgach to'ldiriladi |
| `qoidalar/sifat-tekshiruvi.md` | topshirishdan oldingi tekshiruv | tayyor |

## Ish usuli

- Matn `talabalar/familiya-ism/matn/` da bo'limlarga bo'lib yoziladi; .docx har doim shu manbadan
  `dastur/` orqali qayta yig'iladi. Tayyor .docx qo'lda tahrirlanmaydi.
- Formulalar Word'ning o'z formulasi (OMML) sifatida qo'yiladi, rasm sifatida emas.
- Chizmalar kod orqali chiziladi; manba kodi talaba papkasidagi `chizmalar/` da saqlanadi.
- Har bir tayyor fayl `qoidalar/sifat-tekshiruvi.md` bo'yicha tekshiriladi.

## Qoidalarni yangilash

Foydalanuvchi yangi qoida aytsa yoki biror narsani tuzatsa, tegishli `qoidalar/*.md` faylga yoz
va commit qil. Commit xabari qisqa, o'zbek tilida.
