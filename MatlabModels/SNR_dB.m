function [SNR_linear] = SNR_dB( dB )
    SNR_linear = 10^( dB / 10 );
end