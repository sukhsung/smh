import os 

def runHAADF(settings):
    temsim_dir   = settings['temsim_dir']
    project_dir  = settings['project_dir']
    xyz_dir      = settings['xyz_dir']
    fname_base   = settings['fname_base']


    file_dir = project_dir + fname_base + '/HAADF/'
    astem_params = file_dir + 'astem_params_' + fname_base
    astem_output = file_dir + 'astem_out_' + fname_base + '.tif'
    autostem     = temsim_dir + './autostem'

    makePath(project_dir)
    makePath(file_dir)

    #Parameter for autoslic
    # Name of file with input atomic coord. in x,y,z format:
    astem_xyz = xyz_dir + fname_base + '.xyz'
    #Replicate unit cell by NCELLX,NCELLY,NCELLZ :
    astem_replicate = settings['rep']
    #STEM probe parameters, V0(kv), Cs3(mm), Cs5(mm), df(Angstroms), apert1,2(mrad):
    astem_parameters = settings['voltage'] + ' 0 0 0 0 ' + settings['convergence']
    #type higher order aber. name (as C32a, etc.) followed by a value in mm. (END to end)
    astem_abers = 'END'
    #Do you want to add random pi/4 tunning erros for orders 2 to 5 (y/n)
    astem_random_aber = 'n'
    #Size of specimen transmission function Nx,Ny in pixels :
    astem_specpix = '256 256'
    #Size of probe wave function Nx,Ny in pixels :
    astem_wavepix = '256 256'
    #Crystal tilt x,y in mrad.:
    astem_crystaltilt = '0 0'
    #Do you want to calculate a 1D line scan (y/n) :
    astem_1d = 'n'
    #Number of thickness levels to save, including the end(>=1):
    astem_numthicks = '1'
    #File name prefix to get output of STEM multislice result (no extension):
    astem_stemfname = file_dir + 'HAADF_' + fname_base
    #Number of detector geometries (>=1):
    astem_numdet = '1'
    #Detector 1, type: min max angles(mrad) or radius(Ang.) followed by m or A
    astem_detang0 = settings['ADF_in_out'] + ' m'
    #xi,xf,yi,yf, nxout,nyout :
    astem_scan =  '0 12.547318  0 21.732593 64 64'  # in [Ang, Ang, Ang, Ang, px, px] 
    #Slice thickness (in Angstroms):
    astem_slice = '2'
    #Do you want to include thermal vibrations (y/n) :
    astem_phonon = 'y'
    #Type the temperature in degrees K:
    astem_temp = settings['temp']
    #Type number of configurations to average over:
    astem_phonconfs = settings['num_config']
    #Type source size (FWHM in Ang.):
    astem_source = '0.5'


    f = open(astem_params, 'w')
    f.write(astem_xyz + "\n" + astem_replicate + "\n" + astem_parameters + "\n" + astem_abers + "\n" + astem_random_aber +"\n" + astem_specpix + "\n" + astem_wavepix + "\n" + astem_crystaltilt + "\n" + astem_1d + "\n" + astem_numthicks + "\n"+ astem_stemfname + "\n" + astem_numdet + "\n" + astem_detang0+ "\n" + astem_scan + "\n" + astem_slice + "\n" + astem_phonon + "\n" + astem_temp + "\n" + astem_phonconfs + "\n" + astem_source)
    f.close()


    print('========== Running AUTOSTEM Simulation ==========')

    os.system(autostem + ' ' + fname_base +  ' < ' + astem_params + ' > '+ astem_params+'.out' )

