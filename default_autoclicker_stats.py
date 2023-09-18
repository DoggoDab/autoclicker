import matplotlib.pyplot as plt
import pandas as pd

plt.title('Autoclicker CPS Statistics')
plt.xlabel("Attempts")
plt.ylabel("CPS")

data = {
    "attempts": ['1', '2', '3', '4', '5'],
    "cps (per 5 seconds)": [78.4, 70.2, 69, 66.6, 69.2],
}

df = pd.DataFrame(data)

plt.plot(df["attempts"], df["cps (per 5 seconds)"])

plt.show()