import pandas as pd


# 1) Load synthetic data
DF_PATH = "data/sample_responses.csv"
df = pd.read_csv(DF_PATH)


# 2) Clean a column name (demo: make sure lowercase, underscores)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]


# 3) Compute basic stats
n = len(df)
mean_rt = df["rt_ms"].mean()
acc = df["correct"].mean() # 0..1


# 4) Tiny "insight" string
insight = (
f"N={n} | mean RT={mean_rt:.1f} ms | accuracy={acc:.0%}. "
+ ("Condition A looks faster." if df.groupby("condition")["rt_ms"].mean().idxmin() == "A" else "Condition B looks faster.")
)


print("\n=== Behavioral AI Lab Demo ===")
print(insight)


# Show a 3‑row preview
print("\nPreview:\n", df.head(3).to_string(index=False))