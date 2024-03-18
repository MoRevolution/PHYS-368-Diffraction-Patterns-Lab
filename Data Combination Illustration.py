import numpy as np

import matplotlib.pyplot as plt

def diffraction_pattern(x, slit_width, wavelength):
    beta = np.pi * slit_width * np.sin(x) / wavelength
    intensity = (np.sin(beta) / beta)**2
    return intensity

slit_width = 1e-6
wavelength = 500e-9
x_range = np.linspace(-np.pi/2, np.pi/2, 1000)

intensity_10x = diffraction_pattern(x_range, slit_width, wavelength) * 10
intensity_100x = diffraction_pattern(x_range, slit_width, wavelength) * 100

combined_intensity = intensity_10x.copy()
central_max_index = np.argmax(intensity_10x)
side_fringe_indices = np.where((intensity_100x > intensity_10x) & (np.abs(x_range - x_range[central_max_index]) > 0.5))[0]
combined_intensity[side_fringe_indices] = intensity_100x[side_fringe_indices]

fig, axs = plt.subplots(1, 3, figsize=(12, 8), gridspec_kw={'width_ratios': [1, 1, 2]})

axs[0].plot(x_range, intensity_10x, label='10x Sensitivity')
axs[0].set_title('10x Sensitivity Data')
axs[0].set_ylabel('Intensity (arbitrary units)')
axs[0].legend()

axs[1].plot(x_range, intensity_100x, label='100x Sensitivity')
axs[1].set_title('100x Sensitivity Data')
axs[1].set_ylabel('Intensity (arbitrary units)')
axs[1].legend()

axs[2].plot(x_range, combined_intensity, label='Combined Intensity')
axs[2].set_title('Combined Intensity Profile')
axs[2].set_xlabel('Angle (radians)')
axs[2].set_ylabel('Intensity (arbitrary units)')
axs[2].legend()

plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()
