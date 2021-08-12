from Markers import Markers 
from transform_functions import get_fft, get_features

INPUT_FILENAMES = ['./Dataset/RBDS001runT25markers.txt', './Dataset/RBDS001runT35markers.txt', './Dataset/RBDS001runT45markers.txt',
            './Dataset/RBDS002runT25markers.txt', './Dataset/RBDS002runT35markers.txt', './Dataset/RBDS002runT45markers.txt',
            './Dataset/RBDS003runT25markers.txt', './Dataset/RBDS003runT35markers.txt', './Dataset/RBDS003runT45markers.txt',
            './Dataset/RBDS004runT25markers.txt', './Dataset/RBDS004runT35markers.txt', './Dataset/RBDS004runT45markers.txt',
            './Dataset/RBDS005runT25markers.txt', './Dataset/RBDS005runT35markers.txt', './Dataset/RBDS005runT45markers.txt',
            './Dataset/RBDS006runT25markers.txt', './Dataset/RBDS006runT35markers.txt', './Dataset/RBDS006runT45markers.txt',
            './Dataset/RBDS007runT25markers.txt', './Dataset/RBDS007runT35markers.txt', './Dataset/RBDS007runT45markers.txt',
            './Dataset/RBDS008runT25markers.txt', './Dataset/RBDS008runT35markers.txt', './Dataset/RBDS008runT45markers.txt',
            './Dataset/RBDS009runT25markers.txt', './Dataset/RBDS009runT35markers.txt', './Dataset/RBDS009runT45markers.txt',
            './Dataset/RBDS010runT25markers.txt', './Dataset/RBDS010runT35markers.txt', './Dataset/RBDS010runT45markers.txt',
            './Dataset/RBDS011runT25markers.txt', './Dataset/RBDS011runT35markers.txt', './Dataset/RBDS011runT45markers.txt',
            './Dataset/RBDS012runT25markers.txt', './Dataset/RBDS012runT35markers.txt', './Dataset/RBDS012runT45markers.txt',
            './Dataset/RBDS013runT25markers.txt', './Dataset/RBDS013runT35markers.txt', './Dataset/RBDS013runT45markers.txt',
            './Dataset/RBDS014runT25markers.txt', './Dataset/RBDS014runT35markers.txt', './Dataset/RBDS014runT45markers.txt',
            './Dataset/RBDS015runT25markers.txt', './Dataset/RBDS015runT35markers.txt', './Dataset/RBDS015runT45markers.txt',
            './Dataset/RBDS016runT25markers.txt', './Dataset/RBDS016runT35markers.txt', './Dataset/RBDS016runT45markers.txt',
            './Dataset/RBDS017runT25markers.txt', './Dataset/RBDS017runT35markers.txt', './Dataset/RBDS017runT45markers.txt',
            './Dataset/RBDS018runT25markers.txt', './Dataset/RBDS018runT35markers.txt', './Dataset/RBDS018runT45markers.txt',
            './Dataset/RBDS019runT25markers.txt', './Dataset/RBDS019runT35markers.txt', './Dataset/RBDS019runT45markers.txt',
            './Dataset/RBDS020runT25markers.txt', './Dataset/RBDS020runT35markers.txt', './Dataset/RBDS020runT45markers.txt',
            './Dataset/RBDS021runT25markers.txt', './Dataset/RBDS021runT35markers.txt', './Dataset/RBDS021runT45markers.txt',
            './Dataset/RBDS022runT25markers.txt', './Dataset/RBDS022runT35markers.txt', './Dataset/RBDS022runT45markers.txt',
            './Dataset/RBDS023runT25markers.txt', './Dataset/RBDS023runT35markers.txt', './Dataset/RBDS023runT45markers.txt',
            './Dataset/RBDS024runT25markers.txt', './Dataset/RBDS024runT35markers.txt', './Dataset/RBDS024runT45markers.txt',
            './Dataset/RBDS025runT25markers.txt', './Dataset/RBDS025runT35markers.txt', './Dataset/RBDS025runT45markers.txt',
            './Dataset/RBDS026runT25markers.txt', './Dataset/RBDS026runT35markers.txt', './Dataset/RBDS026runT45markers.txt',
            './Dataset/RBDS027runT25markers.txt', './Dataset/RBDS027runT35markers.txt', './Dataset/RBDS027runT45markers.txt',
            './Dataset/RBDS028runT25markers.txt', './Dataset/RBDS028runT35markers.txt', './Dataset/RBDS028runT45markers.txt',]


data = []
all_data = []
    
