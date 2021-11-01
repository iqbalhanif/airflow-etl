create table DWH_SalesFact as

select distinct 
	a.InvoiceLineId
	,b.InvoiceId
	,c.CustomerId
	,d.TrackId
	,e.AlbumId
	,f.ArtistId
	,concat(c.FirstName,' ',c.LastName) as CustomersName
	,d.Name as TrackName
	,e.Name as AlbumName
	,f.Name as ArtistName
	,a.Quantity
	,a.unitPrice
	,b.Total
from 
	invoiceline2 a
	join invoice2 b on a.InvoiceId = b.InvoiceId
	join customers2 c on b.CustomerId = c.CustomerId
	join track2 d on a.TrackId = d.TrackId
	join album2 e on d.AlbumId = e.AlbumId
	join artist2 f on e.ArtistId = f.ArtistId
limit 10;

