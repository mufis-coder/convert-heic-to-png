from PIL import Image
import os
import pillow_heif
from tqdm import tqdm
import time
import concurrent.futures
from more_itertools import grouper

# for dataframe, sheet in tqdm(zip(dfList, sheetList), total=len(dfList)):

SourceFolder = "D:/Code/Mandiri/Project-root/convert-heic-png/data"
TargetFolder = "D:/Code/Mandiri/Project-root/convert-heic-png/"

start = time.time()


def convert_heic_png(files, global_count):
    files = list(filter(lambda item: item is not None, files))
    
    count = 0
    for file in tqdm(files, total=len(files)):
        if(".HEIC" in file):
            heif_file = pillow_heif.read_heif(SourceFolder+"/"+file)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )
            count += 1
            image.save(TargetFolder+"/thread_" + str(global_count) +
                       "img_"+str(count)+".png", format("png"))


count = 0

if __name__ == '__main__':
    files = os.listdir(SourceFolder)

    # batching
    num_batch = 2
    batchs = [group for group in grouper(num_batch, files)]

    # multiprocess
    # executor = concurrent.futures.ProcessPoolExecutor(max_workers=10)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    futures = [executor.submit(convert_heic_png, batchs[i], i)
               for i in range(0, len(batchs))]
    concurrent.futures.wait(futures)

    end = time.time()
    print(f"Total waktu: {(end - start)}")
