# (c) @AbirHasan2005

import os
import csv
from core.exif import Exif
from core.configs import (
    Config,
    Colors
)


def main():
    Configs.banner()
    image_path = str(input(Configs.ENTER_IMAGE_PATH))
    option = str(input(Configs.CHOOSE_FROM_MENU))
    exif = Exif()
    if option in ["1", "01"]:
        exif_data = exif.extract_data(image_path)
        if not exif_data:
            print(f"{Colors.RED___}No Exif data found in '{Colors.YELLOW}{image_path}{Colors.RED___}'")
            print("\n\n")
            main()
        _csv_file = "exif_data.csv"
        if os.path.exists(_csv_file):
            print(f"{Colors.GREEN_}Deleting old '{Colors.YELLOW}{_csv_file}{Colors.GREEN_}' ...")
            os.remove(_csv_file)
        with open(_csv_file, "a", newline="") as f:
            csv_writer = csv.writer(f)
            for i in exif_data.items():
                csv_writer.writerow(i)
        print(f"{Colors.GREEN_}Data saved in '{Colors.YELLOW}{_csv_file}{Colors.GREEN_}' ...")
    elif option in ["2", "02"]:
        exif.remove_data(image_path)
    elif option in ["0", "00"]
    else:
        main()


if __name__ == "__main__":
    main()
