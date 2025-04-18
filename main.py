# import tkinter as tk
# from tkinter import ttk
# import pandas as pd
# import customtkinter as ctk
# import os
# from PIL import Image
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib
# matplotlib.use('TkAgg')
# import numpy as np
# import seaborn as sns
# from scipy.stats import norm
# from scipy.stats import zscore
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression, LinearRegression
# ctk.set_appearance_mode("Light")
#
# class GUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Heart Attack Predictor")
#         self.root.geometry(f"{1200}x{650}")
#         self.root.grid_rowconfigure(0,weight=1)
#         # self.root.grid_columnconfigure(0,weight=1)
#         self.root.grid_columnconfigure(1,weight=1)
#         self.root.grid_columnconfigure(2,weight=1)
#
#         self.sidebar_light="white"
#         self.sidebar_button_text_light="#201E1F"
#         self.content_frame1_light="#F4FAFF"
#         self.home_frames_light="white"
#         self.home_text_light="#201E1F"
#         self.sidebar_buttons_hover_light="#F6F4D2"
#
#         self.sidebar_dark = "#201E1F"
#         self.sidebar_button_text_dark = "#E2CFEA"
#         self.home_frames_dark = "#201E1F"
#         self.home_text_dark = ""
#         self.content_frame1_dark = "#E2CFEA"
#         self.sidebar_buttons_hover_dark=""
#         # Create a sidebar
#         self.sidebar = ctk.CTkFrame(root, corner_radius=0,fg_color=(self.sidebar_light,self.sidebar_dark),border_color="red")
#         self.sidebar.grid(row=0, column=0,rowspan=7, sticky="nsew")
#         self.sidebar.grid_rowconfigure(2,weight=1)
#         self.sidebar.grid_columnconfigure(1,weight=1)
#
#         self.logo_frame=ctk.CTkFrame(self.sidebar,corner_radius=0,fg_color=(self.sidebar_light,self.sidebar_dark))
#         self.logo_frame.grid(row=0,column=0,padx=(10,0),pady=(20,0),sticky="nsew")
#
#         self.buttons_frame=ctk.CTkFrame(self.sidebar,corner_radius=0,fg_color=(self.sidebar_light,self.sidebar_dark),width=150)
#         self.buttons_frame.grid(row=2,pady=(30,0),column=0,columnspan=2,sticky="nsew")
#         self.buttons_frame.grid_columnconfigure(0,weight=1)
#
#         # Create buttons in the sidebar
#         script_dir = os.path.dirname(os.path.realpath(__file__))
#         images_path = os.path.join(script_dir, "")
#         self.logo_image = ctk.CTkImage(Image.open(os.path.join(images_path, "menu.png")), size=(26, 26))
#         self.home_image = ctk.CTkImage(Image.open(os.path.join(images_path, "home.png")), size=(26, 26))
#         self.chart_image = ctk.CTkImage(Image.open(os.path.join(images_path, "chart.png")), size=(26, 26))
#         self.logo_label = ctk.CTkLabel(self.logo_frame, text=" Sidebar",text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark), image=self.logo_image, compound="left", font=ctk.CTkFont(size=20, weight="bold"))
#         self.logo_label.grid(row=0, column=0, padx=5, pady=10)
#         self.home_button = ctk.CTkButton(self.buttons_frame, corner_radius=10, height=40, border_spacing=10, text="Home", image=self.home_image,fg_color="transparent", text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark), hover_color=(self.sidebar_buttons_hover_light,self.sidebar_buttons_hover_dark), anchor="w", command=self.show_home,font=ctk.CTkFont("Poppins",size=16,weight="bold"))
#         self.home_button.grid(row=2, column=0, sticky="ew")
#
#         self.chart_viewer_button = ctk.CTkButton(self.buttons_frame, corner_radius=10, height=40, border_spacing=10, text="Chart Viewer", image=self.chart_image, fg_color="transparent", text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark), hover_color=(self.sidebar_buttons_hover_light,self.sidebar_buttons_hover_dark), anchor="w", command=self.show_data_viewer,font=ctk.CTkFont("Poppins",size=16,weight="bold"))
#         self.chart_viewer_button.grid(row=3, column=0, sticky="ew")
#
#         self.predict_button = ctk.CTkButton(self.buttons_frame, corner_radius=10, height=40, border_spacing=10, text="Predict", image=self.chart_image,fg_color="transparent", text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark), hover_color=(self.sidebar_buttons_hover_light,self.sidebar_buttons_hover_dark), anchor="w",command=self.predict_model,font=ctk.CTkFont("Poppins",size=16,weight="bold"))
#         self.predict_button.grid(row=4, column=0, sticky="ew")
#
#         self.appearance_mode_label = ctk.CTkLabel(self.sidebar, text="Appearance Mode:",text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark), anchor="w")
#         self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
#         self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self.sidebar, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
#         self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
#         self.appearance_mode_optionmenu.set("Light")
#         # Create a frame for content
#         self.show_home()
#
#     def show_home(self):
#         if 'self.content_frame1' in globals() and self.content_frame1.winfo_exists():
#             for widget in self.content_frame1.winfo_children():
#                 widget.destroy()
#             self.content_frame1.destroy()
#         if 'self.predict_frame' in globals() and self.predict_frame.winfo_children():
#             for widget in self.predict_frame.winfo_children():
#                 widget.destroy()
#             self.predict_frame.destroy()
#
#         # Create a new frame for home
#         self.content_frame = ctk.CTkFrame(self.root, corner_radius=0,
#                                           fg_color=(self.content_frame1_light, self.content_frame1_dark))
#         self.content_frame.grid(row=0, column=1, columnspan=15, rowspan=7, padx=10, sticky="nsew")
#         # self.content_frame.grid_rowconfigure(4,weight=1)
#
#         self.basic_desc_frame=ctk.CTkFrame(self.content_frame,corner_radius=0,fg_color=(self.content_frame1_light,self.content_frame1_dark))
#         self.basic_desc_frame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky="nsew")
#         self.basic_desc_frame.grid_rowconfigure((0,1),weight=1)
#         self.basic_desc_frame.grid_columnconfigure((0,3),weight=1)
#
#         #Frame for count
#         self.count_frame=ctk.CTkFrame(self.basic_desc_frame,corner_radius=10,width=250,height=100,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.count_frame.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky="nsew")
#
#         # Frame for Mean
#         self.mean_frame = ctk.CTkFrame(self.basic_desc_frame,corner_radius=10,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.mean_frame.grid(row=0, column=3, padx=(10, 0), pady=(10, 0), sticky="nsew")
#
#         self.std_frame=ctk.CTkFrame(self.basic_desc_frame,corner_radius=10,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.std_frame.grid(row=2,column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
#
#         self.heart_frame = ctk.CTkFrame(self.basic_desc_frame,corner_radius=10,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.heart_frame.grid(row=2, column=3, padx=(10, 0), pady=(10, 0), sticky="nsew")
#
#         self.user_frame=ctk.CTkFrame(self.content_frame,corner_radius=10,width=200,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.user_frame.grid(row=0,column=4,rowspan=4,padx=(10,0), pady=(10, 0),sticky="nsew")
#
#         self.acc_frame=ctk.CTkFrame(self.content_frame,corner_radius=10,width=200,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.acc_frame.grid(row=0,column=5,rowspan=4,padx=(10,0),pady=(10, 0),sticky="nsew")
#
#         self.chart_frame=ctk.CTkFrame(self.content_frame,width=400,height=200,corner_radius=10,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.chart_frame.grid(row=4,column=1,columnspan=2,rowspan=3,padx=(10,0),pady=(30,0),sticky="nsew")
#
#
#
#         self.bar_chart=ctk.CTkFrame(self.content_frame,width=400,corner_radius=10,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.bar_chart.grid(row=4,column=4,columnspan=5,padx=(20,0),pady=(30,0),sticky="nsew")
#
#
#         self.male_label=ctk.CTkLabel(self.count_frame,text="Male",width=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway",size=14))
#         self.male_label.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky="nsew")
#         self.male_value=ctk.CTkLabel(self.count_frame,text=str(male_count)+"\n",width=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway",size=18,weight='bold'))
#         self.male_value.grid(row=1,column=0,padx=(20,0),sticky="nsew")
#
#         self.female_label=ctk.CTkLabel(self.mean_frame,text="Female",width=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway",size=14))
#         self.female_label.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky="nsew")
#         self.female_value=ctk.CTkLabel(self.mean_frame,text=str(female_count),width=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway",size=18,weight='bold'))
#         self.female_value.grid(row=1,column=0,padx=(20,0),sticky="nsew")
#
#
#         self.chloes_label=ctk.CTkLabel(self.std_frame,text="Cholestrol",width=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway",size=14))
#         self.chloes_label.grid(row=0,column=0,padx=(10,0),pady=(10,0))
#         self.chloes_label=ctk.CTkLabel(self.std_frame,text=str(round(oa_chol,1))+"\n",width=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway",size=18,weight='bold'))
#         self.chloes_label.grid(row=1,column=0,padx=(20,0),sticky="nsew")
#
#         self.heart_label=ctk.CTkLabel(self.heart_frame,text="Heart Cases",width=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway",size=14))
#         self.heart_label.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky="nsew")
#         self.heart_value=ctk.CTkLabel(self.heart_frame,text=str(trg_count),width=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway",size=18,weight='bold'))
#         self.heart_value.grid(row=1,column=0,padx=(20,0),sticky="nsew")
#
#         self.mage_label = ctk.CTkLabel(self.user_frame, text="Male Avg Age          ", width=50, text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway", size=14))
#         self.mage_label.grid(row=0, column=0, padx=(10, 0),sticky="nsew")
#         self.mage_value = ctk.CTkLabel(self.user_frame, text=str(round(male_age_avg,1)), width=50, text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway", size=18, weight='bold'))
#         self.mage_value.grid(row=1, column=0, padx=(10, 0),pady=(10,0), sticky="nsew")
#
#         self.wage_label = ctk.CTkLabel(self.user_frame, text=("Female Avg Age          "), width=50, text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway", size=14))
#         self.wage_label.grid(row=2, column=0, padx=(10, 0), pady=(20, 0))
#         self.wage_value = ctk.CTkLabel(self.user_frame, text=str(round(female_age_avg,1)), width=50, text_color=(self.home_text_light,self.home_text_dark), font=ctk.CTkFont("Raleway", size=18, weight='bold'))
#         self.wage_value.grid(row=3, column=0, padx=(20, 0),pady=(10,0), sticky="nsew")
#
#         self.blood_label = ctk.CTkLabel(self.acc_frame, text="Fast Blood Sugar", width=50, text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont("Raleway", size=16))
#         self.blood_label.grid(row=0, column=0, padx=(10, 0), pady=(20, 0))
#         self.blood_value = ctk.CTkLabel(self.acc_frame, text=str(fbs_count), width=50, text_color=(self.home_text_light,self.home_text_dark), font=ctk.CTkFont("Raleway", size=18, weight='bold'))
#         self.blood_value.grid(row=1, column=0, padx=(10, 0),pady=(10,0), sticky="nsew")
#
#         self.gender_label = ctk.CTkLabel(self.acc_frame, text="Accuracy", width=50,text_color=(self.home_text_light, self.home_text_dark),font=ctk.CTkFont("Raleway", size=16))
#         self.gender_label.grid(row=2, column=0, padx=(10, 0), pady=(10, 0))
#         self.gender_value = ctk.CTkLabel(self.acc_frame, text="90%", width=50, text_color=(self.home_text_light,self.home_text_dark), font=ctk.CTkFont("Raleway", size=18, weight='bold'))
#         self.gender_value.grid(row=3, column=0, padx=(20, 0), pady=(10, 0), sticky="nsew")
#
#         self.countplot_heart_disease()
#         self.pie_chart()
#
#     def show_data_viewer(self):
#         if 'self.content_frame' in globals() and self.content_frame.winfo_exists():
#             for widget in self.content_frame.winfo_children():
#                 widget.destroy()
#             self.content_frame.destroy()
#         if 'self.predict_frame' in globals() and self.predict_frame.winfo_children():
#             for widget in self.predict_frame.winfo_children():
#                 widget.destroy()
#             self.predict_frame.destroy()
#         # Create a new frame for data viewer
#         self.content_frame1 = ctk.CTkFrame(self.root, corner_radius=0,
#                                            fg_color=(self.content_frame1_light, self.content_frame1_dark))
#         self.content_frame1.grid(row=0, column=1, columnspan=15, rowspan=7, sticky="nsew")
#
#
#         self.data_tabview=ctk.CTkTabview(self.content_frame1,corner_radius=30,width=830,height=600,text_color="black",fg_color=(self.content_frame1_light,self.content_frame1_dark),segmented_button_fg_color="white",segmented_button_selected_hover_color="#F5F1ED",segmented_button_unselected_color="white",segmented_button_selected_color="#F5F1ED")
#         self.data_tabview.grid(row=0,column=0,padx=(10,0),pady=(10,0),sticky="nsew")
#
#         self.datatab1=self.data_tabview.add('Tab 1')
#         self.datatab2 = self.data_tabview.add('Tab 2')
#         self.datatab3 = self.data_tabview.add('Tab 3')
#         self.datatab4 = self.data_tabview.add('Tab 4')
#         self.datatab5 = self.data_tabview.add('Tab 5')
#         self.datatab6 = self.data_tabview.add('Tab 6')
#
#         self.datatab2.grid_rowconfigure(0,weight=1)
#
#         self.subtabview2=ctk.CTkTabview(self.datatab2,corner_radius=30,width=250,height=250,text_color="black",fg_color=(self.home_frames_light,self.home_frames_dark),segmented_button_fg_color="white",segmented_button_selected_hover_color="#F5F1ED",segmented_button_unselected_color="white",segmented_button_selected_color="#F5F1ED")
#         self.subtabview2.grid(row=0,column=0,padx=10)
#
#         self.subtab1=self.subtabview2.add('Tab 1')
#         self.subtab2=self.subtabview2.add('Tab 2')
#
#         self.subtabview3 = ctk.CTkTabview(self.datatab2, corner_radius=30, width=250, height=250, text_color="black",fg_color=(self.home_frames_light,self.home_frames_dark), segmented_button_fg_color="white",segmented_button_selected_hover_color="#F5F1ED",segmented_button_unselected_color="white",segmented_button_selected_color="#F5F1ED")
#         self.subtabview3.grid(row=0, column=4, padx=10)
#
#         self.subtab3 = self.subtabview3.add('Tab 1')
#         self.subtab4 = self.subtabview3.add('Tab 2')
#
#
#         self.subtabview4=ctk.CTkTabview(self.datatab4, corner_radius=30, width=250, height=250, text_color="black",fg_color=(self.home_frames_light,self.home_frames_dark), segmented_button_fg_color="white",segmented_button_selected_hover_color="#F5F1ED",segmented_button_unselected_color="white",segmented_button_selected_color="#F5F1ED")
#         self.subtabview4.grid(row=0, column=4, padx=10)
#
#         self.subtab5=self.subtabview4.add('Tab 1')
#         self.subtab6 = self.subtabview4.add('Tab 2')
#
#
#
#         self.histogram_heart_agewise()
#         self.countplot_sex()
#         self.countplot_gender()
#         self.countplot_chestpain_prone()
#         self.countplot_fbs_target()
#         self.histogram_chol_person()
#         self.hist_chol_density()
#         self.hist_chol_gender()
#         self.histplot_chol_heart()
#         self.heatmap_corr()
#         self.hist_norm_age()
#
#     def predict_model(self):
#         if 'self.content_frame' in globals() and self.content_frame.winfo_exists():
#             for widget in self.content_frame.winfo_children():
#                 widget.destroy()
#             self.content_frame.destroy()
#         if 'self.content_frame1' in globals() and self.content_frame1.winfo_children():
#             for widget in self.content_frame1.winfo_children():
#                 widget.destroy()
#             self.content_frame1.destroy()
#         if 'self.model_tabview' in globals() and self.model_tabview.winfo_children():
#             for widget in self.model_tabview.winfo_children():
#                 widget.destroy()
#             self.model_tabview.destroy()
#
#         # Create a new frame for prediction
#
#         self.predict_frame = ctk.CTkFrame(self.root, corner_radius=0,fg_color=(self.content_frame1_light, self.content_frame1_dark))
#         self.predict_frame.grid(row=0, column=1, columnspan=15, rowspan=7, sticky="nsew")
#         self.predict_frame.grid_rowconfigure(0,weight=1)
#         self.predict_frame.grid_columnconfigure(0,weight=1)
#
#         self.entry_frame=ctk.CTkFrame(self.predict_frame,corner_radius=10,fg_color=("white",self.content_frame1_dark))
#         self.entry_frame.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
#         self.heading_label=ctk.CTkLabel(self.entry_frame,text="Prediction",width=50,height=50,text_color=(self.home_text_light,self.home_text_dark),font=ctk.CTkFont('Raleway',size=24,weight='bold'))
#         self.heading_label.grid(row=0,column=0,padx=10,pady=10)
#
#
#         self.age_label=ctk.CTkLabel(self.entry_frame,text="Age:",text_color=(self.home_text_light,self.home_text_dark),width=50,font=ctk.CTkFont('Raleway',size=16))
#         self.age_label.grid(row=2,column=0,padx=(10,0),pady=(10,0))
#         self.age_entry=ctk.CTkEntry(self.entry_frame,placeholder_text="Enter Age",width=200,height=50,border_width=2,corner_radius=10,fg_color=(self.home_frames_light,self.home_frames_dark))
#         self.age_entry.grid(row=2,column=1,columnspan=2,padx=(10,0),pady=(10,0))
#
#         self.sex_label = ctk.CTkLabel(self.entry_frame, text="Gender:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.sex_label.grid(row=3, column=0, padx=(10, 0), pady=(10, 0))
#         self.sex_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter Male or Female", width=200, height=50, border_width=2, corner_radius=10,fg_color=(self.home_frames_light, self.home_frames_dark))
#         self.sex_entry.grid(row=3, column=1,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#
#         self.cp_label = ctk.CTkLabel(self.entry_frame, text="Chest Pain:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.cp_label.grid(row=4, column=0, padx=(10, 0), pady=(10, 0))
#         self.cp_menu = ctk.CTkOptionMenu(self.entry_frame,values=["Typical_angina","Atypical_angina","Non_anginal","Asymptomatic"], width=200, corner_radius=5,fg_color=(self.home_frames_light, self.home_frames_dark),text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark))
#         self.cp_menu.grid(row=4, column=1,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.trest_label = ctk.CTkLabel(self.entry_frame, text="Blood Pressure:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.trest_label.grid(row=5, column=0, padx=(10, 0), pady=(10, 0))
#         self.trest_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter BP", width=200, height=50, border_width=2, corner_radius=10,fg_color=(self.home_frames_light, self.home_frames_dark))
#         self.trest_entry.grid(row=5, column=1,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.chol_label = ctk.CTkLabel(self.entry_frame, text="Cholestrol:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.chol_label.grid(row=6, column=0, padx=(10, 0), pady=(10, 0))
#         self.chol_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter Chol", width=200, height=50, border_width=2, corner_radius=10,fg_color=(self.home_frames_light, self.home_frames_dark))
#         self.chol_entry.grid(row=6, column=1,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.fbs_label = ctk.CTkLabel(self.entry_frame, text="Fast BP(>120):",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.fbs_label.grid(row=7, column=0, padx=(10, 0), pady=(10, 0))
#         self.fbs_menu = ctk.CTkOptionMenu(self.entry_frame,values=["Yes","No"], width=200, corner_radius=5,fg_color=(self.home_frames_light, self.home_frames_dark),text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark))
#         self.fbs_menu.grid(row=7, column=1,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.cm_label = ctk.CTkLabel(self.entry_frame, text="Cardiographic Measurement:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.cm_label.grid(row=8, column=0, padx=(10, 0), pady=(10, 0))
#         self.cm_menu = ctk.CTkOptionMenu(self.entry_frame,values=["Normal","Abnormal","Hypertropy"], width=200, corner_radius=5,fg_color=(self.home_frames_light, self.home_frames_dark),text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark))
#         self.cm_menu.grid(row=8, column=1,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.ch_label = ctk.CTkLabel(self.entry_frame, text="Heart Rate(max):",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.ch_label.grid(row=9, column=0, padx=(10, 0), pady=(10, 0))
#         self.ch_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter Heart Rate", width=200, height=50, border_width=2, corner_radius=10,fg_color=(self.home_frames_light, self.home_frames_dark))
#         self.ch_entry.grid(row=9, column=1,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.ng_label = ctk.CTkLabel(self.entry_frame, text="Excercised Induced Angina:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.ng_label.grid(row=10, column=0, padx=(10, 0), pady=(10, 0))
#         self.ng_menu = ctk.CTkOptionMenu(self.entry_frame,values=["Yes","No"], width=200, corner_radius=5,fg_color=(self.home_frames_light, self.home_frames_dark),text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark))
#         self.ng_menu.grid(row=10, column=1,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.old_label = ctk.CTkLabel(self.entry_frame, text="ST Depression:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.old_label.grid(row=2, column=4, padx=(20, 0), pady=(10, 0))
#         self.old_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter ST", width=200, height=50, border_width=2, corner_radius=10,fg_color=(self.home_frames_light, self.home_frames_dark))
#         self.old_entry.grid(row=2, column=5,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.cg_label = ctk.CTkLabel(self.entry_frame, text="Slope of ST:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.cg_label.grid(row=3, column=4, padx=(10, 0), pady=(10, 0))
#         self.cg_menu = ctk.CTkOptionMenu(self.entry_frame,values=["Upsloping","Flat","Downsloping"], width=200, corner_radius=5,fg_color=(self.home_frames_light, self.home_frames_dark),text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark))
#         self.cg_menu.grid(row=3, column=5,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.ca_label = ctk.CTkLabel(self.entry_frame, text="Major Blood Vessels:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.ca_label.grid(row=4, column=4, padx=(10, 0), pady=(10, 0))
#         self.ca_menu = ctk.CTkOptionMenu(self.entry_frame,values=["0","1","2","3","4"], width=200, corner_radius=5,fg_color=(self.home_frames_light, self.home_frames_dark),text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark))
#         self.ca_menu.grid(row=4, column=5,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.thal_label = ctk.CTkLabel(self.entry_frame, text="Thalassemia:",text_color=(self.home_text_light, self.home_text_dark), width=50,font=ctk.CTkFont('Raleway', size=16))
#         self.thal_label.grid(row=5, column=4, padx=(10, 0), pady=(10, 0))
#         self.thal_menu = ctk.CTkOptionMenu(self.entry_frame,values=["NULL","Defect","Normal","Reversible"], width=200, corner_radius=5,fg_color=(self.home_frames_light, self.home_frames_dark),text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark))
#         self.thal_menu.grid(row=5, column=5,columnspan=2, padx=(10, 0), pady=(10, 0))
#
#         self.predict = ctk.CTkButton(self.entry_frame, corner_radius=10, height=40, border_spacing=10, text="Predict",fg_color=self.sidebar_light, text_color=(self.sidebar_button_text_light,self.sidebar_button_text_dark), hover_color=(self.sidebar_buttons_hover_light,self.sidebar_buttons_hover_dark), anchor="w", command=self.linear_logistic,font=ctk.CTkFont("Poppins",size=16,weight="bold"))
#         self.predict.grid(row=10, column=5, sticky="ew")
#     def linear_logistic(self):
#         # LINEAR REGRESSION
#
#         # Feature selection for linear regression
#         selected_features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak',
#                              'slope', 'ca', 'thal']
#         X = data[selected_features]
#         Y = data['target']
#
#         # Splitting the data into training and testing sets
#         X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
#
#         # Creating and training the linear regression model
#         linear_model = LinearRegression()
#         linear_model.fit(X_train, Y_train)
#         scaler = StandardScaler()
#         X_train_scaled = scaler.fit_transform(X_train)
#         model = LogisticRegression(max_iter=1000)
#         model.fit(X_train_scaled, Y_train)
#
#
#         # Predicting with more features
#         # self.age = 53
#         # self.gender= 0
#         # self.cp= 0
#         # self.trest= 128
#         # self.chol=230
#         # self.fbs=0
#         # self.cg=0
#         # self.ch=169
#
#         self.age = self.age_entry.get()
#         self.gender = self.sex_entry.get()
#         self.cp = self.cp_menu.get()
#         self.trest = self.trest_entry.get()
#         self.chol = self.chol_entry.get()
#         self.fbs = self.fbs_menu.get()
#         self.cm = self.cm_menu.get()
#         self.ch = self.ch_entry.get()
#         self.ng=self.ng_menu.get()
#         self.old=self.old_entry.get()
#         self.cg=self.cg_menu.get()
#         self.ca=self.ca_menu.get()
#         self.thal=self.thal_menu.get()
#
#         if self.gender == "Male":
#             self.gender = "1"
#         elif self.gender == "Female":
#             self.gender = "0"
#
#         if self.cp == "Typical_angina":
#             self.cp = "0"
#         elif self.cp == "Atypical_angina":
#             self.cp = "1"
#         elif self.cp == "Non_anginal":
#             self.cp = "2"
#         elif self.cp == "Asymptomatic":
#             self.cp = "3"
#
#
#         if self.cm=="Normal":
#             self.cm="0"
#         elif self.cm=="Abnormal":
#             self.cm="1"
#         elif self.cm=="Hypertropy":
#             self.cm:"2"
#
#         if self.fbs == "Yes":
#             self.fbs = "1"
#         elif self.fbs == "No":
#             self.fbs = "0"
#
#         if self.cg == "Upsloping":
#             self.cg = "0"
#         elif self.cg == "Flat":
#             self.cg = "1"
#         elif self.cg =="Downsloping":
#             self.cg = "2"
#
#         if self.ng=="Yes":
#             self.ng="1"
#         elif self.ng=="No":
#             self.ng="0"
#
#         if self.thal=="NULL":
#             self.thal="0"
#         elif self.thal=="Defect":
#             self.thal="1"
#         elif self.thal=="Normal":
#             self.thal="2"
#         elif self.thal=="Reversible":
#             self.thal="3"
#
#             # Check that all values are not empty
#         if self.age and self.gender and self.cp and self.trest and self.chol and self.fbs and self.cg and self.ch:
#                 # Convert the values to integers and create the array
#                 new_data = np.array([[int(self.age), int(self.gender), int(self.cp), int(self.trest), int(self.chol), int(self.fbs), int(self.cm), int(self.ch), int(self.ng), float(self.old),int(self.cg),int(self.ca),int(self.thal)]])
#                 linear_prediction = linear_model.predict(new_data)
#
#                 new_data_scaled = scaler.transform(new_data)
#                 prediction = model.predict(new_data_scaled)
#
#                 for widget in self.predict_frame.winfo_children():
#                     widget.destroy()
#                 self.model_tabview = ctk.CTkTabview(self.predict_frame, corner_radius=30, width=830, height=600,
#                                                    text_color="black",
#                                                    fg_color=(self.content_frame1_light, self.content_frame1_dark),
#                                                    segmented_button_fg_color="white",
#                                                    segmented_button_selected_hover_color="#F5F1ED",
#                                                    segmented_button_unselected_color="white",
#                                                    segmented_button_selected_color="#F5F1ED")
#                 self.model_tabview.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
#                 self.modtab1=self.model_tabview.add('Linear 1')
#                 self.modtab2=self.model_tabview.add('Logistic 1')
#                 self.modtab3 = self.model_tabview.add('Logistic 2')
#                 self.modtab4 = self.model_tabview.add('Logistic 3')
#                 self.modtab5 = self.model_tabview.add('Logistic 4')
#
#
#                 #Linear Regression Graph
#                 fig1,ax1=plt.subplots(figsize=(9, 6))
#                 plt.scatter(X_test['age'], Y_test, c='red', label='Heart Problem (Actual)')
#                 ax1.plot(X_test['age'], linear_model.predict(X_test), color='blue', label='Linear Regression Line')
#                 ax1.set_title('Age vs Heart Disease (Linear Regression)')
#                 ax1.set_xlabel('Age')
#                 ax1.set_ylabel('Heart Disease')
#                 canvas1 = FigureCanvasTkAgg(fig1, master=self.modtab1)
#                 canvas1.draw()
#                 canvas1.get_tk_widget().grid(row=0, column=0, padx=20)
#
#
#                 # # Scatter plot and regression line with Z-Score of Age vs Heart Disease
#                 fig2,ax2=plt.subplots(figsize=(9, 6))
#                 plt.scatter(zscore(X_test['age']), Y_test, c='red', label='Heart Problem')
#                 sns.regplot(x=zscore(X_test['age']), y=model.predict(X_test), data=data, logistic=True, ci=None,
#                             scatter=False, color='blue', line_kws={'color': 'blue'})
#                 ax2.set_title('Age vs Heart Disease with Z-Score')
#                 ax2.set_xlabel('Age Z-score')
#                 ax2.set_ylabel('Heart Disease')
#                 canvas2 = FigureCanvasTkAgg(fig2, master=self.modtab2)
#                 canvas2.draw()
#                 canvas2.get_tk_widget().grid(row=0, column=0, padx=20)
#
#
#                 # Scatter plot and regression line for Age vs Heart Disease
#                 fig3,ax3=plt.subplots(figsize=(9, 6))
#                 plt.scatter(X_test['age'], Y_test, c='red', label='Heart Problem')
#                 sns.regplot(x=X_test['age'], y=model.predict(X_test), data=data, logistic=True, ci=None,
#                             scatter=False, color='blue', line_kws={'color': 'blue'})
#                 ax3.set_title('Age vs Heart Disease')
#                 ax3.set_xlabel('Age')
#                 ax3.set_ylabel('Heart Disease')
#                 canvas3 = FigureCanvasTkAgg(fig3, master=self.modtab3)
#                 canvas3.draw()
#                 canvas3.get_tk_widget().grid(row=0, column=0, padx=20)
#
#                 #
#                 # # Scatter plot and regression line for Chest-Pain vs Heart Disease
#                 fig4,ax4=plt.subplots(figsize=(9, 6))
#                 plt.scatter(X_test['cp'], Y_test, c='red', label='Heart Problem')
#                 sns.regplot(x=X_test['cp'], y=model.predict(X_test), data=data, logistic=True, ci=None,
#                             scatter=False, color='blue', line_kws={'color': 'blue'})
#                 ax4.set_title('Chest-Pain vs Heart Disease')
#                 ax4.set_xlabel('Chest-Pain')
#                 ax4.set_ylabel('Heart Disease')
#                 canvas4 = FigureCanvasTkAgg(fig4, master=self.modtab4)
#                 canvas4.draw()
#                 canvas4.get_tk_widget().grid(row=0, column=0, padx=20)
#                 #
#                 # # Scatter plot and regression line for Sex vs Heart Disease
#                 fig5,ax5=plt.subplots(figsize=(9, 6))
#                 plt.scatter(X_test['sex'], Y_test, c='red', label='Heart Problem')
#                 sns.regplot(x=X_test['sex'], y=model.predict(X_test), data=data, logistic=True, ci=None,
#                             scatter=False, color='blue', line_kws={'color': 'blue'})
#                 ax5.set_title('Sex vs Heart Disease')
#                 ax5.set_xlabel('Sex')
#                 ax5.set_ylabel('Heart Disease')
#                 canvas5 = FigureCanvasTkAgg(fig5, master=self.modtab5)
#                 canvas5.draw()
#                 canvas5.get_tk_widget().grid(row=0, column=0, padx=20)
#
#                 print("Logistic Regression")
#                 if prediction[0] == 0:
#                     print("The person does not have any heart disease.")
#
#                 else:
#                     print("The person has heart disease.")
#
#                 print("Linear Regression")
#                 if linear_prediction[0] < 0.5:
#                     print("The person does not have any heart disease.")
#                 else:
#                     print("The person has heart disease.")
#         else:
#             print("Please enter values for all fields.")
#
#
#         # Logistics Model
#
#     def change_appearance_mode_event(self, new_appearance_mode: str):
#         ctk.set_appearance_mode(new_appearance_mode)
#         appearance_mode=ctk.get_appearance_mode()
#         if appearance_mode=="Dark":
#             self.histogram_heart_agewise()
#             self.countplot_sex()
#             self.countplot_gender()
#             self.countplot_chestpain_prone()
#             self.countplot_fbs_target()
#             self.histogram_chol_person()
#             # self.histogram_chol()
#             self.hist_chol_density()
#             self.hist_chol_gender()
#             self.histplot_chol_heart()
#             self.heatmap_corr()
#             self.hist_norm_age()
#             self.countplot_heart_disease()
#             self.pie_chart()
#     def countplot_heart_disease(self):
#         fig1, ax1 = plt.subplots(figsize=(4,4))
#         sns.countplot(x='target', data=data, ax=ax1)
#         ax1.set_xticklabels(['less chance', 'more chance'])
#         ax1.set_title('Chances of Heart Disease')
#         appear_mode=ctk.get_appearance_mode()
#         if appear_mode=="Dark":
#
#             fig1.set_facecolor(self.home_frames_dark)
#             ax1.set_facecolor(self.home_frames_dark)
#         else:
#             fig1.set_facecolor("none")
#             ax1.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig1, master=self.bar_chart)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0,column=0,padx=20)
#
#
#     def histogram_heart_agewise(self):
#         fig2, ax2 = plt.subplots(figsize=(9,6))
#         data['age'].hist(bins=20, ax=ax2)
#         ax2.set_title('Number of People Having Heart Disease Age Wise')
#         ax2.set_xlabel('Age')
#         ax2.set_ylabel('No. of Persons')
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig2.set_facecolor(self.home_frames_dark)
#             ax2.set_facecolor(self.home_frames_dark)
#         else:
#             fig2.set_facecolor("none")
#             ax2.set_facecolor("none")
#         canvas2 = FigureCanvasTkAgg(fig2, master=self.datatab1)
#         canvas2.draw()
#         canvas2.get_tk_widget().grid(row=0,column=0)
#
#     def countplot_sex(self):
#         fig3, ax3 = plt.subplots(figsize=(4, 4))
#         sns.countplot(x='sex', data=data, ax=ax3)
#         ax3.set_xticklabels(['Females', 'Males'])
#         ax3.set_title('Number of Males and Females')
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig3.set_facecolor(self.home_frames_dark)
#             ax3.set_facecolor(self.home_frames_dark)
#         else:
#             fig3.set_facecolor("none")
#             ax3.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig3, master=self.subtab1)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0, column=0, padx=20)
#     def countplot_gender(self):
#             fig4,ax4 = plt.subplots(figsize=(4, 4))
#             sns.countplot(x='sex', data=data, hue='target', ax=ax4)
#             ax4.set_xticklabels(['Females', 'Males'])
#             ax4.set_title('Chances of Heart Disease Gender Wise')
#             ax4.legend(labels=['Less Chance', 'High Chance'])
#             appear_mode = ctk.get_appearance_mode()
#             if appear_mode == "Dark":
#                 fig4.set_facecolor(self.home_frames_dark)
#                 ax4.set_facecolor(self.home_frames_dark)
#             else:
#                 fig4.set_facecolor("none")
#                 ax4.set_facecolor("none")
#             canvas1 = FigureCanvasTkAgg(fig4, master=self.subtab2)
#             canvas1.draw()
#             canvas1.get_tk_widget().grid(row=0, column=5, padx=10,pady=10)
#     def countplot_chestpain_prone(self):
#             fig5,ax5 = plt.subplots(figsize=(9, 6))
#             sns.countplot(x='cp', hue='target', data=data, ax=ax5)
#             ax5.set_xticklabels(["typical angina", "atypical angina", "non-anginal pain", "asymptomatic"])
#             ax5.set_title('Chest pain and number of people having high or low chances of heart attack')
#             ax5.legend(labels=['low chance', 'high chance'])
#             appear_mode = ctk.get_appearance_mode()
#             if appear_mode == "Dark":
#                 fig5.set_facecolor(self.home_frames_dark)
#                 ax5.set_facecolor(self.home_frames_dark)
#             else:
#                 fig5.set_facecolor("none")
#                 ax5.set_facecolor("none")
#             canvas1 = FigureCanvasTkAgg(fig5, master=self.datatab3)
#             canvas1.draw()
#             canvas1.get_tk_widget().grid(row=0, column=0, padx=10,pady=10)
#
#     def histogram_chol_person(self):
#         fig7,ax7 = plt.subplots(figsize=(4, 4))
#         data['chol'].hist(ax=ax7)
#         ax7.set_xlabel('Serum cholestoral (mg/dl)')
#         ax7.set_ylabel('Person')
#         ax7.set_title('Serum Cholesterol Levels in Patients')
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig7.set_facecolor(self.home_frames_dark)
#             ax7.set_facecolor(self.home_frames_dark)
#         else:
#             fig7.set_facecolor("none")
#             ax7.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig7, master=self.subtab3)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0, column=5, padx=20, pady=10)
#
#     # def histogram_chol(self):
#     #     fig8,ax8 = plt.subplots(figsize=(4, 4))
#     #     data['chol'].hist( bins=20, color='skyblue', edgecolor='black', ax=ax8)
#     #     ax8.set_title('Serum Cholesterol Levels in Patients')
#     #     ax8.set_xlabel('Serum Cholesterol (mg/dl)')
#     #     ax8.set_ylabel('Number of Persons')
#     #     canvas1 = FigureCanvasTkAgg(fig8, master=self.datatab4)
#     #     canvas1.draw()
#     #     canvas1.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)
#
#     def countplot_fbs_target(self):
#         fig6, ax6 = plt.subplots(figsize=(4, 4))
#         sns.countplot(x='fbs', hue='target', data=data, ax=ax6)
#         ax6.set_title('Fasting Blood Sugar and Heart Attack')
#         ax6.legend(labels=['low chance', 'high chance'])
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig6.set_facecolor(self.home_frames_dark)
#             ax6.set_facecolor(self.home_frames_dark)
#         else:
#             fig6.set_facecolor("none")
#             ax6.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig6, master=self.datatab4)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)
#
#     def hist_chol_density(self):
#         fig9,ax9=plt.subplots(figsize=(4,4))
#         sns.histplot(data['chol'], kde=True, color='orange', stat='density')
#         ax9.set_xlabel('Serum Cholestoral (mg/dl)')
#         ax9.set_ylabel('Probability Density')
#         ax9.set_title('Cholesterol with Probability Density Curve')
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig9.set_facecolor(self.home_frames_dark)
#             ax9.set_facecolor(self.home_frames_dark)
#         else:
#             fig9.set_facecolor("none")
#             ax9.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig9, master=self.subtab4)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0, column=5, padx=10, pady=10)
#
#     def hist_chol_gender(self):
#        fig10,ax10 = plt.subplots(figsize=(4, 4))
#        sns.histplot(data=combined_chol_data, x="chol", hue="sex", multiple="stack", ax=ax10, palette='YlGnBu')
#        ax10.set_title('Cholesterol vs Participant Gender')
#        ax10.set_xlabel('Cholesterol Value  mg/dL')
#        ax10.set_ylabel('Number of Participants')
#        ax10.legend(title="Sex", labels=["Male", "Female"])
#        appear_mode = ctk.get_appearance_mode()
#        if appear_mode == "Dark":
#            fig10.set_facecolor(self.home_frames_dark)
#            ax10.set_facecolor(self.home_frames_dark)
#        else:
#            fig10.set_facecolor("none")
#            ax10.set_facecolor("none")
#        canvas1 = FigureCanvasTkAgg(fig10, master=self.subtab5)
#        canvas1.draw()
#        canvas1.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)
#
#     def histplot_chol_heart(self):
#         fig11,ax11 = plt.subplots(figsize=(4, 4))
#         sns.histplot(data=combined_chol_data, x="chol", hue="target", multiple="stack", ax=ax11, palette='YlGnBu')
#         ax11.set_title('Cholesterol vs Heart Disease Diagnosis')
#         ax11.set_xlabel('Cholesterol Value mg/dL')
#         ax11.set_ylabel('Number of Participants')
#         ax11.legend(title="Heart Disease", labels=["No", "Yes"])
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig11.set_facecolor(self.home_frames_dark)
#             ax11.set_facecolor(self.home_frames_dark)
#         else:
#             fig11.set_facecolor("none")
#             ax11.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig11, master=self.subtab6)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0, column=5, padx=10, pady=10)
#
#     def pie_chart(self):
#         fig12, ax12 = plt.subplots(figsize=(4, 4))
#         labels = heart_percent.keys()
#         sizes = heart_percent.values()
#         colors = ["#c1d8c1", "#6283af"]
#         explode = (0, 0.1)
#         ax12.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, colors=colors, startangle=90,textprops={'fontsize': 10})
#         ax12.set_title("Heart Disease Percentage", size=10, fontweight="bold")
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig12.set_facecolor(self.home_frames_dark)
#             ax12.set_facecolor(self.home_frames_dark)
#         else:
#             fig12.set_facecolor("none")
#             ax12.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig12, master=self.chart_frame)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)
#
#     def heatmap_corr(self):
#         fig13,ax13=plt.subplots(figsize=(9,6))
#         corr_matrix = data.corr()
#         sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, vmin=-1, vmax=1, center=0,cbar_kws={"shrink": 0.75}, ax=ax13)
#         ax13.set_title('Correlation Heatmap of Updated Features')
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig13.set_facecolor(self.home_frames_dark)
#             ax13.set_facecolor(self.home_frames_dark)
#         else:
#             fig13.set_facecolor("none")
#             ax13.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig13, master=self.datatab5)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0, column=0, padx=10)
#
#     def hist_norm_age(self):
#         fig14, ax14 = plt.subplots(figsize=(9, 6))
#         mu, std = norm.fit(data['age'])
#         ax14.hist(data['age'], bins=20, density=True, alpha=0.6, color='g')
#         xmin, xmax = ax14.get_xlim()
#         x = np.linspace(xmin, xmax, 100)
#         p = norm.pdf(x, mu, std)
#         ax14.plot(x, p, 'k', linewidth=2)
#         ax14.set_xlabel('Age')
#         ax14.set_ylabel('Probability of having heart disease')
#         ax14.set_title('Fitting a Normal Distribution to the Age variable')
#         appear_mode = ctk.get_appearance_mode()
#         if appear_mode == "Dark":
#             fig14.set_facecolor(self.home_frames_dark)
#             ax14.set_facecolor(self.home_frames_dark)
#         else:
#             fig14.set_facecolor("none")
#             ax14.set_facecolor("none")
#         canvas1 = FigureCanvasTkAgg(fig14, master=self.datatab6)
#         canvas1.draw()
#         canvas1.get_tk_widget().grid(row=0, column=0, padx=10)
#
#
# if __name__ == "__main__":
#     # Read the CSV file
#     data = pd.read_csv('heart.csv')
#
#     # 3. Basic Measures and Averages
#
#     # Let's separate the genders as we want to see how men compare to women
#     male_data = data[data['sex'] == 1]
#     female_data = data[data['sex'] == 0]
#
#     # Count of Males & Females in Dataset
#     male_count = data['sex'].value_counts()[1]
#     female_count = data['sex'].value_counts()[0]
#
#     # Avg Age of Males & Females in Dataset
#     male_age_avg = male_data['age'].mean()
#     female_age_avg = female_data['age'].mean()
#
#     oa_chol = data['chol'].mean()  # Avg Cholesterol Level of People in the Dataset
#
#     # Number of Positive Cases (Who have Heart Disease)
#     fbs_count = data['fbs'].value_counts()[1]
#     trg_count = data['target'].value_counts()[1]
#
#
#     male_health_data = male_data[['age', 'sex', 'chol', 'target']]
#     female_health_data = female_data[['age', 'sex', 'chol', 'target']]
#     female_health_data.sort_values(by='chol', ascending=False)
#     male_health_data.sort_values(by='chol', ascending=False)
#     combined_chol_data = pd.concat([male_health_data, female_health_data],
#                                    ignore_index=True)  # Concatenating the two DataFrames along the rows vertically
#
#     # Reset the index
#     combined_chol_data.reset_index(drop=True, inplace=True)
#
#     # # 5. Additional Analysis
#     #
#     # # 5.1. What percentage of participants actually have heart disease?
#     heart_percent = data["target"].value_counts(normalize=True).to_dict()
#     heart_percent["Disease"] = heart_percent.pop(1)
#     heart_percent["Normal"] = heart_percent.pop(0)
#
#     root = ctk.CTk()
#     app = GUI(root)
#     root.mainloop()


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC

