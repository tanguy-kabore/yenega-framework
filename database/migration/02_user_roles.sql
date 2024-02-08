-- user_roles.sql
CREATE TABLE IF NOT EXISTS user_roles (
  user_id INT,
  role_id INT,
  PRIMARY KEY (user_id, role_id)
);
ALTER TABLE user_roles
  ADD FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  ADD FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE;
