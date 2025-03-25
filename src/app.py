import argparse
import logging
import tkinter as tk
from tkinter import ttk
import pandas as pd
import webbrowser
import random
from datetime import date, datetime

from src.collect_trainingdata.get_faces_from_camera import TrainingDataCollector
from src.face_embedding.faces_embedding import GenerateFaceEmbedding
from src.predictor.facePredictor import FacePredictor
from src.training.train_softmax import TrainFaceRecogModel

class RegistrationModule:
    def __init__(self, logFileName):
        self.logFileName = logFileName
        self.window = tk.Tk()
        self.window.title("Face Recognition & Tracking")
        self.window.geometry("880x600")
        self.window.configure(bg="#f5f5f5")
        
        # Styling
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 14), background="#f5f5f5", foreground="#333")
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=5, background="#007acc", foreground="black")
        self.style.configure("TEntry", font=("Arial", 12))
        
        # Header
        header = ttk.Label(self.window, text="Employee face Monitoring Registration", font=("Arial", 18, "bold"), background="#363e75", foreground="white")
        header.pack(fill=tk.X, pady=10)
        
        # Form layout
        form_frame = ttk.Frame(self.window, padding=10)
        form_frame.pack(pady=10)
        
        labels = ["Client ID:", "Emp ID:", "Emp Name:", "Email ID:", "Mobile No:"]
        self.entries = {}
        
        for idx, text in enumerate(labels):
            ttk.Label(form_frame, text=text).grid(row=idx, column=0, padx=10, pady=5, sticky=tk.W)
            entry = ttk.Entry(form_frame, width=30)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries[text] = entry
        
        # Notification Label
        self.message = ttk.Label(self.window, text="", font=("Arial", 12), background="#f5f5f5", foreground="red")
        self.message.pack(pady=5)
        
        # Buttons
        button_frame = ttk.Frame(self.window, padding=10)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Take Images", command=self.collectUserImageForRegistration).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(button_frame, text="Train Model", command=self.trainModel).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(button_frame, text="Predict", command=self.makePrediction).grid(row=0, column=2, padx=10, pady=5)
        ttk.Button(button_frame, text="Quit", command=self.close_window).grid(row=0, column=3, padx=10, pady=5)
        
        self.window.mainloop()
        
    def collectUserImageForRegistration(self):
        name = self.entries["Emp Name:"].get()
        empIDVal = self.entries["Emp ID:"].get()
        clientIDVal = self.entries["Client ID:"].get()
        dates = date.today()
        dt_string = datetime.now().strftime("%I:%M %p")
        
        df = pd.DataFrame({
            'Name': [name],
            'Emp ID': [empIDVal],
            'Client ID': [clientIDVal],
            'Date': [dates],
            'Time': [dt_string],
        })
        df.to_csv('history.csv', mode='a', index=False, header=False)
        
        args = {"faces": 50, "output": f"../datasets/train/{name}"}
        TrainingDataCollector(args).collectImagesFromCamera()
        self.message.config(text=f"Collected {args['faces']} images for training.")
    
    def trainModel(self):
        self.getFaceEmbedding()
        args = {"embeddings": "faceEmbeddingModels/embeddings.pickle", "model": "faceEmbeddingModels/my_model.h5", "le": "faceEmbeddingModels/le.pickle"}
        TrainFaceRecogModel(args).trainKerasModelForFaceRecognition()
        self.message.config(text="Model training successful. Ready for prediction.")
        
    def getFaceEmbedding(self):
        args = {"dataset": "../datasets/train", "embeddings": "faceEmbeddingModels/embeddings.pickle"}
        GenerateFaceEmbedding(args).genFaceEmbedding()
    
    def makePrediction(self):
        FacePredictor().detectFace()
    
    def close_window(self):
        self.window.destroy()
        
logFileName = "ProceduralLog.txt"
regStrtnModule = RegistrationModule(logFileName)
