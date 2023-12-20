import os
import pandas as pd
from urllib.request import urlretrieve
from functools import partial

# TODO: Write codes as Assigned.
# ? Don't forget to add citation.

url = "https://app.bot.or.th/BTWS_STAT/statistics/DownloadFile.aspx?file=EC_MB_001_ENG_ALL.CSV"

# DONE: Initialize Class
class Main():
    def __init__(self):
        # FEATURES: module detection
        # ? Added module detection capability.
        # ? Implement All Library check at initialize stage 
        
        self.setCurrentDir()
        self.fetch(url)
        self.pdInit()
        self._1()
        self._2()
        self._3()
        self._4()
        self._5()
        self.res()

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
            # * src: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.str.casefold.html#pandas.Series.str.casefold
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas-dataframe-insert
            # * src: https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby
            # * src: https://stackoverflow.com/questions/14734533/how-to-access-subdataframes-of-pandas-groupby-by-key#comment33905910_17302673
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.Index.array.html#pandas.Index.array
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas-datetimeindex
            # * src: https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.to_series.html
            # * src: https://stackoverflow.com/questions/54680055/what-is-a-good-way-to-prevent-changes-from-being-applied-to-an-original-data-fra
            # * src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html
            # * src: https://stackoverflow.com/a/44831147
            # * src: https://stackoverflow.com/questions/19851005/rename-pandas-dataframe-index 
            # * src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
            
            # ? Further Reading
            # ? src: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime
            # ? src: https://docs.python.org/3/library/io.html?highlight=stringio#io.StringIO
            # ? src: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas-dataframe-assign
            # ? src: https://pandas.pydata.org/docs/user_guide/dsintro.html#assigning-new-columns-in-method-chains
            # ? src: https://pandas.pydata.org/docs/reference/api/pandas.Index.values.html#pandas.Index.values
            # ? src: https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray
            # ? src: https://docs.python.org/3/library/datetime.html#datetime.datetime
            # ? src: https://stackoverflow.com/questions/60913716/convert-timeindex-of-dataframe-to-datetimeindex-in-place
            # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename
            # ? src: https://docs.python.org/3/library/functions.html?highlight=zip#zip
            # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index
            # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns
            # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index
            # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex
            # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reindex_like.html#pandas.DataFrame.reindex_like
            
            self.data = pd.read_csv(self.fileName, header=5, index_col=0, usecols=[x for x in range(1, 380)]).transpose()
            self.dateName = self.data.index
            self.date = self.data.index.str.title()
            self.date = pd.to_datetime(self.date, format="%b %Y ")
            
            self.dateToLabel = self.dateName.to_series(index=self.date)
            
            self.defaultData = self.data.copy()
            self.data.insert(0, 'time', self.date)
            self.dataKey = self.data.keys()
            
            self.timeData = self.data.copy()
            self.timeData.insert(0, 'labels', self.dateName)
            self.timeData.set_index(self.dataKey[0], inplace=True)
            
            self.dataByYear = self.data.groupby(self.data['time'].dt.year)

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

# DONE: Manipulated it

# DONE: 1.
# ? 1. Mean of monetary base of all February in Leap year.
    def _1(self):
        
        # * src: https://pandas.pydata.org/docs/user_guide/10min.html#getitem
        # * src: https://pandas.pydata.org/docs/user_guide/10min.html#boolean-indexing
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas-series
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas-series-iloc
        
        # ? Further reading
        # ? src: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_leap_year.html#pandas-series-dt-is-leap-year
        # ? src: https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-timestamps
        # ? src: https://docs.python.org/3/library/functions.html?highlight=all#all
        # ? src: https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html#pandas-series-loc
        # ? src: https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/05_add_columns.html
        
        self.data_1 = self.data[self.dataKey[18]]
        self.data_1 = self.data_1.filter(like='F').iloc[0::4]
        self._res_1 = int(round(self.data_1.mean(axis=0), 0))
        # TODO: non-libary method.

