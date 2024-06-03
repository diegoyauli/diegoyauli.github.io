#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use Text::CSV;
use Encode qw(encode decode);

my $cgi = CGI->new;

my $nombre_universidad = uc($cgi->param('nombre_universidad')) || '';
my $periodo_licenciamiento = uc($cgi->param('periodo_licenciamiento')) || '';
my $departamento_local = uc($cgi->param('departamento_local')) || '';
my $denominacion_programa = uc($cgi->param('denominacion_programa')) || '';

print $cgi->header(-type => 'text/html', -charset => 'UTF-8');
print $cgi->start_html('Resultados de la Búsqueda');

my $csv_file = 'ruta/a/tu/archivo/Programas_de_Universidades.csv';

my $csv = Text::CSV->new ({ binary => 1, auto_diag => 1, sep_char => '|' });

open my $fh, '<:encoding(UTF-8)', $csv_file or die "No se puede abrir el archivo CSV: $!";

print "<h2>Resultados de la Búsqueda</h2>";
print "<table>";
while (my $row = $csv->getline($fh)) {
    my ($nombre, $periodo, $departamento, $programa) = @$row;
    if (($nombre_universidad eq '' || lc $nombre eq lc $nombre_universidad) &&
        ($periodo_licenciamiento eq '' || $periodo =~ /$periodo_licenciamiento/i) &&
        ($departamento_local eq '' || lc $departamento eq lc $departamento_local) &&
        ($denominacion_programa eq '' || lc $programa eq lc $denominacion_programa)) {
        print "<tr><td>$nombre</td><td>$periodo</td><td>$departamento</td><td>$programa</td></tr>";
    }
}
print "</table>";

close $fh;
print $cgi->end_html;
