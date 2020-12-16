import os
import re
from read_data import *
from feature import *
from predict_by_knn import *

def get_info_train_data():
	return {
		"Am thuc": 265,
		"Bat dong san": 246,
		"Duong vao WTO": 208,
		"Gia dinh": 213,
		"Hinh su": 155,
		"Khong gian song": 134,
		"Loi song": 223,
		"Mua sam": 187,
		"My thuat": 193,
		"The gioi tre": 331	
	}
def get_info_test_data():
	return {
		"Am thuc": 400,
		"Bat dong san": 282,
		"Duong vao WTO": 191,
		"Gia dinh": 280,
		"Hinh su": 196,
		"Khong gian song": 58,
		"Loi song": 214,
		"Mua sam": 84,
		"My thuat": 144,
		"The gioi tre": 380	
	}
def predict_by_text(text):
	lines = text
	lines = lines.lower()
	lines = re.sub(r"[^\w\d\s]"," ",lines,flags=re.UNICODE)
	lines = re.sub("[0-9]"," ",lines,flags=re.UNICODE)
	lines = lines.split()
	lines = ' '.join(lines)
	test_data_tf = tfTranform([lines])
	return predict_classification(X_data_tf,test_data_tf[0],5)
def predict_1_file(file_path):
	test = []
	with open(file_path, 'r', encoding="utf-16") as f:
		lines = f.readlines()
		lines = ' '.join(lines)
		lines = lines.lower()
		lines = re.sub(r"[^\w\d\s]"," ",lines,flags=re.UNICODE)
		lines = re.sub("[0-9]"," ",lines,flags=re.UNICODE)
		lines = lines.split()
		lines = ' '.join(lines)
		test.append(lines)
	test_data_tf = tfTranform(test)
	return predict_classification(X_data_tf,test_data_tf[0],5)
def predict_folder(folder_path):
	folder_data = []
	dirs = os.listdir(folder_path)
	for file_path in dirs:
		with open(os.path.join(folder_path, file_path), 'r', encoding="utf-16") as f:
			lines = f.readlines()
			lines = ' '.join(lines)
			lines = lines.lower()
			lines = re.sub(r"[^\w\d\s]"," ",lines,flags=re.UNICODE)
			lines = re.sub("[0-9]"," ",lines,flags=re.UNICODE)
			lines = lines.split()
			lines = ' '.join(lines)
			folder_data.append(lines)
	folder_data_tf = tfTranform(folder_data)
	predict_test = []
	for row in range(len(X_test_tf)):
		predict_test.append(predict_classification(X_data_tf,X_test_tf[row],5))
	print(accuracy_metric(y_test,predict_test))
	return predict_test
print(predict_1_file('new test - Copy (3)\Am thuc\AT_NLD_T_ (391).txt'))
print(predict_by_text("Chè sen trứng gà Tách trứng gà ra cho vào nước dấm đang sôi luộc chín, vớt ra thả vào nước chín nguội, cuối cùng vớt ra cho ráo nước, rồi cho vào chè sen.\nNguyên liệu \n100g hạt sen tươi \n6 trứng gà \n100g đường phèn, vani, dấm nuôi \nThực hiện \nHạt sen: Rửa sạch nấu mềm với 300ml nước, cho đường vào nấu tan cho vani vào tắt bếp. Đặt nồi nước nhỏ lên bếp cho 1/2 dấm nhỏ vào nấu sôi. \nTách trứng gà ra cho vào nước dấm đang sôi luộc chín, vớt ra thả vào nước chín nguội, cuối cùng vớt ra cho ráo nước, rồi cho vào chè sen. Dùng nóng hay lạnh đều ngon. "))

	