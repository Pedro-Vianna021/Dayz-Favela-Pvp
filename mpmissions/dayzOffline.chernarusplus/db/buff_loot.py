import xml.etree.ElementTree as ET

# 1. Caminho do arquivo que vamos editar
file_path = 'types.xml'

def ajustar_loot():
    # 2. Carrega o arquivo XML
    tree = ET.parse(file_path)
    root = tree.getroot()

                # 3. Lista de itens que queremos "bombar" no servidor de Favela
                    alvos = ['AK74', 'M4A1', 'Magnum', 'UMP45']

                        print("Iniciando a recalibragem do loot...")

                            # 4. Percorre todos os elementos <type> no XML
                                for item in root.findall('type'):
                                        nome_item = item.get('name')

                                                # 5. Verifica se o item atual está na nossa lista de alvos
                                                        if any(alvo in nome_item for alvo in alvos):
                                                                    # Procura a tag <nominal> (quantidade total no mapa)
                                                                                nominal = item.find('nominal')
                                                                                            if nominal is not None:
                                                                                                            valor_antigo = nominal.text
                                                                                                                            # Dobra o valor do spawn
                                                                                                                                            novo_valor = int(valor_antigo) * 2
                                                                                                                                                            nominal.text = str(novo_valor)

                                                                                                                                                                                            print(f"Item: {nome_item} | Antigo: {valor_antigo} -> Novo: {novo_valor}")

                                                                                                                                                                                                # 6. Salva as alterações de volta no arquivo
                                                                                                                                                                                                    tree.write('types.xml', encoding='utf-8', xml_declaration=True)
                                                                                                                                                                                                        print("\nSucesso! O types.xml foi atualizado.")

                                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                            ajustar_loot())                                                                                                                                    ajustar_loot())
