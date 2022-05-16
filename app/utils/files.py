from unidecode import unidecode
from ..models.sale import Sale

def scrapper(file: bytes):
    
    class_sales = []
    dict_sales = []
    file_data = file.decode('UTF-8').split('\n')

    fields = list(map(lambda x: unidecode(x.lower().replace(' ', '_')), file_data[0].strip().split('\t')))
    rows = list(map(lambda x: x.strip().split('\t'), file_data[1:]))

    '''
    Associando os dados com seus respectivos campos
    '''
    for row in rows:
        dict_sales.append(dict(zip(fields, row)))
    
    '''
    Normalizando os dados
    '''
    try:
        total = 0
        for sale in dict_sales:
            sale['preco_unitario'] = float(sale['preco_unitario'])
            sale['quantidade'] = int(sale['quantidade'])
            sale['total'] = sale['preco_unitario'] * sale['quantidade']
            total += sale['total']
            class_sales.append(Sale(**sale))
        
        return {"dict": dict_sales, "class": class_sales, "total": total}

    except Exception as e:
        raise ValueError("Erro ao extrair as informações. Verifique o arquivo enviado.")
