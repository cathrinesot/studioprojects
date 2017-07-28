Diary 


error : multiple values in columns 

solution:

https://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options

For some reason my df size becomes seventy two rows, so I check the shape of my dataframe all the time to make sure is correct.

Opened the data in open Refine to clean and check the ages. 
I got 14 cases where the offender is 1 year old, but this is not correct, those values should have been unknown
same for 2 years old - example 2 years old father 

DOCUMENTATION 1
https://ucr.fbi.gov/nibrs/addendum-for-submitting-cargo-theft-data/shr

ViZ --> http://www.murderdata.org/p/offenders.html


NOTE : THE UCR csv does not include ind. cases, the SHR does! So I work with the SHR. 

"The MurderData site also allows you to examine individual cases or groups of cases that have been re-ported to the FBI through the Sup-plemental Homicide Report (SHR), an addendum to the UCR. To access SHR data, select the “Search Cas-es” tab. "


SEABORN TUTORIALS

http://seaborn.pydata.org/index.html

link video tutorial HEATMAP: https://www.youtube.com/watch?v=m7uXFyPN2Sk

https://github.com/mGalarnyk/Python_Tutorials/blob/master/Request/Heat%20Maps%20using%20Matplotlib%20and%20Seaborn.ipynb

How to make a pandas crosstab with percentages?

link: https://stackoverflow.com/questions/21247203/how-to-make-a-pandas-crosstab-with-percentages

SOS -->   pd.crosstab(df.A, df.B).apply(lambda r: r/r.sum(), axis=1)


