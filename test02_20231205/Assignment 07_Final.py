import os
import numpy as np
from urllib.request import urlretrieve

# TODO: Write codes as Assigned.
# ? Don't forget to add citation.

url = "https://app.bot.or.th/BTWS_STAT/statistics/DownloadFile.aspx?file=EC_MB_001_ENG_ALL.CSV"

# TODO: Initialize Class
class Main():
    def __init__(self):
        # FEATURES: module detection
        # ? Added module detection capability.
        # ? Implement All Library check at initialize stage
        
        self.setCurrentDir()
        self.fetch(url)
        self.pdInit()
        self._1()

# DONE: Navigate to current directory
    def setCurrentDir(self):
        path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(path)

# DONE: Fetch Data
    def fetch(self, url):
        # * src: https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve
        # * src: https://realpython.com/python-download-file-from-url/#facilitating-file-downloads-with-python
        
        # ? Further Reading
        # ? src: https://urllib3.readthedocs.io/en/stable/
        # ? src: https://requests.readthedocs.io/en/latest/
        # ? src: https://docs.aiohttp.org/en/stable/
        
        self.fileName, res = urlretrieve(url, filename='./EC_MB_001_ENG_ALL.CSV')
        self.fileName = './' + self.fileName
        
        # TODO: Added options for keeping file or not.

# DONE: Read Data using numpy
    def pdInit(self):
        try:
            import pandas as pd
            
            # * src: https://pandas.pydata.org/docs/user_guide/io.html#parsing-options
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose
            self.data = pd.read_csv(self.fileName, header=5, index_col=0).transpose()

        except ModuleNotFoundError:
            userPrompt = input("Couldn't find required library. Would you like to install it? <Y/N>")
            if(userPrompt in 'Yy'):
                self.pdInstall()
            elif(userPrompt in 'Nn'):
                # TODO: No pandas method
                userPrompt = input("Would you want to proceed without pandas anyway? <Y/N>")
            else:
                # TODO: let user choose a choice
                print("Invalid Operation. Please Select operations below:")

# TODO: Manipulated it

# TODO: 1.
# ? 1. Mean of monetary base of all February in Leap year.
    def _1(self):
        self.data_1 = self.data[18]
        self.data_1 = self.data_1[self.data_1]
        print(self.data_1)
        self._res_1 = self.data_1.mean(axis=0, )
        
        # TODO: non-libary method.

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

# TODO: Implement pandas installation.
    def pdInstall(self):
        try:
            os.system("pip install pandas")
        except:
            # TODO: no pip handling
            # TODO: import failed after install pandas
            print

if __name__ == "__main__":
    main = Main()
