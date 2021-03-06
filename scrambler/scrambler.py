#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Scrambler
# Generated: Thu Aug 23 23:45:06 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys


class scrambler(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Scrambler")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Scrambler")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "scrambler")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 24000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_2 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_2.set_update_time(1.0/10)
        self._qtgui_sink_x_2_win = sip.wrapinstance(self.qtgui_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_2_win)
        
        self.qtgui_sink_x_2.enable_rf_freq(True)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(True)
        
        
          
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	0.5, samp_rate, 2700, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/user/scramtest2b.wav', False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('/home/user/scramout.wav', 1, samp_rate, 16)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 3000, 5, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_1, 0), (self.qtgui_sink_x_2, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "scrambler")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_2.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(0.5, self.samp_rate, 2700, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)


def main(top_block_cls=scrambler, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
