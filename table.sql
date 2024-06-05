create TABLE IF NOT EXISTS vendedor(id serial primary key, name text);
create TABLE IF NOT EXISTS cliente(id serial primary key, name text, vendedor_id integer);