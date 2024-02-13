from django.shortcuts import render
import numpy as np
import pandas as pd

# our home page view
def home(request):
    return render(request, 'index.html')
# our result page view
def result(request):

    data = pd.read_csv(r"All_Data.csv")
    data.describe()
    X = data.iloc[:, :-1]  # Features - All columns but last
    y = data.iloc[:, -1]
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
    # random forest regressor
    from sklearn.ensemble import RandomForestRegressor
    rfr = RandomForestRegressor(n_estimators=100)  # estimators is the number of trees built
    rfr.fit(X_train, y_train)
    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
    var6 = float(request.GET['n6'])
    var7 = float(request.GET['n7'])
    var8 = float(request.GET['n8'])
    var9 = float(request.GET['n9'])
    var10 = float(request.GET['n10'])
    var11 = float(request.GET['n11'])
    var12 = float(request.GET['n12'])
    var13 = float(request.GET['n13'])
    var14 = float(request.GET['n14'])
    var15 = float(request.GET['n15'])
    var16 = float(request.GET['n16'])
    var17 = float(request.GET['n17'])
    strength= rfr.predict(np.array([var1,var2,var3,var4, var5, var6, var7, var8,var9,var10, var11, var12, var13, var14,var15, var16, var17]).reshape(1,-1))
    strength = round(strength[0],2)
    result= "The predicted the strength in MPa is " ,float(strength)
    return render(request, 'result.html', {'result': result})
