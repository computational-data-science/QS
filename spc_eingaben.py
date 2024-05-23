import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Funktionen für die einzelnen Seiten
def pruefblatt():
    st.title("Motor Assembly Check Sheet")

    # Datenrahmen initialisieren
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame({
            "Defect Type/Event Occurrence": [
                "Supplied parts rusted", "Misaligned weld", "Improper test procedure",
                "Wrong part issued", "Film on parts", "Voids in casting",
                "Incorrect dimensions", "Adhesive failure", "Masking insufficient", 
                "Spray failure"
            ],
            "Sunday": [0]*10, "Monday": [0]*10, "Tuesday": [0]*10,
            "Wednesday": [0]*10, "Thursday": [0]*10, "Friday": [0]*10,
            "Saturday": [0]*10
        })

    # Dynamisches Eingabefeld für jede Zelle
    for index, row in st.session_state.data.iterrows():
        cols = st.columns([2, 1, 1, 1, 1, 1, 1, 1])
        cols[0].write(row["Defect Type/Event Occurrence"])
        for i, day in enumerate(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]):
            new_val = cols[i+1].number_input(f"", value=row[day], key=f"{index}-{day}", min_value=0, step=1)
            st.session_state.data.at[index, day] = new_val

    # Berechnung der Totalen pro Defektart und pro Tag
    st.session_state.data['TOTAL'] = st.session_state.data.iloc[:, 1:8].sum(axis=1)
    daily_totals = st.session_state.data.iloc[:, 1:8].sum()

    st.write("### Detailierte Ansicht")
    st.dataframe(st.session_state.data)

    st.write("### Tägliche Gesamtwerte")
    st.write(daily_totals)

    st.write("### Gesamtanzahl der Defekte")
    st.write(daily_totals.sum())

def histogram():
    st.title("Histogramm")
    uploaded_file = st.file_uploader("Lade deine Daten für das Histogramm hoch", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        # Daten verarbeiten
        st.write("Datei erfolgreich hochgeladen!")

def pareto_diagramm():
    st.title("Pareto-Diagramm")
    uploaded_file = st.file_uploader("Lade deine Daten für das Pareto-Diagramm hoch", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.write("Datei erfolgreich hochgeladen!")

def ursache_wirkungs_diagramm():
    st.title("Ursache-Wirkungs-Diagramm")
    uploaded_file = st.file_uploader("Lade deine Daten für das Ursache-Wirkungs-Diagramm hoch", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.write("Datei erfolgreich hochgeladen!")

def flowchart():
    st.title("Flowchart")
    uploaded_file = st.file_uploader("Lade deine Daten für das Flowchart hoch", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.write("Datei erfolgreich hochgeladen!")

def streudiagramm():
    st.title("Streudiagramm")
    uploaded_file = st.file_uploader("Lade deine Daten für das Streudiagramm hoch", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.write("Datei erfolgreich hochgeladen!")

def kontrollkarten():
    st.title("Kontrollkarten")
    uploaded_file = st.file_uploader("Lade deine Daten für die Kontrollkarten hoch", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        st.write("Datei erfolgreich hochgeladen!")

# Sidebar zur Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Wähle eine Seite", ["Prüfblatt", "Histogramm", "Pareto-Diagramm", "Ursache-Wirkungs-Diagramm", "Flowchart", "Streudiagramm", "Kontrollkarten"])

if page == "Prüfblatt":
    pruefblatt()
elif page == "Histogramm":
    histogram()
elif page == "Pareto-Diagramm":
    pareto_diagramm()
elif page == "Ursache-Wirkungs-Diagramm":
    ursache_wirkungs_diagramm()
elif page == "Flowchart":
    flowchart()
elif page == "Streudiagramm":
    streudiagramm()
elif page == "Kontrollkarten":
    kontrollkarten()
