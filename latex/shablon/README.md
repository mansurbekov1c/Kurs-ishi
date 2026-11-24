# LaTeX mustaqil ish shabloni

Bu papka muqova, mundarija, ikki bob, xulosa va adabiyotlar tuzilmasini beradi.
Matn, ikki masala va bibliografik maydonlar — **to’ldirgich**, tayyor talaba ishi
emas. Yakuniy ishda yo’riqnomadagi 15 ta masala, har biriga alohida rasm,
5–8 ta tekshirilgan manba va 16–20 bet talablari bajariladi.

1. Papkani **butunligicha** talabaning `manba/tex/` papkasiga nusxalang.
   `asosiy.tex` faylini `main.tex` deb nomlang; boshqa yo’llarni o’zgartirmang.
2. `malumot.tex` ichidagi `\Talaba`, `\Guruh`, `\Yonalish`, `\Fan`, `\Mavzu`,
   `\Rahbar`, `\Fakultet`, `\Kafedra`, `\Yil` makroslarini to’ldiring.
   Fakultet va kafedraga `FAKULTETI`/`KAFEDRASI` so’zlarini qo’shmang.
   Yil sukut bo’yicha kompilyatsiya yilidir; zarur bo’lsa aniq yil yozing.
   LaTeX maxsus belgilarini ekranlang: masalan, `\&`, `\%`, `\_`.
3. `bolimlar/*.tex` ichidagi to’ldirgichlarni almashtiring. Bobni
   `\bob{BOSH HARFLARDAGI NOM}`, bo’limni `\subsection{Nomi}` bilan kiriting.
   Formula uchun `equation`, havola uchun `\eqref{eq:...}` ishlating.
   Yangi rasm/jadvalga takrorlanmaydigan `\label` bering; rasm `\caption`i
   tasvirdan keyin, jadvalniki `tabular`dan oldin yoziladi.
4. `rasmlar/namuna.png`ni o’z chizmangiz bilan almashtiring. Namuna grafigini
   qayta yaratish: `python rasmlar/namuna.py` (matplotlib kerak).
   Kod ishga tushirilgan papkadan qat’i nazar PNGni o’z yoniga yozadi.
   Shablondagi uchta rasm bir xil to’ldirgichni ishlatadi.
5. `05_adabiyotlar.tex`dagi maydonlarni haqiqiy bibliografik ma’lumotlar bilan
   almashtiring; mos `\cite{...}` havolalarini matnda saqlang.
   `Лойцянский` yozuvi kirill shriftini tekshirish uchun berilgan,
   tayyor bibliografik yozuv hisoblanmaydi.

Shu papkada kompilyatsiya (havolalar va mundarija uchun ikki marta):

```powershell
xelatex -interaction=nonstopmode -halt-on-error asosiy.tex
xelatex -interaction=nonstopmode -halt-on-error asosiy.tex
```

Talaba nusxasida buyruqlardagi `asosiy.tex` o’rniga `main.tex` yozing.
`xelatex` PATH’da bo’lmasa, PowerShell’da quyidagi ko’rinishni ikki marta bajaring:

```powershell
& "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64\xelatex.exe" -interaction=nonstopmode -halt-on-error asosiy.tex
```

Log tekshiruvi (talaba nusxasida `main.log`):

```powershell
Select-String -Path asosiy.log -Pattern '^!|Missing character|undefined|Overfull'
```

Yetishmagan paket/shrift bo’lsa, xabardagi nomini qayd eting; oflayn muhitda
avtomatik o’rnatishga urinmang. Shablon `geometry`, `fontspec`, `setspace`,
`indentfirst`, `amsmath`, `graphicx`, `caption`, `ulem` standart paketlarini
ishlatadi. CMU Serif `cm-unicode` to’plamidagi `cmunrm.otf`, `cmunbx.otf`,
`cmunti.otf`, `cmunbi.otf` fayl nomlari orqali ulanadi.

Overleaf’da yangi loyiha ochib, `manba/tex/` **ichidagi barcha manba fayllarini**
papka tuzilishi bilan yuklang (yoki shu fayllardan ZIP tayyorlang). Asosiy hujjat
sifatida `main.tex`, kompilyator sifatida **XeLaTeX** tanlang. PNG tayyor bo’lgani
uchun Overleaf’da Pythonni ishga tushirish shart emas; repo yoki logoga havola yo’q.

PDFning barcha betlarini tekshiring: muqova raqamsiz, mundarija 2-betda;
o’zbekcha va kirill harflar to’liq; formulalar va rasm/jadval raqamlari uzluksiz;
mundarija havolalari to’g’ri. Muqovadagi uzun maydonlar sig’ishini ham ko’ring.
Topshirishdan oldin kompilyatsiya yordamchi fayllarini (`.aux`, `.log`, `.toc`,
`.out`, `.pdf`) manba papkasidan olib tashlang.
