from main import rainbow_cycle, color_shift, alternate, quad_alternate, dash, gradual_fill, strobe, meet, breathe, all_random

modes = [rainbow_cycle, color_shift, alternate, quad_alternate, dash, gradual_fill, strobe, meet, breathe, all_random]
total = 0
for m in modes:
    total += len(m.styles())
print(f"Total: {total}")