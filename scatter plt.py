import seaborn as sns
import matplotlib.pyplot as plt

diamonds = sns.load_dataset('diamonds')

carat = diamonds['carat']
price = diamonds['price']

plt.figure(figsize=(10, 6))
plt.scatter(carat, price, alpha=0.5, edgecolors='w')

plt.title('Scatter Plot of Carat vs Price')
plt.xlabel('Carat')
plt.ylabel('Price')

plt.show()
