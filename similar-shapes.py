big_shape_length = float(input("Side: "))
small_shape_length = float(input("Side: "))

scale_factor = small_shape_length / big_shape_length

if scale_factor < 1:
    scale_factor = big_shape_length / small_shape_length

print(scale_factor)

if (prompt := input("LSF, ASF, VSF: ").lower()) in ("lsf", "l"):
    index = 1
elif prompt in ("asf", "a"):
    index = 2
elif prompt in ("vsf", "v"):
    index = 3

scale_factor = scale_factor ** (1 / index)

side = float(input("Enlarged Side: "))

if (prompt := input("LSF, ASF, VSF: ").lower()) in ("lsf", "l"):
    index = 1
elif prompt in ("asf", "a"):
    index = 2
elif prompt in ("vsf", "v"):
    index = 3

if input("Do you want to scale up or down? (up/down): ").lower() in ("up", "u"):
    print(f"{side * scale_factor ** index}")
else:
    print(f"{side / scale_factor ** index}")
