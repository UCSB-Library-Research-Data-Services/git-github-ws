import csv

def read_csv(file_path: str) -> list[dict]:
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def add_dessert(data: list[dict], rank: int, dessert: str) -> list[dict]:
    if any(row['dessert'] == dessert for row in data):
        print(f"{dessert} is already in the list. No changes made.")
        return data

    for row in data:
        if int(row['rank']) >= rank:
            row['rank'] = str(int(row['rank']) + 1)

    data.append({'rank': str(rank), 'dessert': dessert})
    data.sort(key=lambda x: int(x['rank']))

    return data
    
    
def to_csv(data: list[dict], file_path: str) -> None:
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['rank', 'dessert']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def main(rank: int, dessert: str) -> None:
    """Read the iconic desserts CSV, 
    insert a dessert at the given rank, 
    and save the updated list.

    Args:
        rank (int): Rank at which to insert the dessert.
        dessert (str): Name of the dessert to add.
    """
    data = read_csv('data/iconic_desserts.csv')
    new_data = add_dessert(data, rank, dessert)
    to_csv(new_data, 'data/iconic_desserts.csv')



if __name__ == "__main__":
    # Add a new dessert to the list at rank 3
    main(3, 'Tiramisu')
    # Try adding a dessert that is already in the list
    main(1, 'Chocolate chip cookies')