# Loading the dataset
heart_data = pd.read_csv(r'/Users/Rayyan./Documents/Rayyan/uni work/5th Semester/Probability And Statistics/project/heart.csv')


# LINEAR REGRESSION

# Feature selection for linear regression
selected_features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = heart_data[selected_features]
Y = heart_data['target']

# Splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Creating and training the linear regression model
linear_model = LinearRegression()
linear_model.fit(X_train, Y_train)

# Predicting with more features
new_data = np.array([[58, 0, 0, 100, 248, 0, 0, 122, 0, 1, 1, 0, 2]])  # Replace with input values
linear_prediction = linear_model.predict(new_data)

# Scatter plot and regression line for Age vs Heart Disease using linear regression
plt.figure(figsize=(12, 6))
plt.scatter(X_test['age'], Y_test, c='red', label='Heart Problem (Actual)')
plt.plot(X_test['age'], linear_model.predict(X_test), color='blue', label='Linear Regression Line')
plt.title('Age vs Heart Disease (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Heart Disease')
plt.legend()
plt.show()


print("Linear Regression")
if linear_prediction[0] < 0.5:
    print("The person does not have any heart disease.")
else:
    print("The person has heart disease.")



# LOGISTIC REGRESSION
# Feature selection for logistic regression
selected_features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = heart_data[selected_features]
Y = heart_data['target']

# Splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Standardizing the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Creating and training the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, Y_train)

# Predicting with more features
new_data = np.array([[53, 1, 0, 140, 203, 1, 0, 155, 1, 3.1, 0, 0, 3]])  # Replace with input values
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)

# Scatter plot and regression line with Z-Score of Age vs Heart Disease
plt.figure(figsize=(12, 6))
plt.scatter(zscore(X_test['age']), Y_test, c='red', label='Heart Problem')
sns.regplot(x=zscore(X_test['age']), y=model.predict(X_test), data=heart_data, logistic=True, ci=None, scatter=False, color='blue', line_kws={'color': 'blue'})
plt.title('Age vs Heart Disease with Z-Score')
plt.xlabel('Age Z-score')
plt.ylabel('Heart Disease')
plt.legend()
plt.show()


print("Logistic Regression")
if prediction[0] == 0:
    print("The person does not have any heart disease.")
else:
    print("The person has heart disease.")


# Support Vector Classifier Model (SVC)

# Feature selection
selected_features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = heart_data[selected_features]
Y = heart_data['target']

# Splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Standardizing the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Creating and training the Support Vector Classifier (SVC) model
svc_model = SVC(kernel='linear', C=1.0)
svc_model.fit(X_train_scaled, Y_train)

# Predicting with more features
new_data = np.array([[53, 1, 0, 140, 203, 1, 0, 155, 1, 3.1, 0, 0, 3]])  # Replace with actual values
new_data_scaled = scaler.transform(new_data)
prediction = svc_model.predict(new_data_scaled)

