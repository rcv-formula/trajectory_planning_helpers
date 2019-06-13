import numpy as np


def conv_filt(signal: np.ndarray,
              filt_window: int,
              closed: bool) -> np.ndarray:
    """
    Created by:
    Alexander Heilmeier

    Modified by:
    Tim Stahl

    Documentation:
    Filter a given temporal signal using a convolution (moving average) filter.

    Inputs:
    signal:         temporal signal that should be filtered
    filt_window:    filter window size for moving average filter (must be odd)
    closed:         flag showing if the signal can be considered as closable, e.g. for velocity profiles

    signal input is always unclosed!
    """

    # check if window width is odd
    if not filt_window % 2 == 1:
        raise IOError("Window width of moving average filter must be odd!")

    # calculate half window width - 1
    w_window_half = int((filt_window - 1) / 2)

    # apply filter
    if closed:
        # temporarily add points in front of and behind signal
        signal_tmp = np.concatenate((signal[-w_window_half:], signal, signal[:w_window_half]), axis=0)

        # apply convolution filter used as a moving average filter and remove temporary points
        signal_filt = np.convolve(signal_tmp,
                                  np.ones(filt_window) / float(filt_window),
                                  mode="same")[w_window_half:-w_window_half]

    else:
        # implementation 1: include boundaries during filtering
        # no_points = signal.size
        # signal_filt = np.zeros(no_points)
        #
        # for i in range(no_points):
        #     if i < w_window_half:
        #         signal_filt[i] = np.average(signal[:i + w_window_half + 1])
        #
        #     elif i < no_points - w_window_half:
        #         signal_filt[i] = np.average(signal[i - w_window_half:i + w_window_half + 1])
        #
        #     else:
        #         signal_filt[i] = np.average(signal[i - w_window_half:])

        # implementation 2: start filtering at w_window_half and stop at -w_window_half
        signal_filt = np.copy(signal)
        signal_filt[w_window_half:-w_window_half] = np.convolve(signal,
                                                                np.ones(filt_window) / float(filt_window),
                                                                mode="same")[w_window_half:-w_window_half]

    return signal_filt


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
