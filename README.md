# Giới thiệu

Dự án này sử dụng ba mô hình Random Forest, XGBoost, và Decision Tree để dự đoán khách hàng có được phê duyệt khi vay tiền. Sau khi huấn luyện, chúng tôi đã triển khai chương trình dự đoán cho hai mô hình Random Forest và XGBoost.

# Cấu trúc dự án

### randomforest.ipynb: Huấn luyện mô hình Random Forest.

### xgboot.ipynb: Huấn luyện mô hình XGBoost.

### Decsiontree.ipynb: Huấn luyện mô hình Decision Tree.

### data/raw/loan.csv: Dữ liệu thô về khoản vay.

### models/: Lưu trữ các mô hình đã huấn luyện.

### app.py: Chương trình dự đoán bằng mô hình Random Forest.

### main.py: Chương trình dự đoán bằng mô hình XGBoost.

# Mô tả tập dữ liệu
* loan_id – ID khoản vay, một mã duy nhất để nhận diện từng khoản vay.
* no_of_dependents – Số người phụ thuộc của người vay (ví dụ: con cái, cha mẹ, v.v.).
* education – Trình độ học vấn của người vay (ví dụ: "Graduate", "Not Graduate").
* self_employed – Người vay có tự kinh doanh hay không ("Yes" hoặc "No").
* income_annum – Thu nhập hàng năm của người vay (thường tính theo đơn vị tiền tệ cụ thể, ví dụ: USD).
* loan_amount – Số tiền vay.
* loan_term – Thời hạn khoản vay (có thể tính theo tháng hoặc năm).
* cibil_score – Điểm tín dụng CIBIL của người vay (thường trong khoảng 300 - 900, điểm càng cao càng tốt).
* residential_assets_value – Giá trị tài sản nhà ở của người vay.
* commercial_assets_value – Giá trị tài sản thương mại của người vay (ví dụ: mặt bằng kinh doanh).
* luxury_assets_value – Giá trị tài sản xa xỉ của người vay (xe hơi, du thuyền, v.v.).
* bank_asset_value – Tổng giá trị tài sản của người vay trong ngân hàng.
* loan_status – Trạng thái khoản vay (ví dụ: "Approved" - Được duyệt, "Rejected" - Bị từ chối).

# Các bước thực hiện

## 1.Đọc dữ liệu và xử lý dữ liệu

## 1. Huấn luyện mô hình

* Dữ liệu được tiền xử lý, chia tập huấn luyện và kiểm tra.

* Sử dụng RandomForestClassifier, XGBClassifier, và DecisionTreeClassifier.

* Đánh giá mô hình bằng độ chính xác và ma trận nhầm lẫn.

## 2. Chương trình dự đoán

Sau khi huấn luyện mô hình, bạn có thể chạy chương trình để dự đoán một khoản vay mới có được phê duyệt hay không.

 Chạy dự đoán với Random Forest

python app.py

Bạn sẽ được yêu cầu nhập các thông tin như:

loan_amount: Số tiền vay

cibil_score: Điểm tín dụng

bank_asset_value: Tài sản ngân hàng

residential_assets_value: Giá trị tài sản nhà ở

commercial_assets_value: Giá trị tài sản thương mại

Sau đó, chương trình sẽ hiển thị:

Kết quả dự đoán (0 = Chấp nhận, 1 = Từ chối)

Xác suất dự đoán (nếu có)

Chạy dự đoán với XGBoost

python main.py

Cách nhập dữ liệu tương tự như Random Forest.

## 3. So sánh kết quả

Sau khi chạy cả ba  mô hình,tôi đưa vào thực tế 2 mô hình là mô hình Random Forset và XGboot

 Cách cài đặt và chạy dự án

Cài đặt các thư viện cần thiết:

pip install numpy pandas scikit-learn matplotlib seaborn joblib xgboost

Huấn luyện mô hình bằng cách mở các notebook và chạy toàn bộ cell.

Chạy chương trình dự đoán như hướng dẫn trên.

Kết quả mong đợi

So sánh độ chính xác giữa các mô hình.

Sử dụng mô hình có kết quả tốt nhất để áp dụng vào thực tế.
