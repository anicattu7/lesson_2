from smartninja_sql.sqlite import SQLiteDatabase
db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.pretty_print("SELECT * FROM Invoice LIMIT 10;")

db.pretty_print("SELECT * FROM Customer LIMIT 10;")

#Inner Join
db.pretty_print("""
                    SELECT Invoice.CustomerId, Invoice.BillingCity, Customer.FirstName, Customer.LastName, Invoice.Total
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId 
                    WHERE Invoice.BillingCity='Stockholm' limit 10;
                    """)

# Sum/ AVG/ COUNT/ MAX/ MIN
db.pretty_print("""
                    SELECT COUNT(Invoice.Total) AS 'COUNT', AVG(Invoice.Total) AS 'AVG'
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId 
                    WHERE Invoice.BillingCity='Stockholm' limit 10;
                    """)

# Group By
db.pretty_print("""
                    SELECT Customer.FirstName, SUM(Invoice.Total)
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId 
                    GROUP BY Invoice.CustomerId limit 10;
                    """)

#db.print_tables(verbose=True)