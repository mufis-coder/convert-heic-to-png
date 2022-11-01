from PIL import Image
import os
import pillow_heif

SourceFolder = "D:/Gambar/Teman/#04 Kuliah/Indekos x Ghisna/2022-10-31-Semhas Ghisna"
TargetFolder = "D:/Gambar/Teman/#04 Kuliah/Indekos x Ghisna/2022-10-31-Semhas Ghisna/png"

count = 0
for file in os.listdir(SourceFolder):
    if(".HEIC" in file):
        print(file)
        heif_file = pillow_heif.read_heif(SourceFolder+"/"+file)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",

        )
        count += 1
        image.save(TargetFolder+"/img_"+str(count)+".png", format("png"))
