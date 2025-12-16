import string
import random
import tkinter as tk
from tkinter import ttk, messagebox


## characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password(length, alphabets_count, digits_count, special_characters_count):
	"""Generate a random password based on the given parameters"""
	characters_count = alphabets_count + digits_count + special_characters_count

	## check the total length with characters sum count
	if characters_count > length:
		return None, "Characters total count is greater than the password length"

	## initializing the password
	password = []
	
	## picking random alphabets
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))

	## picking random digits
	for i in range(digits_count):
		password.append(random.choice(digits))

	## picking random special characters
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))

	## if the total characters count is less than the password length
	## add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	return "".join(password), None


class PasswordGeneratorGUI:
	def __init__(self, root):
		self.root = root
		self.root.title("Password Generator")
		self.root.geometry("500x400")
		self.root.resizable(False, False)
		
		# Style
		style = ttk.Style()
		style.configure('TLabel', font=('Arial', 10))
		style.configure('TButton', font=('Arial', 10))
		
		# Main frame
		main_frame = ttk.Frame(root, padding="20")
		main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
		
		# Title
		title_label = ttk.Label(main_frame, text="Password Generator", 
		                        font=('Arial', 16, 'bold'))
		title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
		
		# Length input
		ttk.Label(main_frame, text="Password length:").grid(row=1, column=0, sticky=tk.W, pady=5)
		self.length_var = tk.StringVar(value="12")
		length_entry = ttk.Entry(main_frame, textvariable=self.length_var, width=30)
		length_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
		
		# Alphabets count
		ttk.Label(main_frame, text="Number of letters:").grid(row=2, column=0, sticky=tk.W, pady=5)
		self.alphabets_var = tk.StringVar(value="4")
		alphabets_entry = ttk.Entry(main_frame, textvariable=self.alphabets_var, width=30)
		alphabets_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
		
		# Digits count
		ttk.Label(main_frame, text="Number of digits:").grid(row=3, column=0, sticky=tk.W, pady=5)
		self.digits_var = tk.StringVar(value="4")
		digits_entry = ttk.Entry(main_frame, textvariable=self.digits_var, width=30)
		digits_entry.grid(row=3, column=1, sticky=tk.W, pady=5)
		
		# Special characters count
		ttk.Label(main_frame, text="Number of special characters:").grid(row=4, column=0, sticky=tk.W, pady=5)
		self.special_var = tk.StringVar(value="4")
		special_entry = ttk.Entry(main_frame, textvariable=self.special_var, width=30)
		special_entry.grid(row=4, column=1, sticky=tk.W, pady=5)
		
		# Generate button
		generate_btn = ttk.Button(main_frame, text="Generate Password", 
		                          command=self.generate_password_click)
		generate_btn.grid(row=5, column=0, columnspan=2, pady=20)
		
		# Password result
		ttk.Label(main_frame, text="Generated password:").grid(row=6, column=0, sticky=tk.W, pady=5)
		self.password_text = tk.Text(main_frame, height=3, width=40, font=('Courier', 12))
		self.password_text.grid(row=7, column=0, columnspan=2, pady=5)
		
		# Copy button
		copy_btn = ttk.Button(main_frame, text="Copy", command=self.copy_password)
		copy_btn.grid(row=8, column=0, columnspan=2, pady=10)
		
	def generate_password_click(self):
		try:
			length = int(self.length_var.get())
			alphabets_count = int(self.alphabets_var.get())
			digits_count = int(self.digits_var.get())
			special_count = int(self.special_var.get())
			
			if length <= 0:
				messagebox.showerror("Error", "Length must be greater than 0")
				return
			
			password, error = generate_password(length, alphabets_count, digits_count, special_count)
			
			if error:
				messagebox.showerror("Error", error)
				return
			
			self.password_text.delete(1.0, tk.END)
			self.password_text.insert(1.0, password)
			
		except ValueError:
			messagebox.showerror("Error", "Please enter valid numeric values")
	
	def copy_password(self):
		password = self.password_text.get(1.0, tk.END).strip()
		if password:
			self.root.clipboard_clear()
			self.root.clipboard_append(password)
			messagebox.showinfo("Success", "Password copied to clipboard!")
		else:
			messagebox.showwarning("Warning", "No password to copy")


if __name__ == "__main__":
	root = tk.Tk()
	app = PasswordGeneratorGUI(root)
	root.mainloop()