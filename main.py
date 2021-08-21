names = []
with open('./Input/Names/invited_names.txt') as f:
    lines = f.readlines()

for line in lines:
    names.append(line.strip())

with open('./Input/Letters/starting_letter.txt') as f:
    letter_content = f.read()

for name in names:
    ind_content = letter_content.replace('[name]', name)
    with open(f'./Output/ReadyToSend/letter_for_{name}', mode='w') as f:
        f.write(ind_content)
