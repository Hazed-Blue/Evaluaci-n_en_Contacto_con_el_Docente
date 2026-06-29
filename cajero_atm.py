# =====================================================================
# PROYECTO: SISTEMA DE CAJERO BANCARIO AUTOMÁTICO (ATM)
# ASIGNATURA: LÓGICA DE PROGRAMACIÓN
# =====================================================================

def ejecutar_cajero():
    # --- CAPA DE DATOS: VARIABLES DE ESTADO INICIAL ---
    saldo = 1000.0
    pin_correcto = "2026"
    intentos = 3
    autenticado = False
    otra_transaccion = "S"
    
    print("=== BIENVENIDO A TU BANCO SEGURO ===")
    
    # --- BLOQUE DE AUTENTICACIÓN (Bucle Mientras / Controlled Loop) ---
    while intentos > 0 and not autenticado:
        pin_ingresado = input("Por favor, ingrese su PIN de 4 dígitos: ").strip()
        
        if pin_ingresado == pin_correcto:
            autenticado = True
            print("✔ Autenticación exitosa.")
        else:
            intentos -= 1
            print(f"❌ PIN incorrecto.")
            if intentos > 0:
                print(f"Intentos restantes: {intentos}")
                
    # --- CONTROL DE FALLO DE AUTENTICACIÓN ---
    if not autenticado:
        print("\n Cuenta Bloqueada por motivos de seguridad. Acérquese a una ventanilla.")
        return # Termina la ejecución del programa de forma segura
        
    # --- MENÚ PRINCIPAL Y ESTRUCTURAS REPETITIVAS ---
    while otra_transaccion.upper() == "S":
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        # --- ESTRUCTURAS CONDICIONALES SELECTIVAS MULTIBIFURCADAS ---
        if opcion == "1":
            # Opción 1: Consulta de saldos pura
            print(f"\n Su saldo disponible actual es: ${saldo:.2f}")
            
        elif opcion == "2":
            # Opción 2: Depósitos controlados
            try:
                monto_deposito = float(input("\nIngrese el monto a depositar: $"))
                if monto_deposito > 0:
                    saldo += monto_deposito
                    print(f"✔ Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
                else:
                    print(" Error: El monto debe ser mayor a cero.")
            except ValueError:
                print(" Error: Por favor, ingrese un número válido.")
                
        elif opcion == "3":
            # Opción 3: Retiros con verificación de fondos
            try:
                monto_retiro = float(input("\nIngrese el monto a retirar: $"))
                if monto_retiro > 0 and monto_retiro <= saldo:
                    saldo -= monto_retiro
                    print(f"✔ Retiro exitoso. Retire su efectivo.")
                    print(f"Nuevo saldo: ${saldo:.2f}")
                else:
                    print(" Error: Fondos insuficientes o monto inválido.")
            except ValueError:
                print(" Error: Por favor, ingrese un número válido.")
                
        elif opcion == "4":
            # Opción 4: Salida voluntaria del sistema
            print("\nGracias por utilizar nuestros servicios financieros.")
            break
            
        else:
            print(" Opción no válida. Intente nuevamente de la lista (1-4).")
            continue
            
        # --- MENÚ DE RETORNO / EVALUACIÓN CONTINUA ---
        if opcion != "4":
            otra_transaccion = input("\n¿Desea realizar otra transacción? (S/N): ").strip()
            
    print("\nGracias por operar con nosotros. ¡Que tenga un excelente día!")

# Punto de entrada estándar para la ejecución del script
if __name__ == "__main__":
    ejecutar_cajero()
