import psycopg2
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    API_KEY = os.getenv('URL')
    conn = psycopg2.connect(API_KEY)

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)
    
    
    cur.execute("""Drop table MiembroInfo;""")
    cur.execute("""Drop table Miembro;""")
    cur.execute("""Drop table Pediatra;""")
    cur.execute("""Drop table Usuario;""")
   
    
    cur.execute("""
    CREATE TABLE Usuario(
        ID_Usuario VARCHAR(36) PRIMARY KEY,
        Nombre VARCHAR(45) NOT NULL,
        contrasena VARCHAR(45) NOT NULL,
        contacto VARCHAR(10)
    );
    """)
    
    cur.execute("""
                Create table Pediatra(
    ID_Pediatra varchar(36) primary key,
    Nombre varchar(45) not null,
    contrasena varchar(45) not null,
    contacto varchar(10)
);

""")
    
    cur.execute("""Create table Miembro(
    ID_Miembro varchar(36) primary key,
    ID_Usuario varchar(36),
    ID_Pediatra varchar(36),
    Nombre varchar(45) not null,
    aPaterno varchar(45) not null,
    aMaterno varchar(45) not null,
    CONSTRAINT fk_Usuario FOREIGN KEY (ID_Usuario) REFERENCES Usuario (ID_Usuario),
    CONSTRAINT fk_Pediatra FOREIGN KEY (ID_Pediatra) REFERENCES Pediatra (ID_Pediatra),
    CONSTRAINT Nombre_ch CHECK (Nombre ~* '^[A-Z,a-z, ,.,-áéíóúÁÉÍÓÚüÜñÑ]+$'),
    CONSTRAINT aPaterno_ch CHECK (aPaterno ~* '^[A-Z,a-z, ,.,-áéíóúÁÉÍÓÚüÜñÑ]+$'),
    CONSTRAINT aMaterno_ch CHECK (aMaterno ~* '^[A-Z,a-z, ,.,-áéíóúÁÉÍÓÚüÜñÑ]+$')
);
""")
    
    cur.execute("""Create table MiembroInfo(
    ID_Miembro varchar(36) primary key,
    Edad float not null,
    Estatura float not null,
    Peso float not null,
    Temperatura float not null,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_Miembro FOREIGN KEY (ID_Miembro) REFERENCES Miembro(ID_Miembro),
    constraint Edad_ch CHECK (Edad>=0.0)
);
""")
    
    conn.commit()

    conn.close()


if __name__ == "__main__":
    main()