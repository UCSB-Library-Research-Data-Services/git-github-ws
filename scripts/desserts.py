import csv

def read_csv(file_path: str) -> list[dict]:
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def add_dessert(data: list[dict], rank: int, dessert: str) -> list[dict]:
    
    new_dessert = {'rank': str(rank), 'dessert': dessert}
    
    if new_dessert in data:
        print(f"{dessert} is already in the list at rank {rank}. No changes made.")
        return data
    
    if any(row['dessert'] == dessert for row in data):
        # move the existing dessert to the new rank
        old_rank = int(next(row['rank'] for row in data if row['dessert'] == dessert))
        data = [row for row in data if row['dessert'] != dessert]
        for row in data:
            if int(row['rank']) > old_rank:
                row['rank'] = str(int(row['rank']) - 1)
                
    # Shift ranks of existing desserts inside the list to make room for the new dessert
    for row in data:
        if int(row['rank']) >= rank:
            row['rank'] = str(int(row['rank']) + 1)
    
    # Add the new dessert to the list
    data.append(new_dessert)
    
    # Sort the list of dictionaries by rank to maintain the correct order
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
    data = read_csv('data/iconic_desserts.csv')
    new_data = add_dessert(data, rank, dessert)
    to_csv(new_data, 'data/iconic_desserts.csv')



if __name__ == "__main__":
    # Add a new dessert to the list at rank 3
    main(3, 'Tiramisu')
    # Upgrade the ranking of Donuts
    main(5, 'Donuts')
    # Downgrade the ranking of Cheesecake
    main(10, 'Cheesecake')
    # Test adding a dessert that is already in the list at the same rank
    main(1,'Chocolate chip cookies')