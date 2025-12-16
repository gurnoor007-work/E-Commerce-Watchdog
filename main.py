import os

#We will print the header and footer stuff
columns = os.get_terminal_size().columns

header = f"E-Commerce-Watchdog".center(columns, '=')
print(header)

import data_extraction
import track_prices




print(header)