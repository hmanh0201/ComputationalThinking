import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    vb = float(input_data[1])
    vs = float(input_data[2])
    
    # Danh sach toa do cac tram dung (0-indexed trong code, x[0] ung voi tram 1)
    x = [float(input_data[3 + i]) for i in range(n)]
    xu = float(input_data[3 + n])
    yu = float(input_data[4 + n])
    
    # Sinh vien khong duoc xuong o tram 1, bat dau xet tu tram 2 (chi so 1 trong mang)
    best_idx = 2
    best_dist = math.hypot(x[1] - xu, yu)
    best_time = x[1] / vb + best_dist / vs
    
    eps = 1e-9
    for i in range(2, n):
        cur_dist = math.hypot(x[i] - xu, yu)
        cur_time = x[i] / vb + cur_dist / vs
        
        # So sanh thoi gian toi thieu, neu bang nhau thi uu tien khoang cach nho hon
        if cur_time < best_time - eps:
            best_time = cur_time
            best_dist = cur_dist
            best_idx = i + 1
        elif abs(cur_time - best_time) <= eps:
            if cur_dist < best_dist:
                best_time = cur_time
                best_dist = cur_dist
                best_idx = i + 1
                
    sys.stdout.write(str(best_idx) + "\n")

if __name__ == '__main__':
    main()