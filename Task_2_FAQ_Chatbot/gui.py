import customtkinter as ctk
from bot import get_response


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ChatbotGUI:

    def __init__(self):

        self.root = ctk.CTk()
        self.root.title("Smart FAQ Chatbot")
        self.root.geometry("650x550")
        self.root.resizable(True, True)

        # HEADER
        self.title = ctk.CTkLabel(
            self.root,
            text="🤖 Smart FAQ Assistant",
            font=("Arial", 28, "bold"),
            text_color="#38bdf8"
        )
        self.title.pack(pady=15)

        # CHAT AREA
        self.chat_frame = ctk.CTkScrollableFrame(
            self.root,
            width=600,
            height=400,
            corner_radius=15
        )
        self.chat_frame.pack(pady=10, fill="both", expand=True)

        # INPUT FRAME
        self.input_frame = ctk.CTkFrame(self.root)
        self.input_frame.pack(fill="x", padx=10, pady=10)

        self.entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Ask something...",
            height=45,
            font=("Arial", 14)
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=5)

        self.send_btn = ctk.CTkButton(
            self.input_frame,
            text="Send",
            width=100,
            command=self.send_message
        )
        self.send_btn.pack(side="right", padx=5)

        # ENTER KEY
        self.root.bind("<Return>", lambda event: self.send_message())

    def add_message(self, text, sender):

        color = "#1f2937" if sender == "bot" else "#2563eb"
        anchor = "w" if sender == "bot" else "e"

        msg = ctk.CTkLabel(
            self.chat_frame,
            text=text,
            wraplength=500,
            fg_color=color,
            corner_radius=10,
            padx=10,
            pady=8
        )
        msg.pack(anchor=anchor, pady=5, padx=10)

    def send_message(self):

        user_text = self.entry.get().strip()
        self.entry.delete(0, "end")

        if not user_text:
            return

        self.add_message("You: " + user_text, "user")

        response = get_response(user_text)

        self.add_message("Bot: " + response, "bot")

    def run(self):
        self.root.mainloop()