from tkinter import *

class Converter():
    """
    Temperature conversion tool (°C to "F or "F to "C)
    """

    def __init__(self, root):
        self.temp_frame = Frame(root, padx=15, pady=15)
        self.temp_frame.grid()

        # Heading
        self.temp_heading = Label(
            self.temp_frame,
            text="Temperature Convertor",
            font=("Arial", 18, "bold")
        )
        self.temp_heading.grid(row=0, pady=(0, 10))

        # Instructions
        instructions = (
            "Please enter a temperature below and then press "
            "one of the buttons to convert it from centigrade "
            "to Fahrenheit."
        )

        self.temp_instructions = Label(
            self.temp_frame,
            text=instructions,
            wraplength=300,
            justify="left"
        )
        self.temp_instructions.grid(row=1, pady=(0, 15))

        # Entry
        self.temp_entry = Entry(
            self.temp_frame,
            font=("Arial", 14),
            width=25
        )
        self.temp_entry.grid(row=2, pady=(0, 5))

        # Error label (hidden initially)
        self.temp_error = Label(
            self.temp_frame,
            text="Please enter a number",
            fg="#9C0000"
        )
        self.temp_error.grid(row=3, pady=(0, 15))

        # Buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(
            self.button_frame,
            text="To Celsius",
            bg="#990099",
            fg="#ffffff",
            font=("Arial", 12, "bold"),
            width=14
        )
        self.to_celsius_button.grid(row=0, column=0, padx=5)

        self.to_fahrenheit_button = Button(
            self.button_frame,
            text="To Fahrenheit",
            bg="#009900",
            fg="#ffffff",
            font=("Arial", 12, "bold"),
            width=14
        )
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5)
    # main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter(root)
    root.mainloop()
