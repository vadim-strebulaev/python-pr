from vpython import sphere, box, color, vector, rate

# Create a sphere with a red color
s = sphere(pos=vector(-1, 0, 0), radius=1, color=color.red)

# Create a blue cube
b = box(pos=vector(1, 0, 0), size=vector(1, 1, 1), color=color.blue)

# Create a loop that rotates the sphere and cube around the y-axis
while True:
    rate(60)
    s.rotate(angle=0.01, axis=vector(0, 1, 0))
    b.rotate(angle=0.01, axis=vector(0, 1, 0))