for dataset in INPUT_FILENAMES:
    f = open(dataset, 'r')

    # nomeei as colunas, transformei-as em vetores
    # subtitui os pontos nos nomes das colunas por underlines, por questao de sintaxe da linguagem

    #Articulações do quadril
    Time = []
    R_ASISX = []
    R_ASISY = []
    R_ASISZ = []
    L_ASISX = []
    L_ASISY = []
    L_ASISZ = []
    R_PSISX = []
    R_PSISY = []
    R_PSISZ = []
    L_PSISX = []
    L_PSISY = []
    L_PSISZ = []
    R_Iliac_CrestX = []
    R_Iliac_CrestY = []
    R_Iliac_CrestZ = []
    L_Iliac_CrestX = []
    L_Iliac_CrestY = []
    L_Iliac_CrestZ = []

    #Demais Articulações
    R_Thigh_Top_LateralX = []
    R_Thigh_Top_LateralY = [] 
    R_Thigh_Top_LateralZ = []
    R_Thigh_Bottom_LateralX = []
    R_Thig_Bottom_LateralY = []
    R_Thigh_Bottom_LateralZ = []
    R_Thigh_Top_MedialX = []
    R_Thigh_Top_MedialY = []
    R_Thigh_Top_MedialZ = []
    R_Thigh_Bottom_MedialX = []
    R_Thigh_Bottom_MedialY = []
    R_Thigh_Bottom_MedialZ = []
    R_Shank_Top_LateralX = []
    R_Shank_Top_LateralY = []
    R_Shank_Top_LateralZ = []
    R_Shank_Bottom_LateralX = []
    R_Shank_Bottom_LateralY = []
    R_Shank_Bottom_LateralZ = []
    R_Shank_Top_MedialX = []
    R_Shank_Top_MedialY = []
    R_Shank_Top_MedialZ = []
    R_Shank_Bottom_MedialX = []
    R_Shank_Bottom_MedialY = []
    R_Shank_Bottom_MedialZ = []
    R_Heel_TopX = []
    R_Heel_TopY = []
    R_Heel_TopZ = []
    R_Heel_BottomX = []
    R_Heel_BottomY = []
    R_Heel_BottomZ = []
    R_Heel_LateralX = []
    R_Heel_LateralY = []
    R_Heel_LateralZ = []
    L_Thigh_Top_LateralX = []
    L_Thigh_Top_LateralY = []
    L_Thigh_Top_LateralZ = []
    L_Thigh_Bottom_LateralX = []
    L_Thigh_Bottom_LateralY = []
    L_Thigh_Bottom_LateralZ = []
    L_Thigh_Top_MedialX = []
    L_Thigh_Top_MedialY = []
    L_Thigh_Top_MedialZ = []
    L_Thigh_Bottom_MedialX = []
    L_Thigh_Bottom_MedialY = []
    L_Thigh_Bottom_MedialZ = []
    L_Shank_Top_LateralX = []
    L_Shank_Top_LateralY = []
    L_Shank_Top_LateralZ = []
    L_Shank_Bottom_LateralX = []
    L_Shank_Bottom_LateralY = []
    L_Shank_Bottom_LateralZ = []
    L_Shank_Top_MedialX = []
    L_Shank_Top_MedialY = []
    L_Shank_Top_MedialZ = []
    L_Shank_Bottom_MedialX = []
    L_Shank_Bottom_MedialY = []
    L_Shank_Bottom_MedialZ = []
    L_Heel_TopX = []
    L_Heel_TopY = []
    L_Heel_TopZ = []
    L_Heel_BottomX = []
    L_Heel_BottomY = []
    L_Heel_BottomZ = []
    L_Heel_LateralX = []
    L_Heel_LateralY = []
    L_Heel_LateralZ = []
    R_MT1X = []
    R_MT1Y = []
    R_MT1Z = []
    R_MT5X = []
    R_MT5Y = []
    R_MT5Z = []
    L_MT1X = []
    L_MT1Y = []
    L_MT1Z = []
    L_MT5X = []
    L_MT5Y = []
    L_MT5Z = []
    
    aux = 0
    for line in f:
        line = line.strip()
        if aux>0: #exclui a linha de cabeçalhos
            #criei variaveis auxiliares para receberem os valores lidos dentro de f e as nomeei com o mesmo nome da variavel anterior, mas com q_ na frente
            q_Time, q_R_ASISX, q_R_ASISY, q_R_ASISZ, q_L_ASISX, q_L_ASISY, q_L_ASISZ,	q_R_PSISX, q_R_PSISY, q_R_PSISZ, q_L_PSISX,	q_L_PSISY, q_L_PSISZ, q_R_Iliac_CrestX, q_R_Iliac_CrestY,q_R_Iliac_CrestZ, q_L_Iliac_CrestX, q_L_Iliac_CrestY, q_L_Iliac_CrestZ,q_R_Thigh_Top_LateralX, q_R_Thigh_Top_LateralY, q_R_Thigh_Top_LateralZ,	q_R_Thigh_Bottom_LateralX, q_R_Thig_Bottom_LateralY, q_R_Thigh_Bottom_LateralZ, q_R_Thigh_Top_MedialX, q_R_Thigh_Top_MedialY, q_R_Thigh_Top_MedialZ, q_R_Thigh_Bottom_MedialX, q_R_Thigh_Bottom_MedialY, q_R_Thigh_Bottom_MedialZ, q_R_Shank_Top_LateralX,q_R_Shank_Top_LateralY, q_R_Shank_Top_LateralZ, q_R_Shank_Bottom_LateralX, q_R_Shank_Bottom_LateralY,q_R_Shank_Bottom_LateralZ, q_R_Shank_Top_MedialX, q_R_Shank_Top_MedialY, q_R_Shank_Top_MedialZ, q_R_Shank_Bottom_MedialX, q_R_Shank_Bottom_MedialY, q_R_Shank_Bottom_MedialZ, q_R_Heel_TopX, q_R_Heel_TopY, q_R_Heel_TopZ, q_R_Heel_BottomX, q_R_Heel_BottomY, q_R_Heel_BottomZ, q_R_Heel_LateralX, q_R_Heel_LateralY, q_R_Heel_LateralZ, q_L_Thigh_Top_LateralX, q_L_Thigh_Top_LateralY, q_L_Thigh_Top_LateralZ, q_L_Thigh_Bottom_LateralX, q_L_Thigh_Bottom_LateralY, q_L_Thigh_Bottom_LateralZ, q_L_Thigh_Top_MedialX, q_L_Thigh_Top_MedialY, q_L_Thigh_Top_MedialZ, q_L_Thigh_Bottom_MedialX, q_L_Thigh_Bottom_MedialY, q_L_Thigh_Bottom_MedialZ, q_L_Shank_Top_LateralX, q_L_Shank_Top_LateralY, q_L_Shank_Top_LateralZ, q_L_Shank_Bottom_LateralX, q_L_Shank_Bottom_LateralY, q_L_Shank_Bottom_LateralZ, q_L_Shank_Top_MedialX, q_L_Shank_Top_MedialY, q_L_Shank_Top_MedialZ, q_L_Shank_Bottom_MedialX, q_L_Shank_Bottom_MedialY, q_L_Shank_Bottom_MedialZ, q_L_Heel_TopX, q_L_Heel_TopY, q_L_Heel_TopZ, q_L_Heel_BottomX, q_L_Heel_BottomY, q_L_Heel_BottomZ, q_L_Heel_LateralX, q_L_Heel_LateralY, q_L_Heel_LateralZ, q_R_MT1X, q_R_MT1Y, q_R_MT1Z, q_R_MT5X, q_R_MT5Y, q_R_MT5Z, q_L_MT1X, q_L_MT1Y, q_L_MT1Z, q_L_MT5X, q_L_MT5Y, q_L_MT5Z = line.split()


            #inserção das variaveis auxiliares dentro dos vetores

            Time.append(float(q_Time))
            if ((q_R_ASISX != "nan") & (q_R_ASISX != "NaN") & (q_R_ASISX != "NAN")): R_ASISX.append(float(q_R_ASISX))
            else: R_ASISX.append(R_ASISX[aux-2])

            if ((q_R_ASISY != "nan") & (q_R_ASISY != "NaN") & (q_R_ASISY != "NAN")):R_ASISY.append(float(q_R_ASISY))
            else: R_ASISY.append(R_ASISY[aux - 2])

            if ((q_R_ASISZ != "nan") & (q_R_ASISZ != "NaN") & (q_R_ASISZ != "NAN")):R_ASISZ.append(float(q_R_ASISZ))
            else: R_ASISZ.append(R_ASISZ[aux - 2])

            if ((q_L_ASISX != "nan") & (q_L_ASISX != "NaN") & (q_L_ASISX != "NAN")):L_ASISX.append(float(q_L_ASISX))
            else: L_ASISX.append(L_ASISX[aux - 2])

            if ((q_L_ASISY != "nan") & (q_L_ASISY != "NaN") & (q_L_ASISY != "NAN")):L_ASISY.append(float(q_L_ASISY))
            else: L_ASISY.append(L_ASISY[aux - 2])

            if ((q_L_ASISZ != "nan") & (q_L_ASISZ != "NaN") & (q_L_ASISZ != "NAN")):L_ASISZ.append(float(q_L_ASISZ))
            else: L_ASISZ.append(L_ASISZ[aux - 2])

            if ((q_R_PSISX != "nan") & (q_R_PSISX != "NaN") & (q_R_PSISX != "NAN")):R_PSISX.append(float(q_R_PSISX))
            else: R_PSISX.append(R_PSISX[aux - 2])

            if ((q_R_PSISY != "nan") & (q_R_PSISY != "NaN") & (q_R_PSISY != "NAN")):R_PSISY.append(float(q_R_PSISY))
            else: R_PSISY.append(R_PSISY[aux - 2])

            if ((q_R_PSISZ != "nan") & (q_R_PSISZ != "NaN") & (q_R_PSISZ != "NAN")):R_PSISZ.append(float(q_R_PSISZ))
            else: R_PSISZ.append(R_PSISZ[aux - 2])

            if ((q_L_PSISX != "nan") & (q_L_PSISX != "NaN") & (q_L_PSISX != "NAN")):L_PSISX.append(float(q_L_PSISX))
            else: L_PSISX.append(L_PSISX[aux - 2])

            if ((q_L_PSISY != "nan") & (q_L_PSISY != "NaN") & (q_L_PSISY != "NAN")):L_PSISY.append(float(q_L_PSISY))
            else: L_PSISY.append(L_PSISY[aux - 2])

            if ((q_L_PSISZ != "nan") & (q_L_PSISZ != "NaN") & (q_L_PSISZ != "NAN")):L_PSISZ.append(float(q_L_PSISZ))
            else: L_PSISZ.append(L_PSISZ[aux - 2])

            if ((q_R_Iliac_CrestX != "nan") & (q_R_Iliac_CrestX != "NaN") & (q_R_Iliac_CrestX != "NAN")):R_Iliac_CrestX.append(float(q_R_Iliac_CrestX))
            else: R_Iliac_CrestX.append(R_Iliac_CrestX[aux - 2])

            if ((q_R_Iliac_CrestY != "nan") & (q_R_Iliac_CrestY != "NaN") & (q_R_Iliac_CrestY != "NAN")):R_Iliac_CrestY.append(float(q_R_Iliac_CrestY))
            else: R_Iliac_CrestY.append(R_Iliac_CrestY[aux - 2])

            if ((q_R_Iliac_CrestZ != "nan") & (q_R_Iliac_CrestZ != "NaN") & (q_R_Iliac_CrestZ != "NAN")):R_Iliac_CrestZ.append(float(q_R_Iliac_CrestZ))
            else: R_Iliac_CrestZ.append(R_Iliac_CrestZ[aux - 2])

            if ((q_L_Iliac_CrestX != "nan") & (q_L_Iliac_CrestX != "NaN") & (q_L_Iliac_CrestX != "NAN")):L_Iliac_CrestX.append(float(q_L_Iliac_CrestX))
            else: L_Iliac_CrestX.append(L_Iliac_CrestX[aux - 2])

            if ((q_L_Iliac_CrestY != "nan") & (q_L_Iliac_CrestY != "NaN") & (q_L_Iliac_CrestY != "NAN")):L_Iliac_CrestY.append(float(q_L_Iliac_CrestY))
            else: L_Iliac_CrestY.append(L_Iliac_CrestY[aux - 2])

            if ((q_L_Iliac_CrestZ != "nan") & (q_L_Iliac_CrestZ != "NaN") & (q_L_Iliac_CrestZ != "NAN")):L_Iliac_CrestZ.append(float(q_L_Iliac_CrestZ))
            else: L_Iliac_CrestZ.append(L_Iliac_CrestZ[aux - 2])
