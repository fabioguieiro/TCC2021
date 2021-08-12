import numpy as np
from detect_peaks import detect_peaks

def get_fft(arr): #Recebe o array e retorna a transformada de Fourier
    arr = np.transpose(np.array(arr))
    n = len(arr)  #numero de pontos do gráfico
    freq = np.fft.fftfreq(n)
    mascara = freq > 0
    fft_calculo = np.fft.fft(arr)
    fft_abs = 4.0*np.abs(fft_calculo/n)
    return fft_calculo[mascara], freq[mascara]

def get_first_n_peaks(x, y, no_peaks=7):   #função que retorna os X picos do sinal passado
    x_, y_ = list(x), list(y)
    if len(x_) >= no_peaks:
        return x_[:no_peaks], y_[:no_peaks]
    else:
        missing_no_peaks = no_peaks - len(x_)
        return x_ + [0] * missing_no_peaks, y_ + [0] * missing_no_peaks
        
def get_features(x_values, y_values):
    mph = 0.1 * np.nanmax(y_values)
    indices_peaks = detect_peaks(y_values,mph)
    peaks_x, peaks_y = get_first_n_peaks(x_values[indices_peaks], y_values[indices_peaks])
    return peaks_x + peaks_y