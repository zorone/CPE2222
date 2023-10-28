# https://stackoverflow.com/questions/70609391/pythontkinter-text-widget-doesnt-change-text-immidiately
# temporary FIX: https://github.com/ranaroussi/yfinance#pandas_datareader-override

import tkinter as tk
import pandas_datareader as web
import yfinance as yf

yf.pdr_override() # <== that's all it takes :-)

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x480")
        self.price_text = tk.Text(self.root)
        self.price_text.grid(row=0, column=0, )

        tk.Button(self.root, text="Get", command=self.do_get).grid(row=1, column=0)
        self.root.mainloop()

    def do_get(self):
        self.price_text.delete("1.0", tk.END)
        self.price_text.insert(tk.END, "PLEASE WAIT..")
        result = self.lengthy_job()

    def lengthy_job(self):
        tickers = ["GOOG", "AAPL", "MSFT", "IBM", "F", "AMZN", "NVDA", "NFLX", "DISH", "BABA", "JD", "SHOP", "PDD", "CSCO", "AMD", "INTC", "TXN", "MU", "QCOM"]
        return web.DataReader(tickers, 'yahoo', start="2020-1-1", end="2020-1-31")

GUI()