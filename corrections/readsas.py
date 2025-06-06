import pyreadstat

# Lecture du fichier SAS
df, meta = pyreadstat.read_sas7bdat("../imports/jeutest_2.sas7bdat")
print(df)
print(meta)
print(type(df))


df.info()