# DONE: 2.
# ? 2. means for each year of 'Net Claims on Central Government'
# * Pandas Series
# * 1981 - 1990
    def _2(self):
        # * src: https://pandas.pydata.org/docs/user_guide/timeseries.html#indexing
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html#pandas-series-between
        # * src: https://pandas.pydata.org/docs/user_guide/timeseries.html#truncating-fancy-indexing
        # * src: https://pandas.pydata.org/docs/user_guide/timeseries.html#partial-string-indexing
        # * src: https://stackoverflow.com/questions/43556344/pandas-monthly-rolling-operation
        # * src: https://copyprogramming.com/howto/pandas-find-the-mean-for-each-year
        # * src: https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/09_timeseries.html
        # * src: https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/06_calculate_statistics.html
        # * src: https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/07_reshape_table_layout.html#min-tut-07-reshape
        # * src: https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/03_subset_data.html#how-do-i-select-specific-rows-and-columns-from-a-dataframe
        # * src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
        # * src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.name.html#pandas.Series.name
        
        # ? Further Reading
        # ? src: https://pandas.pydata.org/docs/user_guide/basics.html#dtypes
        # ? src: https://pandas.pydata.org/docs/user_guide/window.html#windowing-operations
        # ? src: https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html#pandas-series-rolling
        # ? src: https://pandas.pydata.org/docs/user_guide/dsintro.html#series-is-ndarray-like
        # ? src: https://pandas.pydata.org/docs/user_guide/timeseries.html#dateoffset-objects
        # ? src: https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html#pandas.Series.between_time
        # ? src: https://stackoverflow.com/questions/14734533/how-to-access-subdataframes-of-pandas-groupby-by-key
        # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.index.html#pandas.Series.index
        
        self._res_2 :pd.Series = self.dataByYear[self.dataKey[9]].mean().loc[1981:1990]
        self._res_2.index.names = [None]
        self._res_2.name = None

# DONE: 3.
# ? 3. List of net loss continuously for 3 months
# * 1991 - 2005
    def _3(self):
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html#pandas.Series.rolling
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html
        # * src: https://stackoverflow.com/questions/57235819/get-if-a-rolling-window-is-increasing-or-decreasing
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html
        # * src: https://stackoverflow.com/a/29370182
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html#pandas.Series.index
        # * src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.iat.html
        
        # ? Further Reading
        # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.get_group.html
        # ? src: https://stackoverflow.com/questions/31535442/select-multiple-groups-from-pandas-groupby-object
        # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html#pandas.Grouper
        # ? src: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.is_monotonic_decreasing.html
        # ? src: https://github.com/pandas-dev/pandas/issues/19248
        # ? src: https://stackoverflow.com/questions/46100962/loop-to-get-rolling-future-values-of-a-pandas-time-indexed-dataframe-can-i-make/46101574#46101574
        # ? src: https://github.com/pandas-dev/pandas/pull/28297
        # ? src: https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html#pandas.Series.between_time
        
        # ! There is nothing wrong with using loop for pandas. So don't think about it too much.
        
        # TODO: needs to format these result later.
        
        self.data_3 = self.timeData[self.dataKey[1]].loc['1991':'2005']
        print(self.data_3)
        self.data_3_index = self.data_3.index
        self._res_3 = tuple()
        for period in range(0, self.data_3.size-2):
            temp :pd.Series = self.data_3.iloc[period:period+3]
            if (temp.is_monotonic_decreasing):
                self._res_3 += temp.iat[-1]
        print(self._res_3)

# DONE: 4.
# ? 4. List of 'Claims on Financial Institutions' is greater than 583757 for at least 3 month, In 6 month ranges
# * 2000 - 2005
# * 583757
    def _4(self):
        
        # * src: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling
        # * src: https://pandas.pydata.org/docs/reference/window.html#window
        # * src: https://pandas.pydata.org/docs/dev/user_guide/indexing.html#selection-by-label
        # * src: https://pandas.pydata.org/docs/dev/user_guide/indexing.html#boolean-indexing
        # * src: https://pandas.pydata.org/docs/dev/user_guide/basics.html#dtypes
        # * src: https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.astype.html#pandas.Series.astype
        # * src: https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes
        
        # ? Further Reading
        # ? src: https://stackoverflow.com/questions/10692602/python-store-function-with-parameters
        # ? src: https://docs.python.org/3/library/functools.html#functools.partial
        # ? src: https://pandas.pydata.org/docs/dev/reference/api/pandas.arrays.BooleanArray.html#pandas.arrays.BooleanArray
        # ? src: https://pandas.pydata.org/docs/dev/user_guide/boolean.html#boolean-kleene
        # ? src: https://en.wikipedia.org/wiki/Three-valued_logic#Kleene_and_Priest_logics
        
        self.data_4 :pd.Series = self.timeData[self.dataKey[4]].loc['2000':'2005']
        test = partial(dataCond, comp=583757, expect=3)
        self._res_4 = self.data_4.rolling(6).apply(test)
        self._res_4 = self._res_4.astype('boolean')
        print(self.data_4[self._res_4])

