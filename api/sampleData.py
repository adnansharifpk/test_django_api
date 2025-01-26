from api.models import Product

# List of 60 products to insert into the database
products = [
    ('Apple iPhone 13', 'Latest iPhone model', 999, 50),
    ('Apple iPhone 12', 'Older iPhone model', 899, 60),
    ('Samsung Galaxy S21', 'Latest Samsung model', 799, 45),
    ('Samsung Galaxy S20', 'Older Samsung model', 699, 30),
    ('Google Pixel 5', 'Google\'s flagship phone', 699, 40),
    ('OnePlus 9', 'Flagship OnePlus phone', 729, 35),
    ('OnePlus 8', 'Older OnePlus model', 649, 55),
    ('Xiaomi Mi 11', 'Xiaomi\'s latest phone', 749, 50),
    ('Xiaomi Mi 10', 'Xiaomi\'s previous model', 649, 65),
    ('Oppo Find X3 Pro', 'Oppo\'s premium phone', 999, 20),
    ('Oppo Reno 5', 'Mid-range Oppo phone', 399, 70),
    ('Sony Xperia 1 II', 'Sony\'s premium flagship', 1200, 15),
    ('Sony Xperia 5 II', 'Compact version of Xperia 1', 1000, 25),
    ('LG Velvet', 'LG\'s stylish smartphone', 699, 40),
    ('LG Wing', 'LG with a rotating screen', 999, 10),
    ('Huawei P40 Pro', 'Huawei\'s flagship phone', 900, 30),
    ('Huawei Mate 40 Pro', 'Flagship Mate series phone', 1200, 20),
    ('Realme 8 Pro', 'Mid-range Realme phone', 329, 60),
    ('Realme X3 SuperZoom', 'Realme with a great camera', 499, 50),
    ('Asus ROG Phone 5', 'Gaming phone by Asus', 999, 25),
    ('Asus Zenfone 8', 'Compact and powerful phone', 799, 40),
    ('Nokia 8.3 5G', 'Nokia\'s 5G-enabled phone', 599, 30),
    ('Nokia 5.4', 'Mid-range Nokia phone', 249, 65),
    ('Motorola Edge+', 'Flagship Motorola phone', 999, 15),
    ('Motorola Moto G Power', 'Budget Motorola phone', 199, 80),
    ('Motorola Moto G Stylus', 'Stylus-enabled Motorola phone', 299, 75),
    ('Samsung Galaxy Z Fold 3', 'Foldable phone by Samsung', 1799, 5),
    ('Samsung Galaxy Z Flip 3', 'Compact foldable phone', 999, 20),
    ('Apple iPad Pro 11" 2021', 'Latest iPad model', 799, 40),
    ('Apple iPad Air 4', 'Affordable iPad model', 599, 50),
    ('Microsoft Surface Pro 7', 'Microsoft\'s hybrid laptop-tablet', 749, 35),
    ('Microsoft Surface Go 2', 'Compact tablet by Microsoft', 399, 60),
    ('Amazon Fire HD 10', 'Amazon\'s budget tablet', 149, 80),
    ('Amazon Fire 7', 'Basic budget tablet by Amazon', 49, 100),
    ('Lenovo Tab P11', 'Lenovo\'s mid-range tablet', 349, 55),
    ('Lenovo Tab M10', 'Budget tablet from Lenovo', 179, 90),
    ('Samsung Galaxy Tab S7', 'Premium tablet by Samsung', 649, 30),
    ('Samsung Galaxy Tab A7', 'Affordable Samsung tablet', 229, 70),
    ('Google Nest Hub', 'Smart display by Google', 89, 120),
    ('Google Nest Mini', 'Small smart speaker by Google', 49, 150),
    ('Amazon Echo Dot 4th Gen', 'Compact smart speaker from Amazon', 39, 180),
    ('Amazon Echo Show 8', 'Smart display with Alexa', 129, 50),
    ('Apple HomePod Mini', 'Smart speaker by Apple', 99, 60),
    ('JBL Flip 5', 'Portable Bluetooth speaker by JBL', 119, 45),
    ('Bose SoundLink Revolve', 'Premium portable speaker by Bose', 199, 30),
    ('Sony WH-1000XM4', 'Noise-cancelling headphones from Sony', 348, 15),
    ('Beats Solo3 Wireless', 'Over-ear headphones by Beats', 199, 40),
    ('Sennheiser Momentum 3', 'Premium headphones by Sennheiser', 399, 20),
    ('Apple AirPods Pro', 'Premium wireless earbuds by Apple', 249, 50),
    ('Samsung Galaxy Buds Pro', 'Premium earbuds by Samsung', 199, 45),
    ('JBL Free X', 'True wireless earbuds from JBL', 79, 70),
    ('Xiaomi Mi True Wireless Earphones 2', 'Affordable wireless earbuds from Xiaomi', 49, 120),
    ('Huawei FreeBuds 3', 'Wireless earbuds by Huawei', 159, 25),
    ('Sony WF-1000XM3', 'Noise-cancelling earbuds by Sony', 229, 30)
]

# Insert products into the database
for product in products:
    Product.objects.create(
        name=product[0],
        description=product[1],
        price=product[2],
        stock=product[3]
    )

print("60 products inserted successfully!")
