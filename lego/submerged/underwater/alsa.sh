# amixer controls
#numid=4,iface=MIXER,name='Master Playback Switch'
#numid=3,iface=MIXER,name='Master Playback Volume'
#numid=2,iface=MIXER,name='Capture Switch'
#numid=1,iface=MIXER,name='Capture Volume'

#amixer scontrols
#Simple mixer control 'Master',0
#Simple mixer control 'Capture',0

# -----------------------------------------------------

# amixer cset numid=3 45%
amixer sset Master,0 45%
#amixer sset Speaker Playback Volume 45%
# amixer cset numid=6 45%

#amixer cset numid=1 95%
amixer sset Capture,0 95%
#amixer sset Mic Capture Volume 95%
#amixer cset numid=8 95%