################################## NORMALIZAÇÂO DAS NOVAS ARTICULAÇÔES #############################################################
            if ((q_R_Thigh_Top_LateralX  != "nan") & (q_R_Thigh_Top_LateralX  != "NaN") & (q_R_Thigh_Top_LateralX  != "NAN")):R_Thigh_Top_LateralX .append(float(q_R_Thigh_Top_LateralX ))
            else: R_Thigh_Top_LateralX .append(R_Thigh_Top_LateralX [aux - 2])
            
            if ((q_R_Thigh_Top_LateralY  != "nan") & (q_R_Thigh_Top_LateralY  != "NaN") & (q_R_Thigh_Top_LateralY  != "NAN")):R_Thigh_Top_LateralY .append(float(q_R_Thigh_Top_LateralY ))
            else: R_Thigh_Top_LateralY .append(R_Thigh_Top_LateralY [aux - 2])

            if ((q_R_Thigh_Top_LateralZ  != "nan") & (q_R_Thigh_Top_LateralZ  != "NaN") & (q_R_Thigh_Top_LateralZ  != "NAN")):R_Thigh_Top_LateralZ .append(float(q_R_Thigh_Top_LateralZ ))
            else: R_Thigh_Top_LateralZ .append(R_Thigh_Top_LateralZ [aux - 2])

            if ((q_R_Thigh_Bottom_LateralX  != "nan") & (q_R_Thigh_Bottom_LateralX  != "NaN") & (q_R_Thigh_Bottom_LateralX  != "NAN")):R_Thigh_Bottom_LateralX .append(float(q_R_Thigh_Bottom_LateralX ))
            else: R_Thigh_Bottom_LateralX .append(R_Thigh_Bottom_LateralX [aux - 2])

            if ((q_R_Thig_Bottom_LateralY  != "nan") & (q_R_Thig_Bottom_LateralY  != "NaN") & (q_R_Thig_Bottom_LateralY  != "NAN")):R_Thig_Bottom_LateralY .append(float(q_R_Thig_Bottom_LateralY ))
            else: R_Thig_Bottom_LateralY .append(R_Thig_Bottom_LateralY [aux - 2])

            if ((q_R_Thigh_Bottom_LateralZ  != "nan") & (q_R_Thigh_Bottom_LateralZ  != "NaN") & (q_R_Thigh_Bottom_LateralZ  != "NAN")):R_Thigh_Bottom_LateralZ .append(float(q_R_Thigh_Bottom_LateralZ ))
            else: R_Thigh_Bottom_LateralZ .append(R_Thigh_Bottom_LateralZ [aux - 2])

            if ((q_R_Thigh_Top_MedialX  != "nan") & (q_R_Thigh_Top_MedialX  != "NaN") & (q_R_Thigh_Top_MedialX  != "NAN")):R_Thigh_Top_MedialX .append(float(q_R_Thigh_Top_MedialX ))
            else: R_Thigh_Top_MedialX .append(R_Thigh_Top_MedialX [aux - 2])

            if ((q_R_Thigh_Top_MedialY  != "nan") & (q_R_Thigh_Top_MedialY  != "NaN") & (q_R_Thigh_Top_MedialY  != "NAN")):R_Thigh_Top_MedialY .append(float(q_R_Thigh_Top_MedialY ))
            else: R_Thigh_Top_MedialY .append(R_Thigh_Top_MedialY [aux - 2])

            if ((q_R_Thigh_Top_MedialZ  != "nan") & (q_R_Thigh_Top_MedialZ  != "NaN") & (q_R_Thigh_Top_MedialZ  != "NAN")):R_Thigh_Top_MedialZ .append(float(q_R_Thigh_Top_MedialZ ))
            else: R_Thigh_Top_MedialZ .append(R_Thigh_Top_MedialZ [aux - 2])

            if ((q_R_Thigh_Bottom_MedialX  != "nan") & (q_R_Thigh_Bottom_MedialX  != "NaN") & (q_R_Thigh_Bottom_MedialX  != "NAN")):R_Thigh_Bottom_MedialX .append(float(q_R_Thigh_Bottom_MedialX ))
            else: R_Thigh_Bottom_MedialX .append(R_Thigh_Bottom_MedialX [aux - 2])

            if ((q_R_Thigh_Bottom_MedialY  != "nan") & (q_R_Thigh_Bottom_MedialY  != "NaN") & (q_R_Thigh_Bottom_MedialY  != "NAN")):R_Thigh_Bottom_MedialY .append(float(q_R_Thigh_Bottom_MedialY ))
            else: R_Thigh_Bottom_MedialY .append(R_Thigh_Bottom_MedialY [aux - 2])

            if ((q_R_Thigh_Bottom_MedialZ  != "nan") & (q_R_Thigh_Bottom_MedialZ  != "NaN") & (q_R_Thigh_Bottom_MedialZ  != "NAN")):R_Thigh_Bottom_MedialZ .append(float(q_R_Thigh_Bottom_MedialZ ))
            else: R_Thigh_Bottom_MedialZ .append(R_Thigh_Bottom_MedialZ [aux - 2])

            if ((q_R_Shank_Top_LateralX  != "nan") & (q_R_Shank_Top_LateralX  != "NaN") & (q_R_Shank_Top_LateralX  != "NAN")):R_Shank_Top_LateralX .append(float(q_R_Shank_Top_LateralX ))
            else: R_Shank_Top_LateralX .append(R_Shank_Top_LateralX [aux - 2])

            if ((q_R_Shank_Top_LateralY  != "nan") & (q_R_Shank_Top_LateralY  != "NaN") & (q_R_Shank_Top_LateralY  != "NAN")):R_Shank_Top_LateralY .append(float(q_R_Shank_Top_LateralY ))
            else: R_Shank_Top_LateralY .append(R_Shank_Top_LateralY [aux - 2])

            if ((q_R_Shank_Top_LateralZ  != "nan") & (q_R_Shank_Top_LateralZ  != "NaN") & (q_R_Shank_Top_LateralZ  != "NAN")):R_Shank_Top_LateralZ .append(float(q_R_Shank_Top_LateralZ ))
            else: R_Shank_Top_LateralZ .append(R_Shank_Top_LateralZ [aux - 2])

            if ((q_R_Shank_Bottom_LateralX  != "nan") & (q_R_Shank_Bottom_LateralX  != "NaN") & (q_R_Shank_Bottom_LateralX  != "NAN")):R_Shank_Bottom_LateralX .append(float(q_R_Shank_Bottom_LateralX ))
            else: R_Shank_Bottom_LateralX .append(R_Shank_Bottom_LateralX [aux - 2])

            if ((q_R_Shank_Bottom_LateralY  != "nan") & (q_R_Shank_Bottom_LateralY  != "NaN") & (q_R_Shank_Bottom_LateralY  != "NAN")):R_Shank_Bottom_LateralY .append(float(q_R_Shank_Bottom_LateralY ))
            else: R_Shank_Bottom_LateralY .append(R_Shank_Bottom_LateralY [aux - 2])

            if ((q_R_Shank_Bottom_LateralZ  != "nan") & (q_R_Shank_Bottom_LateralZ  != "NaN") & (q_R_Shank_Bottom_LateralZ  != "NAN")):R_Shank_Bottom_LateralZ .append(float(q_R_Shank_Bottom_LateralZ ))
            else: R_Shank_Bottom_LateralZ .append(R_Shank_Bottom_LateralZ [aux - 2])

            if ((q_R_Shank_Top_MedialX  != "nan") & (q_R_Shank_Top_MedialX  != "NaN") & (q_R_Shank_Top_MedialX  != "NAN")):R_Shank_Top_MedialX .append(float(q_R_Shank_Top_MedialX ))
            else: R_Shank_Top_MedialX .append(R_Shank_Top_MedialX [aux - 2])

            if ((q_R_Shank_Top_MedialY  != "nan") & (q_R_Shank_Top_MedialY  != "NaN") & (q_R_Shank_Top_MedialY  != "NAN")):R_Shank_Top_MedialY .append(float(q_R_Shank_Top_MedialY ))
            else: R_Shank_Top_MedialY .append(R_Shank_Top_MedialY [aux - 2])

            if ((q_R_Shank_Top_MedialZ  != "nan") & (q_R_Shank_Top_MedialZ  != "NaN") & (q_R_Shank_Top_MedialZ  != "NAN")):R_Shank_Top_MedialZ .append(float(q_R_Shank_Top_MedialZ ))
            else: R_Shank_Top_MedialZ .append(R_Shank_Top_MedialZ [aux - 2])

            if ((q_R_Shank_Bottom_MedialX  != "nan") & (q_R_Shank_Bottom_MedialX  != "NaN") & (q_R_Shank_Bottom_MedialX  != "NAN")):R_Shank_Bottom_MedialX .append(float(q_R_Shank_Bottom_MedialX ))
            else: R_Shank_Bottom_MedialX .append(R_Shank_Bottom_MedialX [aux - 2])

            if ((q_R_Shank_Bottom_MedialY  != "nan") & (q_R_Shank_Bottom_MedialY  != "NaN") & (q_R_Shank_Bottom_MedialY  != "NAN")):R_Shank_Bottom_MedialY .append(float(q_R_Shank_Bottom_MedialY ))
            else: R_Shank_Bottom_MedialY .append(R_Shank_Bottom_MedialY [aux - 2])

            if ((q_R_Shank_Bottom_MedialZ  != "nan") & (q_R_Shank_Bottom_MedialZ  != "NaN") & (q_R_Shank_Bottom_MedialZ  != "NAN")):R_Shank_Bottom_MedialZ .append(float(q_R_Shank_Bottom_MedialZ ))
            else: R_Shank_Bottom_MedialZ .append(R_Shank_Bottom_MedialZ [aux - 2])

            if ((q_R_Heel_TopX  != "nan") & (q_R_Heel_TopX  != "NaN") & (q_R_Heel_TopX  != "NAN")):R_Heel_TopX .append(float(q_R_Heel_TopX ))
            else: R_Heel_TopX .append(R_Heel_TopX [aux - 2])

            if ((q_R_Heel_TopY  != "nan") & (q_R_Heel_TopY  != "NaN") & (q_R_Heel_TopY  != "NAN")):R_Heel_TopY .append(float(q_R_Heel_TopY ))
            else: R_Heel_TopY .append(R_Heel_TopY [aux - 2])

            if ((q_R_Heel_TopZ  != "nan") & (q_R_Heel_TopZ  != "NaN") & (q_R_Heel_TopZ  != "NAN")):R_Heel_TopZ .append(float(q_R_Heel_TopZ ))
            else: R_Heel_TopZ .append(R_Heel_TopZ [aux - 2])

            if ((q_R_Heel_BottomX  != "nan") & (q_R_Heel_BottomX  != "NaN") & (q_R_Heel_BottomX  != "NAN")):R_Heel_BottomX .append(float(q_R_Heel_BottomX ))
            else: R_Heel_BottomX .append(R_Heel_BottomX [aux - 2])

            if ((q_R_Heel_BottomY  != "nan") & (q_R_Heel_BottomY  != "NaN") & (q_R_Heel_BottomY  != "NAN")):R_Heel_BottomY .append(float(q_R_Heel_BottomY ))
            else: R_Heel_BottomY .append(R_Heel_BottomY [aux - 2])

            if ((q_R_Heel_BottomZ  != "nan") & (q_R_Heel_BottomZ  != "NaN") & (q_R_Heel_BottomZ  != "NAN")):R_Heel_BottomZ .append(float(q_R_Heel_BottomZ ))
            else: R_Heel_BottomZ .append(R_Heel_BottomZ [aux - 2])

            if ((q_R_Heel_LateralX  != "nan") & (q_R_Heel_LateralX  != "NaN") & (q_R_Heel_LateralX  != "NAN")):R_Heel_LateralX .append(float(q_R_Heel_LateralX ))
            else: R_Heel_LateralX .append(R_Heel_LateralX [aux - 2])

            if ((q_R_Heel_LateralY  != "nan") & (q_R_Heel_LateralY  != "NaN") & (q_R_Heel_LateralY  != "NAN")):R_Heel_LateralY .append(float(q_R_Heel_LateralY ))
            else: R_Heel_LateralY .append(R_Heel_LateralY [aux - 2])

            if ((q_R_Heel_LateralZ != "nan") & (q_R_Heel_LateralZ != "NaN") & (q_R_Heel_LateralZ != "NAN")):R_Heel_LateralZ.append(float(q_R_Heel_LateralZ))
            else: R_Heel_LateralZ.append(R_Heel_LateralZ[aux - 2])

            if ((q_L_Thigh_Top_LateralX != "nan") & (q_L_Thigh_Top_LateralX != "NaN") & (q_L_Thigh_Top_LateralX != "NAN")):L_Thigh_Top_LateralX.append(float(q_L_Thigh_Top_LateralX))
            else: L_Thigh_Top_LateralX.append(L_Thigh_Top_LateralX[aux - 2])

            if ((q_L_Thigh_Top_LateralY != "nan") & (q_L_Thigh_Top_LateralY != "NaN") & (q_L_Thigh_Top_LateralY != "NAN")):L_Thigh_Top_LateralY.append(float(q_L_Thigh_Top_LateralY))
            else: L_Thigh_Top_LateralY.append(L_Thigh_Top_LateralY[aux - 2])

            if ((q_L_Thigh_Top_LateralZ != "nan") & (q_L_Thigh_Top_LateralZ != "NaN") & (q_L_Thigh_Top_LateralZ != "NAN")):L_Thigh_Top_LateralZ.append(float(q_L_Thigh_Top_LateralZ))
            else: L_Thigh_Top_LateralZ.append(L_Thigh_Top_LateralZ[aux - 2])

            if ((q_L_Thigh_Bottom_LateralX != "nan") & (q_L_Thigh_Bottom_LateralX != "NaN") & (q_L_Thigh_Bottom_LateralX != "NAN")):L_Thigh_Bottom_LateralX.append(float(q_L_Thigh_Bottom_LateralX))
            else: L_Thigh_Bottom_LateralX.append(L_Thigh_Bottom_LateralX[aux - 2])

            if ((q_L_Thigh_Bottom_LateralY != "nan") & (q_L_Thigh_Bottom_LateralY != "NaN") & (q_L_Thigh_Bottom_LateralY != "NAN")):L_Thigh_Bottom_LateralY.append(float(q_L_Thigh_Bottom_LateralY))
            else: L_Thigh_Bottom_LateralY.append(L_Thigh_Bottom_LateralY[aux - 2])

            if ((q_L_Thigh_Bottom_LateralZ != "nan") & (q_L_Thigh_Bottom_LateralZ != "NaN") & (q_L_Thigh_Bottom_LateralZ != "NAN")):L_Thigh_Bottom_LateralZ.append(float(q_L_Thigh_Bottom_LateralZ))
            else: L_Thigh_Bottom_LateralZ.append(L_Thigh_Bottom_LateralZ[aux - 2])

            if ((q_L_Thigh_Top_MedialX != "nan") & (q_L_Thigh_Top_MedialX != "NaN") & (q_L_Thigh_Top_MedialX != "NAN")):L_Thigh_Top_MedialX.append(float(q_L_Thigh_Top_MedialX))
            else: L_Thigh_Top_MedialX.append(L_Thigh_Top_MedialX[aux - 2])

            if ((q_L_Thigh_Top_MedialY != "nan") & (q_L_Thigh_Top_MedialY != "NaN") & (q_L_Thigh_Top_MedialY != "NAN")):L_Thigh_Top_MedialY.append(float(q_L_Thigh_Top_MedialY))
            else: L_Thigh_Top_MedialY.append(L_Thigh_Top_MedialY[aux - 2])

            if ((q_L_Thigh_Top_MedialZ != "nan") & (q_L_Thigh_Top_MedialZ != "NaN") & (q_L_Thigh_Top_MedialZ != "NAN")):L_Thigh_Top_MedialZ.append(float(q_L_Thigh_Top_MedialZ))
            else: L_Thigh_Top_MedialZ.append(L_Thigh_Top_MedialZ[aux - 2])

            if ((q_L_Thigh_Bottom_MedialX != "nan") & (q_L_Thigh_Bottom_MedialX != "NaN") & (q_L_Thigh_Bottom_MedialX != "NAN")):L_Thigh_Bottom_MedialX.append(float(q_L_Thigh_Bottom_MedialX))
            else: L_Thigh_Bottom_MedialX.append(L_Thigh_Bottom_MedialX[aux - 2])

            if ((q_L_Thigh_Bottom_MedialY != "nan") & (q_L_Thigh_Bottom_MedialY != "NaN") & (q_L_Thigh_Bottom_MedialY != "NAN")):L_Thigh_Bottom_MedialY.append(float(q_L_Thigh_Bottom_MedialY))
            else: L_Thigh_Bottom_MedialY.append(L_Thigh_Bottom_MedialY[aux - 2])

            if ((q_L_Thigh_Bottom_MedialZ != "nan") & (q_L_Thigh_Bottom_MedialZ != "NaN") & (q_L_Thigh_Bottom_MedialZ != "NAN")):L_Thigh_Bottom_MedialZ.append(float(q_L_Thigh_Bottom_MedialZ))
            else: L_Thigh_Bottom_MedialZ.append(L_Thigh_Bottom_MedialZ[aux - 2])

            if ((q_L_Shank_Top_LateralX != "nan") & (q_L_Shank_Top_LateralX != "NaN") & (q_L_Shank_Top_LateralX != "NAN")):L_Shank_Top_LateralX.append(float(q_L_Shank_Top_LateralX))
            else: L_Shank_Top_LateralX.append(L_Shank_Top_LateralX[aux - 2])

            if ((q_L_Shank_Top_LateralY != "nan") & (q_L_Shank_Top_LateralY != "NaN") & (q_L_Shank_Top_LateralY != "NAN")):L_Shank_Top_LateralY.append(float(q_L_Shank_Top_LateralY))
            else: L_Shank_Top_LateralY.append(L_Shank_Top_LateralY[aux - 2])

            if ((q_L_Shank_Top_LateralZ != "nan") & (q_L_Shank_Top_LateralZ != "NaN") & (q_L_Shank_Top_LateralZ != "NAN")):L_Shank_Top_LateralZ.append(float(q_L_Shank_Top_LateralZ))
            else: L_Shank_Top_LateralZ.append(L_Shank_Top_LateralZ[aux - 2])

            if ((q_L_Shank_Bottom_LateralX != "nan") & (q_L_Shank_Bottom_LateralX != "NaN") & (q_L_Shank_Bottom_LateralX != "NAN")):L_Shank_Bottom_LateralX.append(float(q_L_Shank_Bottom_LateralX))
            else: L_Shank_Bottom_LateralX.append(L_Shank_Bottom_LateralX[aux - 2])

            if ((q_L_Shank_Bottom_LateralY != "nan") & (q_L_Shank_Bottom_LateralY != "NaN") & (q_L_Shank_Bottom_LateralY != "NAN")):L_Shank_Bottom_LateralY.append(float(q_L_Shank_Bottom_LateralY))
            else: L_Shank_Bottom_LateralY.append(L_Shank_Bottom_LateralY[aux - 2])

            if ((q_L_Shank_Bottom_LateralZ != "nan") & (q_L_Shank_Bottom_LateralZ != "NaN") & (q_L_Shank_Bottom_LateralZ != "NAN")):L_Shank_Bottom_LateralZ.append(float(q_L_Shank_Bottom_LateralZ))
            else: L_Shank_Bottom_LateralZ.append(L_Shank_Bottom_LateralZ[aux - 2])

            if ((q_L_Shank_Top_MedialX != "nan") & (q_L_Shank_Top_MedialX != "NaN") & (q_L_Shank_Top_MedialX != "NAN")):L_Shank_Top_MedialX.append(float(q_L_Shank_Top_MedialX))
            else: L_Shank_Top_MedialX.append(L_Shank_Top_MedialX[aux - 2])

            if ((q_L_Shank_Top_MedialY != "nan") & (q_L_Shank_Top_MedialY != "NaN") & (q_L_Shank_Top_MedialY != "NAN")):L_Shank_Top_MedialY.append(float(q_L_Shank_Top_MedialY))
            else: L_Shank_Top_MedialY.append(L_Shank_Top_MedialY[aux - 2])

            if ((q_L_Shank_Top_MedialZ != "nan") & (q_L_Shank_Top_MedialZ != "NaN") & (q_L_Shank_Top_MedialZ != "NAN")):L_Shank_Top_MedialZ.append(float(q_L_Shank_Top_MedialZ))
            else: L_Shank_Top_MedialZ.append(L_Shank_Top_MedialZ[aux - 2])

            if ((q_L_Shank_Bottom_MedialX != "nan") & (q_L_Shank_Bottom_MedialX != "NaN") & (q_L_Shank_Bottom_MedialX != "NAN")):L_Shank_Bottom_MedialX.append(float(q_L_Shank_Bottom_MedialX))
            else: L_Shank_Bottom_MedialX.append(L_Shank_Bottom_MedialX[aux - 2])

            if ((q_L_Shank_Bottom_MedialY != "nan") & (q_L_Shank_Bottom_MedialY != "NaN") & (q_L_Shank_Bottom_MedialY != "NAN")):L_Shank_Bottom_MedialY.append(float(q_L_Shank_Bottom_MedialY))
            else: L_Shank_Bottom_MedialY.append(L_Shank_Bottom_MedialY[aux - 2])

            if ((q_L_Shank_Bottom_MedialZ != "nan") & (q_L_Shank_Bottom_MedialZ != "NaN") & (q_L_Shank_Bottom_MedialZ != "NAN")):L_Shank_Bottom_MedialZ.append(float(q_L_Shank_Bottom_MedialZ))
            else: L_Shank_Bottom_MedialZ.append(L_Shank_Bottom_MedialZ[aux - 2])

            if ((q_L_Heel_TopX != "nan") & (q_L_Heel_TopX != "NaN") & (q_L_Heel_TopX != "NAN")):L_Heel_TopX.append(float(q_L_Heel_TopX))
            else: L_Heel_TopX.append(L_Heel_TopX[aux - 2])

            if ((q_L_Heel_TopY != "nan") & (q_L_Heel_TopY != "NaN") & (q_L_Heel_TopY != "NAN")):L_Heel_TopY.append(float(q_L_Heel_TopY))
            else: L_Heel_TopY.append(L_Heel_TopY[aux - 2])

            if ((q_L_Heel_TopZ != "nan") & (q_L_Heel_TopZ != "NaN") & (q_L_Heel_TopZ != "NAN")):L_Heel_TopZ.append(float(q_L_Heel_TopZ))
            else: L_Heel_TopZ.append(L_Heel_TopZ[aux - 2])

            if ((q_L_Heel_BottomX != "nan") & (q_L_Heel_BottomX != "NaN") & (q_L_Heel_BottomX != "NAN")):L_Heel_BottomX.append(float(q_L_Heel_BottomX))
            else: L_Heel_BottomX.append(L_Heel_BottomX[aux - 2])

            if ((q_L_Heel_BottomY != "nan") & (q_L_Heel_BottomY != "NaN") & (q_L_Heel_BottomY != "NAN")):L_Heel_BottomY.append(float(q_L_Heel_BottomY))
            else: L_Heel_BottomY.append(L_Heel_BottomY[aux - 2])

            if ((q_L_Heel_BottomZ != "nan") & (q_L_Heel_BottomZ != "NaN") & (q_L_Heel_BottomZ != "NAN")):L_Heel_BottomZ.append(float(q_L_Heel_BottomZ))
            else: L_Heel_BottomZ.append(L_Heel_BottomZ[aux - 2])

            if ((q_L_Heel_LateralX != "nan") & (q_L_Heel_LateralX != "NaN") & (q_L_Heel_LateralX != "NAN")):L_Heel_LateralX.append(float(q_L_Heel_LateralX))
            else: L_Heel_LateralX.append(L_Heel_LateralX[aux - 2])

            if ((q_L_Heel_LateralY != "nan") & (q_L_Heel_LateralY != "NaN") & (q_L_Heel_LateralY != "NAN")):L_Heel_LateralY.append(float(q_L_Heel_LateralY))
            else: L_Heel_LateralY.append(L_Heel_LateralY[aux - 2])

            if ((q_L_Heel_LateralZ != "nan") & (q_L_Heel_LateralZ != "NaN") & (q_L_Heel_LateralZ != "NAN")):L_Heel_LateralZ.append(float(q_L_Heel_LateralZ))
            else: L_Heel_LateralZ.append(L_Heel_LateralZ[aux - 2])

            if ((q_R_MT1X != "nan") & (q_R_MT1X != "NaN") & (q_R_MT1X != "NAN")):R_MT1X.append(float(q_R_MT1X))
            else: R_MT1X.append(0)

            if ((q_R_MT1Y != "nan") & (q_R_MT1Y != "NaN") & (q_R_MT1Y != "NAN")):R_MT1Y.append(float(q_R_MT1Y))
            else: R_MT1Y.append(0)

            if ((q_R_MT1Z != "nan") & (q_R_MT1Z != "NaN") & (q_R_MT1Z != "NAN")):R_MT1Z.append(float(q_R_MT1Z))
            else: R_MT1Z.append(0)

            if ((q_R_MT5X != "nan") & (q_R_MT5X != "NaN") & (q_R_MT5X != "NAN")):R_MT5X.append(float(q_R_MT5X))
            else: R_MT5X.append(R_MT5X[aux - 2])

            if ((q_R_MT5Y != "nan") & (q_R_MT5Y != "NaN") & (q_R_MT5Y != "NAN")):R_MT5Y.append(float(q_R_MT5Y))
            else: R_MT5Y.append(R_MT5Y[aux - 2])

            if ((q_R_MT5Z != "nan") & (q_R_MT5Z != "NaN") & (q_R_MT5Z != "NAN")):R_MT5Z.append(float(q_R_MT5Z))
            else: R_MT5Z.append(R_MT5Z[aux - 2])

            if ((q_L_MT1X != "nan") & (q_L_MT1X != "NaN") & (q_L_MT1X != "NAN")):L_MT1X.append(float(q_L_MT1X))
            else: L_MT1X.append(0)

            if ((q_L_MT1Y != "nan") & (q_L_MT1Y != "NaN") & (q_L_MT1Y != "NAN")):L_MT1Y.append(float(q_L_MT1Y))
            else: L_MT1Y.append(0)

            if ((q_L_MT1Z != "nan") & (q_L_MT1Z != "NaN") & (q_L_MT1Z != "NAN")):L_MT1Z.append(float(q_L_MT1Z))
            else: L_MT1Z.append(0)

            if ((q_L_MT5X != "nan") & (q_L_MT5X != "NaN") & (q_L_MT5X != "NAN")):L_MT5X.append(float(q_L_MT5X))
            else: L_MT5X.append(L_MT5X[aux - 2])

            if ((q_L_MT5Y != "nan") & (q_L_MT5Y != "NaN") & (q_L_MT5Y != "NAN")):L_MT5Y.append(float(q_L_MT5Y))
            else: L_MT5Y.append(L_MT5Y[aux - 2])

            if ((q_L_MT5Z != "nan") & (q_L_MT5Z != "NaN") & (q_L_MT5Z != "NAN")):L_MT5Z.append(float(q_L_MT5Z))
            else: L_MT5Z.append(L_MT5Z[aux - 2])



        aux+=1

    extracted_values = []
    feature = []

