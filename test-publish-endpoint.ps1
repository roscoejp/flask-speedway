#!/usr/bin/env pwsh
$hash = Get-Content -Raw -Path "sample_data.json" | ConvertFrom-json
$JSON = $hash | ConvertTo-Json
$sleep = 5  # seconds
Whilte (1) { Invoke-WebRequest 'http://127.0.0.1:5000/publish' -Body $JSON -Method POST -ContentType "application/json"; sleep $sleep }
