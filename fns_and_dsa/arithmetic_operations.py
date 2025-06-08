
#  prend trois paramètres : deux nombres (num1, num2) et une opération (operation)
def perform_operation(num1, num2, operation):
    # Si l'opération est "add" 
    if operation == "add":
        return num1 + num2

    # Si l'opération est "subtract" 
    elif operation == "subtract":
        return num1 - num2

    # Si l'opération est "multiply" 
    elif operation == "multiply":
        return num1 * num2

    # Si l'opération est "divide" 
    elif operation == "divide":
        # Vérifier si le deuxième nombre est zéro 
        if num2 == 0:
            return "Erreur: division par zéro"  # Message spécial pour éviter l'erreur
        return num1 / num2  # Division normale si num2 ≠ 0

    # Si l'opération n'est pas reconnue
    else:
        return "Opération invalide"
