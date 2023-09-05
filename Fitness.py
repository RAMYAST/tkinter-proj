import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import StringVar

class GymApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gym Sources")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, GymPage, EquipmentPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="WELCOME!!!")
        label.pack(pady=10, padx=10)
        gym_button = ttk.Button(self, text="FITNESS FREAKZZZ",
                                command=lambda: controller.show_frame(GymPage))
        gym_button.pack()
        equipment_button = ttk.Button(self, text="GALLERY",
                                      command=lambda: controller.show_frame(EquipmentPage))
        equipment_button.pack()

class GymPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="HEALTH FITNESS GYM",font=("Helvetica", 20, "bold"))
        label.pack(pady=10, padx=10)
        nav_frame = tk.Frame(self)
        nav_frame.pack(fill="x")
        about_button = ttk.Button(nav_frame, text="ABOUT US",
                                      command=lambda: self.show_content("ABOUT"))
        join_button = ttk.Button(nav_frame, text="JOIN",
                                   command=lambda: self.show_content("JOIN"))
        packages_button = ttk.Button(nav_frame, text="PACKAGES",
                                    command=lambda: self.show_content("PACKAGES"))
        contact_button = ttk.Button(nav_frame, text="CONTACT US",
                                    command=lambda: self.show_content("CONTACT"))
        rules_button = ttk.Button(nav_frame, text="RULES",
                                    command=lambda: self.show_content("RULES"))

        
        about_button.pack(side="left")
        join_button.pack(side="left")
        packages_button.pack(side="left")
        contact_button.pack(side="left")
        rules_button.pack(side="left")
        
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill="both", expand=True)
        
        
        
        back_button = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)

    def show_content(self, content_type):
        for child in self.content_frame.winfo_children():
            child.destroy()
        
        if content_type == "ABOUT":
            content_frame = AboutContent(self.content_frame)
        elif content_type == "JOIN":
            content_frame = JoinContent(self.content_frame)
        elif content_type == "PACKAGES":
            content_frame = PackagesContent(self.content_frame)
        elif content_type == "CONTACT":
            content_frame = ContactContent(self.content_frame)
        elif content_type == "RULES":
            content_frame = RulesContent(self.content_frame)



        content_frame.pack(pady=10)


class AboutContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.text_area = tk.Text(self, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        paragraph = """
     ABOUT OUR HEALTHY FITNESS GYM

Welcome to our Healthy Fitness Gym, a cornerstone of wellness in the community since 2010. With a rich history spanning over a decade, we take immense pride in fostering healthier lives through dedicated fitness and expert guidance.

OUR JOURNEY:
Founded in 2010, our gym embarked on a mission to empower individuals to take charge of their well-being. Over the years, we have evolved with the changing fitness landscape, adapting and innovating to meet our members' diverse needs.

EXPERIENCED TEAM:
Our gym stands out for its exceptional staff. Our team of well-trained fitness professionals is committed to your success. With years of experience and expertise, they are here to provide personalized guidance, clarify doubts, and support you every step of the way.

A DECADE OF EXCELLENCE:
Celebrating a successful journey of a decade, we've achieved significant milestones. From expanding our facilities to introducing cutting-edge fitness programs, we have grown while maintaining our core values of health and vitality.

YOUR WELLNESS HUB:
We are more than just a gym; we are a community where doubts are clarified, friendships are forged, and wellness flourishes. We've cultivated an environment where everyone feels comfortable, motivated, and inspired to work regularly towards their fitness goals.

STAY FIT TOGETHER:
At our gym, we believe that the journey to fitness is best enjoyed together. Our members thrive on the camaraderie and shared commitment to staying fit. From invigorating group workouts to one-on-one sessions, we offer diverse options to suit every preference.

PROJECTING FORWARD:
As we move forward, our gym's vision remains steadfast—to promote a healthier lifestyle and make wellness a sustainable part of your life. With a decade of success behind us, we're excited about the future, where we'll continue to empower, motivate, and guide you towards your fitness aspirations.

Join us on this journey of health, positivity, and personal growth. Discover a place where doubts are resolved, fitness is a way of life, and wellness thrives. Welcome to the Healthy Fitness Gym family.
        """
        self.text_area.insert("1.0", paragraph)


class JoinContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Email:").grid(row=1, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Membership:").grid(row=4, column=0, padx=10, pady=5)
        self.membership_var = tk.StringVar(value="Basic")  
        membership_choices = ["Basic", "Standard", "Premium"]
        self.membership_dropdown = tk.OptionMenu(self, self.membership_var, *membership_choices)
        self.membership_dropdown.grid(row=4, column=1, padx=10, pady=5)

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=6, columnspan=2, pady=10)

    def submit_data(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        membership = self.membership_var.get()
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
        print("Address:", address)
        print("Membership:", membership)


        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

        back_button = ttk.Button(self, text="Back to Home",
                                 command=lambda: self.controller.show_frame(HomePage))
        back_button.grid(row=5, columnspan=2, pady=10)
       


class PackagesContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="""BASIC MEMBERSHIP:

Access to gym facilities and basic amenities.
Price Range: $30 - $80 per month.


GROUP FITNESS PACKAGE:

Unlimited access to group exercise classes.
Price Range: $50 - $150 per month.

PERSONAL TRAINING PACKAGE:

One-on-one sessions with a personal trainer.
Price Range: $50 - $150 per session, or $200 - $600 per month (2-3 sessions per week).

WEIGHT LOSS PACKAGE:

Customized workout plans, nutritional guidance, and progress tracking.
Price Range: $100 - $250 per month.""")
        label.pack()


class ContactContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="CONTACT : 9999999999 \n\n ADDRESS : 100, Ram Nagar, Coimbatore. \n \n follow on : \n \tFacebook : HEALTHY FITNESS \n Instagram : healthy_fit" )
        label.pack()


class RulesContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="""PROPER ATTIRE :

Members are usually required to wear appropriate workout attire, including athletic shoes and workout clothing, for hygiene and safety reasons.

TOWEL USAGE :

Many gyms require members to use a towel to cover equipment while using it and to wipe down equipment after use to maintain cleanliness.

HYGIENE:

Members are expected to maintain personal hygiene by using deodorant, cleaning hands, and showering before and after workouts.

Respect for Others:

Respectful behavior towards staff and fellow members is essential. This includes refraining from offensive language, loud conversations, and disruptive behavior.


Time Limits on Equipment:

To allow others to use the equipment, there might be time limits imposed during peak hours.

Cell Phone Usage:

Some gyms discourage excessive cell phone use on the gym floor to maintain focus and reduce congestion.


Safety Precautions:

Members should follow safety guidelines for equipment usage and avoid risky behavior to prevent injuries.

No Food or Drinks on the Gym Floor:

To maintain cleanliness and prevent spills, food and open drinks might be prohibited on the gym floor.

Membership Card/ID:

Members should carry and present their membership cards or IDs when entering the gym.

Locker Room Etiquette:

Respectful behavior and cleanliness are important in locker rooms. Lockers might be available for storing personal items.

Cancellation Policies:

If the gym offers classes or personal training sessions, there may be specific cancellation policies to avoid charges.

""")
        label.pack()



        
class EquipmentPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Equipment Source",font=("Helvetica", 20, "bold"))  
        label.pack(pady=10, padx=10)

         
        image_paragraphs = {
            "pic1.jpg": "The  FLAT BENCH PRESS  is quite short. It is best for any types of upper body exercise.Mainly best for the chest workouts. With this bench press, one needs to keep the back straight not in a position of the arch. Its market price starts from 9000 rupees."
        }

        for image_path, paragraph_text in image_paragraphs.items():
            image = Image.open(image_path)
            image = image.resize((250,100))
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(self, image=photo)
            image_label.image = photo
            image_label.pack()

            text_label = tk.Label(self, text=paragraph_text, wraplength=500)
            text_label.pack(pady=10)
            tk.Label(self, text="").pack()


        image_paragraphs = {
            "pic2.jpg": "TREADMILLS  are mostly used for cardio training. However, this fitness machine can be used for more boosting your cardiovascular health.It's ideal for strengthening your muscles, including glutes, thighs, and calves. With treadmill workouts, you can always optimize the sessions to suit your goals."
           
        }

        for image_path, paragraph_text in image_paragraphs.items():
            image = Image.open(image_path)
            image = image.resize((250,100))
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(self, image=photo)
            image_label.image = photo
            image_label.pack()

            text_label = tk.Label(self, text=paragraph_text, wraplength=500)
            text_label.pack(pady=10)
            tk.Label(self, text="").pack()

        image = Image.open("pic3.jpg")  
        image = image.resize((250,100))
        photo = ImageTk.PhotoImage(image)
        
        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.pack()

        paragraph_text = """
         DUMBBELLS   allow the user to focus on one arm or leg at a time, which is one way to initiate strength gains by using a heavy overload.
        A single dumbbell can be used for exercises such as a one-arm overhead press or a split-leg goblet squat to create overload in one limb at a time.
        """
        text_label = tk.Label(self, text=paragraph_text, wraplength=500)  
        text_label.pack(pady=10)





        back_button = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame(HomePage))
        back_button.pack(pady=10)




if __name__ == "__main__":
    app = GymApp()
    app.mainloop()
