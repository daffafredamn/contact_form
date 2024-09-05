import tkinter as tk

# Fungsi untuk menangani input dari tombol
def button_click(value):
    current = entry.get()
    if value == '.' and '.' in current:
        return  # Mencegah memasukkan lebih dari satu titik
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def button_clear():
    entry.delete(0, tk.END)

def button_backspace():
    current = entry.get()
    if len(current) > 0:
        entry.delete(len(current)-1)

def button_percentage():
    try:
        current = entry.get()
        result = float(current) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_equal():
    try:
        result = eval(entry.get())
        result_label.config(text=str(result))  # Menampilkan hasil di label
    except Exception as e:
        result_label.config(text="Error")

# Inisialisasi GUI window
root = tk.Tk()
root.title("Kalkulator Android")

# Mengatur ukuran dan warna background window
root.geometry("360x600")
root.configure(bg="#202020")

# Membuat input field
entry = tk.Entry(root, width=17, font=('Arial', 24), borderwidth=0, relief="solid", justify='right', bg="#505050", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Label untuk menampilkan hasil
result_label = tk.Label(root, text='', font=('Arial', 18), bg="#202020", fg="white")
result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky='w')

# Fungsi untuk membuat tombol dengan gaya
def create_button(text, row, column, bg_color, fg_color, width=5, height=2):
    button = tk.Button(root, text=text, width=width, height=height, font=('Arial', 18), bg=bg_color, fg=fg_color, 
                       borderwidth=0, command=lambda: button_click(text) if text not in ['C', '=', '←', '%'] else button_clear() if text == 'C' else button_equal() if text == '=' else button_backspace() if text == '←' else button_percentage())
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

# Warna-warna untuk desain kalkulator Android
button_colors = {
    'numbers': ('#333333', 'white'),  # Tombol angka
    'operations': ('#FF9500', 'white'),  # Tombol operasi (/, *, -, +)
    'other': ('#A6A6A6', 'black')  # Tombol lainnya (C, =, ←, %)
}

# Tombol angka dan operasi
buttons = [
    ('C', 2, 0, 'other'),
    ('←', 2, 1, 'other'),
    ('%', 2, 2, 'other'),
    ('/', 2, 3, 'operations'),
    ('7', 3, 0, 'numbers'),
    ('8', 3, 1, 'numbers'),
    ('9', 3, 2, 'numbers'),
    ('*', 3, 3, 'operations'),
    ('4', 4, 0, 'numbers'),
    ('5', 4, 1, 'numbers'),
    ('6', 4, 2, 'numbers'),
    ('-', 4, 3, 'operations'),
    ('1', 5, 0, 'numbers'),
    ('2', 5, 1, 'numbers'),
    ('3', 5, 2, 'numbers'),
    ('+', 5, 3, 'operations'),
    ('0', 6, 0, 'numbers'),  # Tombol 0 ditempatkan di kolom pertama dengan lebar lebih besar
]

# Membuat tombol berdasarkan list di atas
for (text, row, column, color_type) in buttons:
    bg_color, fg_color = button_colors[color_type]
    create_button(text, row, column, bg_color, fg_color)

# Tombol 0 lebih lebar, jadi ditempatkan secara khusus
button_0 = tk.Button(root, text='0', width=11, height=2, font=('Arial', 18), bg=button_colors['numbers'][0], fg=button_colors['numbers'][1], borderwidth=0, command=lambda: button_click('0'))
button_0.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Tambahkan tombol titik (.) di sebelah kiri tombol "="
button_dot = tk.Button(root, text='.', width=5, height=2, font=('Arial', 18), bg=button_colors['numbers'][0], fg=button_colors['numbers'][1], borderwidth=0, command=lambda: button_click('.'))
button_dot.grid(row=6, column=2, padx=5, pady=5)

# Tambahkan tombol "=" di kolom terakhir baris 6
button_equal = tk.Button(root, text='=', width=5, height=2, font=('Arial', 18), bg=button_colors['operations'][0], fg=button_colors['operations'][1], borderwidth=0, command=button_equal)
button_equal.grid(row=6, column=3, padx=5, pady=5)

# Menjalankan aplikasi GUI
root.mainloop()