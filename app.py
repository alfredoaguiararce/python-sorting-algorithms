import matplotlib
matplotlib.use("TkAgg")  # O "Qt5Agg" si prefieres

import streamlit as st
import matplotlib.pyplot as plt
import time

from algoritms import Algorithms

def animate_sorting(algorithm, arr):
    """
    The `animate_sorting` function takes an algorithm and an array as input, and displays an animated
    bar chart to visualize the sorting process.
    
    :param algorithm: The `algorithm` parameter is a function that represents a sorting algorithm. It
    takes an array as input and returns a list of steps, where each step represents the state of the
    array after a single operation of the sorting algorithm
    :param arr: The `arr` parameter is a list of numbers that you want to sort using the specified
    sorting algorithm
    """
    st.title(f"{algorithm.__name__.replace('_', ' ').title()} Sorting")
    
    chart = st.bar_chart(arr)
    
    for step in algorithm(arr.copy()):
        chart.bar_chart(step)
        time.sleep(0.01/len(arr)) 

def main():
    st.title("Visualización de Algoritmos de Ordenamiento")

    algorithms = Algorithms()
    algorithm = st.selectbox("Selecciona un algoritmo:", ["bubble_sort"])
    numbers = st.text_input("Ingresa una lista de números separados por comas:")

    if st.button("Ordenar"):
        arr = [int(x.strip()) for x in numbers.split(",")]
        animate_sorting(getattr(algorithms, algorithm), arr)

if __name__ == "__main__":
    main()