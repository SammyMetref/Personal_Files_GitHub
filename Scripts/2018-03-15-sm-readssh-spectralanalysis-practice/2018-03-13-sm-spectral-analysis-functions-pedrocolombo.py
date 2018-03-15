import numpy as np
#import scipy.signal as signal
#import scipy.ndimage as im 
from matplotlib import pyplot as plt

pi = np.pi
#--------------------------------------------------------------------------
#Filter routines

def frequency_analysis(data =None,experiment=None,section=None,initial_year=None,\
                      last_year=None):  
    ana_s = np.zeros_like(data)
    ana_f = np.zeros_like(data)
    n = len(data)
    Y = np.fft.fft(data)/n #compute and normalization
    ana_s = Y[range(n/2)]
    Fs=0.5
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range 
    ana_f = np.fft.fftfreq(len(ana_s))
    plt.figure()
    plt.plot(ana_f,abs(ana_s))
    plt.xlabel('Discrete Fourier Sample frequencies')
    plt.ylabel('Spectrum')
    plt.title('Frequency analysis for each density class over all time')
    plt.show(block=False)
    return ana

def filter_average_data(data=None,window_len=5.):
    filtered_data = {}
    filtered_data['t'] = data['t']
    filtered_data['density_class'] = data['density_class']
    filtered_data['transport'] = np.zeros_like(data['transport'])
    quantity_time_points = data['t'].shape[0]
    cont = 0
    while cont < (quantity_time_points - window_days):
          limit_inf = window_days * cont
          limit_sup = window_days * (cont + 1)
          filtered_data['transport'][limit_inf:limit_sup,:] = sum(data['transport'][limit_inf:limit_sup,:]) / window_days
          cont = cont + 1
    return filtered_data

def filter_butter(data=None,cutoff=None,order=None):
    """ Performs a Butterworth low-pass filter given the desired cut off
    frequency of the filter and the order of the filter.
    The filter used is a backward-forward, therefore there is no lag in the output.
    """
    b,a = signal.butter(order, cutoff, btype='lowpass', analog = False)
    y = signal.filtfilt(b,a,data)
    if np.ma.is_masked(data) is True:
       y = np.ma.masked_array(y,data.mask)
    return y

def filter_hamming(data=None,window_len=None):
    """The signal is prepared by introducing reflected copies of the signal
       (with the window size) in both ends so that transient parts are minimized
       in the begining and end part of the output signal.
    """
    s = data
    w=signal.hamming(window_len)
    w = w/np.sum(w)
    y = np.convolve(w,s,'valid')
    y = y[window_len/2.-1:-window_len/2.]
    if np.ma.is_masked(data) is True:
       y = np.ma.masked_array(y,data.mask)
    return y

def filter_hamming_II(data=None,cutoff=None,order=5):
    order = 1000
    a = 1
    b = signal.firwin(numtaps=order,cutoff=cutoff,window='hamming')
    y = signal.filtfilt(b,a,data)
    if np.ma.is_masked(data) is True:
       y = np.ma.masked_array(y,data.mask)
    return y

def is_odd(num):
   return num % 2 != 0

def filter_hanning(data=None,window_len=None):
    s = np.r_[data[window_len-1:0:-1],data,data[-2:-window_len-1:-1]]
    w = np.hanning(window_len)
    w = w/np.sum(w) #Normalize
    y = np.convolve(w,s,'valid')
    y = y[window_len/2.-1:-window_len/2.]
    if np.ma.is_masked(data) is True:
       y = np.ma.masked_array(y,data.mask)
    return y
    

def filter_boxcar(data=None,window_len=None):
    """ Returns the data filtered with a moving average
    """
    w = np.ones(int(window))/float(window)
    y = np.convolve(data,w,'valid')
    y = y[window_len/2.-1:-window_len/2.]
    if np.ma.is_masked(data) is True:
       y = np.ma.masked_array(y,data.mask)
    return y

def filter_sinc(data=None,cutoff=None):
    """Filter using sinc function and a Blackman window
    http://tomroelandts.com/articles/how-to-create-a-simple-low-pass-filter
    """
    fc = cutoff #0.1  # Cutoff frequency as a fraction of the sample rate (in (0, 0.5)).
    b = 0.99 * cutoff  # Transition band, as a fraction of the sample rate (in (0, 0.5)).
    N = int(np.ceil((4 / b)))
    if not N % 2: N += 1  # Make sure that N is odd.
    n = np.arange(N)
    # Compute sinc filter.
    h = np.sinc(2 * fc * (n - (N - 1) / 2.))
    # Compute Blackman window.
    w = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + \
    0.08 * np.cos(4 * np.pi * n / (N - 1))
    # Multiply sinc filter with window.
    h = h * w
    # Normalize to get unity gain.
    h = h / np.sum(h)
    y = np.convolve(data, h,'valid')
    y = y[window_len/2.-1:-window_len/2.]
    if np.ma.is_masked(data) is True:
       y = np.ma.masked_array(y,data.mask)
    return y

