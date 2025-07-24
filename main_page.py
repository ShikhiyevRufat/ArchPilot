from customtkinter import*
from PIL import Image


win = CTk()

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
win_width = 569
win_height = 226

x_position = screen_width - 569 + 200
y_position = screen_height - 226 + 100

win.geometry(f"{win_width}x{win_height}+{x_position}+{y_position}")
win.overrideredirect(True)

transparent_color = '#000001' 
win.config(background=transparent_color)
win.attributes("-transparentcolor", transparent_color)
rounded_corner = CTkFrame(win, corner_radius=20, bg_color=transparent_color, fg_color="#252B2E")
rounded_corner.pack(fill="both", expand=True)

logo_file = 'images/logo.png'


top_frame = CTkFrame(rounded_corner, height=55, width=win_width-150, fg_color="#252B2E")
top_frame.pack()

body_frame = CTkFrame(rounded_corner, height=65, width=win_width-150, fg_color="#252B2E")
body_frame.pack()

tile_frame = CTkFrame(rounded_corner, width=win_width-150, fg_color="#252B2E")
tile_frame.pack()


options_language = ["Python", "C#", "Kotlin", "Dart", "JavaScript", "React", "Java"]
str_var_lang = StringVar(value="Choose Language")

option_menu_language = CTkOptionMenu(
    master=top_frame,
    values=options_language,
    corner_radius=20,
    fg_color="#515151",
    button_color="#515151",
    button_hover_color="#3A3A3A",
    variable=str_var_lang,
    width=200
)
option_menu_language.grid(row=0, column=0, sticky="w", padx=10, pady=10)

options_architecture = [
    "Monolithic",
    "Microservices",
    "Serverless",
    "Event-Driven",
    "Layered (N-tier)",
    "Hexagonal",
    "Clean",
    "MVVM",
    "MVP",
    "MVC",
    "CQRS",
    "Onion",
    "Headless",
    "Service-Oriented",
    "Modular",]


str_var_architect = StringVar(value="Choose Architecture")

option_menu_architecture = CTkOptionMenu(
    master=top_frame,
    values=options_architecture,
    corner_radius=20,
    fg_color="#515151",
    button_color="#515151",
    button_hover_color="#3A3A3A",
    variable=str_var_architect,
    width=200

)
option_menu_architecture.grid(row=0, column=1, sticky="e", padx=10, pady=10)

top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)

my_logo = CTkImage(dark_image=Image.open(logo_file), size=(43,44))
logo_label = CTkLabel(body_frame, image=my_logo, text="")
logo_label.pack(pady= 20)


prompt_entry = CTkEntry(tile_frame, height=40, width=win_width - 150, corner_radius=20, fg_color="#515151")
prompt_entry.place(x=0, y=30)

def get_data():
    from start_app import start
    prompt = prompt_entry.get()
    language = option_menu_language.get()
    architecture = option_menu_architecture.get()
    start(prompt, language, architecture)
    

send_button = CTkButton(
    tile_frame,
    text="➤",  
    width=30,
    height=25,
    corner_radius=20,
    bg_color="#515151",
    fg_color="#3A3A3A",
    hover_color="#2A2A2A",
    text_color="white",
    command=get_data
)
send_button.place(x=win_width - 205, y=38)


win.mainloop()