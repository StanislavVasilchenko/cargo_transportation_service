import csv


def read_csv_locations():
    with open("uszips.csv", 'r') as csvfile:
        data = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_csv = {
                'city': row.get('city'),
                'state': row.get('state_name'),
                'zipcode': row.get('zip'),
                'latitude': row.get('lat'),
                'longitude': row.get('lng'),

            }
            data.append(data_csv)
        return data


def zip_code_checker(zipcode: str) -> str | None:
    length = len(zipcode)
    if length < 5:
        difference = 5 - length
        new_zipcode = "0" * difference + zipcode
        return new_zipcode
    return zipcode
