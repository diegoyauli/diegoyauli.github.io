#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);     # Importa los métodos comunes de CGI
use CGI::Carp qw(fatalsToBrowser);  # Muestra errores en el navegador
use Text::CSV;             # Módulo para trabajar con archivos CSV
use Encode qw(encode decode);  # Módulo para codificación de caracteres

# Crear objeto CGI
my $cgi = CGI->new;

# Obtener parámetros de búsqueda del formulario
my $nombre_universidad = uc($cgi->param('nombre_universidad')) || '';
my $periodo_licenciamiento = uc($cgi->param('periodo_licenciamiento')) || '';
my $departamento_local = uc($cgi->param('departamento_local')) || '';
my $denominacion_programa = uc($cgi->param('denominacion_programa')) || '';

# Imprimir cabecera HTTP y comienzo del HTML
print $cgi->header(-type => 'text/html', -charset => 'UTF-8');
print $cgi->start_html('Resultados de la Búsqueda');

# Establecer la ruta al archivo CSV
my $csv_file = 'C:\Users\Usuario\Downloads\Programas de Universidades.csv';

# Crear objeto Text::CSV para leer el archivo CSV
my $csv = Text::CSV->new ({ binary => 1, auto_diag => 1, sep_char => '|' });

# Abrir el archivo CSV
open my $fh, '<:encoding(UTF-8)', $csv_file or die "No se puede abrir el archivo CSV: $!";

# Mostrar resultados de la búsqueda
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

# Cerrar el archivo CSV y finalizar el HTML
close $fh;
print $cgi->end_html;
