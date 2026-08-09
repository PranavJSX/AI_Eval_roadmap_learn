from functions import (
    add_credential,
    get_credential,
    update_password,
    list_services,
    delete_credential,
    load_or_generate_key,
    load_vault
)

def main():

    cipher = load_or_generate_key()
    vault = load_vault()

    while True:
        print("--------------MY PASSWORD MANAGER !! PLEASE CHOOSE ONE OF THE BELOW OPTIONS--------------")
        print("1--------------ADD CREDENTIAL")
        print("2--------------GET CREDENTIAL")
        print("3-----------UPDATE CREDENTIAL")
        print("4-----------DELETE CREDENTIAL")
        print("5-----------LIST ALL SERVICES")
        print("6------------ALL DONE EXIT !!")

        choice = input("OPTION SELECT :").strip()
        
        if choice == "1":
            service = input("---ENTER SERVICE---").strip().lower()
            username = input("---ENTER USERNAME---").strip()
            password = input("---ENTER PASSWORD---").strip()
            add_credential(vault=vault, cipher=cipher, service=service,username=username, password=password)

        elif choice == "2":
            service = input("---ENTER SERVICE---").strip().lower()
            get_credential(vault=vault, cipher=cipher, service=service)

        elif choice == "3":
            service = input("---ENTER SERVICE---").strip().lower()
            password = input("---UPDATED PASSWORD---").strip()
            update_password(vault=vault, cipher=cipher, service=service, new_password=password)

        elif choice == "4":
            service = input("---ENTER SERVICE---").strip().lower()
            delete_credential(vault=vault, service=service)

        elif choice == "5":
            list_services(vault=vault)

        elif choice == "6":
            print("HAVE A GOOD DAY")
            break
        else:
            print("INVALID !! PLEASE CHOOSE OF THE VALID OPTIONS")

if __name__=="__main__":
    main()