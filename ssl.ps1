# Define el nombre del host del servidor web
#$hostName = 'www.pandrama.com'

param(
    [string]$url
)

# Intenta establecer una conexión SSL con el servidor web
try {
    # Solicita el certificado SSL/TLS
    $cert = [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
    $request = [Net.WebRequest]::Create("https://$url")
    $response = $request.GetResponse()
    $response.Close()
    $cert = $request.ServicePoint.Certificate
    $certBytes = $cert.Export([Security.Cryptography.X509Certificates.X509ContentType]::Cert)

    # Crea un objeto X509Certificate2 a partir del certificado obtenido
    $x509 = New-Object Security.Cryptography.X509Certificates.X509Certificate2
    $x509.Import($certBytes)

    # Formatea y muestra la información del certificado
    Write-Host "Detalles del Certificado para: $url" -ForegroundColor Green
    Write-Host "Sujeto: " -NoNewline; Write-Host $x509.Subject -ForegroundColor Cyan
    Write-Host "Emisor: " -NoNewline; Write-Host $x509.Issuer -ForegroundColor Cyan
    Write-Host "Válido desde: " -NoNewline; Write-Host $x509.NotBefore -ForegroundColor Yellow
    Write-Host "Válido hasta: " -NoNewline; Write-Host $x509.NotAfter -ForegroundColor Yellow
    Write-Host "Algoritmo de firma: " -NoNewline; Write-Host $x509.SignatureAlgorithm.FriendlyName -ForegroundColor Magenta
    Write-Host "Número de serie: " -NoNewline; Write-Host $x509.SerialNumber -ForegroundColor Gray
    Write-Host "Thumbprint (hash del certificado): " -NoNewline; Write-Host $x509.Thumbprint -ForegroundColor Gray

    # Comprueba si el certificado está caducado y formatea la salida
    if ($x509.NotAfter -lt (Get-Date)) {
        Write-Host "El certificado ha caducado." -ForegroundColor Red
    } else {
        Write-Host "El certificado es válido." -ForegroundColor Green
    }
} catch {
    Write-Host "No se pudo establecer una conexión SSL con el servidor web o el certificado no es válido." -ForegroundColor Red
}
 