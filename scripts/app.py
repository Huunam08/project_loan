import numpy as np
from joblib import load

# Đường dẫn đến mô hình đã lưu
model =  load("notebooks/model/randomforest_model.model")



# Danh sách chỉ số cần nhập
feature_names = ["loan_amount", "cibil_score", "bank_asset_value", 
                 "residential_assets_value", "commercial_assets_value"]

print("\n Mô hình yêu cầu nhập các chỉ số sau:")
for i, name in enumerate(feature_names):
    print(f"{i+1}. {name}")

# Yêu cầu người dùng nhập từng chỉ số
input_values = []
print(" Nhập các giá trị đầu vào:")

for name in feature_names:
    while True:
        try:
            value = float(input(f"Nhập {name}: "))
            input_values.append(value)
            break
        except ValueError:
            print(" Giá trị không hợp lệ! Hãy nhập một số.")

# Chuyển đổi thành mảng numpy
input_data = np.array([input_values])

# Kiểm tra số lượng cột khớp với mô hình
if input_data.shape[1] != model.n_features_in_:
    print(f" Lỗi: Số lượng giá trị nhập ({input_data.shape[1]}) không khớp với mô hình ({model.n_features_in_}).")
    exit()

# Dự đoán kết quả
prediction = model.predict(input_data)
print("\n Kết quả dự đoán:", prediction[0])

# Nếu mô hình hỗ trợ xác suất dự đoán, hiển thị thêm xác suất
if hasattr(model, "predict_proba"):
    probs = model.predict_proba(input_data)
    print(" Xác suất dự đoán:", probs)
