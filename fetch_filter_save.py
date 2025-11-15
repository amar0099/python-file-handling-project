import requests, csv

response = requests.get('https://jsonplaceholder.typicode.com/users')

if response.status_code == 200:
    data = response.json()

    # Flatten the keys manually
    with open('users_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Create header (flattened)
        header = [
            'id', 'name', 'username', 'email',
            'address_street', 'address_suite', 'address_city', 'address_zipcode',
            'geo_lat', 'geo_lng',
            'phone', 'website',
            'company_name', 'company_catchPhrase', 'company_bs'
        ]
        writer.writerow(header)

        # Write data
        for user in data:
            writer.writerow([
                user['id'],
                user['name'],
                user['username'],
                user['email'],
                user['address']['street'],
                user['address']['suite'],
                user['address']['city'],
                user['address']['zipcode'],
                user['address']['geo']['lat'],
                user['address']['geo']['lng'],
                user['phone'],
                user['website'],
                user['company']['name'],
                user['company']['catchPhrase'],
                user['company']['bs']
            ])
