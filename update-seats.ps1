# Update the Food Days confirmed-seat count and deploy.
# Usage:  .\update-seats.ps1 12        -> sets booked to 12
#         .\update-seats.ps1 30       -> page flips to sold out + delivery
param([Parameter(Mandatory=$true)][int]$Booked)

$json = Join-Path $PSScriptRoot "site\data\food-days.json"
$cfg = Get-Content $json -Raw | ConvertFrom-Json
$cfg.booked = $Booked
[System.IO.File]::WriteAllText($json, ($cfg | ConvertTo-Json -Depth 5), (New-Object System.Text.UTF8Encoding $false))
Write-Host ("booked = {0} / {1}" -f $Booked, $cfg.capacity)
& (Join-Path $PSScriptRoot "deploy.ps1") ("Food Days: seats {0}/{1}" -f $Booked, $cfg.capacity)
