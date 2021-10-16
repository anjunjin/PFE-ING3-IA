import csv
# w : write
create_file_csv = open("data.csv","w")
# creer objet file_csv avec constructeur .writer
file_csv = csv.writer(create_file_csv)
# titre du csv
file_csv.writerow(['site' ,'categorie' ,'description'])