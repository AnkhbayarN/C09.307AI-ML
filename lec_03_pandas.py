import pandas as pd
import matplotlib.pyplot as plt

#series
# a = [1,2,3,4,5]
# ser = pd.Series(a)
# print(ser)

#label
# a = [1,3,5,7,9]
# ser = pd.Series(a)
# print(ser[0])

# label
# a = [1,3,5,7,9]
# ser = pd.Series(a)
# print(ser)
# print(ser[1:4])

# index
# a = [2,4,6,8,10]
# label = ['a', 'b', 'c', 'd', 'e']
# ser = pd.Series(a, index=label)
# print(ser['b':'d'])


# dataframe
# a = [[1,2,3],[4,5,6]]
# df = pd.DataFrame(a)
# print(df)

# dataframe
# a = {
#     'height':[180, 175,156],
#     'weight':[75, 60, 48]
# }
# df = pd.DataFrame(a)
# print(df['height'][1:])

# loc
# a = {
#     'height':[180, 175,156],
#     'weight':[75, 60, 48]
# }
# df = pd.DataFrame(a)
# print(df.loc[0:2])
# print(df[0:2])

# read csv
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv')
# print(csv)
# print(csv.loc[0:5]['Temperature'])

# Chart
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv')
# x = csv['Temperature']
# y = csv['Ice Cream']
# plt.scatter(x, y)
# plt.show()

# head tail info
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv')
# print(csv.head())
# print(csv.tail())
# print(csv.info())

# corr
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv', usecols=['Temperature', 'Ice Cream'])
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv')
# print(csv[10:][['Temperature', 'Ice Cream']])
# print(csv)
# print(csv.corr())

# import pandas as pd
# import matplotlib.pyplot as plt

#series
# a = [1,2,3,4,5]
# ser = pd.Series(a)
# print(ser)

#label
# a = [1,3,5,7,9]
# ser = pd.Series(a)
# print(ser[0])

# label
# a = [1,3,5,7,9]
# ser = pd.Series(a)
# print(ser)
# print(ser[1:4])

# index
# a = [2,4,6,8,10]
# label = ['a', 'b', 'c', 'd', 'e']
# ser = pd.Series(a, index=label)
# print(ser['b':'d'])


# dataframe
# a = [[1,2,3],[4,5,6]]
# df = pd.DataFrame(a)
# print(df)

# dataframe
# a = {
#     'height':[180, 175,156],
#     'weight':[75, 60, 48]
# }
# df = pd.DataFrame(a)
# print(df['height'][1:])

# loc
# a = {
#     'height':[180, 175,156],
#     'weight':[75, 60, 48]
# }
# df = pd.DataFrame(a)
# print(df.loc[0:2])
# print(df[0:2])

# read csv
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv')
# print(csv)
# print(csv.loc[0:5]['Temperature'])

# Chart
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv')
# x = csv['Temperature']
# y = csv['Ice Cream']
# plt.scatter(x, y)
# plt.show()

# head tail info
# csv = pd.read_csv('lessonAI/lec_example/lab_02_ice_cream_sales.csv')
# # print(csv.head(10))
# print(csv.tail(5))

# corr
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv', usecols=['Temperature', 'Ice Cream'])
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv')
# print(csv[10:][['Temperature', 'Ice Cream']])
# print(csv)
# print(csv.corr())

# plotting
# csv = pd.read_csv('lessonAI/lec_example/ice_cream_sales.csv')
# csv.plot()
# plt.show();
