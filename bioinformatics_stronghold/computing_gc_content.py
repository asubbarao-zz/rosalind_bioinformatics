
from collections import defaultdict




def make_seq_id_dict(filepath_or_sequence):
	"""this function can either take in a string of FASTA sequences, or a .txt file"""

	list_of_seqs = filepath_or_sequence.split()
	id_seq_dict = defaultdict(str)

	#if the line begins with '>' it is the seq_id, otherwise, continue appending the sequence to the current ID

	try:
		f = open(filepath_or_sequence).read().split('\n')
		for line in f:
			if line.startswith('>'):
				current_seq = line[1:]
			else:
				id_seq_dict[current_seq] += line

	except IOError:
	    for line in list_of_seqs:
	    	if line.startswith('>'):
	    		current_seq = line[1:]
	    	else:
	    	    id_seq_dict[current_seq] += line 

	return np.array([[key, value] for key, value in id_seq_dict.iteritems()])
    


def calculate_gc(sequence):
	"""calculate the # of guanine and cytosine, divided by the total length of the sequence"""

  	gc_percentage = (sequence.count('G') + sequence.count('C')) / float(len(sequence))
  	return gc_percentage


def get_highest_gc(seq_dict):
	"""calculate the %_gc values for each sequence, then run a max() on the percentages, finally return
	the sequence ID and %_gc of the highest-GC-content sequence"""

    new_array = np.c_[seq_dict, map(calculate_gc, seq_dict[:,1])] #add new column calculate_gc 
    max_gc_entry = new_array[new_array[:,2] == max(new_array[:,2])] #find the row with the highest gc %
    max_gc_percent = float(max_gc_entry[0,2])*100 
    return max_gc_entry[0,0] + " " + str(max_gc_percent)

