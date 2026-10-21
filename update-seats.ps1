# Update the Food Days confirmed-seat count and deploy.
# Usage:  .\update-seats.ps1 12        -> sets booked to 12
#         .\update-seats.ps1 30       -> page flips to sold out + delivery
param([Parameter(Mandatory=$true)][int]$Booked)

$json = Join-Path $PSScriptRoot "site\data\food-days.json"
$cfg = Get-Content $json -Raw | ConvertFrom-Json
$cfg.booked = $Booked
$cfg | ConvertTo-Json -Depth 5 | Set-Content $json -Encoding utf8
Write-Host ("booked = {0} / {1}" -f $Booked, $cfg.capacity)
& (Join-Path $PSScriptRoot "deploy.ps1") ("Food Days: seats {0}/{1}" -f $Booked, $cfg.capacity)
