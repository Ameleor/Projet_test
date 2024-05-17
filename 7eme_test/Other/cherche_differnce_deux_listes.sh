while IFS= read -r line; do
    value=$(echo "$line" | cut -d ',' -f 1)  # Assuming columns are separated by ,
    grep -q "^$value" Other/list_PGC_present.csv || echo "$value not found in second file"
done < results/lists/list_PGC_infos.csv
