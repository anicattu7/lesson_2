from smartninja_sql.sqlite import SQLiteDatabase
db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.print_tables(verbose=True)

#db.pretty_print("SELECT * FROM Invoice LIMIT 10;")

#db.pretty_print("SELECT * FROM Customer LIMIT 10;")

db.pretty_print("SELECT * FROM Track LIMIT 10;")

# What order (Invoice) was the most expensive? Which one was the cheapest?
db.pretty_print("SELECT MAX(Invoice.Total) AS Max_Total,* FROM Invoice;")
db.pretty_print("SELECT MIN(Invoice.Total) AS Min_Total,* FROM Invoice;")

# Which city (BillingCity) has the most orders?
db.pretty_print("""SELECT Invoice.BillingCity, COUNT(*) AS 'Invoice_Total_Count'
                    FROM Invoice GROUP BY Invoice.BillingCity
                    ORDER BY Invoice_Total_Count DESC limit 10;""")

# Calculate (or count) how many tracks have this MediaType: Protected AAC audio file.
db.pretty_print("""SELECT COUNT(*) AS 'Protected ACC AF' FROM Track 
                    JOIN MediaType ON MediaType.MediaTypeId = Track.MediaTypeId
                    WHERE MediaType.Name='Protected AAC audio file';""")

# Find out what Artist has the most albums? (hint: check ORDER BY)
db.pretty_print("""SELECT Artist.Name, COUNT(*) AS 'Album_Count' FROM Artist 
                    INNER JOIN Album ON Album.ArtistId= Artist.ArtistId 
                    GROUP BY Album.ArtistId
                    ORDER BY Album_Count DESC LIMIT 10;""")

# What genre has the most tracks?
db.pretty_print("""SELECT Genre.Name, COUNT(*) AS 'Track_Count' FROM Genre 
                    INNER JOIN Track ON Genre.GenreId= Track.GenreId 
                    GROUP BY Genre.GenreId
                    ORDER BY Track_Count DESC LIMIT 10;""")

# Which customer spent the most money so far?
db.pretty_print("""SELECT Customer.FirstName, SUM(Invoice.Total) AS 'Total' FROM Customer 
                    JOIN Invoice ON Customer.CustomerId=Invoice.CustomerId 
                    GROUP BY Customer.CustomerId
                    ORDER BY Total DESC LIMIT 10;""")

# What songs were bought with each order?
db.pretty_print("""SELECT Invoice.InvoiceId, Track.Name FROM Track INNER 
                    JOIN InvoiceLine ON Track.TrackId=InvoiceLine.TrackId 
                    JOIN Invoice ON InvoiceLine.InvoiceId=Invoice.InvoiceId LIMIT 10;""")
