# LaTeX bo'limi — Claude uchun ish tartibi

Foydalanuvchi yangi chatda "LaTeX" desa (yoki LaTeX ishi uchun talaba bersa) — shu tartib ishlaydi.
Word kurs ishlari tartibi (`kurs_ishi/CLAUDE.md`) bilan bir xil, faqat papkalar va natija boshqa.

| Nima | Qayerda |
|---|---|
| Ish papkasi (GitHub'ga ketmaydi) | `kurs_ishi/latex/` |
| Adabiyotlar, namuna | `latex/materiallar/adabiyotlar/`, `latex/materiallar/namuna/` |
| Kitoblar ro'yxati | `latex/materiallar/adabiyotlar-royxati.md` |
| Talabalar | `latex/talabalar/N.Familiya_Ism/` (raqamlash Word talabalaridan alohida, 1 dan) |
| Qoidalar (repo) | `Kurs-ishi/latex/yoriqnoma.md` + umumiy `Kurs-ishi/qoidalar/yoriqnoma.md` |
| Codex ko'rsatmasi (repo) | `Kurs-ishi/latex/codex.md` (`latex/AGENTS.md` unga yo'naltiradi) |
| Topshiriq andozasi (repo) | `Kurs-ishi/latex/topshiriq-andoza.md` |
| LaTeX shablon (repo) | `Kurs-ishi/latex/shablon/asosiy.tex` (namunadan yasaladi) |

## Yangi chatda o'qish

`kurs_ishi/CLAUDE.md` → shu fayl → `latex/yoriqnoma.md` → umumiy `yoriqnoma.md` → `codex.md` →
`latex/materiallar/adabiyotlar-royxati.md`.

## Yangi talaba

1. Anketani tekshir (Familiya Ism, guruh, fan, mavzu, rahbar; `kurs_ishi/talaba-anketa.md`); yetishmasa so'ra.
2. `latex/talabalar/N.Familiya_Ism/manba/` ni yarat (N = `latex/talabalar/` dagi eng katta raqam + 1),
   `manba/malumot.md` ga anketani jadval qilib yoz.
3. Adabiyotlarni `latex/materiallar/adabiyotlar-royxati.md` dan tanla. "Tekshirilmagan" bo'lsa —
   PDF mundarijasini o'qib ro'yxatni to'ldir. Papkada yo'q kitobni bor deb atama.
4. Bo'lim nomlari berilmagan bo'lsa taklif qil (topshiriqqa yoz, tasdiq kutib turma).
5. `Kurs-ishi/latex/topshiriq-andoza.md` bo'yicha `latex/talabalar/N.Familiya_Ism/topshiriq.md` ni yoz.
6. Codex'ni ishga tushir (pastda), tugashini kut, natijani tekshir.

### Codex buyrug'i (`kurs_ishi/latex` papkasida)

```
codex exec -m gpt-6.1-sol -c model_reasoning_effort=high --sandbox workspace-write --skip-git-repo-check -o talabalar/N.Familiya_Ism/manba/codex-oxirgi-xabar.txt "AGENTS.md ni to'liq o'qi, keyin talabalar/N.Familiya_Ism/topshiriq.md dagi vazifani unga ko'ra oxirigacha bajar."
```

- Codex `latex/` papkasida ishga tushadi: sandbox faqat shu papkaga yozishga ruxsat beradi, `../Kurs-ishi`
  va Word bo'limiga yozolmaydi.
- Claude'ning shelli MiKTeX o'rnatilishidan oldin ochilgan bo'lsa, PATH'ga qo'sh:
  `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64`.
- Internet manbalari uchun: `-c sandbox_workspace_write.network_access=true`.

## Codex tugagach

1. `manba/hisobot.md` ni o'qi; `Familiya_Ism.pdf` va `Familiya_Ism_overleaf.zip` tepada, qolgani `manba/` da
   ekanini tekshir; `manba/tekshiruv/` tozalangan; `Kurs-ishi/` ga hech narsa tushmagan
   (`git --no-optional-locks status`).
2. PDF betlarini rasm qilib o'zing ko'r (`yoriqnoma.md`, 3-bo'lim) — Codex'ning "o'tdi" degani yetarli emas.
3. Xato bo'lsa `tuzatish.md` yoz va Codex'ni qayta ishga tushir (oxirgi gap: "...tuzatish.md dagi tuzatishni bajar").

## Namuna kelganda (bir martalik ish)

1. Namunani (`latex/materiallar/namuna/`) o'qi: muqova, tuzilma, shrift, hoshiya, raqamlash, adabiyotlar shakli.
2. Farqlarni `Kurs-ishi/latex/yoriqnoma.md` ga yoz (0-bo'limdagi ochiq savollar).
3. `shablon/asosiy.tex` ni yasat (Codex) va sandbox'dan TASHQARIDA bir marta kompilyatsiya qil —
   MiKTeX kerakli paketlarni shunda yuklab oladi.
4. Commit qil.
