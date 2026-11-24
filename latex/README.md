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
3. Mavzuni amaliy to'plamdagi (`3_mex (1).pdf`) mavzulardan biriga bog'la — ro'yxat va bet raqamlari
   `adabiyotlar-royxati.md` da. Mos mavzu topilmasa, foydalanuvchidan so'ra (15 masala shu yerdan olinadi).
   Adabiyotlarni `latex/materiallar/adabiyotlar-royxati.md` dan tanla. "Tekshirilmagan" bo'lsa —
   PDF mundarijasini o'qib ro'yxatni to'ldir. Papkada yo'q kitobni bor deb atama.
4. Bo'lim nomlari berilmagan bo'lsa taklif qil (topshiriqqa yoz, tasdiq kutib turma).
5. `Kurs-ishi/latex/topshiriq-andoza.md` bo'yicha `latex/talabalar/N.Familiya_Ism/topshiriq.md` ni yoz.
6. Codex'ni ishga tushir (pastda), tugashini kut, natijani tekshir.

### Codex buyrug'i (`kurs_ishi` papkasida — `latex/` da EMAS)

```
codex exec -m gpt-6.1-sol -c model_reasoning_effort=high -c windows.sandbox=unelevated --sandbox workspace-write --add-dir "C:\Users\abdul\AppData\Roaming\MiKTeX" --add-dir "C:\Users\abdul\AppData\Local\MiKTeX" --skip-git-repo-check -o latex/talabalar/N.Familiya_Ism/manba/codex-oxirgi-xabar.txt "Kurs-ishi/latex/codex.md ni to'liq o'qi (kurs_ishi/AGENTS.md bu vazifaga tegishli emas), keyin latex/talabalar/N.Familiya_Ism/topshiriq.md dagi vazifani unga ko'ra oxirigacha bajar."
```

- Nega `kurs_ishi` da: Codex'ning odatiy (elevated) Windows sandbox'i ish papkasidan tashqarini o'qiy olmadi
  (2026-11-24); qoidalar `Kurs-ishi/` da, adabiyotlar `latex/materiallar/` da — hammasi `kurs_ishi` ichida.
- **`-c windows.sandbox=unelevated` va ikkala `--add-dir` SHART** (2026-11-24 sinovdan o'tgan). Odatiy sandbox
  buyruqlarni alohida `CodexSandboxOffline` foydalanuvchisi nomidan ishlatadi; MiKTeX sozlamalari esa
  foydalanuvchining reestrida (HKCU) — sandbox'da `xelatex` "fresh TeX installation"/"Access is denied" bilan
  to'xtaydi. Unelevated rejim shu foydalanuvchi nomidan cheklangan huquq bilan ishlaydi; `--add-dir` MiKTeX'ga
  log va keshlarini yozishga ruxsat beradi. Windows ACL'ni o'zgartirish kerak emas (sinab ko'rilgan, foyda bermadi).
- Claude'ning shelli MiKTeX o'rnatilishidan oldin ochilgan bo'lsa, PATH'ga qo'sh:
  `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64`.
- Internet manbalari uchun: `-c sandbox_workspace_write.network_access=true`.

## Codex tugagach

1. `manba/hisobot.md` ni o'qi; `Familiya_Ism.pdf` va `Familiya_Ism_overleaf.zip` tepada, qolgani `manba/` da
   ekanini tekshir; `manba/tekshiruv/` tozalangan; `Kurs-ishi/` ga hech narsa tushmagan
   (`git --no-optional-locks status`).
2. PDF betlarini rasm qilib o'zing ko'r (`yoriqnoma.md`, 7-bo'lim) — Codex'ning "o'tdi" degani yetarli emas.
3. Xato bo'lsa `tuzatish.md` yoz va Codex'ni qayta ishga tushir (oxirgi gap: "...tuzatish.md dagi tuzatishni bajar").

## Namuna kelganda (bir martalik ish — 2026-11-24 bajarildi, yangi namuna kelsa takrorlanadi)

1. Namunani (`latex/materiallar/namuna/`) o'qi: muqova, tuzilma, shrift, hoshiya, raqamlash, adabiyotlar shakli.
2. Farqlarni `Kurs-ishi/latex/yoriqnoma.md` ga yoz (0-bo'limdagi ochiq savollar).
3. `shablon/asosiy.tex` ni yasat (Codex) va sandbox'dan TASHQARIDA bir marta kompilyatsiya qil —
   MiKTeX kerakli paketlarni shunda yuklab oladi.
4. Commit qil.
