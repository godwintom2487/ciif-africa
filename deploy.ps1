# Redeploy ciif.africa to GitHub Pages.
# Usage:  .\deploy.ps1 "commit message"
param([Parameter(Mandatory=$true)][string]$Message)

git add -A
git commit -m $Message
git branch -D gh-pages 2>$null
git subtree split --prefix site -b gh-pages
git push origin master
git push -f origin gh-pages
Write-Host "Pushed. GitHub Pages rebuilds in ~1 minute."
