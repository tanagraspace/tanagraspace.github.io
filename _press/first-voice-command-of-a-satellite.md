---
title: "First Voice Command of a Satellite Achieved Through ESA's OPS-SAT Space Lab"
excerpt: "ESA's OPS-SAT PRETTY heard a spoken command from the ground, understood it, and carried it out in orbit."
date: 2026-10-05
published: true
header:
  overlay_color: "#140a0a"
  og_image: /assets/opssat-pretty-doomed/opssat-pretty-doomed-social-card.png
  teaser: /assets/press/first-voice-command-thumbnail.png
---

<p class="ts-dateline">OCT 2026</p>

<p class="ts-standfirst">OPS-SAT PRETTY is the first satellite to understand a spoken command and carry it out. Tanagra Space and volunteer radio amateurs in Norway designed and ran the experiment. The experiment flew through OPS-SAT Space Lab, a European Space Agency (ESA) service, with TU Graz supporting spacecraft operations.</p>

On 27 July 2026, a radio amateur on a rooftop in Oslo spoke into a microphone: *"LIMA ALFA FOUR OSCAR, PRETTY PLAY DOOM DOOM DOOM, PRETTY PLAY DOOM DOOM DOOM."* Overhead, ESA's OPS-SAT PRETTY satellite captured the transmission and transcribed it with a speech recognition model running on board. It found the command and launched DOOM, the classic 1993 first-person shooter video game.

## Repurposing a Science Satellite

Receiving voice commands was not part of the original spacecraft design of the OPS-SAT PRETTY mission. The satellite's primary mission is GNSS reflectometry and radiation monitoring. Almost three years after launch, new software developed by Tanagra Space was uploaded to the satellite. The software taught the satellite to listen for a human voice, on a frequency its antennas were never designed for.

That flexibility is rare in spacecraft design. It comes from a reconfigurable onboard computer and a software-defined radio. Together, they enable mission extension through software alone.

> "ESA's OPS-SAT Space Lab satellites give experimenters all over the world an opportunity to try their ideas on-board a real, flying mission. Running all these different experiments requires flexibility both from the spacecraft design and its operational team."
>
> **Vladimir Zelenevskiy**, Experimenter and former OPS-SAT-1 Mission Control Team engineer

OPS-SAT Space Lab, ESA's service for outside experimenters, embraced the idea and let volunteer radio amateurs transmit to the spacecraft. The ESA and TU Graz mission operations teams scheduled passes over amateur ground stations in Poland and Norway. It took seven flight runs, from April to July, to get the command through.

> "Not many teams get to point a radio at an orbiting ESA spacecraft and try something nobody has done before. Thank you to ESA and OPS-SAT Space Lab for this unique opportunity, and to the ESA and TU Graz operators who made every pass happen."
>
> **Georges Labrèche**, Founder and Principal Investigator, Tanagra Space

## The Radio Amateurs

Volunteer radio amateurs were the ground segment. Operators in Legnica, Poland, made the first four attempts from April to June 2026. In July, the Oslo Group of the Norwegian Radio Relay League (LA4O) took over.

Feedback from the radio amateurs also changed the flight software. In a raw recording from their first attempt on 3 July, the Oslo team could recognize the operator's voice but not the words. Their analysis showed that the receiver channel on board was far wider than the voice signal, and they proposed narrowing it.

On most satellite missions, changing flight software takes months of reviews. On OPS-SAT PRETTY, volunteers on a rooftop proposed a fix, Tanagra Space accepted it the same day, and about a week later the updated flight software was delivered to ESA.

<figure>
  <img src="/assets/press/la4o-evening-pass-operator_LA7IJ.jpg" alt="An operator wearing a headlamp speaks into a microphone at a folding table of radio equipment on a rooftop at night, with the lights of Oslo behind.">
  <figcaption>Jon Bergli Heier (LB9BJ) speaks the command on the rooftop at Nedre Rommen during the evening pass on 27 July. Photo: Truls Johansen (LA7IJ), LA4O.</figcaption>
