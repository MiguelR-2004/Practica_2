import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("CONVERSIONES")
ventana.geometry("300x250")  # Ajustar el tamaño para incluir el Entry
ventana.configure(bg="skyblue")

titulo = tk.Label(ventana, text="CONVERSIONES", bg="skyblue", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

def toBin():
    try:
        numero = int(entry_resultado.get())
        resultado = bin(numero)[2:]  # Convertir a binario
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        print(f"Resultado en Binario: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número entero válido")

def toOct():
    try:
        numero = int(entry_resultado.get())
        resultado = oct(numero)[2:]  # Convertir a octal
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        print(f"Resultado en Octal: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número entero válido")

def toHex():
    try:
        numero = int(entry_resultado.get())
        resultado = hex(numero)[2:].upper()  # Convertir a hexadecimal
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        print(f"Resultado en Hexadecimal: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número entero válido")

# Entry para ingresar el número y mostrar el resultado
entry_resultado = tk.Entry(ventana, font=("Arial", 10), justify="center")
entry_resultado.pack(pady=10)

btn_binario = tk.Button(ventana, text="Binario", bg="white", fg="black", font=("Arial", 10, "bold"), command=toBin)
btn_binario.pack(pady=5)

btn_octal = tk.Button(ventana, text="Octal", bg="white", fg="black", font=("Arial", 10, "bold"), command=toOct)
btn_octal.pack(pady=5)

btn_hexadecimal = tk.Button(ventana, text="Hexadecimal", bg="white", fg="black", font=("Arial", 10, "bold"), command=toHex)
btn_hexadecimal.pack(pady=5)

ventana.mainloop()
