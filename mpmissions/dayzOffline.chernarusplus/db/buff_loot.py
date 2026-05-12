import xml.etree.ElementTree as ET

file_path = 'types.xml'

def ajustar_loot():
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        alvos = ['AK74', 'M4A1', 'Magnum', 'UMP45']
        
        print("Iniciando a recalibragem do loot...")
        
        for item in root.findall('type'):
            nome_item = item.get('name')
            
            if nome_item and any(alvo in nome_item for alvo in alvos):
                nominal = item.find('nominal')
                if nominal is not None:
                    valor_antigo = nominal.text
                    novo_valor = int(valor_antigo) * 2
                    nominal.text = str(novo_valor)
                    print(f"Item: {nome_item} | Antigo: {valor_antigo} -> Novo: {novo_valor}")
                    
        tree.write('types.xml', encoding='utf-8', xml_declaration=True)
        print("\nSucesso! O types.xml foi atualizado.")
    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    ajustar_loot()