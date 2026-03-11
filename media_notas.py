def calcular_media(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")
    return sum(notas) / len(notas)


def main():
    num_media = int(input ("Digite quantos numeros serão usados: "))
    if num_media == 0:
        raise ValueError ("o número de elementos não pode ser zero")

    notas = []
    for i in range(1, (num_media+1)):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)

    media = calcular_media(notas)
    print(f"A média das notas é: {media:.2f}")


if __name__ == "__main__":
    main()
