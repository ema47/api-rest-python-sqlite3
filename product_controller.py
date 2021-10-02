
from db import get_db

def insert_product(name, productType, price, rating, image, description):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO product(name, producType, price, rating, image, description) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [str(name), str(productType), int(price), int(rating), str(image), str(description)])
    db.commit()
    return True


def update_product(id, name, productType, price, rating, image, description):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE product SET name = ?, producType=?, price = ?, rating = ?, image=?, description=? WHERE id = ?"
    cursor.execute(statement, [str(name), str(productType), int(price), int(rating), str(image), str(description), id])
    db.commit()
    return True


def delete_product(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM product WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, producType, price, rating, image, description FROM product WHERE id = ?"
    cursor.execute(statement, [id])
    product=[dict(id=row[0],name=row[1],producType=row[2],price=row[3],rating=row[4],image=row[5],description=row[6])
    for row in cursor.fetchall() 
    ]
    return product
    


def get_products():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, producType, price, rating, image, description FROM product"
    cursor.execute(query)
    products=[dict(id=row[0],name=row[1],producType=row[2],price=row[3],rating=row[4],image=row[5],description=row[6])
    for row in cursor.fetchall() 
    ]
    return products
    """return cursor.fetchall()"""
