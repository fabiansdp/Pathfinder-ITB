#Program Mencari Rute di ITB
#Menentukan Rute di ITB dari Lokasi A ke Lokasi B

#Kamus

#Prosedur
import heapq
def Masukkan_data_ITB():
    global grid
    for i in range(8,30):
        grid[i][9]="Unknown"
    grid[26][14]="Unknown"
    grid[35][12]="Unknown"
    for i in range(6,13):
        grid[34][i]="Unknown"
    for i in range(29,40):
        for j in range(8,11):
            grid[i][j]="Jalan A"
    for i in range(29,37):
        grid[i][6]="Jalan B"
    for i in range(29,40):
        grid[i][4]="Jalan C"
    for i in range(8,40):
        grid[i][2]="Jalan D"
    for i in range(14,23):
        grid[i][5]="Jalan E"
    for i in range(8,14):
        grid[i][5]="Jalan F"
    for i in range(8,30):
        grid[i][13]="Jalan G"
    for i in range(10,30):
        grid[i][17]="Jalan H"
    for i in range(29,35):
        grid[i][12]="Jalan I"
    for i in range(26,38):
        grid[i][15]="Jalan J"
    for i in range(37,40):
        grid[i][14]="Jalan J"

    for i in range(2,15):
        grid[39][i]="Jalan 1"
    for i in range(2,18):
        grid[29][i]="Jalan 2"
    for i in range(2,6):
        grid[22][i]="jalan 3"
    for i in range(5,14):
        grid[21][i]="Jalan 4"
    for i in range(5,14):
        grid[13][i]="Jalan 5"
    for i in range(13,15):
        grid[31][i]="Jalan 6"
    for i in range(14,18):
        grid[18][i]="Jalan 7"
    for i in range(14,18):
        grid[16][i]="Jalan 8"
    for i in range(13,18):
        grid[10][i]="Jalan 9"
    for i in range(2,14):
        grid[8][i]="Jalan 10"

    grid[14][14]="CRCS"
    grid[12][14]="Labtek IV"
    grid[15][14]="Basic Science B"
    grid[17][14]="Gedung Kimia Baru"
    grid[29][14]="Gedung Kimia Lama"
    grid[21][14]="Kantin Bengkok"
    grid[22][14]="Laboratorium Hidrolik"
    grid[25][15]="GKU Timur"
    grid[26][16]="Gedung eks-PPFK"
    grid[27][14]="Laboratorium Doping"
    grid[30][13]="Teknik Lingkungan"
    grid[33][13]="Labtek IXA"
    grid[33][14]="Labtek IXC"
    grid[35][14]="Labtek IXB"
    grid[35][13]="FSRD"
    grid[38][13]="Galeri Soemardja"
    grid[40][14]="Parkiran SR"
    grid[40][12]="Lapangan SR"
    grid[36][12]="LFM"
    grid[37][11]="Aula Timur"
    grid[35][11]="ATM Center"
    grid[33][11]="Lapangan CC Timur"
    grid[31][11]="CC Timur"
    grid[25][10]="Labtek VIII"
    grid[23][10]="Labtek VII"
    grid[20][10]="DPR timur"
    grid[17][10]="Gedung PLN"
    grid[15][10]="Laboratorium Fisika Dasar"
    grid[16][12]="Labtek I"
    grid[10][12]="CAS"
    grid[10][10]="Perpustakaan"
    grid[11][9]="Sunken Court"
    grid[21][9]="Plaza Widya"
    grid[24][9]="Intel"
    grid[31][9]="Information Center"
    grid[25][8]="Labtek V"
    grid[23][8]="Labtek VI"
    grid[20][8]="DPR barat"
    grid[18][8]="TVST"
    grid[15][8]="Oktagon"
    grid[10][8]="PAU"
    grid[31][7]="CC Barat"
    grid[33][7]="Lapangan Voli"
    grid[37][7]="Aula Barat"
    grid[10][6]="CADL"
    grid[15][6]="Labtek X"
    grid[18][6]="Labtek XI"
    grid[40][6]="Lapangan Sipil"
    grid[28][5]="Laboratorium Konversi Energi"
    grid[31][5]="Gedung Fisika Dasar"
    grid[33][5]="S2 PSDA"
    grid[35][5]="Sipil"
    grid[37][5]="MRK"
    grid[9][4]="SBM"
    grid[12][4]="Labtek XIV"
    grid[14][4]="Labtek III"
    grid[17][4]="Labtek II"
    grid[20][4]="FTMD"
    grid[23][4]="GKU Barat"
    grid[40][4]="Parkiran Sipil"
    grid[37][3]="Benteng Sipil"
    grid[33][3]="Basic Science A"
    grid[31][3]="CIBE"
    grid[27][3]="Lapangan Radar"
    grid[25][3]="Laboratorium Radar"
    grid[7][9]="Tunnel"
    grid[6][9]="Sarana Olahraga"

