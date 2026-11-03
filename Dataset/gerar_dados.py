import csv
import json
import random
import sqlite3
from datetime import datetime, timedelta

# Seed fixa para determinismo
random.seed(42)

def generate_loja_aurora(scale='small'):
    """
    Gera o dataset Loja Aurora.
    Small: Milhares de linhas.
    Large: Milhões de linhas.
    """
    num_customers = 1000 if scale == 'small' else 100_000
    num_products = 200 if scale == 'small' else 5_000
    num_orders = 5000 if scale == 'small' else 1_000_000

    print(f"Gerando dataset {scale}...")

    # --- Customers ---
    customers = []
    for i in range(1, num_customers + 1):
        # Introduzir defeitos realistas: alguns nulos no email
        email = f"user{i}@example.com" if random.random() > 0.05 else None
        customers.append({
            'customer_id': i,
            'name': f"Customer {i}",
            'email': email,
            'city': random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Salvador']),
            'created_at': (datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1000))).isoformat()
        })

    # --- Products ---
    products = []
    for i in range(1, num_products + 1):
        products.append({
            'product_id': i,
            'name': f"Product {i}",
            'category': random.choice(['Eletrônicos', 'Casa', 'Vestuário', 'Livros', 'Esportes']),
            'price': round(random.uniform(10.0, 2000.0), 2)
        })

    # --- Orders ---
    orders = []
    for i in range(1, num_orders + 1):
        # Introduzir datas inválidas ou futuras
        date = datetime(2021, 1, 1) + timedelta(days=random.randint(0, 1500))
        if random.random() < 0.01:
            date = datetime(2099, 1, 1) # Data futura

        orders.append({
            'order_id': i,
            'customer_id': random.randint(1, num_customers),
            'order_date': date.isoformat(),
            'status': random.choice(['Delivered', 'Shipped', 'Cancelled', 'Pending']),
            'total_amount': 0.0 # Será calculado pelos itens
        })

    # --- Order Items ---
    items = []
    for o_id in range(1, num_orders + 1):
        # 1 a 5 itens por pedido
        for _ in range(random.randint(1, 5)):
            p_id = random.randint(1, num_products)
            qty = random.randint(1, 3)
            price = next(p['price'] for p in products if p['product_id'] == p_id)
            items.append({
                'item_id': len(items) + 1,
                'order_id': o_id,
                'product_id': p_id,
                'quantity': qty,
                'unit_price': price
            })
            # Atualizar total do pedido (simplificado para o script)
            orders[o_id-1]['total_amount'] += qty * price

    # --- Logs (Eventos) ---
    logs = []
    event_types = ['page_view', 'add_to_cart', 'purchase', 'login']
    for i in range(num_orders * 2):
        logs.append({
            'log_id': i,
            'customer_id': random.randint(1, num_customers),
            'event_type': random.choice(event_types),
            'timestamp': (datetime(2021, 1, 1) + timedelta(seconds=random.randint(0, 100_000_000))).isoformat(),
            'user_agent': random.choice(['Chrome', 'Firefox', 'Safari', 'Edge'])
        })

    return customers, products, orders, items, logs

def save_to_csv(data, filename, fieldnames):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def save_to_sql(customers, products, orders, items, logs, filename):
    # Usando SQLite para gerar o dump SQL inicial
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE customers (customer_id INT, name TEXT, email TEXT, city TEXT, created_at TEXT)")
    cursor.execute("CREATE TABLE products (product_id INT, name TEXT, category TEXT, price REAL)")
    cursor.execute("CREATE TABLE orders (order_id INT, customer_id INT, order_date TEXT, status TEXT, total_amount REAL)")
    cursor.execute("CREATE TABLE order_items (item_id INT, product_id INT, order_id INT, quantity INT, unit_price REAL)")
    cursor.execute("CREATE TABLE logs (log_id INT, name TEXT, event_type TEXT, timestamp TEXT, user_agent TEXT)") # Intencional: 'name' em vez de 'customer_id' para bug

    # Insertions... (simplificado para o arquivo final)
    # Em um cenário real, geraríamos os INSERTs em texto
    conn.close()

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("-- Dump SQL Loja Aurora\n")
        f.write("CREATE TABLE customers (customer_id INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), city VARCHAR(50), created_at TIMESTAMP);\n")
        f.write("CREATE TABLE products (product_id INT PRIMARY KEY, name VARCHAR(100), category VARCHAR(50), price NUMERIC(10,2));\n")
        f.write("CREATE TABLE orders (order_id INT PRIMARY KEY, customer_id INT, order_date TIMESTAMP, status VARCHAR(20), total_amount NUMERIC(10,2));\n")
        f.write("CREATE TABLE order_items (item_id INT PRIMARY KEY, product_id INT, order_id INT, quantity INT, unit_price NUMERIC(10,2));\n")
        f.write("CREATE TABLE logs (log_id INT PRIMARY KEY, customer_id INT, event_type VARCHAR(20), timestamp TIMESTAMP, user_agent VARCHAR(50));\n")

        # Apenas alguns exemplos de inserts para o arquivo SQL
        f.write("\n-- Amostras de dados\n")
        # ... (Inserir alguns dados reais do gerador aqui)

if __name__ == "__main__":
    # Small scale
    c_s, p_s, o_s, i_s, l_s = generate_loja_aurora('small')
    save_to_csv(c_s, 'Vault-Engenharia-de-Dados/Dataset/customers_small.csv', ['customer_id', 'name', 'email', 'city', 'created_at'])
    save_to_csv(p_s, 'Vault-Engenharia-de-Dados/Dataset/products_small.csv', ['product_id', 'name', 'category', 'price'])
    save_to_csv(o_s, 'Vault-Engenharia-de-Dados/Dataset/orders_small.csv', ['order_id', 'customer_id', 'order_date', 'status', 'total_amount'])
    save_to_csv(i_s, 'Vault-Engenharia-de-Dados/Dataset/order_items_small.csv', ['item_id', 'order_id', 'product_id', 'quantity', 'unit_price'])
    save_to_csv(l_s, 'Vault-Engenharia-de-Dados/Dataset/logs_small.csv', ['log_id', 'customer_id', 'event_type', 'timestamp', 'user_agent'])

    # JSON Sample
    save_to_json(c_s[:10], 'Vault-Engenharia-de-Dados/Dataset/customers_sample.json')

    # SQL Dump
    save_to_sql(c_s, p_s, o_s, i_s, l_s, 'Vault-Engenharia-de-Dados/Dataset/loja_aurora.sql')

    print("Dataset gerado com sucesso!")
