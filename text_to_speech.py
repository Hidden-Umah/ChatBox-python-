from customtkinter import *
import pyttsx3 


app = CTk()
app.geometry('700x500')
app.resizable(False,False)
app.title("Voicen LEGEND")

#  The chat display Area
display_area = CTkTextbox(app, width=650 , height=400,state="disabled")
display_area.pack(pady=10)


#  this is the entry text box
text_box = CTkEntry(app , width=550 ,height=50, placeholder_text="Enter your prompt")
text_box.place(relx = 0.42, rely = 0.9 ,anchor = "center")

def clear_area():
    display_area.configure(state="normal")      
    display_area.delete("1.0", "end")           
    display_area.configure(state="disabled")  




#  clear button
clear_button = CTkButton(app,width=100,height=40, text="clear",corner_radius=32,bg_color="#FFFFFF",fg_color="#B4140F", command=clear_area)




# Send message function
def send_message():
    message = text_box.get()
    if message.strip():
        display_area.configure(state = "normal")
        display_area.insert("end", f"you: {message}","right")
        display_area.configure(state="disabled")
        display_area.see("end")
        text_box.delete(0,"end")
        clear_button.place(relx=0.87,rely=0.5,anchor="center")
        voice_button.place(relx=0.87,rely=0.4,anchor="center")
        


engine = pyttsx3.init()

# This is the button that sends to screen
send_button = CTkButton(app , width=100,height=40, text="send",corner_radius=32,bg_color="#ECEAEA",border_color="#032F4D",command=send_message)
send_button.place(relx = 0.9, rely= 0.9, anchor = "center")

def voice_it ():
    display_area.configure(state = "normal")
    message = display_area.get("1.0","end")
    display_area.configure(state="disabled")
    if message.strip():
       cleaned_message = message.replace('you:',"",1)
       engine.say(cleaned_message)
       engine.runAndWait()


voice_button = CTkButton(app , width=100,height=40, text="voice it",corner_radius=32,bg_color="#FFFFFF",border_color="#032F4D",command=voice_it)








app.mainloop()






    


