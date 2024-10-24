USE interview;
CREATE TABLE InvoiceDetails (
    lineNo INT PRIMARY KEY,
    productName VARCHAR(100) NOT NULL,
    UnitNo INT NOT NULL,
    price DECIMAL(5, 2) NOT NULL,
    quantity DECIMAL(5, 2) NOT NULL,
    total DECIMAL(5, 2) NOT NULL,
    expiryDate DATETIME NOT NULL
);
CREATE TABLE Unit (
    unitNo INT PRIMARY KEY,
    unitName VARCHAR(100) NOT NULL
);
DESCRIBE unit;
DESCRIBE invoicedetails_invoicedetails;
SELECT * FROM invoicedetails_invoicedetails;


 
 
 
 