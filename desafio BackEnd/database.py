import sqlite3
DATABASE_NAME = "task.db"

#Cria a conexão com o banco de dados
def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

#Cria a tabela de tasks, contendo incremento automático de ID,
#nome da tarefa e descrição da mesma.
def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
            """
    ]
    db = get_db() 
    cursor = db.cursor()
    #após selecionar a conexão com o Banco, executa a Query definida
    for table in tables:
        cursor.execute(table)