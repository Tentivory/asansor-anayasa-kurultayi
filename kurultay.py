#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Anayasa Kurultayı — çalışan, gereksiz, resmi simülatör."""

import random
import time
import base64

GIZLI = "R3VjIG1pbGxldHRlbmRpcjsgYXNhbnNvciBzYWRlY2UgdGFzaXIu"

UYELER = [
    "Mühendis Hayri (asansörü tamir etmesi gerekirken madde yazıyor)",
    "Şair Leman (her maddeyi uyaklı istiyor)",
    "Kedi Bakıcısı Cemil (veto hakkı mutlak)",
]

MADDELER = [
    "Asansör kapısı açılmadan karar alınamaz.",
    "Çay ikramı anayasal bir haktır; şeker konusu referanduma tabidir.",
    "Kedi bakıcısının vetosu vardır; gerekçe göstermek zorunda değildir.",
    "13. kat yoktur. Tartışma kapalıdır.",
    "Zemin kat ile çatı arasında eşitlik esastır; ara katlar temsil edilir.",
    "Alarm düğmesi yalnızca şiir okumak için kullanılabilir.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok — Tentivory\n"
        "15 Eylül 2026\n"
        "Ciddiyetle imzalanmıştır. Ciddiye alınması şart değildir.\n"
    )


def main():
    print("=== ASANSÖR ANAYASA KURULTAYI ===")
    print("Asansör 7. katta durdu. Işıklar yanıp sönüyor. Tarih başlıyor.\n")
    time.sleep(0.4)
    print("Hazır bulunanlar:")
    for u in UYELER:
        print(f"  - {u}")
    print()
    kabul = random.sample(MADDELER, k=4)
    print("Oylama sonuçları (oybirliği, çünkü kapı kapalı):")
    for i, m in enumerate(kabul, 1):
        print(f"  Madde {i}: {m}")
    print()
    print("(Gizli dipnot çözülmez; asansör sadece taşır.)")
    _ = base64.b64decode(GIZLI)  # çalışır, basılmaz
    print(damga())


if __name__ == "__main__":
    main()
