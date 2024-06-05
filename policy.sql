ALTER TABLE cliente ENABLE ROW LEVEL SECURITY;

-- estamos convertendo o vendedor_id para texto para validar com o current user
CREATE POLICY vendedor_cliente ON cliente USING (vendedor_id::text = current_user);