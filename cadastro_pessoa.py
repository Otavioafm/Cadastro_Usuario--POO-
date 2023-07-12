dados=[]

while True:
  temp_dados={}
  
  while True:
    temp_dados['Nome']=str(input("Digite seu nome: ")).strip()
    if temp_dados['Nome'].isalpha():
      break
    else:
      print("ERRO! DIGITE APENAS LETRAS\n")
  
  while True:
    temp_dados['Idade']=str(input("\nDigite a sua idade: ")).strip()
    if temp_dados['Idade'].isdigit():
       break
    else:
      print("ERRO! DIGITE APENAS NÚMEROS\n")
  while True:
    temp_dados['Sexo']=str(input("\nDigite seu sexo [M/F]: ")).upper().strip()
    if temp_dados['Sexo']=="M" or temp_dados['Sexo']=="F":
      break
    else:
      print("ERRO! DIGITE APENAS [M ou F]\n")
      
  dados.append(temp_dados)
      
  continuar=str(input("\nDeseja continuar [S/N]: ")).upper().strip() 
  if continuar == "N":
      break
  elif continuar != "S":
      print("ERRO! DIGITE APENAS [S ou N]\n")
              
print("\nPessoas cadastradas:")
for pessoa in dados:
  print(pessoa['Nome'])
print("\nIdade dos Usuários:")

for idade_usuario in dados:
  print(idade_usuario['Idade'])

cont_M=0
cont_F=0
for sexo_total in dados:
  if sexo_total['Sexo']=="M":
    cont_M+=1
    
  elif sexo_total['Sexo']=="F":
    cont_F+=1
    
print(f"\nTotal de homens cadastrados: {cont_M}")
print(f"\nTotal de mulheres cadastradas:{cont_F}")