def filter_median(data=None,window_len=None):
    y = signal.medfilt(data,window)
    if np.ma.is_masked(data) is True:
       y = np.ma.masked_array(y,data.mask)
    return y

def filter_lanczos(data=None,cutoff=None):
    fc = cutoff 
    fs = 1. / 1. # Sampling frequency 1*5(days mean) = 5 days
    fc_norm = fc * 2. / fs
    n = 2. * 1. / fc
    fc = fc_norm
    k = np.arange(-n,n+1)
    w = (np.sin(2 * pi * fc * k) / (pi * k) * \
        np.sin(pi * k / n) / (pi * k / n))
    #Particular case where k=0
    w[n] = 2 * fc
    #Normalization of coefficients
    w = w / np.sum(w)
    #Compute the filter
    y = np.convolve(data,w,mode='valid')
    y = y[window_len/2.-1:-window_len/2.]
    if np.ma.is_masked(data) is True:
       y = np.ma.masked_array(y,data.mask)
    return y    

def eval_filter_transport(data = None,type_filter="hamming",window_len=4,cutoff=0.25,order=5):
    filtered_data = {} 
    filtered_data['t'] = data['t'] 
    filtered_data['transport'] = np.zeros_like(data['transport'])
    freq_filters = ("butter","sinc","hamming_II")
    window_filters = ("boxcar","median","hanning","hamming")
    data_transport = data['transport']
    #Choose filter
    if type_filter in freq_filters:
       filtered_data['transport'] = eval('filter_'+type_filter+\
                                         '(data=data_transport,'\
                                         'cutoff=cutoff,order=order)')
    if type_filter in window_filters:
       filtered_data['transport'] = eval('filter_'+type_filter+\
                                         '(data=data_transport,'\
                                         'window_len=window_len)')     
    return filtered_data

def loop_filter_cdfsigtrp(type_filter = "butter",data=None,cutoff=None,order=None, window_len=None):
    """Loops the desired filter with the type of data that comes from cdfsigtrp
    """
    #Set output data structure
    filtered_data = {}
    filtered_data['t'] = data['t']
    filtered_data['density_class'] = data['density_class']
    filtered_data['transport'] = np.zeros_like(data['transport'])
    quantity_data_sets = data['density_class'].shape[0]
    data_transport = data['transport']
    cont = 0
    freq_filters = ("butter","sinc","hamming_II")
    window_filters = ("boxcar","median","hanning","hamming")
    #Loop over the data set
    while cont < quantity_data_sets:
          if type_filter in freq_filters:
             filtered_data['transport'][:,cont] = eval('filter_'+type_filter+\
                                                  '(data=data_transport[:,cont],'\
                                                   'cutoff=cutoff,order=order)')
          if type_filter in window_filters:
             filtered_data['transport'][:,cont] = eval('filter_'+type_filter+\
                                                  '(data=data_transport[:,cont],'\
                                                  'window_len=window_len)')
          cont = cont + 1
    return filtered_data

def loop_filter_vel_dens(type_filter = "butter",data=None,cutoff=None,order=None, window_len=None):
    """Loops the desired filter with data coming from a dictionary with the data of
       the velocity and the density of a section
    """
    #Set output data structure
    filtered_data = {}
    filtered_data['t'] = data['t']
    filtered_data['sigma'] = np.ma.copy(data['sigma'])
    filtered_data['normal_vel'] = np.ma.copy(data['normal_vel'])
    quantity_vertical_levels = data['normal_vel'].shape[1]
    quantity_horizontal_levels = data['normal_vel'].shape[2]
    data_normal_vel = data['normal_vel']
    data_sigma = data['sigma']
    cont_v = 0
    #Loop over the data set
    while cont_v < quantity_vertical_levels:
          cont_h = 0
          while cont_h < quantity_horizontal_levels:
                # Filters that use a cutoff frequency
                if type_filter is "butter" or "sinc" or "hamming_II":
                   # Filter evaluation in Normal Velocity
                   filtered_data['normal_vel'][:,cont_v,cont_h] = eval('filter_'+type_filter+'\
                   (data=data_normal_vel[:,cont_v,cont_h],cutoff=cutoff,order=order)')
                   #Filter evaluation in density
                   filtered_data['sigma'][:,cont_v,cont_h] = eval('filter_'+type_filter+'\
                   (data=data_sigma[:,cont_v,cont_h],cutoff=cutoff,order=order)')
                # Window filters
                if type_filter is "boxcar" or "median" or "hanning" or "hamming":
                   # Filter evaluation in Normal Velocity
                   filtered_data['normal_vel'][:,cont_v,cont_h] = eval('filter_'+type_filter+'\
                   (data=data_normal_vel[:,cont_v,cont_h],window_len=window_len)')
                   #Filter evaluation in density
                   filtered_data['sigma'][:,cont_v,cont_h] = eval('filter_'+type_filter+'\
                   (data=data_sigma[:,cont_v,cont_h],window_len=window_len)')   
                cont_h = cont_h + 1
          cont_v = cont_v + 1
    return filtered_data
