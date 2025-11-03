import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
sns.scatterplot(
    x='area',               # Diện tích
    y='price_million',      # Giá theo triệu đồng
    data=df,
    hue='district',         # Tô màu theo quận (tùy chọn)
    palette='Set2',
    alpha=0.7
)
plt.title("Mối quan hệ giữa diện tích và giá thuê")
plt.xlabel("Diện tích (m²)")
plt.ylabel("Giá thuê (triệu đồng)")
plt.legend(title="Quận")
plt.grid(alpha=0.3)
plt.show()
