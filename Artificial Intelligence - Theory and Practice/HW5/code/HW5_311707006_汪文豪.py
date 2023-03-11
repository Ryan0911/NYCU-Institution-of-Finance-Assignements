import numpy as np
from PIL import Image
x1 = 159
y1 = 56
x2 = 388
y2 = 81
x3 = 159
y3 = 396
x4 = 387
y4 = 380

p1 = 0
q1 = 0
p2 = 873
q2 = 0
p3 = 0
q3 = 1107
p4 = 873
q4 = 1107
A = np.zeros((8, 8))
b = np.zeros((8, 1))
A[0, :] = [x1, y1, 1, 0, 0, 0, -p1*x1, -p1*y1]
A[1, :] = [x2, y2, 1, 0, 0, 0, -p2*x2, -p2*y2]
A[2, :] = [x3, y3, 1, 0, 0, 0, -p3*x3, -p3*y3]
A[3, :] = [x4, y4, 1, 0, 0, 0, -p4*x4, -p4*y4]
A[4, :] = [0, 0, 0, x1, y1, 1, -q1*x1, -q1*y1]
A[5, :] = [0, 0, 0, x2, y2, 1, -q2*x2, -q2*y2]
A[6, :] = [0, 0, 0, x3, y3, 1, -q3*x3, -q3*y3]
A[7, :] = [0, 0, 0, x4, y4, 1, -q4*x4, -q4*y4]
b[:, 0] = [p1, p2, p3, p4, q1, q2, q3, q4]
x = np.linalg.lstsq(A, b)[0]
H = np.zeros((3, 3))
H[0, 0] = x[0]
H[0, 1] = x[1]
H[0, 2] = x[2]
H[1, 0] = x[3]
H[1, 1] = x[4]
H[1, 2] = x[5]
H[2, 0] = x[6]
H[2, 1] = x[7]
H[2, 2] = 1
BG = Image.open('photo1.jpg')
BG_data = np.asarray(BG).copy()
I = Image.open('Myphoto.jpg')
data = np.asarray(I)

[BGH, BGW, t] = BG_data.shape
[IH, IW, t] = data.shape
xy1 = np.ones((3, 1))
pq1 = np.ones((3, 1))

for h in range(BGH):
    for w in range(BGW):
        xy1[0] = w
        xy1[1] = h
        pq1 = np.dot(H, xy1)
        p = int(pq1[0][0]/pq1[2][0])
        q = int(pq1[1][0]/pq1[2][0])
        if(p >= 0 and p < IW and q >= 0 and q < IH):
            BG_data[h, w, :] = data[q, p, :]
I2 = Image.fromarray(BG_data)
I2.show()
I2.save("311707006_汪文豪_HW5.jpg")
