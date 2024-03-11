#i = int(input("What is the current temperature outside in farennheit? "))
#temp = (i-32)*5/9
#print("That means it is currently",f"{temp:.1f}""°C outside.") 


midiNote = 64
if midiNote < 64:
  print("MIDI note is smaller than 64.")
elif midiNote > 64:
  print("MIDI note is greater than 64.")
else:
  print("MIDI note is equal to 64.")