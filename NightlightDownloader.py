"""
Script to download nightlight file data. The data will be downloaded as a zipped file.

Steps to run:

    1) Change the path to the folder to which you want to download the images
    2) Run
"""
import shutil
import urllib.request
import os
import gzip

path = ""

files = ["F101992",
         "F101993",
         "F101994",
         "F121994",
         "F121995",
         "F121996",
         "F121997",
         "F121998",
         "F121999",
         "F141997",
         "F141998",
         "F141999",
         "F142000",
         "F142001",
         "F142002",
         "F142003",
         "F152000",
         "F152001",
         "F152002",
         "F152003",
         "F152004",
         "F152005",
         "F152006",
         "F152007",
         "F162004",
         "F162005",
         "F162006",
         "F162007",
         "F162008",
         "F162009",
         "F182010",
         "F182011",
         "F182012",
         "F182013"]

url = "https://ngdc.noaa.gov/eog/data/web_data/v4composites/"
end = ".v4.tar"
urls = [url + file + end for file in files]

print("Beginning file download with urllib2...")

for url in urls:

    name = url[-14:-7]

    os.chdir(path)

    dir = os.path.join(f"{name}")
    if not os.path.exists(dir):
        os.mkdir(dir)

    urllib.request.urlretrieve(url, path + f"/{name}/{name}.v4.tar")

    os.chdir(path + f"/{name}")

    shutil.unpack_archive(f"{name}.v4.tar",
                          extract_dir=path + f"/{name}")

print("Files successfully downloaded")

#####################################

# Extract the files

os.chdir(path)

folders = [folder for folder in os.listdir() if "F1" in folder]

dir = os.path.join("Images")
if not os.path.exists(dir):
    os.mkdir(dir)

file_types = [".v4b_web.stable_lights.avg_vis.tif.gz",
              ".v4c_web.stable_lights.avg_vis.tif.gz",
              ".v4d_web.stable_lights.avg_vis.tif.gz"]

for folder in folders:
    os.chdir(path + f"/{folder}")
    target_file_comp = ""
    for file in os.listdir():
        for file_type in file_types:
            if file_type in file:
                target_file_comp = file

    target_file = target_file_comp.replace(".gz", "")
    with gzip.open(target_file_comp, 'rb') as f_in:
        with open(target_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    shutil.move(path + f"/{folder}/{target_file}",
                path + f"/Images/{target_file}")

print(
    " Download Successful \nAll files downloaded and extracted to the folder called images in your working directory.")
