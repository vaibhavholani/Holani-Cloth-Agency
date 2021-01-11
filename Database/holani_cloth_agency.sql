CREATE TABLE supplier (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	address VARCHAR(300),
	UNIQUE (name),
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
	);

CREATE TABLE party (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	address VARCHAR(300),
	UNIQUE (name),
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
	);

CREATE TABLE bank (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	address VARCHAR(300),
	UNIQUE (name),
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
	);

CREATE TABLE Transport (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	address VARCHAR(300),
	UNIQUE (name),
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
	);

CREATE TABLE register_entry (
	id INT AUTO_INCREMENT PRIMARY KEY,
	supplier_id INT,
	party_id INT, 
	register_date DATETIME,
	amount DECIMAL(10, 2),
	partial_amount DECIMAL(10,2) DEFAULT 0,
	bill_number INT,
	status VARCHAR(2) DEFAULT 'N',
	d_amount INT DEFAULT 0,
	d_percent INT DEFAULT 0,
	UNIQUE (bill_number, supplier_id, party_id, register_date),
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (party_id) REFERENCES party(id),
	FOREIGN KEY (supplier_id) REFERENCES supplier(id)
	);

CREATE TABLE memo_entry(
	id INT AUTO_INCREMENT PRIMARY KEY,
	memo_number INT,
	supplier_id INT,
	party_id INT, 
	register_date DATETIME,
	UNIQUE (memo_number, party_id, supplier_id, register_date),
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (party_id) REFERENCES party(id),
	FOREIGN KEY (supplier_id) REFERENCES supplier(id)
	);

CREATE TABLE memo_payments(
	memo_id INT, 
	bank_id INT,
	cheque_number INT,
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (memo_id) REFERENCES memo_entry(id),
	FOREIGN KEY (bank_id) REFERENCES bank(id)
	);

CREATE TABLE memo_bills (
	memo_id INT, 
	bill_number INT,
	type VARCHAR(2),
	amount INT,
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (memo_id) REFERENCES memo_entry(id)
);

CREATE TABLE gr_settle(
	supplier_id INT,
	party_id INT, 
	start_date DATETIME,
	end_date DATETIME,
	settle_amount INT,
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (party_id) REFERENCES party(id),
	FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);

CREATE TABLE supplier_party_account(
	supplier_id INT,
	party_id INT,
	partial_amount INT DEFAULT 0,
	gr_amount DECIMAL(10, 2) DEFAULT 0,
	UNIQUE(supplier_id, party_id),
	last_update TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (party_id) REFERENCES party(id),
	FOREIGN KEY (supplier_id) REFERENCES supplier(id)
	);

CREATE TABLE last_update(
	updated_at TIMESTAMP
);

INSERT into last_update(updated_at) VALUES (CURRENT_TIMESTAMP);

