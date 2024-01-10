# Note : matplotlib and sklearn is not supported for py -3.10. It is supported by py -3.8
# cmd : py -3.8 -m <cmd follows>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt                         # Supporting py -3.8 (py -3.8 -m pip install matplotlib)
from sklearn.linear_model import LinearRegression       # Supporting py -3.8
from sklearn.model_selection import train_test_split



# Input as an csv file
file_path = "data1.csv"
data = pd.read_csv(file_path)

# Extract features (speed, feed rate, point angle) and target variable (thrust force), creating a varibale for the same
X = data[['speed', 'feed_rate', 'point_angle']]
y = data[['thrust_force']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()      # Linear regression (y = a0 + a1X1.....anXn), sklearn module(py -3.8 -m)

# class LinearRegression(
#     *,
#     fit_intercept: bool = True,
#     copy_X: bool = True,
#     n_jobs: Int | None = None,
#     positive: bool = False
# )
model.fit(X_train, y_train)
# model.fit(X_test,y_test)            # this will only ahow predicted values

y_pred = model.predict(X_test)      # predictions on the test set

# Plot the results
fig, axs = plt.subplots(2, 2, figsize=(12, 8))


# Speed vs. Thrust Force plot
axs[0, 0].scatter(X_test['speed'], y_test, color='blue', label='Actual')
axs[0, 0].scatter(X_test['speed'], y_pred, color='red', label='Predicted')
axs[0, 0].set_xlabel('Speed')
axs[0, 0].set_ylabel('Thrust Force')
axs[0, 0].legend()

# Feed Rate vs. Thrust Force plot
axs[0, 1].scatter(X_test['feed_rate'], y_test, color='blue', label='Actual')
axs[0, 1].scatter(X_test['feed_rate'], y_pred, color='red', label='Predicted')
axs[0, 1].set_xlabel('Feed Rate')
axs[0, 1].set_ylabel('Thrust Force')
axs[0, 1].legend()

# Point Angle vs. Thrust Force chart will be plotted
axs[1, 0].scatter(X_test['point_angle'], y_test, color='blue', label='Actual')
axs[1, 0].scatter(X_test['point_angle'], y_pred, color='red', label='Predicted')
axs[1, 0].set_xlabel('Point Angle')
axs[1, 0].set_ylabel('Thrust Force')
axs[1, 0].legend()

#Predicted vs. Actual Thrust Force Chart will be displayed
axs[1, 1].scatter(y_test, y_pred, color='blue')
axs[1, 1].plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
axs[1, 1].set_xlabel('Actual Thrust Force')
axs[1, 1].set_ylabel('Predicted Thrust Force')



plt.tight_layout()
plt.show()


