student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]

def find_student_by_id (records, student_id):
    student = next((s for s in records if s["student_id"] == student_id), None)
    return student


def display_statements(records):
    print("-" * 67, "SAO KÊ ĐIỂM SỐ", "-" * 67)
    for i,r in enumerate(records,start=1):
        if r["current_points"] > 1500:
            status = "Thành viên ưu tú"

        elif r["current_points"] >= 500:
            status = "Thành viên tiềm năng"

        else :
            status = "Cần tích lũy thêm"

        print(
            f"{i}."
            f"Mã: {r["student_id"]:<4} | "
            f"Tên: {r["name"]:<25} | "
            f"Hiện có: {r["current_points"]:<6} | "
            f"Đã tiêu: {r["spent_points"]:<6} | "
            f"Hoàn trả: {r["refunded_points"]:<6} | "
            f"Hệ số: x{r["multiplier"]:<4} | "
            f"Trạng thái: {status} "
        )
    print("-"*150)

def redeem_rewards(records):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if student_id == "":
            print("Mã học viên không hợp lệ!")
            continue
        else:
            break
    
    student = find_student_by_id(records, student_id)
    if student:
        while True:
            points_to_spend = int(input("Nhập số điểm tiêu: "))
            if points_to_spend > student["current_points"]:
                print("Số dư điểm không đủ để thực hiện giao dịch!")
                continue
            else:
                student["spent_points"] = student["spent_points"] + points_to_spend
                student["current_points"] = student["current_points"] - points_to_spend
                print(f">> Hoàn điểm thành công! '{student['name']}' đã tiêu {points_to_spend} điểm. Số dư còn lại: {student["current_points"]} điểm")
                break
    else:
        print("Không tìm thấy sinh viên!")

def appeal_score(records):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if student_id == "":
            print("Mã học viên không hợp lệ!")
            continue
        else:
            break
    
    student = find_student_by_id(records, student_id)
    if student:
        while True:
            points_to_refund = int(input("Nhập số điểm hoàn lại: "))
            if points_to_refund > student["spent_points"]:
                print("Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu!")
                continue
            else:
                student["spent_points"] = student["spent_points"] - points_to_refund
                student["current_points"] = student["current_points"] + points_to_refund
                student["refunded_points"] = student["refunded_points"] + points_to_refund
                print(f">> Hoàn điểm thành công! '{student['name']}' được cộng lại {points_to_refund} điểm.")
                break
    else:
        print("Không tìm thấy sinh viên!")

def activate_multiplier(records):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if student_id == "":
            print("Mã học viên không hợp lệ!")
            continue
        else:
            break
    
    student = find_student_by_id(records, student_id)
    if student:
        while True:
            new_multiplier = float(input("Nhập hệ số nhân mới (1.0 - 3.0): "))
            if new_multiplier > 3 or new_multiplier < 1:
                print("Hệ số nhân không hợp lệ.Chỉ chấp nhận số từ 1.0 đến 3.0")
                continue
            else:
                
                student["multiplier"] = new_multiplier
                print(f">> Đã kích hoạt hệ số x{new_multiplier} cho học viên '{student['name']}' .")
                break
    else:
        print("Không tìm thấy sinh viên!")

def grade_assignment(records):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if student_id == "":
            print("Mã học viên không hợp lệ!")
            continue
        else:
            break
    
    student = find_student_by_id(records, student_id)
    if student:
        while True:
            original_score = float(input("Nhập điểm số gốc đạt được: "))
            if original_score  < 0:
                print("Hệ số không hợp lệ!")
                continue
            else:
                final_score = student['multiplier'] * original_score
                student['current_points'] += final_score
                print(f">> Hệ số hiện tại của '{student['name']}' là: x{student['multiplier']}. Điểm thực nhận {final_score}")
                print(f">> Đã cộng {final_score} điểm vào tài khoản!")
                break
    else:
        print("Không tìm thấy sinh viên!")

def main():
    menu = {
        1:display_statements,
        2:redeem_rewards,
        3:appeal_score,
        4:activate_multiplier,
        5:grade_assignment,
        6: lambda records: exit("Thoát chương trình!")
    }

    while True:
        choice = input(f"""
    ===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====
    1. Hiển thị sao kê điểm số
    2. Đổi điểm lấy phần thưởng
    3. Phúc khảo bài thi (Hoàn điểm)
    4. Kích hoạt (Hệ số nhân điểm)
    5. Chấm bài (thêm điểm)
    6. Thoát chương trình
    =====================================================
    Nhập lựa chọn (1-6):
        """).strip()
        if not choice.isdigit():
            print("Vui lòng nhập số!")
            continue

        choice = int(choice)
        if choice in menu:
                menu[choice](student_records)
        else:
            print("Lựa chọn không hợp lệ!")
        
if __name__ == "__main__": 
    main()
    