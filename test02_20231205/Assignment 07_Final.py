import os
import pandas as pd
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
            # FIXME: Will move import pandas outside, please put it back later
            # * src: https://pandas.pydata.org/docs/user_guide/io.html#parsing-options
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose
            # * src: https://pandas.pydata.org/docs/user_guide/io.html#handling-column-names
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime
            # * src: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.str.casefold.html#pandas.Series.str.casefold
            
            # ? Further Reading
            # ? src: https://docs.python.org/3/library/io.html?highlight=stringio#io.StringIO
            
            self.data = pd.read_csv(self.fileName, header=5, index_col=0, usecols=[x for x in range(1, 380)]).transpose()
            self.dataKey = self.data.keys()
            self.date = self.data.index.str.title()
            print(self.data)
            print(self.dataKey)
            print(self.date)
            
            self.date = pd.to_datetime(self.date, format="%b %Y ")
            print(self.date)

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
        
        # * src: https://pandas.pydata.org/docs/user_guide/10min.html#getitem
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_leap_year.html#pandas-series-dt-is-leap-year
        # * src: https://pandas.pydata.org/docs/user_guide/10min.html#boolean-indexing
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas-series
        
        # ? Further reading
        # ? src: https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-timestamps
        # ? src: https://docs.python.org/3/library/functions.html?highlight=all#all
        
        self.data_1 = self.data[self.dataKey[17]]
        self.data_1_check = self.date.is_leap_year
        
        self.data_1 = self.data_1[self.data_1_check]
        print(self.data_1)
        
        self.data_1 = self.data_1.
        # self._res_1 = self.data_1.mean(axis=0, )
        
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
