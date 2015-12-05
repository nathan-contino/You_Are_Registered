#!/usr/bin/perl
use LWP::Simple;

my $url = 'http://nathan-contino.github.io/Archive/AllCourses.html';

my $content = get $url;

@lines = split(/\n/, $content);

foreach $line (@lines){
	if($line =~ /lblCRN">(.*)<\/span>/){
		print "\n".$1."\t";
	}
	elsif($line =~ /lblCNum">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblTitle">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblCredits">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblDay">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblStartTime">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblEndTime">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblBuilding">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblRoom">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblSectionCap">(.*)<\/span>/){
		print $1."\t";
	}
	elsif($line =~ /lblInstructors">(.*)<\/span>/){
		print $1;
	}
}
print "\n";