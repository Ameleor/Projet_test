import openpyxl
import warnings

# Ignore warning
warnings.simplefilter("ignore")

xlsx_file = "../data/supp_data_from_thiel_et_al_2018/pp69_bryant_supplemental_table3.xlsx"
# Important sheets
sheets = [1, 2, 3]

output_file = "../results/files/data_supp.txt"

# Retrieving of the 5th columns and it's informations
def extract_column(sheet):
    column_data = []
    for row in sheet.iter_rows():
        if row[4].value and str(row[4].value).startswith("GC"):
            column_data.append(row[4].value)
    return column_data

# Excel files as workbook
workbook = openpyxl.load_workbook(xlsx_file)

with open(output_file, "w") as output:
    # browsing of the sheets
    for sheet_index in sheets:
        sheet = workbook.worksheets[sheet_index - 1]
        column_data = extract_column(sheet)
        for data in column_data:
            output.write(str(data) + "\n")

print("Extraction terminée. Les données ont été écrites dans", output_file)
