

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ---------------- EMI ----------------
def calculate_emi(p, r, t):
    r = r / (12 * 100)
    return p * r * (1 + r)**t / ((1 + r)**t - 1)


# ---------------- VALIDATION ----------------
def validate_input(p, r, t):
    if p <= 0 or r <= 0 or t <= 0:
        raise ValueError("Values must be positive")


# ---------------- SAVE/LOAD ----------------
def save_data(loans):
    with open("data.json", "w") as f:
        json.dump(loans, f, indent=4)


def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return []


# ---------------- NUMPY ANALYSIS ----------------
def numpy_analysis(loans):
    emis = [loan["emi"] for loan in loans]
    arr = np.array(emis)

    print("\n--- NumPy Analysis ---")
    print("Average EMI:", np.mean(arr))
    print("Max EMI:", np.max(arr))
    print("Min EMI:", np.min(arr))


# ---------------- PANDAS ANALYSIS ----------------
def pandas_analysis(loans):
    df = pd.DataFrame(loans)

    print("\n--- Pandas Data ---")
    print(df)

    print("\nAverage EMI:", df["emi"].mean())


# ---------------- VISUALIZATION ----------------
def plot_graph(loans):
    names = [f"Loan{i+1}" for i in range(len(loans))]
    emis = [loan["emi"] for loan in loans]

    plt.bar(names, emis)
    plt.title("EMI Comparison")
    plt.xlabel("Loans")
    plt.ylabel("EMI")
    plt.show()