################################## (TO DO) Obtenção de features da transformada  #############################################################

    fft_calculo, freq = get_fft(R_ASISX)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_ASISY)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_ASISZ)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_ASISX)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_ASISY)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_ASISZ)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_PSISX)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_PSISY)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_PSISZ)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_PSISX)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_PSISY)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_PSISZ)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Iliac_CrestX)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Iliac_CrestY)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Iliac_CrestZ)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Iliac_CrestX)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Iliac_CrestY)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Iliac_CrestZ)
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)
######
    fft_calculo, freq = get_fft(R_Thigh_Top_LateralX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Top_LateralY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Top_LateralZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Bottom_LateralX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thig_Bottom_LateralY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Bottom_LateralZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Top_MedialX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Top_MedialY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Top_MedialZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Bottom_MedialX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Bottom_MedialY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Thigh_Bottom_MedialZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Top_LateralX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Top_LateralY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Top_LateralZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Bottom_LateralX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Bottom_LateralY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Bottom_LateralZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Top_MedialX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Top_MedialY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Top_MedialZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Bottom_MedialX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Bottom_MedialY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Shank_Bottom_MedialZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_TopX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_TopY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_TopZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_BottomX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_BottomY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_BottomY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_LateralX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_LateralY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_Heel_LateralZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Top_LateralX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Top_LateralY )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Top_LateralZ )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Bottom_LateralX )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Bottom_LateralY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Bottom_LateralZ  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Top_MedialX  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Top_MedialY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Top_MedialZ  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Bottom_MedialX  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Bottom_MedialY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Thigh_Bottom_MedialZ  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Top_LateralX  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Top_LateralY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Top_LateralZ  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Bottom_LateralX   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Bottom_LateralY   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Bottom_LateralZ   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Top_MedialX  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Top_MedialY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Top_MedialZ  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Bottom_MedialX  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Bottom_MedialY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Shank_Bottom_MedialY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Heel_TopX  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Heel_TopY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Heel_TopZ  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Heel_BottomX  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Heel_BottomY  )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)
    
    fft_calculo, freq = get_fft(L_Heel_BottomZ   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Heel_LateralX   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Heel_LateralY   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_Heel_LateralZ   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_MT1X   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_MT1Y   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_MT1Z   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_MT5X   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_MT5Y   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(R_MT5Z   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_MT1X   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_MT1Y   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_MT1Z   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_MT5X   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_MT5Y   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

    fft_calculo, freq = get_fft(L_MT5Z   )
    feature = get_features(freq, fft_calculo)
    extracted_values.append(feature)

################################## (TO DO) Obtenção de features da transformada  #############################################################

    all_data.append(extracted_values)
    data.append(Markers(Time, R_ASISX, R_ASISY, R_ASISZ, L_ASISX, L_ASISY, L_ASISZ, R_PSISX, R_PSISY, R_PSISZ, L_PSISX, L_PSISY, L_PSISZ, R_Iliac_CrestX, R_Iliac_CrestY, R_Iliac_CrestZ, L_Iliac_CrestX, L_Iliac_CrestY, L_Iliac_CrestZ) )
