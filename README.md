# Sound Block
Sound can be percieved in 3 main components.

## Pitch
Nyquist theorem

## Loudness
loudness is a subjective perception of sound intensity and is measured using decibels;
loundness is related to intensity which is the power (energy over time) of the sound per unit area.

intensity is directly proportional to the square of the amplitude of vibration.

### fyi:
humans are capable of detecting a range of intensities from
1*10^-12 W/m^2  to  1W/m^2. 
sound intensity is specified using a logarithmic scale known as the sound level.
sound level (decibels) is defined by 10*logbase10(intensity/reference intensity)
for reference intensity, the minimum intensity audible to humans is typically used.

can be complex but theres a typical algorithm for calculating loudness with
RMS amplitude (average power); 
A-weighting is often incorporated as humans are more sensitive to certain frequencies.

play around with top_db param


## Timbre
"colour" of the sound

Timbre is the shape of the wave - sine, square, sawtooth, triangle, or something else. 

from reddit:  When you hear a sound, you're not just hearing one sound, i.e. one sound wave. That would sound like just a sine wave. You're actually hearing lots of waves that combine to make a composite sound. In the case of a musical pitch, you're hearing a fundamental frequency (that's the loudest one, and that's the frequency of the "pitch" of that note) but you're also hearing a lot of other, quieter frequencies corresponding to something called the overtone series. The difference between sounds of differing timbres is that the balance of all those overtones is different, even if the fundamental frequency and amplitude remains the same. 

softer to richer

## Graphic
vispy

## Testing
include testing that makes a very simple visualisation of each of the 3 components
individually; particularily to test loudness. 
maybe a 1d line and see how it jumps as the sound plays

## Next iterations
Stereo mode (L R)

v2: transitioning sounds (show transition between points)

modes for types of input