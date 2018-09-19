import os 

def runSAED(fname_base,temsim_dir,project_dir,xyz_dir):
    #Run Autusolice
    file_dir = project_dir + fname_base + '/'
    aslic_params = file_dir + 'aslic_params_' + fname_base
    image_params = file_dir + 'image_params_' + fname_base
    aslic_output = file_dir + 'aslic_out_' + fname_base + '.tif'
    image_output = file_dir + 'image_out_' + fname_base + '.tif'
    autoslice = temsim_dir + './autoslic'
    image =     temsim_dir + './image'

    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)


    #Parameter for autoslic
    # Name of file with input atomic coord. in x,y,z format:
    xyz = xyz_dir + fname_base + '.xyz'
    #Replicate unit cell by NCELLX,NCELLY,NCELLZ :
    rep = '1 1 1'
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
    incident_beam_e = '300'
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
    temp = '300'
    #Type number of configurations to average over:
    num_config = '30'
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
    print('Running Autoslice')
    os.system(autoslice  +  ' < ' + aslic_params + ' > '+ aslic_output+'.out' )
    #Run Image
    print('Running Image')
    os.system(image  +  ' < ' + image_params + ' > '+ image_output+'.out' )


temsim_dir   = '/Users/sukhyun/Documents/temsim/'
project_dir  = '/Users/sukhyun/Documents/TaS2_PLD/'
xyz_dir      = '/Users/sukhyun/Documents/xyz/'
fname_base   = 'TaS2_PLD_A1_0.00_A2_0.00'

runSAED(fname_base,temsim_dir,project_dir,xyz_dir)
