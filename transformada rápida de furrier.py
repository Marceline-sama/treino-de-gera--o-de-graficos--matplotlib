import numpy as np
import matplotlib.pyplot as plt

# Criando um sinal de exemplo (somatório de duas frequências)
fs = 1000  # Frequência de amostragem
t = np.arange(0, 1, 1/fs)  # Vetor de tempo de 0 a 1 segundo com amostragem de 1/fs
f1 = 5  # Frequência da primeira componente
f2 = 50  # Frequência da segunda componente
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Calculando a FFT
fft_result = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(fft_result), d=1/fs)  # Vetor de frequências correspondentes

# Plotando o sinal no domínio do tempo
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Sinal no Domínio do Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

# Plotando a magnitude da FFT
plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(fft_result))
plt.title('Magnitude da FFT')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
