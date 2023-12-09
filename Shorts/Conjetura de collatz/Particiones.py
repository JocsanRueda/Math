def count_solutions(n):
    # Inicializamos una lista para la programación dinámica.
    dp = [0] * (n + 1)
    
    # Caso base: Hay una única solución para n = 0 (sin tomar ningún número).
    dp[0] = 1

    # Llenamos la lista utilizando programación dinámica.
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]

# Ejemplo de uso:
n = 2000  # Cambia el valor de n según lo que necesites
solutions = count_solutions(n)
print(f"El número de soluciones enteras positivas para n = {n} es {solutions}")


