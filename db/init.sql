CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    completada BOOLEAN DEFAULT FALSE
);

INSERT INTO tareas (descripcion) VALUES ('Aprobar la práctica de DevOps');