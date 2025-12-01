import csv


products = {}
try:
    with open('tech.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product_id = row['product_id']
            products[product_id] = {
                'product_name': row['product_name'],
                'price': row['price'],
                'discount': row['discount']
            }
except FileNotFoundError:
    print("Error: The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

if products:
    while True:

        product_id = input("Enter the product ID to check price: ").strip()

        if product_id in products:
            product = products[product_id]
            product_name = product['product_name']
            price = product['price']
            discount = product['discount']

            print(f"\nProduct: {product_name}")
            print(f"Original Price: ${price:}")
            print(f"Discount: {discount}%")
        else:
            print("Error: Invalid product ID. Please try again.")

        another = input("\nDo you want to check another product? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the Price Checker!")
            break
