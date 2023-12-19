print("Hello Git 3!")

lines_cleaned = [''.join(['|' + re.sub('Unnamed: .*', '', cell).strip() for cell in line.split('|')[1:]]) + '\n' for line in lines]
lines_cleaned1 = [''.join(['|' + re.sub(r'^:---.*', ':-', cell).strip() for cell in line.split('|')[1:]]) + '\n' for line in lines_cleaned]