def runSAED(settings):
    temsim_dir   = settings['temsim_dir']
    project_dir  = settings['project_dir']
    xyz_dir      = settings['xyz_dir']
    fname_base   = settings['fname_base']


    file_dir = project_dir + fname_base + '/SAED/'
    aslic_params = file_dir + 'aslic_params_' + fname_base
    image_params = file_dir + 'image_params_' + fname_base
    aslic_output = file_dir + 'aslic_out_' + fname_base + '.tif'
    image_output = file_dir + 'image_out_' + fname_base + '.tif'
    autoslice = temsim_dir + './autoslic'
    image =     temsim_dir + './image'

    makePath(project_dir)
    makePath(file_dir)

    #Parameter for autoslic
    # Name of file with input atomic coord. in x,y,z format:
    xyz = xyz_dir + fname_base + '.xyz'
    #Replicate unit cell by NCELLX,NCELLY,NCELLZ :
    rep = settings['rep']
    #Name of file to get binary aslic_output of multislice result:
    binary_aslic_output = aslic_output
    #Do you want to include partial coherence (y/n) ?
    partial_coherance = 'n'
    #Do you want to calculate CBED with TDS (y/n) :
    cbed_tds = 'n'
    #Do you want to calculate diffraction with TDS (y/n):
    diff_tds = 'n'
    #Do you want to start from previous result? (y/n);
    prev = 'n'
    #Incident beam energy in kev:
    incident_beam_e = settings['voltage']
    #Wavefunction size in pixels, Nx,Ny:
    wavefn_size = '2048 2048'
    #Crystal tilt x,y in mrad.:
    cry_tilt = '0 0'
    #Slice thickness (in Angstroms):
    slice_thick = '1.5'
    #Do you want to record the (real,imag) value of selected beams vs thickness (y/n)
    selec_beam = 'n'
    #Do you want to include thermal vibrations (y/n) :
    include_thermal = 'n'
    #Type the temperature in degrees K:
    temp = settings['temp']
    #Type number of configurations to average over:
    num_config = settings['num_config']
    #DO you want to aslic_output intensity vs. depth cross section (y/n)
    depth_cros = 'n'


    #Parameter for image
    #Name of file with input multislice result:
    im_prevfilename = aslic_output
    #Type 0 for coherent real space image, or 1 for partially coherent real space image, or 2 for diffraction pattern output
    im_type = '2'
    #Name of file to get defocused output
    im_resfilename = image_output
    #DO you want to include central beam? (y/n)
    cent_beam = 'n'
    #Do you want to impose aperture? (y/n)
    im_aperture = 'n'
    #Objective lens and aperture center x,y in mrad
    ap_center = '0 0'
    #Type 0 for linear scale, 1 to do log scale, 2 to do log(1+c*pixel)
    scale = '0';


    f = open(aslic_params, 'w')
    f.write(xyz + "\n" + rep + "\n" + binary_aslic_output + "\n" + partial_coherance + "\n" + cbed_tds + "\n"+ diff_tds + "\n"
        + prev + "\n" + incident_beam_e + "\n" + wavefn_size + "\n" + cry_tilt + "\n" + slice_thick + "\n" + selec_beam + "\n"
        + include_thermal + "\n"  + depth_cros)
    f.close()

    f = open(image_params, 'w')
    f.write(im_prevfilename + "\n" + im_type + "\n" + im_resfilename + "\n" + cent_beam + "\n" + im_aperture + "\n"  + "\n" + ap_center + "\n" +scale)
    f.close()


    #Run Autoslice
    print('========== Running Autoslice Simulation ==========')
    os.system(autoslice  +  ' < ' + aslic_params + ' > '+ aslic_output+'.out' )
    #Run Image
    print('========== Running Image Simulation ==========')
    os.system(image  +  ' < ' + image_params + ' > '+ image_output+'.out' )

def makePath(directory) :
    if not os.path.exists(directory) :
        os.makedirs(directory)

def run(settings) :
    mode = settings['mode']
    if mode == 'SAED' :
        runSAED(settings)
    elif mode == 'HAADF' :
        runHAADF(settings)


settings = {
    'mode'          : 'HAADF', #SAED, HAADF
    'voltage'       : '100',    #keV
    'temp'          : '0', #Kelvin
    'num_config'    : '1',  #Number of Configurations to average over
    'rep'           : '1 1 1', # Unit Cell replication
    'convergence'   : '20',   #mrad
    'ADF_in_out'    : '60 200', # HAADF Detector angle in mrad
    'temsim_dir'    : '/Users/sukhyun/Documents/temsim/',
    'project_dir'   : '/Users/sukhyun/Documents/TaS2_PLD/',
    'xyz_dir'       : '/Users/sukhyun/Documents/xyz/',
    'fname_base'    : 'TaS2_PLD_SuperCell_A1_0.00_A2_0.00'
}

run(settings)
