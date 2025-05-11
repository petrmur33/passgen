import random
from tkinter import *
import string


def generate(upper: bool, lower: bool, digits: bool, special: bool, length: int) -> str:
    alphabet = ''
    if upper: alphabet += string.ascii_uppercase
    if lower: alphabet += string.ascii_lowercase
    if digits: alphabet += string.digits
    if special: alphabet += string.punctuation
    
    return ''.join(random.choices(alphabet, k=length))


def entry_update_text(entry: Entry, text: str) -> None:
    entry.delete(0, len(entry.get()))
    entry.insert(0, text)


def generate_button_clicked(entry: Entry, is_upper: BooleanVar, is_lower: BooleanVar, is_digits: BooleanVar, is_special: BooleanVar, length: StringVar) -> None:
    try:
        length_int = int(length.get())
    except ValueError:
        entry_update_text(entry, "Enter a correct integer")
        entry.configure(foreground='red')
        return
    generated = generate(is_upper.get(), is_lower.get(), is_digits.get(), is_special.get(), length_int)
    entry_update_text(entry, generated)
    entry.configure(foreground='black')
    entry.clipboard_clear()
    entry.clipboard_append(generated)


def main() -> None:
    root = Tk()
    root.geometry('560x140')
    root.title('Password Generator')
    root.resizable(width=False, height=False)

    is_upper = BooleanVar()
    is_lower = BooleanVar()
    is_digits = BooleanVar()
    is_special = BooleanVar()
    length = StringVar()

    settings_text = Label(root, text='Settings:')
    settings_text.grid(row=0, column=0)

    len_pass = Label(root, text='Length of password:')
    len_pass.grid(row=4, column=0)

    len_pass_input = Entry(root, textvariable=length)
    len_pass_input.grid(row=4, column=1)

    upper_flag = Checkbutton(root, text='Upper letters', variable=is_upper, onvalue=True, offvalue=False)
    upper_flag.grid(row=0, column=1, sticky='W')

    lower_flag = Checkbutton(root, text='Lower letters', variable=is_lower, onvalue=True, offvalue=False)
    lower_flag.grid(row=1, column=1, sticky='W')

    digits_flag = Checkbutton(root, text='Digits', variable=is_digits, onvalue=True, offvalue=False)
    digits_flag.grid(row=2, column=1, sticky='W')

    special_flag = Checkbutton(root, text='Special symbols', variable=is_special, onvalue=True, offvalue=False)
    special_flag.grid(row=3, column=1, sticky='W')

    output_entry = Entry(root)
    output_entry.grid(column=3, row=1)

    generate_button = Button(root, text='Generate', command=lambda : generate_button_clicked(output_entry, is_upper, is_lower, is_digits, is_special, length))
    generate_button.grid(row=0, column=3)

    root.mainloop()


if __name__ == "__main__":
    main()
