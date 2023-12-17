import os
from urllib.request import urlretrieve
import pandas

# TODO: Write codes as Assigned.
# ? Don't forget to add citation.

# TODO: Initialize Class
class Main():
    def __init__(self):
        # FEATURES: module detection
        # ? Added module detection capability.
        
        try:
            self.setCurrentDir()
        except ModuleNotFoundError:
            print

# DONE: Navigate to current directory
    def setCurrentDir(self):
        path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(path)

# TODO: Fetch Data
    def fetch(self, url):
        # * src: https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve
        # * src: https://realpython.com/python-download-file-from-url/#facilitating-file-downloads-with-python
        
        # ? Further Reading
        # ? src: https://urllib3.readthedocs.io/en/stable/
        # ? src: https://requests.readthedocs.io/en/latest/
        # ? src: https://docs.aiohttp.org/en/stable/
        print

# TODO: Read Data using numpy

# TODO: Manipulated it

# TODO: 1.
# ? 1. Mean of monetary base of all February in Leap year.

# TODO: 2.
# ? 2. means for each year of 'Net Claims on Central Government'
# * Pandas Series
# * 1981 - 1990

# TODO: 3.
# ? 3. List of net loss continuously for 3 months
# * 1991 - 2005

# TODO: 4.
# ? 4. List of 'Claims on Financial Institutions' is greater than 583757 for at least 3 month, In 6 month ranges
# * 2000 - 2005
# * 583757

# TODO: 5.
# ? 5. Tables of data, for min, mean, and max, of 'Other Liabilities to Financial Institutions' and 'Other Items (net)' for all year, based on each month.
# * 2-Ordered Pandas Data Frame
# * In this Form:
# * 'Other Liabilities to Financial Institutions': min, mean, max
# * 'Other Items (net)': min, mean, max

if __name__ == "__main__":
    main = Main()
