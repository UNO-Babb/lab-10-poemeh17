#MapPlot.py
#Name:
#Date:
#Assignment:

import graduates
import pandas
import matplotlib.pyplot as plt

grad_major = graduates.get_grad_major()

degree_totals = {
    "Bachelors": 0,
    "Masters": 0,
    "Doctorates": 0,
    "Professionals": 0
}

for grad in grad_major:

    degree_dict = grad["Education"]["Degrees"]
    status = grad["Employment"]["Status"]["Employed"]

 
    if status >= 1000000:
        for degree, count in degree_dict.items():
            degree_totals[degree] += count


df = pandas.DataFrame({"Degrees": list(degree_totals.keys()),
    "Status": list(degree_totals.values())})

print(df)

df.plot(kind='bar', x='Degrees', y='Status')
plt.savefig("output")



