import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Funktionen für die einzelnen Seiten
def pruefblatt():
    st.title("Prüfblatt")
    st.write("Informationen zum Prüfblatt")

def histogram():
    st.title("Histogramm")
    data = np.random.normal(size=1000)
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30)
    plt.title("Histogramm Beispiel")
    st.pyplot(plt)

def pareto_diagramm():
    st.title("Pareto-Diagramm")
    data = pd.Series(np.random.randint(1, 100, 10))
    data = data.value_counts().sort_values(ascending=False)
    cumsum = data.cumsum() / data.sum() * 100
    cumsum = cumsum.reset_index(drop=True)

    fig, ax1 = plt.subplots()
    data.plot(kind='bar', ax=ax1)
    ax1.set_ylabel('Häufigkeit')
    ax2 = ax1.twinx()
    cumsum.plot(ax=ax2, color='red', marker='D')
    ax2.set_ylabel('Kumulierte Prozentsätze')
    ax2.grid(False)
    st.pyplot(fig)

def ursache_wirkungs_diagramm():
    st.title("Ursache-Wirkungs-Diagramm")
    st.write("Hier könnte ein Ursache-Wirkungs-Diagramm implementiert werden.")

def flowchart():
    st.title("Flowchart")
    st.write("Hier könnte ein Flowchart implementiert werden.")

def streudiagramm():
    st.title("Streudiagramm")
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.scatter(x, y)
    plt.title("Streudiagramm Beispiel")
    st.pyplot(plt)

def kontrollkarten():
    st.title("Kontrollkarten")
    data = np.random.rand(100)
    control_limit_upper = np.mean(data) + np.std(data) * 3
    control_limit_lower = np.mean(data) - np.std(data) * 3
    plt.figure(figsize=(10, 5))
    plt.plot(data, marker='o')
    plt.axhline(np.mean(data), color='green', label='Mittelwert')
    plt.axhline(control_limit_upper, color='red', linestyle='--', label='Obere Kontrollgrenze')
    plt.axhline(control_limit_lower, color='blue', linestyle='--', label='Untere Kontrollgrenze')
    plt.title("Kontrollkarte")
    plt.legend()
    st.pyplot(plt)

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