</figure>

## What the Satellite Sent Back

After launching DOOM, the payload computer put together a report for the ground team:

- Screenshots and a frame-by-frame animation of the gameplay.
- The transcription, command detection scores, and signal level statistics for each capture.
- A spectrogram, a constellation plot, and a power spectrum of each radio capture.
- A postcard that combines a gameplay frame, the transcription, and the signal diagnostics.

<figure>
  <img src="/assets/opssat-pretty-doomed/postcard-evening.png" alt="A DOOM-themed postcard composed on board the satellite: a gameplay frame with logos, the onboard transcription, and signal diagnostics.">
  <figcaption>The postcard the satellite composed and sent back after an operator spoke the command live into a microphone. The printed text is the onboard transcription. It is rough, but the satellite detected the <em>"PLAY DOOM"</em> command and launched DOOM.</figcaption>
</figure>

> "The key part of being able to pull this off is the portability and deterministic aspect of DOOM."
>
> **Ólafur Waage**, Experiment Co-Designer and Co-Developer

The satellite also sent back its own recording of the live voice command:

{% include audio-player.html src="/assets/opssat-pretty-doomed/command.mp3" %}

## Detecting Signals That Are Not Precisely Defined

No two people say *"PLAY DOOM"* the same way, and noise, Doppler shift, and an antenna tuned for a different frequency distort the signal further. PRETTY detected the command anyway. The signal processing ran on GNU Radio and the speech recognition on Sherpa-ONNX, two open-source tools that also run on ordinary home computers and edge devices.

> "This experiment is fun, but the idea behind it is key. Space-ground communication is normally defined precisely, down to the bit sequence. Here, a reconfigurable software-defined radio, a powerful processor, and terrestrial software repurposed for in-space applications detected something that is not very well defined, a human voice."
>
> **David Evans**, Head of OPS-SAT Space Lab, ESA

Jamming, misuse of protected frequencies, and distress signals are just as hard to define in advance, and the same approach can detect them. Analyzing these signals on the ground means waiting for a ground station pass, and then for a person to review the data. A satellite that detects and recognizes the signal on board can react right away and send down readily available results.

## What Else Could a Satellite Listen To?

Recognizing a voice from orbit is useful for more than commands. Someone in distress at sea or in a remote area could transmit *"mayday"* or *"help"* on a radio. A satellite overhead could detect the call, transcribe it, and use AI to put it in context: the language, the words that matter, and how urgent the call sounds. It could then pass an alert to rescue services, without waiting for a ground station to process a recording.

The speech model on board was small, about 27 MB, and its transcription of the live voice was rough. It still caught the command. A larger model could understand full sentences and their context, not just spot a keyword.

> "The voice was only the test signal. What we've demonstrated with PRETTY is a satellite that can listen to any type of radio signal and act on what it hears. Train the same setup on something other than speech, and it becomes a different instrument."
>
> **Georges Labrèche**, Founder and Principal Investigator, Tanagra Space

The same idea reaches well beyond voice. A radio telescope satellite could carry a model trained to catch bursts from deep space, and downlink only the bursts it finds. Any other signal processing application just needs a different model, uplinked from the ground. Not a different spacecraft, not even different hardware.

## Resources

- [Project page](/opssat-pretty-doomed/)
- [Source code and flight record](https://github.com/georgeslabreche/opssat-pretty-doomed)
- [Oslo (LA4O) campaign report](https://doom.lb6aj.net/)
- [Video: DOOM In Space with Voice Commands](https://www.youtube.com/shorts/1ULb2WJK00Y)
- [OPS-SAT Space Lab: register an experiment](https://opssat.esa.int/)

## About Tanagra Space

Tanagra Space is an Estonian AI consultancy that develops machine learning for autonomous decision-making in space. It runs experiments and technology demonstrators onboard ESA's OPS-SAT spacecraft.

## Media Contact

{% include contact-form.html subject="Press inquiry: First voice command of a satellite" %}
