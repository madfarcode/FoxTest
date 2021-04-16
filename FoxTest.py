

p1 >> bell(P[8,6,4,[4,5,6,[8,6,7,5,]]], dur=[1/2], pan=[-1,-0.5,0,0.5,1], 
        room=0.8, mix=0.2, scale=Scale.default, vib=4, vibdepth=0.02, hpf=160, hpr=0.01).every(16, "reverse")
p3 >> glass([0,4,6,0],oct=3, dur=2, amp=1.5, scale=Scale.default)
p2 >> play(" x x x x",room=0.6, mix=0.3, amp=1.5, sample=5)
p6 >> play("- ---f- ",room=0.6, mix=0.3, amp=1.5, sample=5)
p4 >> play(" f" , dur=4, amp=1.6)
p5 >> piano(P[8,6,4,[4,5,6,[8,6,7,8]]], dur=[1/4], hpf=800, scale= Scale.default).every(128, "reverse")
p7 >> dbass([0, 0, 0 ,0], dur=1/2, amp=0.6, hpf=200, room=0.8, mix=0.2 )

p1.stop()

p2.stop()

p3.stop()

p4.stop()

p5.stop()

p6.stop()

p7.stop()

print (Samples)
print (SynthDefs)
