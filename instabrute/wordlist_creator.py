fname = input("First Name : ").strip()
lname = input("Last Name, if not press Enter : ").strip()
dob = input("Input Date of Birth in format YYYY/MM/DD : ").strip()
insta_id = input("Enter instagram id: ").strip()
insta_user_no = input("Enter the Phone no. of the Instagram Profile : ").strip()
any_other_date = input("Input any other dates in format YYYY/MM/DD, if not press Enter : ").strip()
nickname = input("Enter a nickname if not press Enter : ").strip()
other_name = input("Any other person name seems to be in password (bro/sis or bf/gf), if not press Enter : ").strip()
symbols = ["@", "#", "~", "_", "-", "!"]
dob_parts = dob.split('/') if dob else []
any_other_date_parts = any_other_date.split('/') if any_other_date else []
wordlist = []
name_combinations = [
    fname, lname, nickname, other_name, insta_id, insta_user_no,
    fname + lname, lname + fname, nickname + lname, fname + other_name,
    fname.title(), lname.title(), nickname.title(), other_name.title(),
    fname.lower(), lname.lower(), nickname.lower(), other_name.lower(),
    fname.upper(), lname.upper(), nickname.upper(), other_name.upper(),
    fname + "123", lname + "123", nickname + "123", other_name + "123"
]
if dob_parts:
    year, month, day = dob_parts
    date_combinations = [
        year, month, day, year + month + day, year[-2:] + month + day,
        fname + year, lname + year, nickname + year, other_name + year,
        fname + month + day, lname + month + day, nickname + month + day
    ]
    name_combinations.extend(date_combinations)

if any_other_date_parts:
    other_year, other_month, other_day = any_other_date_parts
    date_combinations = [
        other_year, other_month, other_day,
        other_year + other_month + other_day
    ]
    name_combinations.extend(date_combinations)
for name in name_combinations:
    for symbol in symbols:
        wordlist.append(name + symbol)
        wordlist.append(symbol + name)
        for other_name in name_combinations:
            if name != other_name:
                wordlist.append(name + symbol + other_name)
wordlist = list(set(wordlist))
with open('wordlist.txt', 'w') as f:
    for word in wordlist:
        f.write(f"{word}\n")

print(f"Generated {len(wordlist)} possible password combinations.")
print("Wordlist saved to 'wordlist.txt'")
