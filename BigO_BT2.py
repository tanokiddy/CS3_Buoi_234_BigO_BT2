# i = 0
# while i < n:
#     i = i + 100


#1: Phân tích
    #1: Đối với vòng lặp:
        # while i < n: (N / 100) lần
        # i = i + 100: (2N / 100) lần
        # Input càng lớn thì số lần lặp càng nhiều, với vòng lặp while trên thì tổng số lần lặp của toàn bộ các dòng lệnh là : 1 + 3N/100

        # Ví dụ: n = 600
        # i = 0: 1 lần
        # while i < n: 6 lần
        #     i = i + 100: 12 lần (2 phép toán)
        # Số lần lặp là: 1 + 3*600/100 = 19 lần thực thi
    #2: Đối với đệ quy:
        # Đệ quy bản chất là 1 hàm gọi lại chính nó bên trong hàm đó
        # Điều kiện dừng trong đệ quy dùng để thoát vòng lặp, nếu không có điều kiện dừng đệ quy thì nó sẽ lặp vô tận
        
    #3: Đối với thao tác khác:
        # i = 0: 1 lần (i nằm ngoài vòng lặp)
        # while i < n: (N / 100) lần
        # i = i + 100: (2N / 100) lần (2 phép toán)
#2: Output
    # F(N) = 1 + N/100 + 2N/100 (1 + 3N/100)
    # O(N)