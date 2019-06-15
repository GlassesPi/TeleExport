import json
import csv
csv_columns = ['first_name','last_name','phone_number']

with open('result.json', encoding='utf-8') as contactsFile:
    with open('contacts.csv','a',encoding="utf-8-sig", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        data = json.load(contactsFile)
        for p in data['contacts']['list']:
            f_name = str(p['first_name']).encode('utf-8').decode('utf-8')
            l_name = str(p['last_name']).encode('utf-8').decode('utf-8')
            p_num = str(p['phone_number']).encode('utf-8').decode('utf-8')
            if p_num[:4] == '0098':
                p_num = str(p_num.replace(p_num[:4], '0'))
            writer.writerow({'first_name': f_name, 'last_name': l_name, 'phone_number':p_num})
