Clear-Host

# Definimos el bloque de arte en una variable (Here-String)
$banner = @'
  ____ _   _ ____  ____   ___  ____  
 / ___| | | |  _ \/ ___| / _ \/ ___| 
| |   | | | | |_) \___ \| | | \___ \ 
| |___| |_| |  _ < ___) | |_| |___) |
 \____|\___/|_| \_\____/ \___/|____/ 

     _  ___  _   _     _     _     _   
    | |/ _ \| \ | |   / \   / \   / \  
 _  | | | | |  \| |  / _ \ / _ \ / _ \ 
| |_| | |_| | |\  | / ___ / ___ / ___ \
 \___/ \___/|_| \_|/_/   /_/   /_/   /_/
'@

# Imprimimos con un color seguro
Write-Host $banner -ForegroundColor Cyan

# Separador visual simple
Write-Host ("-" * 45) -ForegroundColor Gray
Write-Host " [!] Cargando panel de Jonaaa..."
