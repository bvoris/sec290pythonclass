D = {'date': ['Sun Jul 24 12:39:15 2022','Sun Jul 24 12:39:43 2022'],
     'name': ['joe', 'kim'],
     'comment': ["dogs sniff alot!","cats sleep a lot"]}

for category, content in D.items():
    print("\nEmployee ID:", category)
    for category in content:
        print(category, content[category])
        
        dictionary = {
    "date":["Sun Jul 24 12:39:15 2022","Sun Jul 24 12:39:43 2022"],
    "name":["joe","kate"],
    "comment":["dogs sniff alot!","cats sleep a lot"]
    }