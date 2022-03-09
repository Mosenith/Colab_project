# authenticate
from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials as GC
gc = gspread.authorize(GC.get_application_default())
# create, and save df
from gspread_dataframe import set_with_dataframe
title = 'New Sheet'
gc.create(title)  # if not exist
sheet = gc.open(title).sheet1
set_with_dataframe(sheet, df) 
# include_index=False, include_column_header=True, resize=False
