import streamlit as st
import matplotlib.pyplot as plt
import time



def bubble_sort(arr):
    """
    The above function implements the bubble sort algorithm to sort an array in ascending order and
    yields the intermediate steps of the sorting process.
    
    :param arr: The parameter "arr" is a list of elements that you want to sort using the bubble sort
    algorithm
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr




def animate_sorting(algorithm, arr):
    """
    The `animate_sorting` function takes an algorithm and an array as input, and animates the sorting
    process using matplotlib.
    
    :param algorithm: The `algorithm` parameter is a function that represents a sorting algorithm. It
    takes an array as input and returns a generator that yields the intermediate steps of the sorting
    process
    :param arr: The `arr` parameter is a list of numbers that you want to sort. It represents the array
    or list that you want to visualize the sorting process for
    """
    fig, ax = plt.subplots()
    ax.set_title(f"{algorithm.__name__.replace('_', ' ').title()} Sorting")
    bars = ax.bar(range(len(arr)), arr)

    for step in algorithm(arr.copy()):
        for i, bar in enumerate(bars):
            bar.set_height(step[i])
        plt.pause(0.1)
        fig.canvas.draw()

def main():
    st.title("Visualización de Algoritmos de Ordenamiento")

    algorithm = st.selectbox("Selecciona un algoritmo:", ["bubble_sort"])
    numbers = st.text_input("Ingresa una lista de números separados por comas:")

    if st.button("Ordenar"):
        arr = [int(x.strip()) for x in numbers.split(",")]
        animate_sorting(eval(algorithm), arr)

if __name__ == "__main__":
    main()
