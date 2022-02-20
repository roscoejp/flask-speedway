Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Invoke-Expression -Command "$HOME\.venv\$(Split-Path -Path (Get-Location) -Leaf)\Scripts\Activate.ps1"
