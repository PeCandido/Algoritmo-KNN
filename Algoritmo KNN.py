from math import sqrt

class Flor:
    sepal_length = -1
    sepal_width = -1
    petal_length = -1
    petal_width = -1
    name = ""

# Leitura do arquivo
def ler_arquivo(nome_arq):
    flores = []
    arq = open(f"{nome_arq}", "r")
    for linha in arq:
        info = linha.strip().split(',')
        f = Flor()
        f.sepal_length = float(info[0])
        f.sepal_width = float(info[1])
        f.petal_length = float(info[2])
        f.petal_width = float(info[3])
        f.name = info[4]
        flores.append(f)
    arq.close()
    return flores

# calculo da distância euclidiana 
def calcular_distancia(flor_d, flor_c):
    sepal_length1 = flor_d.sepal_length
    sepal_width1 = flor_d.sepal_width
    petal_length1 = flor_d.petal_length
    petal_width1 = flor_d.petal_width

    sepal_length2 = flor_c.sepal_length
    sepal_width2 = flor_c.sepal_width
    petal_length2 = flor_c.petal_length
    petal_width2 = flor_c.petal_width
            
    dist_euclidiana = sqrt(((sepal_length1 - sepal_length2)**2) + 
                            ((sepal_width1 - sepal_width2)**2) + 
                            ((petal_length1 - petal_length2)**2) + 
                            ((petal_width1 - petal_width2)**2))
    
    return dist_euclidiana

# Ordenação das distâncias em ordem crescente
def organizar_especies(flores_desconhecidas, flores_conhecidas):
    nomes = []                  
    for flor_des in flores_desconhecidas:
        distancias = []
        for flor_con in flores_conhecidas:
            dist_euclidiana = calcular_distancia(flor_des, flor_con) 
            distancias.append((flor_con.name, dist_euclidiana))
        nomes.append(distancias)
    
    ordenado = []
    for distancias in nomes:
        distancias_ordenadas = sorted(distancias, key= lambda valor: valor[1])
        ordenado.append(distancias_ordenadas)

    return ordenado

# Análise das K distâncias mais próximas
def frequencia(matriz, k):
    versicolor_cont = 0
    setosa_cont = 0
    virginica_cont = 0
    
    for i in range(k):
        especie = matriz[i][0]
        if "versicolor" in especie:
            versicolor_cont += 1
        
        elif "setosa" in especie:
            setosa_cont += 1
        
        elif "virginica" in especie:
            virginica_cont += 1
        
    
    if versicolor_cont > setosa_cont and versicolor_cont > virginica_cont:
        return "versicolor"
    
    elif setosa_cont > versicolor_cont and setosa_cont > virginica_cont:
        return "setosa"
    
    else:
        return "virginica"


def main():
    flores_conhecida = ler_arquivo("iris.data.csv")
    try:
        k = int(input("Valor K elementos (insira um valor numérico inteiro): ")) # Entrada dos K elementos mais próximos
        arquivo = input("Nome do arquivo: ") # Entrada do nome do arquivo sem o nome das espécies
        flores_desconhecida = ler_arquivo(arquivo)
    except:
        print("ERRO: não foi possivel realizar operação")
    else:
        distancias = organizar_especies(flores_desconhecida, flores_conhecida) 
        i = 0
        for dist in distancias:
            i += 1
            especie = frequencia(dist, k)
            print(f"Flor {i} é {especie}")

main()