class Cell(object):
    def __init__(self, x,y,reachable):
        self.reachable=reachable
        self.x=x
        self.y=y
        self.parent=None
        self.g=0
        self.h=0
        self.f=0
    def __lt__(self, other):
        return self.f < other.f
class Astar(object):
    def __init__(self):
        #open list
        self.opened=[]
        heapq.heapify(self.opened)
        #visited cells list
        self.closed=set()
        #grid cells
        self.cells=[]
        self.grid_height=None
        self.grid_width=None

    def init_grid(self,height,width, walls, start, end):
        global grid
        self.grid_height=height
        self.grid_width=width
        for x in range(self.grid_height):
            for y in range(self.grid_width):
                if grid[x][y]=="*":
                    reachable=False
                else:
                    reachable=True
                self.cells.append(Cell(x,y,reachable))
        self.start=self.get_cell(*start)
        self.end=self.get_cell(*end)

    def get_heuristic(self,cell):
        return 20*(abs(cell.x-self.end.x)+abs(cell.y-self.end.y))

    def get_cell(self,x,y):
        return self.cells[x * self.grid_width + y]

    def get_adjacent_cells(self, cell):
        cells=[]
        if (cell.x<self.grid_height-1):
            cells.append(self.get_cell(cell.x+1, cell.y))
        if (cell.y>0):
            cells.append(self.get_cell(cell.x, cell.y-1))
        if (cell.x>0):
            cells.append(self.get_cell(cell.x-1,cell.y))
        if (cell.y<self.grid_width-1):
            cells.append(self.get_cell(cell.x,cell.y+1))
        return cells
    def get_path(self):
        cell=self.end
        path=[(cell.x,cell.y)]
        while cell.parent is not self.start:
            cell=cell.parent
            path.append((cell.x,cell.y))
        path.append((self.start.x,self.start.y))
        path.reverse()
        return path

    def display_path(self):
        cell=self.end
        while cell.parent is not self.start:
            cell=cell.parent
            print (cell.x,cell.y)

    def update_cell(self, adj,cell):
        adj.g=cell.g+10
        adj.h=self.get_heuristic(adj)
        adj.parent=cell
        adj.f=adj.h+adj.g

    def solve(self):
        heapq.heappush(self.opened, (self.start.f,self.start))
        while len(self.opened):
            f,cell = heapq.heappop(self.opened)
            self.closed.add(cell)
            if cell is self.end:
                return self.get_path()


            adj_cells=self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.g>cell.g+10):
                        self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))




#Fungsi
def Cari_posisi(target, koordinat):
    Target_x=0
    Target_y=0
    for i in range(1,42):
        for j in range(1,19):
            if (target==grid[i][j]):
                Target_x=i
                Target_y=j

    if (koordinat=="x"):
        return Target_x
    else:
        return Target_y

#Algoritma
Sudah_pernah=[[False for j in range(19)] for i in range(42)]
grid = [['*' for j in range(19)] for i in range(42)]
Rute=[]
Jalan_yang_dilewati=0
Masukkan_data_ITB()
#####################################################################
print("Masukkan Posisi Anda:", end=" ")
Posisi_awal=input()
print("Masukkan Tujuan Anda:", end=" ")
Posisi_akhir=input()

Awal_x=Cari_posisi(Posisi_awal, "x")
Awal_y=Cari_posisi(Posisi_awal, "y")
Awal=(Awal_x,Awal_y)
Akhir_x=Cari_posisi(Posisi_akhir, "x")
Akhir_y=Cari_posisi(Posisi_akhir, "y")
Akhir=(Akhir_x,Akhir_y)
#####################################################################
print("Pilihan Transportasi")
print("1. Sepeda")
print("2. Jalan Kaki")
Moda_Transportasi=int(input("Tentukan Pilihan Transportasi: "))
if (Moda_Transportasi==1):
    Kecepatan=2
elif (Moda_Transportasi==2):
    Kecepatan=1
#####################################################################
tidakbisa=set()
for i in range(42):
    for j in range(19):
        if grid[i][j]=="*":
            tidakbisa.add((i,j))
Jalan_jalan=Astar()
Jalan_jalan.init_grid(42,19,tidakbisa,Awal,Akhir)
Jawaban=Jalan_jalan.solve()
#######################################################################
print("Estimasi Waktu Kedatangan: "+str(len(Jawaban)*20/Kecepatan/60)+ " menit")
#######################################################################
print("Rute jalan dari "+Posisi_awal+" ke "+Posisi_akhir)
for i in range(len(Jawaban)):
    if (i==0):
        tmp=grid[Jawaban[i][0]][Jawaban[i][1]]
        print("- " +str(grid[Jawaban[i][0]][Jawaban[i][1]]))
    elif (tmp==grid[Jawaban[i][0]][Jawaban[i][1]] or grid[Jawaban[i][0]][Jawaban[i][1]]=="Unknown" ):
        continue
    else:
        tmp=grid[Jawaban[i][0]][Jawaban[i][1]]
        print("- "+str(grid[Jawaban[i][0]][Jawaban[i][1]]))
###################ALHAMDULILLAH#########################
input()