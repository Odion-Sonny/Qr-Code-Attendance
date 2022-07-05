from MyQR import myqr
import os

# read student name/id from students.txt
f = open('students.txt','r')
lines = f.read().split("\n")
print(lines)

# encode name/id in QR and generate QR
for _ in range (0,len(lines)):
    data = lines[_]
    version,level,qr = myqr.run(
        str(data),
        level='H',
        version=1,
        picture="Bg.png",
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name = str(lines[_]+'.png'),
        save_dir=os.getcwd()
    )
