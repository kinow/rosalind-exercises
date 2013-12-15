#!/usr/bin/perl
use strict;
use warnings;
use Data::Dumper;
use Bio::SeqIO;
use Bio::SeqUtils;

my $string = <<END;
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
END
my $format = 'fasta';
open(my $stringfh, "<", \$string) or die "Could not open string for reading: $!";
my $seqio = Bio::SeqIO->new(
                             -fh     => $stringfh,
                             -format => $format,
                             -alphabet => 'dna'
                             );
while( my $seq = $seqio->next_seq ) {
    # process each seq
    #print $seq->id . ' = '.$seq->seq()."\n";
    $a = $seq->translate();
    print Dumper \$a;
}