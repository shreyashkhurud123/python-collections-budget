from . import Expense
import matplotlib.pyplot as plt
import collections

#spending_data = pd.read_csv(r'python-collections-budget.budget.data/spending_data.csv')

expenses = Expense.Expenses()
#print(expenses)

expenses.read_expenses('data/spending_data.csv')


spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
#print(spending_categories)

spending_counter = collections.Counter(spending_categories)

print(spending_counter )
 
top5 = spending_counter.most_common(5)

#print(top5 , '\n ',  type(top5))

categories , count = zip(*top5)
#print(categories , " " , count )

fig , ax = plt.subplots()

#print(fig," " , ax , "\n" , type(fig) , type (ax))

ax.bar(categories , count)
ax.set_title('# of Purchases by Category')

plt.show()