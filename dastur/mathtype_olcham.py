#!/usr/bin/env python3
"""MathType'ga aylantirilgan formulalarni 12 pt dan 14 pt ga kattalashtiradi.

MathType "Convert Equations" formulalarni o'zining standart o'lchamida (12 pt) yaratadi, matn esa
14 pt. Bu skript har bir MathType obyektining ko'rinadigan o'lchamini va qatordagi vertikal siljishini
14/12 marta kattalashtiradi (formula vektor rasm bo'lgani uchun sifat buzilmaydi).

Ishlatish:  python3 mathtype_olcham.py kirish.docx chiqish.docx
Diqqat: har bir faylga FAQAT BIR MARTA ishlatiladi (qayta ishlatilsa yana kattalashadi).
Eslatma: formula MathType'da qayta ochib saqlansa, o'sha formula yana 12 pt bo'lib qoladi.
"""
import re, sys, zipfile

K = 14 / 12

def pt(v, u):
    return float(v) * (72 if u == "in" else 1)

def tuzat(xml):
    def sh(m):
        return f'style="width:{pt(m[1], m[2]) * K:.2f}pt;height:{pt(m[3], m[4]) * K:.2f}pt"'
    xml, n = re.subn(r'style="width:([\d.]+)(pt|in);height:([\d.]+)(pt|in)"(?=[^>]*o:ole)', sh, xml)
    pos = lambda m: re.sub(r'<w:position w:val="(-?\d+)"/>',
                           lambda q: f'<w:position w:val="{round(int(q[1]) * K)}"/>', m[0], count=1)
    xml = re.sub(r'<w:r\b(?:(?!</w:r>).)*?<w:object.*?</w:r>', pos, xml, flags=re.S)
    return xml, n

def main(kirish, chiqish):
    with zipfile.ZipFile(kirish) as zi, zipfile.ZipFile(chiqish, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            data = zi.read(item.filename)
            if item.filename == "word/document.xml":
                xml, n = tuzat(data.decode("utf-8"))
                data = xml.encode("utf-8")
                print(f"{n} ta formula kattalashtirildi")
            zo.writestr(item, data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
