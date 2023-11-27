import psycopg2
from lxml import etree

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.port = '5432'
        self.user = 'postgres'
        self.password = 'root'
        self.database = 'webservices'

    def get_connection(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except psycopg2.Error as err:
            print(f"Error: {err}")
            return None

db = Database()

connection = db.get_connection()

if connection:
    cursor = connection.cursor()

    query = "SELECT id, nome, semestres, id_coordenador FROM curso"
    cursor.execute(query)

    results = cursor.fetchall()

    root = etree.Element('cursos')

    for result in results:
        curso = etree.SubElement(root, 'curso')
        id_element = etree.SubElement(curso, 'id')
        id_element.text = str(result[0])
        nome_element = etree.SubElement(curso, 'nome')
        nome_element.text = result[1]
        semestres_element = etree.SubElement(curso, 'semestres')
        semestres_element.text = str(result[2])
        id_coordenador_element = etree.SubElement(curso, 'id_coordenador')
        id_coordenador_element.text = str(result[3])

    tree = etree.ElementTree(root)
    tree.write('database.xml', pretty_print=True, encoding='utf-8')

    cursor.close()
    connection.close()
else:
    print("Falha ao obter conexão com o banco de dados.")
