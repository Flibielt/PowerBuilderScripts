print("RGB: ", end="")
rgb = input()
if rgb.endswith(","):
    rgb = rgb[:len(rgb) - 1]
color = rgb.split(", ")
r = int(color[0])
g = int(color[1])
b = int(color[2])

pbColor = 65536 * b + 256 * g + r
print("PowerBuilder color code: " + str(pbColor))
