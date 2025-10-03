
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    address TEXT NOT NULL,
    country VARCHAR(50) NOT NULL,
    phone VARCHAR(50),
    company VARCHAR(50)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

CREATE TABLE orders (
    order_id UUID PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_amount NUMERIC(10,2) NOT NULL,
    order_date DATE NOT NULL
);

CREATE TABLE customers_complete (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    address TEXT NOT NULL,
    country VARCHAR(50) NOT NULL,
    phone VARCHAR(50),
    company VARCHAR(50),
    postcode VARCHAR(6),
    Bundesland VARCHAR(50)
);