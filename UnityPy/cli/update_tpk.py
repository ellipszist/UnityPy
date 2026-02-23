import os
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

from UnityPy.tools.TpkClassGenerator import generate_classes

URL = "https://nightly.link/AssetRipper/Tpk/workflows/type_tree_tpk/master/uncompressed_file.zip"
RESOURCE_PATH = os.path.join(os.path.dirname(__file__), "..", "resources")


def update_tpk():
    print("Updating TPK file...")
    print("\tDownloading...")
    with urlopen(URL) as response:
        zip_data = response.read()
    print("\tExtracting...")
    with ZipFile(BytesIO(zip_data)) as zip_file:
        zip_file.extract("uncompressed.tpk", path=RESOURCE_PATH)
    print("\tGenerating classes...")
    generate_classes()
    print("\tDone.")


__all__ = ["update_tpk"]
