from tkinter import *

# Initialize the main window
root = Tk()
root.title("PA0 - Aasav Badera(Roll No. - 18075001)")
# Define the size of the window
root.geometry("820x350")
# Text for encipher and decipher
encryptLabel = Label(
    root,
    text="Enter the text to encipher: ",
    padx=10,
    pady=10,
    font=("Times New Roman", 13),
)
decryptLabel = Label(
    root,
    text="Enter the text to decipher: ",
    padx=10,
    pady=10,
    font=("Times New Roman", 13),
)
emptyLabel = Label(root, text="    ")

# Input boxes
encryptBox = Text(root, bg="light yellow", width=40, borderwidth=5, height=10)
decryptBox = Text(root, bg="light yellow", width=40, borderwidth=5, height=10)

# Function to encrypt the text in Encrypt Box
def encrypt():
    # Fetch the string
    string = encryptBox.get("1.0", "end-1c")
    # Perform the transformation
    output = "".join(
        [
            chr(ord("a") + (25 + ord("a") - ord(ch)))
            if ord(ch) >= ord("a") and ord(ch) <= ord("z")
            else (
                chr(ord("A") + (25 + ord("A") - ord(ch)))
                if ord(ch) >= ord("A") and ord(ch) <= ord("Z")
                else ch
            )
            for ch in string
        ]
    )
    # Reset and print the output
    decryptBox.delete("1.0", END)
    decryptBox.insert("1.0", output)
    return


def decrypt():
    # Fetch the string
    string = decryptBox.get("1.0", "end-1c")
    # Perform the transformation
    output = "".join(
        [
            chr(ord("z") - (25 - ord("z") + ord(ch)))
            if ord(ch) >= ord("a") and ord(ch) <= ord("z")
            else (
                chr(ord("Z") - (25 - ord("Z") + ord(ch)))
                if ord(ch) >= ord("A") and ord(ch) <= ord("Z")
                else ch
            )
            for ch in string
        ]
    )
    # Reset and print the output
    encryptBox.delete("1.0", END)
    encryptBox.insert("1.0", output)
    return


# Place the input boxes and text messages in the main window
encryptLabel.grid(row=0, column=1, columnspan=4)
emptyLabel.grid(row=0, column=5)
emptyLabel.grid(row=0, column=0)
decryptLabel.grid(row=0, column=7, columnspan=4)
# Initialize the buttons for functionalities
encryptButton = Button(
    root, text="Encipher", command=encrypt, width=15, pady=15, background="dark grey"
)
encryptBox.grid(row=1, column=1, columnspan=4, rowspan=3)
encryptButton.grid(row=5, column=2, columnspan=2, rowspan=2)

decryptButton = Button(
    root, text="Decipher", command=decrypt, width=15, pady=15, background="dark grey"
)
decryptBox.grid(row=1, column=7, columnspan=4, rowspan=3)
decryptButton.grid(row=5, column=8, columnspan=2, rowspan=2)

# Implement the reset functionality
def reset():
    encryptBox.delete("1.0", END)
    decryptBox.delete("1.0", END)
    return


resetButton = Button(
    root, text="Reset", command=reset, width=15, pady=15, background="dark grey"
)
resetButton.grid(row=8, column=5, columnspan=2, rowspan=2)

root.mainloop()
