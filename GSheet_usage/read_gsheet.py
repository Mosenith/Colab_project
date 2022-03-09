from gspread_dataframe import get_as_dataframe
sheet = gc.open(title).sheet1
df = get_as_dataframe(sheet).dropna(0, 'all').dropna(1, 'all')
# remove empty (NA) columns and rows
