  #!/usr/bin/perl 

use Bio::Tools::Run::Alignment::Clustalw;
use Bio::AlignIO;

  #  Build a clustalw alignment factory
  @params = ('ktuple' => 2, 'matrix' => 'BLOSUM');
  $factory = Bio::Tools::Run::Alignment::Clustalw->new(@params);

  #  Pass the factory a list of sequences to be aligned.	
  $inputfilename = '/home/kinow/Downloads/sample_long.txt';
  $aln = $factory->align($inputfilename); # $aln is a SimpleAlign object.

  # ...or
  #$seq_array_ref = \@seq_array;

  # where @seq_array is an array of Bio::Seq objects
  #$aln = $factory->align($seq_array_ref);

  # Use Bio::AlignIO to read in the alignment
  #$str = Bio::AlignIO->new(-file => '/home/kinow/Downloads/rosalind_long.pfam');
  #$aln = $str->next_aln();

  # Describe
  #print $aln->length;
  #print $aln->num_residues;
  #print $aln->is_flush;
  #print $aln->num_sequences;
  #print $aln->score;
  #print $aln->percentage_identity;
  print $aln->consensus_string(0.1), "\n\n";