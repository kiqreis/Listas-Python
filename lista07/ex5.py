import ast, json
dic = input("Digite um dicionário: ")
print(ast.literal_eval(dic) == json.loads(dic)) 
