from lxml import etree

def validar_dtd(xml_file, dtd_file):
    try:
        with open(dtd_file, 'rb') as dtd:
            dtd_content = etree.DTD(dtd)
        
        with open(xml_file, 'rb') as xml:
            xml_content = etree.parse(xml)
            dtd_content.assertValid(xml_content)
            print(f"O documento {xml_file} é válido em relação à DTD {dtd_file}.")
    except etree.DocumentInvalid as e:
        print(f"Erro de validação: {e}")

validar_dtd("professores.xml", "professores.dtd")

validar_dtd("disciplinas.xml", "disciplinas.dtd")

validar_dtd("cursos.xml", "cursos.dtd")