# DONE: 5.
# ? 5. Tables of data, for min, mean, and max, of 'Other Liabilities to Financial Institutions' and 'Other Items (net)' for all year, based on each month.
# * 2-Ordered Pandas Data Frame
# * In this Form:
# * 'Other Liabilities to Financial Institutions': min, mean, max
# * 'Other Items (net)': min, mean, max
    def _5(self):
        # * src: https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.agg.html
        # * src: https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.agg.html
        # * src: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#defined-levels
        # * src: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#creating-a-multiindex-hierarchical-index-object
        
        # ? Further Reading
        # ? src: https://stackoverflow.com/questions/60999753/pandas-future-warning-indexing-with-multiple-keys
        # ? src: https://github.com/pandas-dev/pandas/issues/49247
        # ? src: https://pandas.pydata.org/docs/whatsnew/v2.1.0.html#other-deprecations (GH 41090, GH 50684, GH 52849)
        # ?     src-mention: https://github.com/pandas-dev/pandas/issues/41090
        # ? --> src-mention: https://github.com/pandas-dev/pandas/issues/50684
        # ?     --> src-mention: https://github.com/pandas-dev/pandas/pull/50744
        # ?         src-mention: https://github.com/pandas-dev/pandas/issues/46944
        # ?     src-mention: https://github.com/pandas-dev/pandas/issues/52849
        # ? src: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#reconstructing-the-level-labels
        
        # TODO: some more formatting.
        
        self.dataByMonth = self.data.groupby(self.data['time'].dt.month).agg({self.dataKey[24]: ['min', 'mean', 'max'], self.dataKey[27]: ['min', 'mean', 'max']})
        tempDictIndex = dict()
        tempDictColumn = dict()
        for i, name in enumerate(('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'), start=1):
            tempDictIndex[i] = name
        
        for name in ('min', 'mean', 'max'):
            tempDictIndex[name] = name.upper()
        
        self.dataByMonth.rename(index=tempDictIndex, inplace=True)
        self.dataByMonth.rename(columns=tempDictColumn, inplace=True, level=1)
        self.dataByMonth.index.names = [None]
        print(self.dataByMonth)
    
    def res(self):
        # * src: https://stackoverflow.com/a/20686659
        # * src: https://docs.python.org/3/library/stdtypes.html?highlight=center#str.center
        
        # ? Further Reading
        # ? src: https://docs.python.org/3/library/functions.html?highlight=print#print
        
        pageBreak = '-'*160
        print('Pandas Application'.center(160))
        print(pageBreak)
        print('Average of "Monetary Base" [Only February on Leap Years]: {}'.format(format(self._res_1, ',')))
        
        print(pageBreak)
        print('2) Pandas Series of Annual Average of "Net Claims on Central Government" [1981-1990]:')
        print(self._res_2)
        
        print(pageBreak)
        print('3) The 3 consecutive monthly decreases of "Net Foreign Assets" [1991-2005]:')
        

# TODO: Implement pandas installation.
    def pdInstall(self):
        try:
            os.system("pip install pandas")
        except:
            # TODO: no pip handling
            # TODO: import failed after install pandas
            print

def dataCond(valList, comp, expect):
    count = 0
    for val in valList:
        if(val > comp):
            count += 1
    if count >= expect:
        return True
    else:
        return False

if __name__ == "__main__":
    main = Main()