# Scatter plot and regression line with Z-Score of Age vs Heart Disease
plt.figure(figsize=(12, 6))
plt.scatter(X_test['age'], Y_test, c='red', label='Heart Problem')
sns.regplot(x=X_test['age'], y=svc_model.predict(X_test_scaled), data=heart_data, ci=None, scatter=False, color='blue', line_kws={'color': 'blue'})
plt.title('Age vs Heart Disease with SVC')
plt.xlabel('Age')
plt.ylabel('Heart Disease')
plt.legend()
plt.show()

# Scatter plot and regression line for Age vs Heart Disease
plt.figure(figsize=(12, 6))
plt.scatter(X_test['age'], Y_test, c='red', label='Heart Problem')
sns.regplot(x=X_test['age'], y=svc_model.predict(X_test), data=heart_data, logistic=True, ci=None, scatter=False, color='blue', line_kws={'color': 'blue'})
plt.title('Age vs Heart Disease with SVC')
plt.xlabel('Age')
plt.ylabel('Heart Disease')
plt.legend()
plt.show()

# Scatter plot and regression line for Chest-Pain vs Heart Disease
plt.figure(figsize=(12, 6))
plt.scatter(X_test['cp'], Y_test, c='red', label='Heart Problem')
sns.regplot(x=X_test['cp'], y=svc_model.predict(X_test), data=heart_data, logistic=True, ci=None, scatter=False, color='blue', line_kws={'color': 'blue'})
plt.title('Chest-Pain vs Heart Disease with SVC')
plt.xlabel('Chest-Pain')
plt.ylabel('Heart Disease')
plt.legend()
plt.show()

