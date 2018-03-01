import sqlite3
import customer_points 


print("Hello, Welcome to Escobar Mart.")
print("Are you a returning customer?")



conn = sqlite3.connect('customer_points.db')
cust_1 = customer('James', 'Gibson', 670)
cust_2= customer('Holly ', 'Burns', 12039)
cust_3 = customer('Alyson', 'Harper', 835)
cust_4 = customer('Kimberly', 'Reeves', 23489)


c = conn.cursor()


def insert_cust(cust):
    with conn:
        c.execute("INSERT INTO customers VALUES(:first, :last, :points)", {'first': cust.first, 'last':cust.last, 'points': cust.points}) 



def get_cust_by_name(lastname):
    c.execute("SELECT * FROM customers WHERE last =last",  {'last': lastname})
    return c.fetchall()

def update_points(cust, points):
    with conn:
        c.execute("""UPDATE customers SET points = :points
                           WHERE first = :first AND last = last""",
                          {'first': cust.first, 'last':cust.last, 'points': points})

def remove_customer(cust):
    with conn:
        c.execute("DELETE from customers WHERE first = :first AND last= :last",
                  {'first':cust.first, 'last': cust.last, 'points':points})

cust_1 = customer('James', 'Gibson', 670)
cust_2= customer('Holly ', 'Burns', 12039)
cust_3 = customer('Alyson', 'Harper', 835)
cust_4 = customer('Kimberly', 'Reeves', 23489)

insert_cust(cust_1)
insert_cust(cust_2)

custs = get_custs_by_name('Harper')
print(custs)
conn.close()
