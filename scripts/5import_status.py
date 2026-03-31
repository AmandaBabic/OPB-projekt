import pandas as pd

visit_df = pd.read_csv("data/visit.csv")

status_df = pd.DataFrame(visit_df['status'].unique(), columns=['status_name'])
status_df.insert(0, 'status_id', range(1, len(status_df) + 1))  # dodamo ID kot prvi stolpec

visit_df = visit_df.merge(status_df, left_on='status', right_on='status_name', how='left')

visit_df = visit_df.drop(columns=['status', 'status_name'])


cols = visit_df.columns.tolist()

status_index = 7  # indeks kjer je bil prej status
cols.remove('status_id')
cols.insert(status_index, 'status_id')
visit_df = visit_df[cols]

# Odstranimo vrstice z neveljavnim cargo_type_id
visit_df = visit_df[visit_df["cargo_type_id"] <= 53]

visit_df.to_csv("data/visit.csv", index=False)
status_df.to_csv("data/status.csv", index=False)

print("CSV-ji so ustvarjeni: visit.csv in status.csv")