# Retrieving information about a specific bacteria
grep "GCA_019285715.1_ASM1928571v1" list_with_taxonomy.csv | awk -F ',' '{print $16}'

# Code to find which bacteria got a hit:*
#"find ." to search in the current folder
#"-type f": to search uniquely in files
#"-exec": execute a command for each line found:
#"grep -l "Systems found:"": print every line where "Systems founds:" are found
#"{}": place holder for the list to grep into
#"+": make all the iteration processed in a single command line
find . -type f -exec grep -l "Systems found:" {} +