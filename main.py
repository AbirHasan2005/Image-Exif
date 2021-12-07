# (c) @AbirHasan2005

import os
import csv
from core.exif import Exif


def main():
    image_path = input("\nEnter image path: ")
    option = input("\n[1] Get Exif Data\n[2] Destroy Exif Data\n\nChoose an option: ")
    exif = Exif()
    if option == 1:
        exif_data = exif.extarct_data(image_path)
        _csv_file = "exif_data.csv"
        if os.path.exists(_csv_file):
            print(f"Deleting old '{_csv_file}' ...")
            os.remove(_csv_file)
        with open(_csv_file, "a", newline="") as f:
            csv_writer = csv.writer(f)
            for i in exif_data.items():
                csv_writer.writerow(i)
        print(f"Data saved in '{_csv_file}' ...")
    elif option == 2:
        exif.remove_data(image_path)
    else:
        print("\n\n")
        main()


if __name__ == "__main__":
    main()
