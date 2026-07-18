import customtkinter as ctk
from tkinter import messagebox, filedialog
from pathlib import Path
import pyttsx3
from gtts import gTTS
import pygame
import tempfile
import os

from translator import translate_text

# -------------------------------
# App Theme
# -------------------------------

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class TranslatorGUI:

    def __init__(self):

        self.root = ctk.CTk()
        self.root.title("🌍 AI Language Translator")
        self.root.geometry("1200x760")
        self.root.resizable(False, False)

        # Background Color
        self.root.configure(fg_color="#dbeafe")

        # Text To Speech
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)

        # -------------------------------
        # Languages
        # -------------------------------

        self.languages = {

            "🌐 Auto Detect": "auto",
            "🇬🇧 English": "en",
            "🇵🇰 Urdu": "ur",
            "🇸🇦 Arabic": "ar",
            "🇮🇳 Hindi": "hi",
            "🇫🇷 French": "fr",
            "🇩🇪 German": "de",
            "🇪🇸 Spanish": "es",
            "🇮🇹 Italian": "it",
            "🇷🇺 Russian": "ru",
            "🇹🇷 Turkish": "tr",
            "🇯🇵 Japanese": "ja",
            "🇰🇷 Korean": "ko",
            "🇨🇳 Chinese": "zh-CN",
            "🇵🇹 Portuguese": "pt",
            "🇳🇱 Dutch": "nl",
            "🇬🇷 Greek": "el",
            "🇵🇱 Polish": "pl",
            "🇸🇪 Swedish": "sv",
            "🇩🇰 Danish": "da",
            "🇳🇴 Norwegian": "no",
            "🇫🇮 Finnish": "fi",
            "🇹🇭 Thai": "th",
            "🇻🇳 Vietnamese": "vi",
            "🇮🇩 Indonesian": "id",
            "🇲🇾 Malay": "ms",
            "🇮🇱 Hebrew": "iw"

        }

        # -------------------------------
        # Main Card
        # -------------------------------

        self.main = ctk.CTkFrame(
            self.root,
            corner_radius=25,
            fg_color="white"
        )

        self.main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        # -------------------------------
        # Heading
        # -------------------------------

        self.title = ctk.CTkLabel(
            self.main,
            text="🌍 AI LANGUAGE TRANSLATOR",
            font=("Segoe UI", 30, "bold"),
            text_color="#2563eb"
        )

        self.title.pack(pady=(20, 5))

        self.subtitle = ctk.CTkLabel(
            self.main,
            text="Translate text into multiple languages instantly",
            font=("Segoe UI", 15),
            text_color="gray40"
        )

        self.subtitle.pack(pady=(0, 20))

        # -------------------------------
        # Language Selection
        # -------------------------------

        self.language_frame = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.language_frame.pack(pady=10)

        self.source = ctk.CTkComboBox(
            self.language_frame,
            values=list(self.languages.keys()),
            width=260,
            height=40,
            font=("Segoe UI", 15)
        )

        self.source.set("🌐 Auto Detect")

        self.source.grid(
            row=0,
            column=0,
            padx=15
        )

        target_languages = [
            lang for lang in self.languages.keys()
            if lang != "🌐 Auto Detect"
        ]

        self.target = ctk.CTkComboBox(
            self.language_frame,
            values=target_languages,
            width=260,
            height=40,
            font=("Segoe UI", 15)
        )

        self.target.set("🇬🇧 English")

        self.target.grid(
            row=0,
            column=1,
            padx=15
        )

        # -------------------------------
        # Input Label
        # -------------------------------

        self.input_label = ctk.CTkLabel(
            self.main,
            text="Input Text",
            font=("Segoe UI", 18, "bold")
        )

        self.input_label.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        self.input_box = ctk.CTkTextbox(
            self.main,
            height=170,
            corner_radius=15,
            font=("Segoe UI", 15)
        )

        self.input_box.pack(
            fill="x",
            padx=30
        )
                # -------------------------------
        # Buttons
        # -------------------------------

        self.button_frame = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.button_frame.pack(
            pady=25
        )

        self.translate_btn = ctk.CTkButton(
            self.button_frame,
            text="🌍 Translate",
            width=170,
            height=45,
            corner_radius=12,
            font=("Segoe UI", 15, "bold"),
            command=self.translate
        )

        self.translate_btn.grid(
            row=0,
            column=0,
            padx=10
        )

        self.clear_btn = ctk.CTkButton(
            self.button_frame,
            text="🗑 Clear",
            width=150,
            height=45,
            corner_radius=12,
            fg_color="#ef4444",
            hover_color="#dc2626",
            font=("Segoe UI", 15, "bold"),
            command=self.clear
        )

        self.clear_btn.grid(
            row=0,
            column=1,
            padx=10
        )

        self.save_btn = ctk.CTkButton(
            self.button_frame,
            text="💾 Save",
            width=150,
            height=45,
            corner_radius=12,
            fg_color="#16a34a",
            hover_color="#15803d",
            font=("Segoe UI", 15, "bold"),
            command=self.save
        )

        self.save_btn.grid(
            row=0,
            column=2,
            padx=10
        )

        self.listen_btn = ctk.CTkButton(
            self.button_frame,
            text="🔊 Listen",
            width=150,
            height=45,
            corner_radius=12,
            fg_color="#7c3aed",
            hover_color="#6d28d9",
            font=("Segoe UI", 15, "bold"),
            command=self.speak
        )

        self.listen_btn.grid(
            row=0,
            column=3,
            padx=10
        )

        # -------------------------------
        # Output Label
        # -------------------------------

        self.output_label = ctk.CTkLabel(
            self.main,
            text="Translated Text",
            font=("Segoe UI", 18, "bold")
        )

        self.output_label.pack(
            anchor="w",
            padx=35,
            pady=(10, 5)
        )

        self.output_box = ctk.CTkTextbox(
            self.main,
            height=170,
            corner_radius=15,
            font=("Segoe UI", 15)
        )

        self.output_box.pack(
            fill="x",
            padx=30,
            pady=(0, 20)
        )

        # Footer

        self.footer = ctk.CTkLabel(
            self.main,
            text="Developed with Python • CustomTkinter • Google Translate API",
            font=("Segoe UI", 12),
            text_color="gray50"
        )

        self.footer.pack(
            pady=(5, 15)
        )
        
            # ==========================================
    # Translate
    # ==========================================

    def translate(self):

        text = self.input_box.get("1.0", "end").strip()

        if text == "":
            messagebox.showwarning(
                "Warning",
                "Please enter some text."
            )
            return

        try:

            translated = translate_text(
                text,
                self.languages[self.source.get()],
                self.languages[self.target.get()]
            )

            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", translated)

        except Exception as e:

            messagebox.showerror(
                "Translation Error",
                str(e)
            )
            
        # ==========================================
    # Clear
    # ==========================================

    def clear(self):

        self.input_box.delete("1.0", "end")
        self.output_box.delete("1.0", "end")

    # ==========================================
    # Save
    # ==========================================

    def save(self):

        text = self.output_box.get("1.0", "end").strip()

        if text == "":
            messagebox.showwarning(
                "Warning",
                "Nothing to save."
            )
            return

        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )

        if file:
            try:
                with open(file, "w", encoding="utf-8") as f:
                    f.write(text)

                messagebox.showinfo(
                    "Success",
                    "Translation saved successfully!"
                )

            except Exception as e:
                messagebox.showerror("Error", str(e))

    # ==========================================
    # Speak / Listen
    # ==========================================

    def speak(self):

        text = self.output_box.get("1.0", "end").strip()

        if text == "":
            messagebox.showwarning(
                "Warning",
                "There is no translated text to read."
            )
            return

        try:
            # Get selected language code (optional future use)
            language = self.languages[self.target.get()]

            # Text-to-speech (offline)
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ==========================================
    # Run Application
    # ==========================================

    def run(self):

        self.root.mainloop()

    