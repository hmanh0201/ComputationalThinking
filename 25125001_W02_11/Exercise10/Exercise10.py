import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    requests = [int(val) for val in input_data[2:2 + n]]
    
    xc = (k + 1) // 2
    yc = (k + 1) // 2
    
    # Tien xu ly mang cong don khoang cach theo toa do cot y
    pref_dist_y = [0] * (k + 1)
    for y in range(1, k + 1):
        pref_dist_y[y] = pref_dist_y[y - 1] + abs(y - yc)
        
    # occupied[x][y] = 1 neu ghe da duoc mua, 0 neu con trong
    occupied = [[0] * (k + 1) for _ in range(k + 1)]
    # pref_occ[x][y] = so luong ghe da bi chiem tu cot 1 den cot y tren hang x
    pref_occ = [[0] * (k + 1) for _ in range(k + 1)]
    
    results = []
    
    for m in requests:
        best_cost = float('inf')
        best_x = -1
        best_yl = -1
        best_yr = -1
        
        # Duyet x tu 1 den k va yl tu 1 den k - m + 1 de tu dong thoa man tie-breaking
        for x in range(1, k + 1):
            row_pref = pref_occ[x]
            cost_x = m * abs(x - xc)
            
            for yl in range(1, k - m + 2):
                yr = yl + m - 1
                
                # Kiem tra nhanh toan bo doan [yl, yr] co trong hay khong
                if row_pref[yr] == row_pref[yl - 1]:
                    total_cost = cost_x + (pref_dist_y[yr] - pref_dist_y[yl - 1])
                    if total_cost < best_cost:
                        best_cost = total_cost
                        best_x = x
                        best_yl = yl
                        best_yr = yr
                        
        if best_x != -1:
            results.append(f"{best_x} {best_yl} {best_yr}")
            # Danh dau cac ghe vua duoc dat
            for y in range(best_yl, best_yr + 1):
                occupied[best_x][y] = 1
            # Cap nhat lai mang tien to tren hang best_x
            for y in range(1, k + 1):
                pref_occ[best_x][y] = pref_occ[best_x][y - 1] + occupied[best_x][y]
        else:
            results.append("-1")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()