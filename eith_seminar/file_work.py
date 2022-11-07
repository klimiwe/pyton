import json
def load():
            with open('BD.json', 'r', encoding='utf-8') as file:  
                BD_local = json.load(file)  
            return BD_local
def save(inp):
            
            with open('BD.json', 'w', encoding='utf-8') as file:  
                file.write(json.dumps(inp,
                                    ensure_ascii=False)) 