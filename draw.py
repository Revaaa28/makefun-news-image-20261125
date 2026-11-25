#!/usr/bin/env python3
"""THE TUESDAY LEDGER - renderer for make.fun news-image-20261125.

Draws the one-image broadsheet of Wednesday 25 November 2026 at 2x
supersampling (2048x2048) and downscales to the committed 1024x1024
entry.png with a Lanczos filter. Local build tool only; the grader
runs main.py, which copies the committed entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

from stories import HEROES, CARDS, ALSO, REGION_NAMES, STATS, TIMELINE, DATE_CHECK, PINS
from cards import CARDS_TEXT
from worldmap import MAP

S = 2                      # supersampling factor
W = 1024 * S
HERE = os.path.dirname(os.path.abspath(__file__))

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

INK = (24, 22, 18)
PAPER = (247, 243, 233)
RULE = (24, 22, 18)
ACCENT = (146, 32, 26)
MUTED = (96, 90, 78)
PANEL = (255, 252, 244)
CHIP_BG = {"REPORTED": (32, 84, 46), "FORECAST": (146, 96, 20), "CLAIM": (120, 40, 90)}


def F(path, size):
    return ImageFont.truetype(path, int(size * S))


def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, text, font, maxw, leading, fill=INK, max_lines=None):
    """x, y, maxw, leading are in final (1024px) units; font is pre-scaled."""
    lines = wrap(d, text, font, maxw * S)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x * S, y * S), ln, font=font, fill=fill)
        y += leading
    return y


def scene(d, x, y, w, h, kind, seed):
    """Small code-drawn illustrated scene inside box (x,y,w,h) at final scale."""
    x, y, w, h = x * S, y * S, w * S, h * S
    skies = {"chartdown": (38, 44, 66), "rocket": (16, 22, 48), "pact": (24, 58, 74),
             "ballot": (52, 40, 70), "flags": (58, 52, 40), "shield": (20, 48, 44),
             "blast": (74, 44, 26), "medic": (30, 62, 52), "boots": (66, 54, 30),
             "cradle": (70, 44, 58), "ship": (22, 52, 72), "chartup": (30, 58, 40),
             "flagsrow": (56, 44, 66), "network": (26, 40, 62), "globe": (40, 50, 66)}
    top = skies.get(kind, (40, 40, 50))
    for i in range(int(h)):
        t = i / max(h - 1, 1)
        c = tuple(int(top[j] + (top[j] * 0.55 + 30) * t) for j in range(3))
        d.line([(x, y + i), (x + w, y + i)], fill=c)
    g = lambda fx, fy: (x + fx * w, y + fy * h)  # fractional point
    white = (240, 238, 228)
    gold = (232, 178, 60)
    red = (216, 84, 60)
    green = (92, 196, 110)
    if kind == "chartdown":
        pts = [g(0.06, 0.25), g(0.3, 0.35), g(0.5, 0.3), g(0.72, 0.62), g(0.94, 0.82)]
        d.line(pts, fill=red, width=3 * S)
        for px, py in pts:
            d.ellipse([px - 3 * S, py - 3 * S, px + 3 * S, py + 3 * S], fill=red)
        d.polygon([g(0.94, 0.82), g(0.86, 0.8), g(0.93, 0.7)], fill=red)
    elif kind == "chartup":
        pts = [g(0.06, 0.8), g(0.3, 0.62), g(0.52, 0.68), g(0.74, 0.38), g(0.94, 0.2)]
        d.line(pts, fill=green, width=3 * S)
        for px, py in pts:
            d.ellipse([px - 3 * S, py - 3 * S, px + 3 * S, py + 3 * S], fill=green)
        d.polygon([g(0.94, 0.2), g(0.85, 0.2), g(0.93, 0.32)], fill=green)
    elif kind == "rocket":
        for i, (fx, fy) in enumerate([(0.15, 0.2), (0.3, 0.6), (0.8, 0.25), (0.65, 0.5), (0.88, 0.65)]):
            px, py = g(fx, fy)
            d.ellipse([px - S, py - S, px + S, py + S], fill=white)
        d.polygon([g(0.5, 0.06), g(0.58, 0.4), g(0.42, 0.4)], fill=white)
        d.rectangle([g(0.42, 0.4), g(0.58, 0.62)], fill=white)
        d.ellipse([g(0.465, 0.2), g(0.535, 0.32)], fill=(60, 120, 200))
        d.polygon([g(0.42, 0.55), g(0.34, 0.72), g(0.44, 0.66)], fill=red)
        d.polygon([g(0.58, 0.55), g(0.66, 0.72), g(0.56, 0.66)], fill=red)
        d.polygon([g(0.46, 0.64), g(0.54, 0.64), g(0.5, 0.92)], fill=gold)
        d.polygon([g(0.475, 0.64), g(0.525, 0.64), g(0.5, 0.8)], fill=(255, 230, 150))
    elif kind == "pact":
        d.ellipse([g(0.08, 0.55), g(0.55, 0.95)], fill=(38, 110, 90))
        d.ellipse([g(0.5, 0.5), g(0.95, 0.92)], fill=(44, 122, 96))
        d.line([g(0.3, 0.12), g(0.3, 0.6)], fill=white, width=2 * S)
        d.polygon([g(0.3, 0.12), g(0.48, 0.2), g(0.3, 0.28)], fill=gold)
        d.line([g(0.72, 0.12), g(0.72, 0.6)], fill=white, width=2 * S)
        d.polygon([g(0.72, 0.12), g(0.9, 0.2), g(0.72, 0.28)], fill=(80, 160, 230))
    elif kind == "ballot":
        d.rectangle([g(0.3, 0.35), g(0.7, 0.85)], fill=white)
        d.rectangle([g(0.38, 0.45), g(0.62, 0.53)], outline=INK, width=2 * S)
        d.line([g(0.41, 0.49), g(0.47, 0.56)], fill=green, width=3 * S)
        d.line([g(0.47, 0.56), g(0.6, 0.42)], fill=green, width=3 * S)
        d.rectangle([g(0.42, 0.18), g(0.58, 0.36)], fill=gold)
    elif kind == "flags":
        for i, fx in enumerate((0.25, 0.5, 0.75)):
            d.line([g(fx, 0.15), g(fx, 0.85)], fill=white, width=2 * S)
            col = [red, gold, green][i]
            d.polygon([g(fx, 0.15), g(fx + 0.16, 0.22), g(fx, 0.3)], fill=col)
    elif kind == "shield":
        d.polygon([g(0.5, 0.08), g(0.78, 0.2), g(0.78, 0.55), g(0.5, 0.92), g(0.22, 0.55), g(0.22, 0.2)],
                  fill=(46, 130, 110), outline=white, width=2 * S)
        d.line([g(0.36, 0.48), g(0.47, 0.6)], fill=white, width=4 * S)
        d.line([g(0.47, 0.6), g(0.66, 0.32)], fill=white, width=4 * S)
        d.line([g(0.1, 0.3), g(0.2, 0.42)], fill=red, width=3 * S)
        d.line([g(0.2, 0.3), g(0.1, 0.42)], fill=red, width=3 * S)
    elif kind == "blast":
        cx, cy = g(0.5, 0.55)
        for r, col in ((0.34, (200, 90, 40)), (0.24, gold), (0.14, (255, 226, 140))):
            d.ellipse([cx - r * w, cy - r * h, cx + r * w, cy + r * h], fill=col)
        d.rectangle([g(0.05, 0.85), g(0.95, 0.92)], fill=(60, 50, 44))
    elif kind == "medic":
        d.rectangle([g(0.42, 0.2), g(0.58, 0.8)], fill=(235, 60, 50))
        d.rectangle([g(0.2, 0.42), g(0.8, 0.58)], fill=(235, 60, 50))
        d.ellipse([g(0.3, 0.12), g(0.7, 0.9)], outline=white, width=3 * S)
    elif kind == "boots":
        for fx in (0.35, 0.62):
            d.rectangle([g(fx, 0.15), g(fx + 0.1, 0.6)], fill=(90, 74, 40))
            d.polygon([g(fx, 0.6), g(fx + 0.2, 0.6), g(fx + 0.2, 0.78), g(fx, 0.78)], fill=(70, 56, 30))
        d.rectangle([g(0.05, 0.85), g(0.95, 0.9)], fill=(120, 100, 55))
    elif kind == "cradle":
        d.arc([g(0.2, 0.25), g(0.8, 0.95)], start=0, end=180, fill=white, width=4 * S)
        d.line([g(0.2, 0.6), g(0.8, 0.6)], fill=white, width=3 * S)
        d.ellipse([g(0.42, 0.3), g(0.58, 0.52)], fill=gold)
        d.arc([g(0.35, 0.35), g(0.65, 0.75)], start=200, end=340, fill=gold, width=3 * S)
    elif kind == "ship":
        d.rectangle([g(0.05, 0.72), g(0.95, 0.8)], fill=(70, 150, 200))
        d.polygon([g(0.15, 0.72), g(0.85, 0.72), g(0.78, 0.55), g(0.22, 0.55)], fill=(200, 70, 50))
        for i in range(4):
            d.rectangle([g(0.3 + i * 0.11, 0.38), g(0.39 + i * 0.11, 0.55)],
                        fill=[gold, green, (80, 160, 230), red][i])
        d.line([g(0.5, 0.12), g(0.5, 0.38)], fill=white, width=2 * S)
    elif kind == "flagsrow":
        for i, fx in enumerate((0.14, 0.32, 0.5, 0.68, 0.86)):
            d.line([g(fx, 0.2), g(fx, 0.85)], fill=white, width=2 * S)
            d.polygon([g(fx, 0.2), g(fx + 0.11, 0.26), g(fx, 0.33)], fill=(235, 120, 30))
        d.rectangle([g(0.05, 0.85), g(0.95, 0.9)], fill=(90, 70, 100))
    elif kind == "network":
        nodes = [(0.2, 0.3), (0.5, 0.18), (0.8, 0.3), (0.35, 0.62), (0.68, 0.6), (0.5, 0.85)]
        for a in range(len(nodes)):
            for b in range(a + 1, len(nodes)):
                if (a + b) % 2 == 0:
                    d.line([g(*nodes[a]), g(*nodes[b])], fill=(120, 170, 220), width=S)
        for fx, fy in nodes:
            px, py = g(fx, fy)
            d.ellipse([px - 4 * S, py - 4 * S, px + 4 * S, py + 4 * S], fill=gold)
    elif kind == "globe":
        cx, cy = g(0.5, 0.5)
        r = 0.36 * w
        d.ellipse([cx - r, cy - r * h / w, cx + r, cy + r * h / w], outline=white, width=2 * S)
        d.ellipse([cx - r * 0.45, cy - r * h / w, cx + r * 0.45, cy + r * h / w], outline=white, width=S)
        d.line([cx - r, cy, cx + r, cy], fill=white, width=S)


def chip(d, x, y, label):
    f = F(SANS_B, 8.5)
    tw = d.textlength(label, font=f)
    d.rounded_rectangle([x * S, y * S, (x + tw / S + 10) * S, (y + 13) * S], radius=3 * S,
                        fill=CHIP_BG.get(label, INK))
    d.text(((x + 5) * S, (y + 1.5) * S), label, font=f, fill=(255, 255, 255))
    return tw / S + 10


def main():
    img = Image.new("RGB", (W, W), PAPER)
    d = ImageDraw.Draw(img)
    total = len(HEROES) + len(CARDS) + len(ALSO)
    counts = {}
    for it in HEROES + CARDS:
        counts[it["region"]] = counts.get(it["region"], 0) + 1
    for _, rg, _ in ALSO:
        counts[rg] = counts.get(rg, 0) + 1

    M = 26  # margin, final px
    CW = 1024 - 2 * M

    def hr(y, thick=2):
        d.rectangle([M * S, y * S, (1024 - M) * S, (y + thick) * S], fill=RULE)

    # ---- top band
    band = f"{total} STORIES · 7 REGIONS · EVERY ONE DATED WEDNESDAY 25 NOVEMBER 2026"
    f = F(SANS_B, 11)
    d.text(((1024 - d.textlength(band, font=f) / S) / 2 * S, 12 * S), band, font=f, fill=ACCENT)
    hr(30, 3)

    # ---- masthead
    f = F(SERIF_B, 63)
    title = "THE TUESDAY LEDGER"
    while d.textlength(title, font=f) > CW * S:
        f = ImageFont.truetype(SERIF_B, f.size - 2)
    d.text(((1024 - d.textlength(title, font=f) / S) / 2 * S, 38 * S), title, font=f, fill=INK)
    hr(112, 1)
    f = F(SERIF, 12.5)
    dl = "Wednesday, the twenty-fifth of November, two thousand and twenty-six"
    d.text(((1024 - d.textlength(dl, font=f) / S) / 2 * S, 117 * S), dl, font=f, fill=INK)
    f = F(SERIF, 11.5)
    strap = "Asia's rout deepens as tariffs loom · Shenzhou-24's first foreign astronaut · Australia's Pacific pact"
    y = 136
    for ln in wrap(d, strap, f, CW * S):
        d.text(((1024 - d.textlength(ln, font=f) / S) / 2 * S, y * S), ln, font=f, fill=MUTED)
        y += 15
    hr(y + 3, 2)

    # ---- stat strip
    y0 = y + 9
    sw = CW / 6
    for i, (num, cap) in enumerate(STATS):
        x = M + i * sw
        if i:
            d.line([(x * S, y0 * S), (x * S, (y0 + 44) * S)], fill=MUTED, width=S)
        f = F(SERIF_B, 17)
        d.text(((x + 6) * S, y0 * S), num, font=f, fill=ACCENT)
        text_block(d, x + 6, y0 + 24, cap, F(SANS, 7.6), sw - 12, 9.5, MUTED, 2)
    hr(y0 + 44, 1)

    # ---- region bar
    y0 += 48
    f = F(SANS_B, 10.5)
    parts = [f"{name} {counts.get(code, 0)}" for code, name in REGION_NAMES]
    line = "   ·   ".join(parts)
    while d.textlength(line, font=f) > CW * S:
        f = ImageFont.truetype(SANS_B, f.size - 1)
    d.text(((1024 - d.textlength(line, font=f) / S) / 2 * S, y0 * S), line, font=f, fill=INK)
    hr(y0 + 17, 2)

    # ---- timeline
    y0 += 23
    f = F(SANS_B, 9.5)
    d.text((M * S, y0 * S), "THE DAY IN UTC", font=f, fill=ACCENT)
    tx = M + d.textlength("THE DAY IN UTC", font=f) / S + 12
    f = F(SANS, 8.8)
    for t, ev in TIMELINE:
        seg = f"{t} {ev}"
        segw = d.textlength(seg, font=f) / S
        if tx + segw > 1024 - M:
            y0 += 13
            tx = M
        d.text((tx * S, y0 * S), seg, font=f, fill=INK)
        tx += segw + 14
    hr(y0 + 16, 1)

    # ---- heroes
    y0 += 22
    hw = (CW - 2 * 12) / 3
    hh = 230
    for i, hz in enumerate(HEROES):
        x = M + i * (hw + 12)
        d.rectangle([x * S, y0 * S, (x + hw) * S, (y0 + hh) * S], fill=PANEL, outline=RULE, width=S)
        scene(d, x + 6, y0 + 6, hw - 12, 84, hz["kind"], i)
        yy = y0 + 96
        f = F(SANS_B, 9)
        d.text(((x + 8) * S, yy * S), f"{hz['num']}. {hz['region_name']}", font=f, fill=ACCENT)
        chip(d, x + hw - 66, yy - 1, hz["chip"])
        yy += 15
        yy = text_block(d, x + 8, yy, hz["headline"], F(SERIF_B, 15), hw - 16, 18, INK, 3)
        yy += 2
        yy = text_block(d, x + 8, yy, hz["summary"], F(SERIF, 9.8), hw - 16, 12.3, INK, 4)
        d.text(((x + 8) * S, (y0 + hh - 14) * S), hz["source"].upper(), font=F(SANS_B, 7.4), fill=MUTED)
    y0 += hh + 8

    # ---- cards 4 x 3
    cw4 = (CW - 3 * 10) / 4
    chh = 76
    for idx, cd in enumerate(CARDS):
        r, c = divmod(idx, 4)
        x = M + c * (cw4 + 10)
        yy0 = y0 + r * (chh + 4)
        d.rectangle([x * S, yy0 * S, (x + cw4) * S, (yy0 + chh) * S], fill=PANEL, outline=RULE, width=S)
        scene(d, x + 5, yy0 + 5, 44, chh - 10, cd["kind"], idx + 3)
        tx = x + 55
        f = F(SANS_B, 8)
        d.text((tx * S, (yy0 + 5) * S), f"{cd['num']}.", font=f, fill=ACCENT)
        tw = d.textlength(f"{cd['num']}.", font=f) / S
        chip(d, tx + tw + 5, yy0 + 3.5, cd["chip"])
        hl, sm = CARDS_TEXT[cd["num"]]
        text_block(d, tx, yy0 + 19, hl, F(SERIF_B, 10.3), cw4 - 60, 12, INK, 2)
        text_block(d, tx, yy0 + 44, sm, F(SERIF, 8.4), cw4 - 60, 9.8, INK, 2)
        d.text((tx * S, (yy0 + chh - 11) * S), cd["source"].upper(), font=F(SANS_B, 6.8), fill=MUTED)
    y0 += 3 * (chh + 4) + 2

    # ---- map + date check
    mh = 86
    d.rectangle([M * S, y0 * S, (M + 596) * S, (y0 + mh) * S], fill=(238, 233, 218), outline=RULE, width=S)
    d.text(((M + 8) * S, (y0 + 4) * S), "WHERE WEDNESDAY HAPPENED — PICTURED STORIES 1-15", font=F(SANS_B, 8.5), fill=ACCENT)
    gx, gy, gw, gh = M + 8, y0 + 18, 580, 62
    cellx, celly = gw / 96, gh / len(MAP)
    for ri, row in enumerate(MAP):
        for ci, ch in enumerate(row):
            if ch == "#":
                px, py = gx + ci * cellx, gy + ri * celly
                d.ellipse([px * S, py * S, (px + cellx * 0.55) * S, (py + celly * 0.62) * S], fill=(150, 142, 122))
    for num, (ci, ri) in PINS.items():
        px, py = gx + ci * cellx + cellx / 2, gy + ri * celly + celly / 2
        d.ellipse([(px - 5.5) * S, (py - 5.5) * S, (px + 5.5) * S, (py + 5.5) * S], fill=ACCENT)
        f = F(SANS_B, 7)
        t = str(num)
        d.text(((px - d.textlength(t, font=f) / S / 2) * S, (py - 3.6) * S), t, font=f, fill=(255, 255, 255))
    dx = M + 608
    dw = 1024 - M - dx
    d.rectangle([dx * S, y0 * S, (1024 - M) * S, (y0 + mh) * S], fill=(250, 240, 226), outline=ACCENT, width=S)
    d.text(((dx + 8) * S, (y0 + 4) * S), "DATE CHECK — LEFT OUT ON PURPOSE", font=F(SANS_B, 8.5), fill=ACCENT)
    yy = y0 + 17
    for item in DATE_CHECK:
        yy = text_block(d, dx + 8, yy, "· " + item, F(SERIF, 8.2), dw - 16, 10, INK, 2) + 1.5
    y0 += mh + 8

    # ---- also
    f = F(SANS_B, 10)
    d.text((M * S, y0 * S), "ALSO ON WEDNESDAY 25 NOVEMBER", font=f, fill=ACCENT)
    hr(y0 + 14, 1)
    y0 += 19
    half = (len(ALSO) + 1) // 2
    colw = (CW - 16) / 2
    for ci, group in enumerate((ALSO[:half], ALSO[half:])):
        x = M + ci * (colw + 16)
        yy = y0
        for num, rg, txt in group:
            yy = text_block(d, x, yy, f"{num}. {txt}", F(SERIF, 8.2), colw, 9.4, INK, 2) + 0.7
    print("also ends at y =", yy)
    y0 = 972

    # ---- footer
    hr(y0, 2)
    f = F(SANS, 8.2)
    foot = ("SOURCES: Reuters · AP · AFP · Xinhua · Yonhap · Al Jazeera · UN News · UN Women · WAM — every figure checked "
            "against the wire text on Wednesday morning, UTC.")
    d.text((M * S, (y0 + 5) * S), foot, font=f, fill=INK)
    foot2 = ("HOW TO READ THE TAGS: REPORTED = the wire reports it happened · CLAIM = one side's assertion, unverified · "
             "FORECAST = scheduled, not yet happened. THE TUESDAY LEDGER · ONE IMAGE, ONE DAY · 25 NOVEMBER 2026")
    for ln in wrap(d, foot2, f, CW * S):
        y0 += 11
        d.text((M * S, (y0 + 5) * S), ln, font=f, fill=MUTED)

    img = img.resize((1024, 1024), Image.LANCZOS)
    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes;", total, "stories;", counts)


if __name__ == "__main__":
    main()