# Scatter plot and regression line for Sex vs Heart Disease
plt.figure(figsize=(12, 6))
plt.scatter(X_test['sex'], Y_test, c='red', label='Heart Problem')
sns.regplot(x=X_test['sex'], y=svc_model.predict(X_test), data=heart_data, logistic=True, ci=None, scatter=False, color='blue', line_kws={'color': 'blue'})
plt.title('Sex vs Heart Disease with SVC')
plt.xlabel('Sex')
plt.ylabel('Heart Disease')
plt.legend()
plt.show()

print("Support Vector Classifier Model (SVC)")
if prediction[0] == 0:
    print("The person does not have any heart disease.")
else:
    print("The person has heart disease.")




# Calculate accuracy score for Logistic Regression
Y_test_pred = model.predict(X_test)
accuracy_logistic_regression = accuracy_score(Y_test, Y_test_pred)
print(f"Accuracy Score of Logistic Regression: {accuracy_logistic_regression}")



# Calculating accuracy score for Linear Regression
# Predicting on the test set
Y_test_pred = linear_model.predict(X_test)
# Convert predicted probabilities to binary outcomes (0 or 1)
Y_test_pred_binary = (Y_test_pred >= 0.5).astype(int)
# Convert the true labels to binary outcomes for comparison
Y_test_binary = (Y_test == 1).astype(int)

# Calculate accuracy score
accuracy_linear_regression = accuracy_score(Y_test_binary, Y_test_pred_binary)
print(f"Accuracy Score: {accuracy_linear_regression}")



# Calculate accuracy score for SVC Model
Y_test_pred_svc = svc_model.predict(X_test_scaled)
accuracy_svc = accuracy_score(Y_test, Y_test_pred_svc)
print(f"SVC Accuracy Score: {accuracy_svc}")



# Plotting Bar Graph to compare Models
models = ['Linear Regression', 'Logistic Regression', 'SVC']

# Accuracy scores
accuracy_scores = [accuracy_linear_regression, accuracy_logistic_regression, accuracy_svc]

# Plotting bar graph
plt.figure(figsize=(10, 6))
plt.bar(models, accuracy_scores, color=['blue', 'orange', 'green'])
plt.ylim(0, 1)  # Set the y-axis limit from 0 to 1 for accuracy scores
plt.title('Comparison of Accuracy Scores')
plt.xlabel('Models')
plt.ylabel('Accuracy Score')
plt.show()
