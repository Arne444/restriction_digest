## Set up restriction digest with two restriction enzymes

from opentrons import containers, robot, instruments

# specify containers
output = containers.load('96-PCR-flat', 'C1', 'output')
trash = container.load('trash-box', 'A3')
source_tubes = container.load('tube-rack-2ml', 'D1', 'tube_rack')
cold_tubes = container.load('tube-rack-2ml', 'E5', 'cold_rack')

#Create 6x12 p20 tip rack
containers.create(
	'tiprack-200ul-6x12',
	grid=(6,12),
	spacing=(9, 9),
	diameter=5,
	depth=60
)

p20_rack = containers.load('tiprack-200ul-6x12', 'B2', 'p20_rack')

#Create 3x6 2ml tube rack for DNA samples
containers.create(
	'3x6-tube-rack-2ml',
	grid=(3,6),
	spacing=(19.5,19.5),
	diameter=9.5,
	depth=40
)

DNA_tubes = containers.load('3x6-tube-rack-2ml', 'C3', 'DNA_rack')

###INPUT### volumes for restriction digest

total_volume = 50

buffer_volume = 10
enzymeA_volume = 2
enzymeB_volume = 2
DNA_volumes = [5, 10, 15]
water_volumes = []
for v in DNA_volumes:
	water_volumes.append(total_volume - v - buffer_volume - enzymeA_volume - enzymeB_volume)

num_DNA_samples = len(DNA_volumes)

#Define sources
buffer_source = source_tubes.wells('A1')
enzymeA_source = cold_tubes.wells('A1')
enzymeB_source = cold_tubes.wells('A2')
water_source = source_tubes.wells('A2')

DNA_sources = dna_tubes.wells('A1', length=num_DNA_samples)


#Distribute buffer
p20.transfer(
	buffer_volume,
	buffer_source,
	output.wells('A1', length(num_DNA_samples),
	touch_tip=True,
	blow_out=True
)

#Distribute enzymeA
p20.transfer(
	enzymeA_volume,
	enzymeA_source,
	output.wells('A1', length(num_DNA_samples),
	touch_tip=True,
	blow_out=True,
)

#Distribute enzymeB
p20.transfer(
	enzymeB_volume,
	enzymeB_source,
	output.wells('A1', length(num_DNA_samples),
	touch_tip=True,
	blow_out=True,
)

#Add DNA
p20.transfer(
	DNA_volumes,
	DNA_sources,
	output.wells('A1', length(num_DNA_samples),
	mix_after(3,20)
	touch_tip=True,
	blow_out=True
)

#Add water and mix
p200.transfer(
	water_volumes,
	water_source,
	output.wells('A1', length(num_DNA_samples),
	mix after(5, 48),
	touch_tip=True,
	blow_out=True
)