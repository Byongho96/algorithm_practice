w, h = map(int, input().split())
si, sj = map(int, input().split())
T = int(input())

ei_s, ei_r = divmod(si + T, w)
ej_s, ej_r = divmod(sj + T, h)

ei, ej = -1, -1
if ei_s % 2:
    ei = w - ei_r
else:
    ei = ei_r

if ej_s % 2:
    ej = h - ej_r
else:
    ej = ej_r

print(ei, ej)
