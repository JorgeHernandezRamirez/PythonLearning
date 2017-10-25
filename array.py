if __name__ == "__main__":
    vectorElementos = [1, 2, 3, 4, 5, 6]
    print("Hay", vectorElementos.count(1), "veces el elemento 1");
    print(1 in vectorElementos);
    print(7 not in vectorElementos);
    vectorElementos.append(7)
    print(7 in vectorElementos);
    vectorElementos.pop()
    print(7 in vectorElementos);