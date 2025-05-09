import numpy as np
# import matplotlib.pyplot as plt
# import os

def strain_analysis_greenfield(disp_vertical, disp_horizontal, length_beam_element, length_beam, nu):
    """
    Analyze the strain and deformation parameters for greenfield displacements.

    Parameters:
    disp_vertical : array_like - Vertical displacements of the ground [m]
    disp_horizontal : array_like - Horizontal displacements of the ground [m]
    length_beam_element : float - Length of beam element [m]
    length_beam : float - Total length of the beam [m]
    nu : float - Poisson's ratio [-]

    Returns:
    eps_tensile : array_like - Maximum tensile strain [-]
    beta_max : float - Maximum angular distortion [rad]
    horizontal_strain_max : float - Maximum horizontal strain [-]
    """
    # save_input_variables(disp_vertical, disp_horizontal, length_beam_element, length_beam, nu)

    # Calculate horizontal strain
    horizontal_strain = np.gradient(disp_horizontal[0], length_beam_element)  # [-] Horizontal strain

    vert_for_tilt = disp_vertical[0]  # Unpacking, sometimes needed

    omega_greenfield = (vert_for_tilt[-1] - vert_for_tilt[0]) / length_beam  # [rad] tilt of structure
    # Calculate angular distortion

    slope = np.gradient(disp_vertical[0], length_beam_element)

    angular_distortion = abs(slope - omega_greenfield)  # [rad] Angular distortion

    # print('max angular distorsion = ', max(angular_distortion), ', max horizontal strain = ', max(horizontal_strain))

    eps_tensile = ((horizontal_strain * (1 - nu)) / 2) + np.sqrt((((horizontal_strain * (1 + nu)) / 2) ** 2) +
                                                                 ((angular_distortion / 2) ** 2))
    '''
    x = np.linspace(0, length_beam, int(length_beam / length_beam_element + 1))
    plt.plot(x, eps_tensile * 100, 'k-', label='ε_t', linewidth=3)  # Black solid line
    plt.plot(x, horizontal_strain * 100, 'k:', label='ε_h', linewidth=3)  # Black dotted line
    plt.plot(x, (angular_distortion / 2) * 100, 'k--', label='ε_xy', linewidth=3)  # Black dashed line
    plt.plot([min(x), max(x)], [0.0, 0.0], 'k--', label='Cat 0')
    plt.plot([min(x), max(x)], [0.05, 0.05], 'k--', label='Cat 1 Very slight')
    plt.plot([min(x), max(x)], [0.075, 0.075], 'k:', label='Cat 2 Slight')
    plt.plot([min(x), max(x)], [0.15, 0.15], 'k-', label='Cat 3 Moderate')
    plt.ylabel('Deformation (%)')
    plt.xlim([0, length_beam])

    # Move the legend a bit to the right and make the text smaller
    plt.legend(loc='upper left', bbox_to_anchor=(0.64, 1), borderaxespad=0., prop={'size': 10})

    plt.title('Tensile strain along the building due to Greenfield movements')
    plt.xlabel('Offset (m)')

    # Adjust figure size to accommodate the legend within the plot
    plt.gcf().set_size_inches(15 / 2.54, 8 / 2.54)  # Convert cm to inches for figure size
    plt.gcf().set_facecolor('w')
    plt.gca().tick_params(length=0.0200 * 10, width=0.050 * 10)  # Adjust tick length and width

    # Create subfolder with the name in the string inside 'toMATLAB' directory
    save_name = 'Greenfield_standard'
    save_dir = os.path.join('toMATLAB', save_name)
    os.makedirs(save_dir, exist_ok=True)

    # Save the figure as PDF in the subfolder
    plt.savefig(os.path.join(save_dir, save_name + '.pdf'), dpi=300)
    plt.close()
    # Save the data to a txt file in the subfolder
    data_file_path = os.path.join(save_dir, save_name + '_data.txt')
    with open(data_file_path, 'w') as f:
        f.write('x: {}\n'.format(x.tolist()))
        f.write('eps_tensile: {}\n'.format((eps_tensile * 100).tolist()))
        f.write('horizontal_strain: {}\n'.format((horizontal_strain * 100).tolist()))
        f.write('angular_distortion: {}\n'.format((angular_distortion / 2 * 100).tolist()))

    '''
    return eps_tensile, max(angular_distortion), max(horizontal_strain)


def save_input_variables(disp_vertical, disp_horizontal, length_beam_element, length_beam, nu, filename='input_variables.txt'):
    """
    Save the input variables to a file.

    Parameters:
    disp_vertical : array_like - Vertical displacements of the ground [m]
    disp_horizontal : array_like - Horizontal displacements of the ground [m]
    length_beam_element : float - Length of beam element [m]
    length_beam : float - Total length of the beam [m]
    nu : float - Poisson's ratio [-]
    filename : str - Name of the file to save the variables to
    """
    with open(filename, 'w') as f:
        f.write(f"disp_vertical: {disp_vertical.tolist()}\n")
        f.write(f"disp_horizontal: {disp_horizontal.tolist()}\n")
        f.write(f"length_beam_element: {length_beam_element}\n")
        f.write(f"length_beam: {length_beam}\n")
        f.write(f"nu: {nu}\n")

    print(f"Input variables have been saved to {filename}.")

def print_min_max(array):
    print('minimum value')
    print(min(array))
    print('maximum value')
    print(max(array))
