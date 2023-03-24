import pikepdf



pdf = pikepdf.open(r'C:\Users\sures\Downloads\Statement_MAR2023_163907076.pdf', password="SELV3006")


pdf.save(r"C:\Users\sures\Downloads\Statement_MAR2023_163907076_pr.pdf" )
