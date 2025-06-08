#  oughlane



def display_menu():
    print("\n=== Gestionnaire de Liste de Courses ===")
    print("1. Ajouter un article")
    print("2. Supprimer un article")
    print("3. Afficher la liste")
    print("4. Quitter")

# Fonction principale
def main():
    shopping_list = [] 

    while True:
        display_menu()  
        choice = input("Entrez votre choix (1-4) : ")

        # Choix 1 : Ajouter un article
        if choice == '1':
            item = input("Entrez le nom de l'article à ajouter : ")
            shopping_list.append(item)  # Ajouter à la liste
            print(f"✅ '{item}' a été ajouté à la liste.")

        # Choix 2 : Supprimer un article
        elif choice == '2':
            item = input("Entrez le nom de l'article à supprimer : ")
            if item in shopping_list:
                shopping_list.remove(item)  # Supprimer de la liste
                print(f"🗑️ '{item}' a été supprimé de la liste.")
            else:
                print("⚠️ Article non trouvé dans la liste.")

        # Choix 3 : Afficher la liste
        elif choice == '3':
            if not shopping_list:
                print("🛒 La liste est vide.")
            else:
                print("\n🛍️ Liste de courses actuelle :")
                for i, article in enumerate(shopping_list, 1):
                    print(f"{i}. {article}")

        
        elif choice == '4':
            print("👋 Au revoir !")
            break

        # Choix invalide
        else:
            print("❌ Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

# Point d’entrée du script
if __name__ == "__main__":
    main()
