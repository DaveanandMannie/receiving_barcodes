from csv import DictReader, DictWriter

type label_data = list[dict[str, str]]

def generate_data(file_path: str) -> label_data:
    data: label_data = []
    with open(file_path) as file:
        reader = DictReader(file)
        for row in reader:
            if row['Reference']:
                ref = row['Reference']

            in_qty = float(row['Operations/Stock Operation/Demand'])
            pkg_qty = float(row['Operations/Packaging Quantity'])
            quants: tuple[float, float] = divmod(in_qty, pkg_qty)
            csv_data: dict[str, str] = {
                'reference': ref.replace('/','-'),
                'partial': 'False',
                'product': row['Operations/Display Name'],
                'qty': str(pkg_qty) if pkg_qty else 'Update Product Packaging',
                'barcode': row['Operations/Barcode']
            }
            for _ in range(int(quants[0])):
                data.append(csv_data)
            if quants[1] != 0.0:
                partial_data = dict(csv_data)
                partial_data.update(partial='True', qty=str(quants[1]))
                data.append(partial_data)
    return data

def generate_csv(out_path: str, data: label_data):
    headers = ['reference', 'product', 'qty', 'barcode', 'partial']
    with open(out_path, 'w', newline='') as file:
        writer = DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
