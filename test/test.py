import gurobipy as gp


# 問題を設定
model_1 = gp.Model(name = "GurobiSample1")


# 変数を設定（変数単体にかかる制約を含む）
x = model_1.addVar(lb = 0, ub = 3, vtype = gp.GRB.CONTINUOUS, name = "ekkusu")
y = model_1.addVar(lb = 0, ub = 5, vtype = gp.GRB.CONTINUOUS, name = "wai")


# 目的関数を設定
model_1.setObjective(2 * x + y, sense = gp.GRB.MAXIMIZE)


# 制約を設定
c_1 = model_1.addConstr(x + y <= 4, name = "seiyaku_1")
c_2 = model_1.addConstr(x + 2 * y <= 6, name = "seiyaku_2")


# 解を求める計算
print("↓点線の間に、Gurobi Optimizerからログが出力")
print("-" * 40)

model_1.optimize()

print("-" * 40)
print()


# 最適解が得られた場合、結果を出力
if model_1.Status == gp.GRB.OPTIMAL:
    # 解の値
    x_opt = x.X
    y_opt = y.X
    # 目的関数の値
    val_opt = model_1.ObjVal
    print(f"最適解は x = {x_opt}, y = {y_opt}")
    print(f"最適値は {val_opt}")